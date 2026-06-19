# MDR format

An MDR (Model Design Record) is a decision about the model, kept as immutable evidence. It is the modeling analog of an ADR.

File: `docs/evidence/mdr/NNNN-kebab-title.md`, numbered in sequence.

**Status**, one of:

- `provisional` : an expedient choice made to unblock work.
- `accepted` : a considered decision.
- `superseded by MDR-NNNN` : replaced. The replacement carries the real reasoning.

**When to write one.** Not "is it hard to undo." Write an MDR when a reader of the model or its results would be misled without it. That catches two cases the old "hard to reverse" test misses:

- a structural choice that is easy to change in code but shapes how every result is read (well-mixed vs age-structured), and
- a placeholder, which is trivial to undo but disastrous to leave unrecorded, because someone will build on it thinking it is settled.

**Shape:**

- title and status
- the decision, in a line or two
- why. For a provisional, why it was the parsimonious thing to unblock work.
- for a provisional: the open question it stands in for, and the trigger that should make you revisit it
- links to the provenance docs or findings it bears on

A plainly stated assumption is still a decision: record it as an `accepted` MDR. The assumptions register is compiled from these, so adding to that register costs no more than typing the assumption down.
