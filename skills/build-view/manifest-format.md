# View manifest format

A manifest is the contract for one bespoke view (Recipe 2). It lives at `docs/views/<name>/manifest.md` and is read by `build-view` (to know how to compile the view) and by the `wiki-ingest` refresh tail step (to know whether a new source feeds it). Recipe 1 (the free knowledge graph) needs no manifest.

The frontmatter is generic — nothing in it is PHOTON-specific (no `extracts: claim`, no assumed `dashboard.html`). Every field is settled in the interview.

```yaml
---
type: view
title: <view name>
description: <one line: what the view shows>
timestamp: <ISO 8601, stamped once at creation>
status: registered            # one-shot | registered
unit: <what one extraction represents — defined in the grill; omit if none>
store: <pages | csv | json | table | ...>
applies_to: <which sources feed it, e.g. { tags: [nutrition, tb] }>
refresh: <the procedure to re-run — e.g. reference viewer | ./extract.py | manual>
output: <file(s) — or none>
---
# Codebook

<the dimensions + controlled vocabulary the extraction must fill — this body is the only extraction instruction>
```

Notes:

- `type: view` is a meta-type for view configuration, distinct from the eight knowledge types. A manifest will appear as a (default-colored) node in the knowledge graph; that is fine — it is part of the bundle.
- `status: registered` means the view is living and is refreshed by the `wiki-ingest` tail step; `one-shot` means it was compiled once and is not maintained.
- `applies_to` is the match the refresh tail step tests a new source against. Keep it declarative (tags, a path glob, a list of source ids) so the test is cheap.
- `refresh` names the procedure that rebuilds the view's data: the reference viewer for a graph, or the view's own `docs/views/<name>/` script for a bespoke view. It re-reads the corpus and leaves the rendered page fixed. Do not regenerate the page on refresh.
