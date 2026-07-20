#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pymupdf4llm>=0.0.17",
#     "pymupdf>=1.25",
#     "pypdf>=4.0",
#     "pdfplumber>=0.11",
#     "pandas>=2.0",
# ]
# ///
"""Extract text, tables, metadata, and images from an academic PDF.

Usage:
    uv run extract_pdf.py paper.pdf -o outdir/
    uv run extract_pdf.py paper.pdf -o outdir/ --name smith2022

Output directory will contain:
    paper.pdf / smith2022.pdf   copy of the source PDF (renamed with --name)
    content.md                  full text as markdown (pymupdf4llm, handles multi-column)
    metadata.json               title, authors, page count, etc.
    tables/                     each detected table as a CSV (pdfplumber)
    images/                     embedded images >5KB (pdfimages, needs poppler-utils)
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pandas as pd
import pdfplumber
import pymupdf4llm
from pypdf import PdfReader


def extract_metadata(pdf_path: Path) -> dict:
    reader = PdfReader(pdf_path)
    meta = reader.metadata
    info: dict = {
        "file": pdf_path.name,
        "pages": len(reader.pages),
    }
    if meta is not None:
        info.update({
            "title": meta.get("/Title") or meta.title,
            "author": meta.get("/Author") or meta.author,
            "subject": meta.get("/Subject") or meta.subject,
            "creator": meta.get("/Creator") or meta.creator,
            "producer": meta.get("/Producer"),
            "creation_date": str(meta.get("/CreationDate", "")),
        })
    return {k: v for k, v in info.items() if v is not None}


def extract_markdown(pdf_path: Path) -> str:
    return pymupdf4llm.to_markdown(str(pdf_path))


def extract_tables(pdf_path: Path, out_dir: Path) -> int:
    created = not out_dir.exists()
    out_dir.mkdir(exist_ok=True)
    count = 0
    with pdfplumber.open(pdf_path) as pdf:
        for page_idx, page in enumerate(pdf.pages, 1):
            tables = page.extract_tables()
            for tbl_idx, table in enumerate(tables, 1):
                if not table or len(table) < 2:
                    continue
                flat = [c for row in table for c in row if c]
                if len(flat) < 3:
                    continue
                count += 1
                header = table[0]
                header = [str(h).strip() if h else f"col_{i}" for i, h in enumerate(header)]
                rows = table[1:]
                df = pd.DataFrame(rows, columns=header)
                df.to_csv(out_dir / f"p{page_idx:02d}_t{tbl_idx}.csv", index=False)
    if count == 0 and created:
        out_dir.rmdir()
    return count


def extract_images(pdf_path: Path, out_dir: Path) -> int:
    if not shutil.which("pdfimages"):
        return -1
    created = not out_dir.exists()
    out_dir.mkdir(exist_ok=True)
    result = subprocess.run(
        ["pdfimages", "-all", "-p", str(pdf_path), str(out_dir / "img")],
        capture_output=True,
    )
    if result.returncode != 0:
        msg = result.stderr.decode(errors="replace").strip()
        print(f"pdfimages failed (exit {result.returncode}): {msg}", file=sys.stderr)
        if created and not any(out_dir.iterdir()):
            out_dir.rmdir()
        return -1
    kept = 0
    for f in list(out_dir.iterdir()):
        if f.stat().st_size < 5120:
            f.unlink()
        else:
            kept += 1
    if kept == 0 and created:
        out_dir.rmdir()
    return kept


def process(src: Path, out_dir: Path, name: str | None) -> None:
    src = src.resolve()
    if not src.exists() or src.suffix.lower() != ".pdf":
        print(f"not a PDF: {src}", file=sys.stderr)
        sys.exit(1)

    out_dir = out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    dest_name = f"{name}.pdf" if name else src.name
    dest_pdf = out_dir / dest_name
    shutil.copy2(str(src), str(dest_pdf))

    md = extract_markdown(dest_pdf)
    (out_dir / "content.md").write_text(md, encoding="utf-8")

    meta = extract_metadata(dest_pdf)
    (out_dir / "metadata.json").write_text(
        json.dumps(meta, indent=2, default=str, ensure_ascii=False),
        encoding="utf-8",
    )

    n_tables = extract_tables(dest_pdf, out_dir / "tables")
    n_images = extract_images(dest_pdf, out_dir / "images")

    parts = [f"{dest_pdf.stem}: {meta.get('pages', '?')}pp"]
    parts.append(f"{n_tables} tables")
    if n_images == -1:
        parts.append("images skipped (no pdfimages)")
    else:
        parts.append(f"{n_images} images")
    parts.append(f"{len(md)} chars markdown")
    print(", ".join(parts))


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("pdf", type=Path, help="path to the source PDF")
    parser.add_argument("-o", "--output", type=Path, required=True, help="output directory")
    parser.add_argument("--name", help="rename the PDF copy (without .pdf extension)")
    args = parser.parse_args()
    process(args.pdf, args.output, args.name)


if __name__ == "__main__":
    main()
