---
name: grill-with-docs
description: The primary working interface. Interrogate a plan or topic until decisions settle, then route each one into the project. Also captures already-made decisions without interrogation. Use when the user wants to work through a modeling choice, make a plan, record a decision, or mentions "grill".
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time.

If a question can be answered by exploring the project, explore the project instead.

If a decision is already settled, skip interrogation and route it directly.

As each decision settles, route it into the project at once:

- a value's justification -> a parameter provenance doc (wiki)
- a structural or methodological choice -> an accepted decision, a DR (evidence)
- an expedient placeholder -> a provisional decision, a DR (evidence)
- a term worth pinning down -> the glossary
- a claim that needs checking -> spin off an investigation with `wiki-ingest`
- a tangent for later -> stash it, resolve it now, or drop it

An open question or placeholder is a provisional DR. The open-decisions register is compiled from provisional DRs by `wiki-query`, so once the DR is written, the register picks it up automatically.

Every page you write is conformant: it carries the authored-core frontmatter — `type`, `title`, `description`, and a birth `timestamp` stamped once — and cross-links to other pages with relative markdown links. Formats for each artifact are in this folder: `decision-format.md`, `provenance-format.md`, `glossary-format.md`.

Before you finish a write, append a line to `docs/log.md` (`## [date] grill | Title`) and update `docs/index.md`.
