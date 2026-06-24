# docs

Agent skills that keep a computational modeler thinking rigorously and leave a durable, navigable trail behind every choice.

The project docs are the authoritative record of what was decided and why — examined, defended, and kept. The body of reasoned decisions grows as you work, appended to but never rewritten.

## The problem

In modeling, the gap between "I made a decision" and "I wrote down why" is where reproducibility dies. Parameter choices, structural assumptions, and the evidence behind them live in someone's head or an orphan notebook. Six months later nobody, including you, can reconstruct why a value is what it is, whether a piece of the model is a considered position or a placeholder, or which parameter set produced a given figure.

The fix is to make capture a non-optional side effect of the verbs you already want to run, never a "remember to update the docs" you will skip.

## The one-sentence model

Sources feed the wiki. Decisions are internal sources. Collaborators browse the wiki, not the sources.

## Quickstart

Run `setup-docs` in your project. It will scaffold the project structure and write the config layer.

If the project already has sources, code, or undocumented decisions, run `onramp-docs` next — it surveys what exists, triages it, and produces a phased plan for bringing everything into the record.

## Zones, split by mutability

- **sources** : actual source files (PDFs, CSVs). Immutable, human-managed.
- **evidence** : immutable, append-only, citeable. What you observed and what you decided — findings and decisions (DRs). You append, re-run, or supersede; you never quietly rewrite.
- **wiki** : mutable, synthesized. What you currently believe, built on top of sources and evidence. Source summaries, parameter provenance, concept pages, traces. It grows incrementally as you work; in principle you could rebuild it from sources and evidence.
- **views** : generated. Interactive HTML compiled from the conformant corpus by `build-view` — a knowledge graph or bespoke dashboards. A projection, never ground truth.

## One OKF bundle

The whole thing is a single OKF bundle (Open Knowledge Format v0.1): markdown with YAML frontmatter, a non-empty `type` on every page. That keeps it readable without tooling, diffable in git, and compilable into the interactive views in `docs/views/`. Capture is born-conformant — the writing skills emit the authored core (`type`, `title`, `description`, a birth `timestamp`) on every page they create — so there is nothing to "remember to update."

## Structure

Everything lives under a single root (default `docs/`) so the skills do not pollute the project directory.

```
docs/
  sources/             actual source files (PDFs, CSVs)
  evidence/
    findings/          analysis results
    decisions/         model design records (DR-NNNN)
  wiki/                flat — source summaries, provenance, concepts, traces, registers, glossary
  views/               compiled interactive views (build-view output)
  index.md             root index; carries okf_version; maps across zones, grouped by type
  log.md               append-only changelog
```

## What writes where

| Skill | Writes | Reads |
|-------|--------|-------|
| grill-with-docs | `docs/evidence/decisions`, `docs/wiki` (provenance, glossary) | evidence, wiki |
| wiki-ingest | `docs/evidence/findings`, `docs/wiki` (source summaries), `docs/sources/` | evidence, wiki |
| wiki-query | `docs/wiki` (concepts, traces, registers) | evidence, wiki |
| build-view | `docs/views/` (compiled HTML + data) | the conformant corpus |
| audit-code-with-docs | nothing — reports in-session | model code, evidence, wiki |
| maintain-docs | tidying repairs across evidence + wiki | everything |
| onramp-docs | `docs/onramp-plan.md` | sources, code, evidence, wiki |
| handoff | OS temp (outside project) | project state |
| setup-docs | schema, CLAUDE.md | project structure |

## The skills

- **setup-docs** : scaffold a project and tune behavior. The one place that owns the config layer. Re-run it to retune.
- **onramp-docs** : survey an existing project's sources and code, triage what needs capturing, and produce a phased plan. Run after setup when the project has existing work. Re-runnable when new material appears.
- **grill-with-docs** : the primary working interface. Interrogate a plan or topic until decisions settle, then route each one into the project.
- **wiki-ingest** : bring evidence in, a source you read or a finding you ran.
- **wiki-query** : answer questions over the evidence, and trace a value, finding, or result back through its provenance.
- **build-view** : compile the conformant corpus into interactive views — a knowledge graph or bespoke dashboards.
- **audit-code-with-docs** : check the model's code against its recorded reasoning. The only skill that reads code; it reports in-session and writes nothing.
- **maintain-docs** : a health pass that finds problems and tidies them, in one go, on demand.
- **handoff** : a short, disposable note so another session can pick up the thread.

## Two ideas worth holding onto

The wiki is built incrementally as you work, not regenerated from scratch. Sources and evidence are ground truth; the wiki is a compiled view over them. Given the same questions, you would get similar answers, so the wiki is not precious in the way evidence is. In practice it grows page by page as decisions settle and syntheses accumulate. Because the whole thing is a git repo, history is the time machine for the mutable wiki, so making provenance docs mutable costs nothing in auditability.

The parameter lifecycle is read, not set. There is no freeze button. A value with only sources behind it reads as a prior; once a calibration finding exists, it reads as calibrated. The stage is a property the wiki compiles, not a state you advance.

## Built on

- [Matt Pocock's engineering skills](https://github.com/mattpocock/skills) : decisions get written down as they crystallize; documentation is never its own skill
- [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) : a persistent knowledge base that pre-compiles synthesis instead of re-deriving it every time
- [OKF (Open Knowledge Format)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) : the page format — markdown with YAML frontmatter, a non-empty `type` on every page
