# project schema

The central configuration file. `setup-docs` writes it. Edit it here, or re-run `setup-docs`, to change a default. The values below are the defaults; the bracketed ones are set at setup.

**Substrate root:** `[where the project memory lives, default docs/]`

The project memory is a single bundle rooted at `<root>/`. Every page is markdown with YAML frontmatter; the zone directories (`sources/`, `evidence/`, `wiki/`) are ordinary groups, not separate bundles.

**Structure**

```
<root>/
  sources/             actual source files — PDFs, CSVs (immutable, human-managed)
  evidence/
    findings/          analysis results (immutable, append-only)
    decisions/         model design records — DR-NNNN (immutable, append-only)
  wiki/                flat — all synthesized pages (mutable)
  views/               compiled interactive views — build-view output (generated)
  index.md             root index; its only frontmatter is okf_version; maps across zones, grouped by type
  log.md               append-only, one line per write: ## [date] verb | Title
```

**Frontmatter** — every page carries a YAML frontmatter block, in three tiers:

- **Hard floor: `type`.** A page is conformant with just a non-empty `type`. Never block a page for anything else.
- **Authored core: `type` + `title` + `description`.** What every writing skill emits on every page. `title` is the display label; `description` is a one-line summary. Both render in the graph viewer (title as the node label, description on hover) and in indexes.
- **`timestamp`: stamped once at birth, never hand-maintained.** Evidence is immutable, so birth time is correct forever; for the mutable wiki, git history is the modified-time record.
- **`resource`** where the page describes an external asset. Ordering: prefer a web-accessible canonical identifier (DOI strongly preferred for academic works, else a stable URL); fall back to a local path (`<root>/sources/…`) only when nothing web-accessible exists.

Producers may add any other keys; consumers preserve unknown keys and never reject a page for them.

**Types** (eight, all lowercase):

| Type | Zone | What it is | Format doc |
|------|------|-----------|------------|
| `decision` | evidence/decisions | a model design record (DR) | `skills/grill-with-docs/decision-format.md` |
| `finding` | evidence/findings | the result of an analysis you ran | `skills/wiki-ingest/finding-format.md` |
| `source` | wiki | summary of an external source (the file itself sits in `sources/`) | `skills/wiki-ingest/source-format.md` |
| `provenance` | wiki | why a parameter has its value | `skills/grill-with-docs/provenance-format.md` |
| `trace` | wiki | an end-to-end citation trail | `skills/wiki-query/trace-format.md` |
| `concept` | wiki | a synthesis page worth keeping | — (filed by `wiki-query`) |
| `glossary` | wiki | the project's term list (`wiki/glossary.md`) | `skills/grill-with-docs/glossary-format.md` |
| `register` | wiki | a compiled register (assumptions, open decisions) | — (compiled by `wiki-query`) |

**Cross-links:** plain markdown links, kept **relative** (`../evidence/decisions/DR-0007.md`), never bundle-relative `/`-links. The graph viewer follows relative links and silently drops `/`-prefixed ones.

**Citations:** external sources backing a page's claims go under a `# Citations` heading at the bottom of the page, numbered.

**Which verb writes where**

| Skill | Writes | Reads |
|-------|--------|-------|
| grill-with-docs | `<root>/evidence/decisions`, `<root>/wiki` (provenance, glossary) | evidence, wiki |
| wiki-ingest | `<root>/evidence/findings`, `<root>/wiki` (source summaries), `<root>/sources/` | evidence, wiki |
| wiki-query | `<root>/wiki` (concepts, traces, registers) | evidence, wiki |
| build-view | `<root>/views/` (compiled HTML + data) | the conformant corpus |
| audit-code-with-docs | nothing — reports in-session | model code, evidence, wiki |
| maintain-docs | tidying repairs across evidence + wiki | everything |
| onramp-docs | `<root>/onramp-plan.md` | sources, code, evidence, wiki |
| handoff | OS temp (outside project) | project state |
| setup-docs | schema, CLAUDE.md | project structure |

**Justification kinds:** measured, derived, calibrated, assumed

**Decision (DR) statuses:** provisional, accepted, superseded by DR-NNNN

**Lifecycle:** read off the evidence, not set. Sources only reads as a prior; a calibration finding existing reads as calibrated. There is no freeze step.

**Format docs**

- decision: `skills/grill-with-docs/decision-format.md`
- provenance: `skills/grill-with-docs/provenance-format.md`
- glossary: `skills/grill-with-docs/glossary-format.md`
- source: `skills/wiki-ingest/source-format.md`
- finding: `skills/wiki-ingest/finding-format.md`
- trace: `skills/wiki-query/trace-format.md`
- index/log: `skills/setup-docs/index-format.md`
- view manifest: `skills/build-view/manifest-format.md`

**Bundle version:** declared as `okf_version: "0.1"` in the root `index.md` frontmatter — the one place frontmatter is permitted in an index.

**GitHub wiki sync:** `[none | enabled]` — when enabled, `<root>/wiki/` is also pushed to `<repo>.wiki.git` for browsing via the GitHub wiki UI.

**Placeholder-aging threshold:** `[e.g. 90 days]`
