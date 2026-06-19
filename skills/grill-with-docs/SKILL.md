---
name: grill-with-docs
description: The primary working interface. Interrogate a plan or topic until decisions settle, then route each one into the project. Also captures already-made decisions without interrogation. Use when the user wants to work through a modeling choice, make a plan, record a decision, or mentions "grill".
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time.

If a question can be answered by exploring the project, explore the project instead.

As each decision settles, route it into the project at once:

- a value's justification -> a parameter provenance doc (wiki)
- a structural or methodological choice -> an accepted MDR (evidence)
- an expedient placeholder -> a provisional MDR (evidence)
- a term worth pinning down -> the glossary
- a claim that needs checking -> spin off an investigation with `wiki-ingest`
- a tangent for later -> park it with `stash`

When an open question or placeholder lands, hand it to `to-issues` so it becomes an issue you can schedule.

Formats for each artifact are in this folder: `mdr-format.md`, `provenance-format.md`, `glossary-format.md`.

Before you finish a write, append a line to `docs/log.md` (`## [date] grill | Title`) and update `docs/index.md`.
