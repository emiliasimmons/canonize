---
name: build-docs-view
description: Compile the conformant corpus into an interactive HTML view on request — a knowledge graph of the evidence trail, or a bespoke dashboard. Use when the user wants to build, compile, or refresh a view of the project. Optional and pull-only; nothing in normal operation depends on a view existing.
---

Views live under `docs/views/<name>/` and are always generated, never hand-edited.

## Recipe 1 — knowledge graph

`graph.py` in this skill's directory walks the corpus and renders the graph. Run it against the substrate root:

```
python3 <build-docs-view-skill-path>/graph.py --root docs --out docs/views/graph/index.html
```

One HTML page: a Cytoscape graph, topic clusters, nodes colored by type, click a node for its rendered body, plus search and a type filter. Rendering needs a network connection. A page becomes a node only if it has a `type` (index and log files drop out); root-anchored `.md` links and the typed relations (`derived_from`, `bears_on`, `supersedes`) become edges.

## Recipe 2 — bespoke view

Write the D3/Leaflet/etc. page each time. Run a /grilling session until these settle:

- **what feeds it** (`applies_to`) — which sources or pages
- **the unit of extraction** — one claim / one parameter / all parameters / …
- **the fields + controlled vocabulary** — the codebook
- **the storage target** (`store`) — pages / csv / json / inline table / …
- **the output** — the file(s)

Record the settled design in a manifest at `docs/views/<name>/manifest.md` (format: `manifest.md`); the manifest's Codebook is the only extraction instruction.

Then build the pipeline. A bespoke view is always a script — or a set of scripts — running extraction → data → visualization, and it must be re-runnable on its own, without an agent. Write the extractor(s) into `docs/views/<name>/`: they read the corpus (frontmatter, or values parsed out of bodies) and emit the data file the page renders.

The one exception is when the extraction itself needs the agent — sentiment analysis, or any judgement an LLM has to make. Do not wire that through chat; recommend an agent SDK for that step.

To change an existing view, load its manifest and scripts and change them directly.

## Refresh

A view refreshes by re-running its scripts — `graph.py` for a graph, or a bespoke view's extractor(s) — which re-read the corpus into the view's data while the rendered page stays fixed.
