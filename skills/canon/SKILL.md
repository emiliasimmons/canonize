---
name: canon
description: How the canon system works and how to run its script — compile, check, sequence. Load when writing pages, compiling surfaces, checking conformance, or reasoning about the project's structure. Other skills load this instead of carrying script mechanics.
---

# Canon

The system's knowledge layer: how a project is laid out, and how to drive the deterministic `canon` script. Other skills load this rather than restating any of it.

## How the project is laid out

Three zones, three postures:

- `sources/` — raw files (PDFs, CSVs). Flat. Immutable, human-managed.
- `evidence/findings/` and `evidence/decisions/` — flat within type, tagged. Append-only. Decisions carry sequential `DR-NNNN` ids.
- `wiki/topics/` — topic hubs and their member pages. Mutable, built incrementally.

Storage is zone-first; navigation is topic-first. `wiki/topics/<name>.md` is the hub; `wiki/topics/<name>/` holds its members. A page joins a hub **by tag**: its home topic (the directory it lives in) is always also a tag, and every other topic it is tagged with lists it in that hub too. Evidence has no single-parent constraint — a decision appears in every hub it is tagged to.

`index.md` is the root orientation page: an authored preamble, then the compiled taxonomy and state blocks. `schema.md` holds the type registry (what each type is, where it lives, which surfaces it feeds) and the tag vocabulary.

## What is compiled vs authored

Every navigation surface is compiled from frontmatter and never hand-edited: the taxonomy and state blocks on `index.md`, the member list on each hub, the assumptions and open-decisions registers, the per-zone indexes. Compiled blocks are delimited by `<!-- compiled:NAME -->` … `<!-- /compiled:NAME -->`; only the inner content is regenerated, never the authored prose around it. All links are root-anchored from the bundle root (`/evidence/...`).

Evidence is append-only: append, supersede, or re-run — never quietly rewrite.

## Running the script

Stdlib Python, shipped beside the skills. Resolve it from the calling skill's own directory and run it against the project's substrate root (default `docs`, set in `schema.md`):

```
python3 <canonize-skills>/canon/canon.py --root <substrate-root> <subcommand>
```

### compile — regenerate compiled blocks from frontmatter

Incremental (named blocks) in the routine write path; full-corpus (`all`, the default) as a maintenance repair. Idempotent — recompiling an unchanged corpus writes nothing.

```
--block members --page <hub> …    one or more hubs a written page joined
--block taxonomy --block state    the root, after any page write
--block registers                 after any decision write or supersession
                                   (no flag = full recompile of everything)
```

One call carries several `--block`/`--page` flags.

### check — conformance and link integrity

```
--frontmatter    every page has a type; authored core present; type is registered
--links          root-anchored links resolve; file-relative .md links flagged
                 (no flag = both)
```

Non-zero exit on a blocking issue.

### sequence — hand out the next id

```
--kind decision    prints the next DR-NNNN atomically
```

Never pick a DR number by hand.

## When to record a decision

Only when one of these holds:

1. **Hard to reverse** — the choice constrains future work.
2. **Surprising without context** — a future reader will wonder why.
3. **A real trade-off** — genuine alternatives existed and one was chosen for specific reasons.

A provisional decision is legitimate when the choice is forced but the rationale is thin; it lands in the open-decisions register automatically. Writing the page itself is /record-doc's job.

## What needs sign-off

Structural taxonomy changes — a new topic, a new type, a split, merge, or rename — are proposed and wait for approval. Tag minting is unilateral but registered in the same write.
