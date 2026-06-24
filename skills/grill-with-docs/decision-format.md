# Decision format

A decision record (DR) is a decision about the model, kept as immutable evidence. It is the domain-neutral sibling of an ADR — the modeling analog of one.

File: `docs/evidence/decisions/DR-NNNN-kebab-title.md`, numbered in sequence. Type `decision`.

**Frontmatter:**

```
---
type: decision
title: <the decision as a short noun phrase>
description: <one line: what was decided>
timestamp: <ISO 8601, stamped once at creation>
status: <provisional | accepted | superseded by DR-NNNN>
---
```

`title` and `description` are the authored core — they render as the node label and hover text in a compiled view, and as the line in the index. `timestamp` is stamped once at birth and never hand-maintained. `status` lives in frontmatter so the assumptions and open-decisions registers can be compiled by reading it.

**Status**, one of:

- `provisional` : an expedient choice made to unblock work.
- `accepted` : a considered decision.
- `superseded by DR-NNNN` : replaced. The replacement carries the real reasoning.

**When to write one.** Not "is it hard to undo." Write a DR when a reader of the model or its results would be misled without it. That catches two cases the old "hard to reverse" test misses:

- a structural choice that is easy to change in code but shapes how every result is read (well-mixed vs age-structured), and
- a placeholder, which is trivial to undo but disastrous to leave unrecorded, because someone will build on it thinking it is settled.

**Body shape:**

- the decision, in a line or two
- why. For a provisional, why it was the parsimonious thing to unblock work.
- for a provisional: the open question it stands in for, and the trigger that should make you revisit it
- links to the provenance docs or findings it bears on, as relative markdown links (`../../wiki/<name>.md`, `../findings/<name>.md`)
- a `# Citations` section if the decision rests on external sources

A DR never points at code; code changes, decisions don't. Code pointers live in provenance docs, not here.

A plainly stated assumption is still a decision: record it as an `accepted` DR. The assumptions register is compiled from these, so adding to that register costs no more than typing the assumption down.
