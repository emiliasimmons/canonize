---
name: maintain-docs
description: Run a health pass over the project — find what is broken, fix the mechanical parts, and propose the structural ones. Use when the user asks for a health check, a cleanup, or to fix internal consistency, or when the agent has noticed something clearly broken and the user agrees to a pass. Do NOT use when "maintain" or "clean up" appear in passing about other things.
---

Orient with /canon. Both modes use the /canon script.

## Mechanical (unilateral)

Fix in one pass, no permission needed:

- **Broken and non-root-anchored links.** /canon check --links finds them. A moved page's outgoing links survive root-anchoring; only inbound links need repair, and this is that greppable set.
- **Format conformance.** /canon check --frontmatter flags pages missing `type` or the authored core, or carrying an unregistered type.
- **Full recompile.** /canon compile regenerates every compiled surface from frontmatter. Run it to heal any block that drifted.
- **Orphan and near-duplicate tags.** Flag tags past the aging threshold with too few members, and merge near-duplicates into one canonical form.
- **Aged placeholders.** Provisional DRs past the placeholder-aging threshold: surface them for the user to revisit.

## Structural curation (proposal + sign-off)

These change the taxonomy, so argue each one conversationally and get approval before files move:

- **Split a fat topic** or **merge duplicate topics**; **rename** as vocabulary sharpens; **move member pages** between topics.
- **Rewrite a hub synthesis** — the only thing that resets a hub's staleness counter and stamps the rewrite date. Surface stale hubs (by counter) when you run.

Moves go through the file system, then /canon check --links to repair inbound links and /canon compile to regenerate the affected blocks.

## Boundary

Only reads the project's own pages. Checks against the model's **code** belong to /audit-code. Anything needing a real decision or re-synthesis (a contradiction, lifecycle drift, a missing concept page) — flag and route to /grill-with-docs or /query-docs. Repairs commit with a `maintain:` message.
