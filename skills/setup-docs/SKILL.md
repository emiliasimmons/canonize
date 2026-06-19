---
name: setup-docs
description: Scaffold a canon project and tune how the skills behave. Use when setting canon up in a project for the first time, or when the user wants to change how the skills work (too chatty, asking too often, wrong tracker, memory in the wrong place). Do NOT use for ordinary modeling work; this skill only writes the config layer.
---

Run this once to set a project up, and again any time the behavior needs tuning. You own the config layer: the schema (the file every other skill reads to find its way around) and the steering block in `CLAUDE.md`. Nothing else writes them, so this is the one place that knows where every setting lives.

Explore first. Look at the project before asking anything: is there already a `CLAUDE.md`, a git remote, a `docs/` directory. Present what you found, then ask only what you could not work out, one question at a time:

- Where the project memory should live: in the model's repo, its own repo, or alongside as a submodule.
- What tracks to-dos, if anything: git issues, or nothing for now.
- How to check in while working: confirm each write, or work in a batch and show the user periodically.
- Whether to set up GitHub wiki sync for the wiki zone. If the repo has a GitHub remote, offer to enable the GitHub wiki and explain that `docs/wiki/` content can be pushed to `<repo>.wiki.git` so collaborators can browse it through the GitHub wiki UI. This is optional — the wiki works fine as plain files in-repo.

Default everything else silently, and tell the user it is editable: the four justification kinds (measured, derived, calibrated, assumed), the MDR statuses (provisional, accepted, superseded), how the parameter lifecycle is read off rather than set, the wiki page types (provenance, source, trace, concept — see the schema), the log and index formats (`index-format.md` in this folder), where each format doc lives, and the placeholder-aging threshold. Capture starts as a plain inbox folder with no external channel.

Scaffold the full directory tree up front so the user can see the structure immediately. Create the `docs/` root and all zone directories (`docs/inbox/`, `docs/sources/`, `docs/evidence/findings/`, `docs/evidence/mdr/`, `docs/wiki/`) even if they start empty.

When re-run to tune, take the complaint in plain words, find the setting it maps to (check-in cadence and grilling intensity live in `CLAUDE.md`; the rest live in the schema), change it, and say what changed.

Write the schema and the `CLAUDE.md` steering block at the end. Start from `schema.template.md` and `CLAUDE.template.md` in this folder.

If the project has existing sources, code, or undocumented decisions, point the user to `onramp` to survey and plan their ingestion.
