---
name: to-issues
description: Turn an open item in the project into a tracked issue, and close it when it resolves. Use when an open question or placeholder needs to be schedulable, or when called by grill-with-docs or wiki-query. Do NOT use when the user says "track" about something unrelated.
---

The link between the project's open items and wherever you schedule work. The project stays the source of truth for what is open; the issue is just the schedulable copy of it.

When an open question or placeholder lands, spawn an issue carrying a link back to its MDR. When the item resolves, close the issue. You can also read issue status back for planning.

If no tracker is set, append the item to the open-decisions register in the wiki so it is still visible. The user wires a tracker through `setup-docs`.
