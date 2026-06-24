---
name: setup-docs
description: Scaffold a canon project and tune how the skills behave. Use when setting canon up in a project for the first time, or when the user wants to change how the skills work (too chatty, asking too often, memory in the wrong place). Do NOT use for ordinary modeling work; this skill only writes the config layer.
---

This skill writes the config layer: the schema and the steering block in `CLAUDE.md`. No other skill writes them.

Explore first. Look at the project before asking anything: is there already a `CLAUDE.md`, a git remote, a `docs/` directory. Present what you found, then ask only what you could not work out, one question at a time:

- Where the project memory should live: in the model's repo, its own repo, or alongside as a submodule.
- How to check in while working: confirm each write, or work in a batch and show the user periodically.
- Whether to enable GitHub wiki sync (if the repo has a GitHub remote). Optional — the wiki works fine as plain files.

Use defaults from `schema.template.md` for everything else, and mention that they are editable.

Scaffold the full directory tree up front so the user can see the structure immediately. Create the `docs/` root and all zone directories (`docs/sources/`, `docs/evidence/findings/`, `docs/evidence/decisions/`, `docs/wiki/`, `docs/views/`) even if they start empty. Seed the root `docs/index.md` with its `okf_version: "0.1"` frontmatter.

When re-run to tune, take the complaint in plain words, find the setting it maps to (check-in cadence and grilling intensity live in `CLAUDE.md`; the rest live in the schema), change it, and say what changed.

Write the schema and the `CLAUDE.md` steering block at the end. Start from `schema.template.md` and `CLAUDE.template.md` in this folder.

If the project has existing sources, code, or undocumented decisions, point the user to `onramp-docs` to survey and plan their ingestion.
