---
name: audit-code-with-docs
description: Check that the model's code and its recorded reasoning still agree. Use when the user wants to verify the code matches the project record, before a release or review, or when checking for drift between code values and provenance. Do NOT use to check whether the model fits the data; that is a finding from an analysis, recorded with wiki-ingest.
---

The reproducibility check, and the only skill that reads the model's code. Read it, never run it. Report findings in the conversation and route actionable items through `grill-with-docs` or `wiki-ingest` — do not write to the project record directly.

Values. Find provenance docs in the wiki by their `type: provenance` frontmatter. Each one names where its value lives in code. Follow that pointer and check the value matches. A frozen value that disagrees with code is a problem. Then scan the code the other way: any value with no provenance pointing at it is an orphan worth flagging.

Implementation. Read the code against the decisions (DRs) and check it still does what they say. Is the thing a DR calls a random screen still a random screen? Has a structural change slipped in without a DR being superseded? This is the part that needs real reading, not a lookup.

If the project memory is shared across repos, audit only this repo against the shared record.
