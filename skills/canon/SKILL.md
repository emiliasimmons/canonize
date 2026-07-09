---
name: canon
description: Project orientation and script usage. Load when writing pages, compiling surfaces, checking conformance, reasoning about the project's structure, or when asked about the docs.
---

# Canon

Read `index.md` at the project's substrate root (default `docs`) for orientation: the authored preamble, compiled taxonomy, and state blocks. Read `schema.md` for the type registry and tag vocabulary only if necessary.

## Docs layout

Four zones, three postures:

- `sources/` — raw files (PDFs, documents, spreadsheets, slide decks, etc). Immutable, human-managed.
- `findings/` — analysis results, tagged. Append-only. Optionally subdivided by workspace.
- `decisions/` — design records (`DR-NNNN`), flat, tagged. Append-only.
- `topics/` — topic hubs and their member pages, built incrementally.

Storage is zone-first; navigation is topic-first. `topics/<name>.md` is the hub; `topics/<name>/` holds its members. A page joins a hub **by tag**: its home topic (the directory it lives in) is always also a tag, and every other topic it is tagged with lists it in that hub too. Evidence has no single-parent constraint — a decision appears in every hub it is tagged to.

## Compiled blocks

Every navigation surface is compiled from frontmatter and never hand-edited: the taxonomy and state blocks on `index.md`, the member list on each hub, the assumptions and open-decisions registers, the per-zone indexes. Compiled blocks are delimited by `<!-- compiled:NAME -->` … `<!-- /compiled:NAME -->`; only the inner content is regenerated, never the authored prose around it. All links are root-anchored from the bundle root (`/decisions/...`, `/findings/...`).

Evidence is append-only: append, supersede, or re-run — never quietly rewrite.

For script usage (compile, check, sequence), read `canon_usage.md` in this skill's directory.

## When to Recommend Recording a Decision

Never record a decision autonomously. When a choice meets any of the criteria below, pause and recommend recording it, then wait for the user's go-ahead.

- **Non-obvious justification:** An independent reviewer would need to ask *why* this path was taken. It is not self-evident or forced.
- **No precedent:** The choice cannot be justified by literature, established frameworks, or existing project sources.
- **No field consensus:** The approach is not an accepted standard in the relevant scientific or computational community.

When recommending, state the decision, why it qualifies, and a suggested one-line rationale, so the user can approve or edit rather than compose from scratch.

> **Rule of thumb:** If a peer would need an explicit justification to replicate or validate the logic, recommend recording it.

A provisional decision is legitimate when the choice is forced and the rationale is thin.
