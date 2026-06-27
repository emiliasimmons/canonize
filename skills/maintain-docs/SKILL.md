---
name: maintain-docs
description: Run a health pass over the project, find what is broken and tidy it up in one go. Use when the user asks for a health check, a cleanup, or to fix the project's internal consistency, or when the agent has noticed something clearly broken and the user agrees to a pass. Do NOT use when "maintain" or "clean up" appear in passing about other things.
---

What to look for:

- orphans
- pages that contradict each other
- claims a newer source has overtaken
- missing or broken cross-references
- frontmatter missing or non-conformant (no `type`, or missing the authored core `title`/`description`)
- pages that carry their `type` but have no cross-links (flag for re-linking)
- wiki claims that no longer trace back to sources or evidence
- index entries that do not match what actually exists
- workspace registered in the schema but its directory missing, or a subdirectory under `evidence/findings/` that is not a registered workspace
- placeholders past the aging threshold
- provenance still showing a prior when a calibration finding now exists

This half only reads the project. Checks against the model's code belong to `audit-code-with-docs`.

Then repair. Prefer supersession: to fix a source summary, write a corrected one and mark the old one superseded; to resolve duplicate decisions, write a new DR that supersedes both. If the user chooses to rewrite an evidence file directly instead, that is their call, but log what changed and why in `docs/log.md` and update `docs/index.md` before making the edit. Either way, confirm repairs with the user first, grouped by related change rather than one prompt at a time.

Anything that needs a real decision or a re-synthesis (a contradiction, lifecycle drift, a missing concept page) you flag and route to `grill-with-docs` or `wiki-query`. You do not resolve it here.

Log all repairs to `docs/log.md` and update `docs/index.md`.
