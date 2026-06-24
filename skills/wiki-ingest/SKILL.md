---
name: wiki-ingest
description: Record a new piece of evidence into the project, either a source you read (a paper, a dataset) or a finding from an analysis you ran. Use when the user has read something worth keeping, or has run an analysis and wants the result recorded, including a validation result.
---

Two kinds of evidence come in.

**A source you read.** Drop the file into `docs/sources/` and write a summary into `docs/wiki/`. Cross-check it against what the project already holds. If it conflicts with something already assumed (a frozen prior, an accepted decision), say so plainly and name what it conflicts with. Do not hand-append to the open-decisions register — that register is compiled, so a manual line will be overwritten on the next recompile. If the conflict is not resolved on the spot, it becomes a provisional DR via `grill-with-docs`, which then shows up in the register on recompile. Do not supersede a decision here. Resolving a conflict is a decision, and decisions go through `grill-with-docs`.

**A finding from an analysis you ran.** Write it into `docs/evidence/findings/` with enough detail to understand and re-run it: the question, the method as a pointer to the re-runnable artifact (never paste the script), the inputs that mattered, and the result with its diagnostic. Findings are immutable once written: append, re-run, or supersede, never quietly rewrite. A validation result lands here like any other finding.

Every page you write is conformant: source summaries and findings carry the authored-core frontmatter — `type`, `title`, `description`, and a birth `timestamp` stamped once — and link to what they bear on with relative markdown links. A source summary also carries `resource` (a DOI or stable URL where one exists, else the local `docs/sources/...` path). Formats are in this folder: `source-format.md`, `finding-format.md`.

Before you finish, append a line to `docs/log.md` (`## [date] ingest | Title`) and update `docs/index.md`.

**Refresh registered views.** After ingesting a source, read `docs/views/*/manifest.md` and refresh any registered view whose `applies_to` matches the new source. Refreshing means re-running the view's declared `refresh` procedure to rebuild its data file — never regenerating the rendered page. See `skills/build-view`.
