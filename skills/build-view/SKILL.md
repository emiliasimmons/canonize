---
name: build-view
description: Compile the conformant corpus into an interactive view. Use when the user wants to build or compile a view of the project — a knowledge graph of the evidence trail, or a bespoke dashboard.
---

Evidence is ground truth; a view is a compiled projection over it — the same philosophy as the wiki, but HTML instead of markdown. Views live under `docs/views/<name>/` and are always generated, never hand-edited.

Two recipes. A graph of how everything connects → Recipe 1. A custom dashboard over data you extract → Recipe 2.

## Recipe 1 — knowledge graph

The reference implementation includes a graph viewer that walks the corpus. Point it at the corpus and write the result into the views zone.

- **Generator:** `references/knowledge-catalog/okf/src/reference_agent/viewer/` (`generator.py` + `bundle/document.py`). It depends only on `pyyaml` — do **not** `pip install` the full `reference-agent` package, which pulls heavy unrelated deps (google-adk, bigquery). Run it lean, e.g.:

  ```
  PYTHONPATH=<path-to-canonize>/references/knowledge-catalog/okf/src \
    python -c "from reference_agent.viewer import generate_visualization; \
    generate_visualization('docs', 'docs/views/graph/index.html')"
  ```

- **Output:** `docs/views/graph/index.html`.

It produces one HTML page: a Cytoscape graph, nodes colored by type, click a node for its rendered body, plus search and type-filter. A page becomes a node only if it has a non-empty `type` (so `index.md`, `log.md`, and untyped scratch drop out); relative cross-links become edges. The page loads its graph library from a CDN, so it needs a network connection to render.

`references/` is gitignored; if absent, re-fetch the reference implementation. Always use the reference viewer rather than reimplementing the walk.

## Recipe 2 — bespoke view (e.g. PHOTON-class)

A custom dashboard over data you extract from the corpus. There is no reusable dashboard engine: you write the D3/Leaflet/etc. page each time. `references/photon_index.html` is **one** worked example (a TB×Nutrition dashboard, coordinated D3 views, compiled from a spreadsheet) to imitate as a pattern — **not** a template. It happens to extract many claims per paper; another view may extract one parameter, all parameters, or something not yet imagined, and store them as pages, CSV, or otherwise. Hardcode none of PHOTON's shape.

The value is the **interview** that defines everything for each view. Grill the user (one question at a time, a recommended answer each) until these settle:

- **what feeds it** (`applies_to`) — which sources or pages
- **the unit of extraction** — one claim / one parameter / all parameters / whatever. This defines a schema; per `AGENTS.md`, that is an ask-first change.
- **the fields + controlled vocabulary** — the codebook
- **the storage target** (`store`) — `pages` / `csv` / `json` / inline table / … . "Direct to CSV" is as first-class as "one page per claim."
- **the output** — the file(s), or none
- **the refresh policy**

Record the settled design in a manifest at `docs/views/<name>/manifest.md` (format: `manifest-format.md`). The manifest body's Codebook is the only extraction instruction. Then write the page.

**Extraction.** If the view's data is just page frontmatter, read it straight from the corpus — frontmatter is plain YAML at the top of each page. If the view needs data the generic walk can't reach — values parsed out of page *bodies*, PHOTON-style — write a small extraction script into `docs/views/<name>/` that reads the corpus and emits the view's data file. That script is the per-view extractor and lives with the view in the project.

## Refresh

A registered view refreshes by re-running its **declared `refresh` procedure** (the manifest field) — the reference viewer for a graph, or the view's own `docs/views/<name>/` script for a bespoke view. Refresh re-reads the corpus into the view's data; the rendered page stays fixed (do not regenerate the D3, or you get a different page each run).

`wiki-ingest` runs this after every ingest: it reads `docs/views/*/manifest.md` and re-runs the declared refresh of any registered view whose `applies_to` matches.

Before you finish, append a line to `docs/log.md` (`## [date] view | Title`) and link the view from `docs/index.md` if it is worth navigating to.
