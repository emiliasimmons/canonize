---
name: maintain-docs
description: Run a health pass over the project, find what is broken and tidy it up in one go. Also triages the inbox. Use when the user asks for a health check, a cleanup, to triage the inbox, or to fix the project's internal consistency, or when the agent has noticed something clearly broken and the user agrees to a pass. Do NOT use when "maintain" or "clean up" appear in passing about other things.
---

Find what is broken and fix the tidying parts, in one pass. Run it when asked. The rest of the time, if you happen to notice something clearly broken while doing other work, say so and offer a pass. Never run it unprompted, and never on a schedule.

What to look for: orphans, pages that contradict each other, claims a newer source has overtaken, missing or broken cross-references, wiki pages with missing or wrong `type:` frontmatter, the regenerability check that every wiki claim still traces to sources or evidence, index entries that do not match what actually exists, placeholders that have sat past the aging threshold, provenance still showing a prior when a calibration finding now exists, and inbox scraps that were never triaged. This half only reads the project. Checks against the model's code belong to `audit-code-with-docs`.

To triage the inbox, route each item to where it belongs: a value's justification to `grill-with-docs`, a source to `wiki-ingest`, a tangent to `to-issues` or discard. Clear the inbox as items are routed.

Then repair. Prefer supersession: to fix a source summary, write a corrected one and mark the old one superseded; to resolve duplicate MDRs, write a new MDR that supersedes both. If the user chooses to rewrite an evidence file directly instead, that is their call, but log what changed and why in `docs/log.md` and update `docs/index.md` before making the edit. Either way, confirm repairs with the user first, grouped by related change rather than one prompt at a time.

Anything that needs a real decision or a re-synthesis (a contradiction, lifecycle drift, a missing concept page) you flag and route to `grill-with-docs` or `wiki-query`. You do not resolve it here.
