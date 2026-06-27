---
name: setup-docs
description: Scaffold a canon project, link a repo to an existing project's evidence trail, or tune how the skills behave. Use when setting canon up in a project for the first time, linking to an existing project's docs, or when the user wants to change how the skills work (too chatty, asking too often, memory in the wrong place). Do NOT use for ordinary modeling work; this skill only writes the config layer.
---

This skill writes the config layer: the schema and the steering block in `CLAUDE.md`. No other skill writes them.

Two modes: **new project** and **linked**.

## New project mode

Explore first. Look at the project before asking anything: is there already a `CLAUDE.md`, a git remote, a `docs/` directory. Present what you found, then ask only what you could not work out, one question at a time:

- Where the project memory should live: in the model's repo, its own repo, or alongside as a submodule.
- How to check in while working: confirm each write, or work in a batch and show the user periodically.
- Whether to enable GitHub wiki sync (if the repo has a GitHub remote). Optional — the wiki works fine as plain files.

Use defaults from `schema.template.md` for everything else, and mention that they are editable.

Scaffold the full directory tree up front so the user can see the structure immediately. Create the `docs/` root and all zone directories (`docs/sources/`, `docs/evidence/findings/`, `docs/evidence/decisions/`, `docs/wiki/`, `docs/views/`) even if they start empty. Seed the root `docs/index.md` with its `okf_version: "0.1"` frontmatter.

Write the schema and the `CLAUDE.md` steering block at the end. Start from `schema.template.md` and `CLAUDE.template.md` in this folder.

If the project has existing sources, code, or undocumented decisions, point the user to `onramp-docs` to survey and plan their ingestion.

## Linked mode

Use when the user says this repo should share an existing project's evidence trail — e.g. "link to ../poc-doxypep" or "set this up as a calibration repo for ...". Do not assume calibration; the workspace might be for sensitivity analysis, presentations, or any other purpose.

Explore first. Check whether the upstream `docs/` exists and has a schema. Check whether this repo already has a `docs/` directory or symlink. Check what other skill systems or plugins are loaded (look at `CLAUDE.md`, `.claude/`, plugin configs) — note their presence so the `CLAUDE.md` steering block can mention them, but do not hardcode any specific plugin.

Ask the user, one question at a time:

1. **Upstream project** — where is the upstream project root? (e.g. `../poc-doxypep`). Recommend based on sibling directories if possible. The symlink will target `<upstream>/docs/`.
2. **Workspace name** — what should this repo's workspace be called? Recommend a short slug based on the repo name (e.g. `calib-zim` for `poc-doxypep-calib-zim`, `sensitivity-network` for a sensitivity analysis repo). This becomes a subdirectory under `evidence/findings/`.
3. **Workspace description** — a one-line description of what this workspace is for.

Then:

1. Create the symlink: `docs/ -> <upstream-path>/docs/`.
2. Add `docs` to `.gitignore` (the upstream repo tracks it, not this one).
3. Create the workspace subdirectory: `docs/evidence/findings/<workspace>/`.
4. Register the workspace in the shared `docs/schema.md` — add an entry to the `workspaces` list with name, description, and repo.
5. Write the `CLAUDE.md` steering block, noting: the shared docs path, the workspace name, and any other loaded skill systems or plugins. Use the `CLAUDE.template.md` as a base and add the linked-repo context.
6. Append to `docs/log.md`: `## [date] setup | Linked workspace: <workspace>`.

Do not scaffold zone directories — they already exist in the upstream. Do not create a new schema — use the upstream's.

## Tuning (both modes)

When re-run to tune, take the complaint in plain words, find the setting it maps to (check-in cadence and grilling intensity live in `CLAUDE.md`; the rest live in the schema), change it, and say what changed.
