---
name: wiki-ingest
description: Record a new piece of evidence into the project, either a source you read (a paper, a dataset) or a finding from an analysis you ran. Use when the user has read something worth keeping, or has run an analysis and wants the result recorded, including a validation result.
---

Two things come in when you record.

A source you read. Drop the file itself into `docs/sources/` and write a summary into `docs/wiki/`. Cross-check it against what the project already holds. If it conflicts with something already assumed (a frozen prior, an accepted MDR), say so plainly, name what it conflicts with, and leave a breadcrumb so it is not lost: a line in the open-decisions register, or an issue via `to-issues`. Record and surface. Do not supersede a decision here. Resolving a conflict is a decision, and decisions go through `grill-with-docs`.

A finding from an analysis you ran. Write it into `docs/evidence/findings/` so it describes itself: the question, the method as a pointer to the re-runnable artifact (never paste the script), the inputs that mattered as data, and the result with its diagnostic. Findings are immutable once written: you append, re-run, or supersede, never quietly rewrite. A validation result, the check of whether the model reproduces a real-world target, lands here like any other finding.

Formats are in this folder: `source-format.md`, `finding-format.md`.

Before you finish, append a line to `docs/log.md` (`## [date] ingest | Title`) and update `docs/index.md`.
