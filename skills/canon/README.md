# canon

The deterministic layer beneath the skills. One Python script, stdlib only, living beside the skills and invoked only by them. A project never needs it — a project is pure data. `canon` owns exactly the mechanical work that drifts when an LLM does it by hand: block regeneration, conformance checking, DR sequencing. Everything judgement-shaped stays in skill prose.

## Invoking it

The script ships beside the skills. From a skill, resolve it relative to the skill's own directory and run it against the project's substrate root:

```
python3 <canonize-skills>/canon/canon.py --root <substrate-root> <subcommand>
```

`<canonize-skills>` is the directory these skills live in (the parent of this `canon/` folder); `<substrate-root>` is the project's bundle root (default `docs`).

## Subcommands

- `compile [--block taxonomy|state|members|registers|indexes|all] [--page HUB ...]`
  Regenerate compiled blocks from frontmatter. `all` (default) does a full-corpus recompile; a named `--block` (and, for `members`, one or more `--page` hubs) is the incremental routine path. Idempotent: recompiling an unchanged corpus writes nothing.

- `check [--frontmatter] [--links]`
  Conformance against the type registry (every page has a `type`; authored core present) and link integrity (root-anchored links resolve; file-relative `.md` links are flagged). With no flag it runs both. Exit status is non-zero when a blocking issue is found.

- `sequence --kind decision`
  Print the next `DR-NNNN` id atomically from the existing decisions.

## What it reads

`schema.md` at the substrate root: the `## Settings` bullets, the `## Type registry` table, and the `## Tag vocabulary` table. The registry's `surfaces` column drives which types appear in hub member lists and taxonomy counts, so a new type becomes hub-visible with a registry row and no code change.

Compiled blocks are delimited by `<!-- compiled:NAME -->` … `<!-- /compiled:NAME -->`. `canon` replaces only the inner content and never touches authored prose around a block.
