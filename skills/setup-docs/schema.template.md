# project schema

The file every skill reads to find its way around. `setup-docs` writes it. Edit it here, or re-run `setup-docs`, to change a default. The values below are the defaults; the bracketed ones are set at setup.

**Substrate root:** `[where the project memory lives, default docs/]`

**Structure**

```
<root>/
  inbox/               scratch, untriaged captures (mutable, disposable)
  sources/             actual source files — PDFs, CSVs (immutable, human-managed)
  evidence/
    findings/          analysis results (immutable, append-only)
    mdr/               model design records (immutable, append-only)
  wiki/                flat — all synthesized pages (mutable)
  index.md             map across zones, grouped by type
  log.md               append-only, one line per write: ## [date] verb | Title
```

**Which verb writes where**

| Skill | Writes | Reads |
|-------|--------|-------|
| grill-with-docs | evidence/mdr, wiki (provenance, glossary) | evidence, wiki |
| wiki-ingest | evidence/findings, wiki (source summaries), sources/ | evidence, wiki |
| wiki-query | wiki (concepts, traces, registers) | evidence, wiki |
| audit-code-with-docs | inbox (report) | model code, evidence, wiki |
| maintain-docs | tidying repairs across evidence + wiki | everything |
| to-issues | issue tracker, or open-decisions register if none | evidence/mdr |
| stash | inbox | — |
| handoff | OS temp (outside project) | project state |
| setup-docs | schema, CLAUDE.md | project structure |

**Justification kinds:** measured, derived, calibrated, assumed

**MDR statuses:** provisional, accepted, superseded by MDR-NNNN

**Lifecycle:** read off the evidence, not set. Sources only reads as a prior; a calibration finding existing reads as calibrated. There is no freeze step.

**Wiki page types**

Every wiki page begins with a YAML frontmatter block containing its type:

```
---
type: provenance
---
```

| Type | What it is | Format doc |
|------|-----------|------------|
| `provenance` | why a parameter has its value | `skills/grill-with-docs/provenance-format.md` |
| `source` | summary of an external source | `skills/wiki-ingest/source-format.md` |
| `trace` | end-to-end citation trail | `skills/wiki-query/trace-format.md` |
| `concept` | synthesis page worth keeping | — (filed by `wiki-query`) |

The glossary (`wiki/glossary.md`) is a single known file and does not need a type field.

**Format docs**

- MDR: `skills/grill-with-docs/mdr-format.md`
- provenance: `skills/grill-with-docs/provenance-format.md`
- glossary: `skills/grill-with-docs/glossary-format.md`
- source: `skills/wiki-ingest/source-format.md`
- finding: `skills/wiki-ingest/finding-format.md`
- trace: `skills/wiki-query/trace-format.md`
- index: `skills/setup-docs/index-format.md`

**Tracker:** `[none | git issues | ...]`

**GitHub wiki sync:** `[none | enabled]` — when enabled, `docs/wiki/` is also pushed to `<repo>.wiki.git` for browsing via the GitHub wiki UI.

**Placeholder-aging threshold:** `[e.g. 90 days]`
