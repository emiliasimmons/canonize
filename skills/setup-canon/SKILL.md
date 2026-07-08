---
name: setup-canon
description: Bootstrap a canon project, adopt an existing one, link a repo to a shared evidence trail, or tune how the skills behave. Use when setting canon up for the first time, adopting a project that already has sources or code, linking to another project's docs, or when the user wants to change how the skills work (too chatty, asking too often). Do NOT use for ordinary modeling work; this skill only writes the config layer and scaffold.
disable-model-invocation: true
---

This skill writes the config layer: `schema.md`, the root orientation page, the directory scaffold, and the `## docs` steering block. No other skill writes them. Start from `schema.template.md` and `steering.template.md` in this folder, and load /canon for the layout and the script.

Three modes: **new project**, **adopt**, **linked**.

## New project

Explore first. Look before asking: existing agent instructions file, git remote, any `docs/` directory. Present what you found, then ask only what you could not work out, one question at a time:

- Where the memory lives: the model's repo, its own repo, or a submodule (sets `substrate_root`).
- Check-in cadence: confirm each write, or batch and show periodically.
- Whether to enable GitHub wiki sync, if the repo has a GitHub remote (optional).

Use `schema.template.md` defaults for everything else and say they are editable.

Scaffold the tree up front so the structure is visible immediately:

- directories: `<root>/sources/`, `<root>/evidence/findings/`, `<root>/evidence/decisions/`, `<root>/wiki/topics/`, `<root>/views/`
- `<root>/index.md`: `okf_version: "0.1"` frontmatter (its only frontmatter), a short authored preamble written like a wiki landing page, then the two compiled markers `<!-- compiled:taxonomy -->…<!-- /compiled:taxonomy -->` and `<!-- compiled:state -->…<!-- /compiled:state -->`, then links to the registers and glossary
- `<root>/wiki/glossary.md`, `<root>/wiki/assumptions.md`, `<root>/wiki/open-decisions.md` — the registers scaffolded with a `<!-- compiled:register -->` block each (formats in `record-doc/`)
- `<root>/schema.md` from the template, with the chosen values filled and an empty `## Tag vocabulary` table

Offer the **stock-optional** types (`provenance`, `trace`); for each the user accepts, copy its row from the template's stock-optionals table into the live `## Type registry`. Custom types are not minted here unless asked — that is a brief /grilling session on what the type captures, then a registry row plus a format doc from the template, with sign-off.

Finish: run /canon compile to populate the empty spine, /canon check to confirm conformance, write the steering block, and commit `setup: scaffold canon project`.

If the project already has sources, code, or undocumented decisions, go to adopt.

## Adopt

Adoption is setup plus one batch ingest — no separate onramp machinery, no plan file. Run the new-project scaffold first, then hand the existing sources to /ingest-source in batch mode. That first batch doubles as initial taxonomy construction: with no topics yet, the placement plan's clusters *are* the proposed topic set. The user approves the taxonomy and placements once, and it executes. Undocumented decisions surfaced while reading are proposed as DRs through /record-doc.

## Linked

Use when this repo should share another project's evidence trail ("link to ../poc-doxypep", "set this up as a calibration repo for …"). Do not assume the purpose; the workspace might be calibration, sensitivity analysis, presentations, or anything.

Explore first: does the upstream `docs/` exist with a `schema.md`; does this repo already have a `docs/` or symlink; what other skill systems or plugins are loaded. Then ask, one at a time:

1. **Upstream project** — the upstream root (e.g. `../poc-doxypep`); the symlink targets `<upstream>/docs/`.
2. **Workspace name** — a short slug from the repo name; becomes `evidence/findings/<name>/`.
3. **Workspace description** — one line.

Then:

1. Symlink `docs/ -> <upstream>/docs/`.
2. Add `docs` to `.gitignore` (the upstream tracks it).
3. Create `docs/evidence/findings/<workspace>/`.
4. Register the workspace in the shared `schema.md` `workspaces` list (name, description, repo).
5. Write the steering block noting the shared path, the workspace, and any other loaded skill systems.
6. Commit `setup: link workspace <workspace>`.

Do not scaffold zones or write a new schema — the upstream owns them.

## Tuning (any mode)

Take the complaint in plain words, map it to its setting (check-in cadence and grilling live in the steering block; thresholds and types live in `schema.md`), change it, and say what changed.
