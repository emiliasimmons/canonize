# canon.py usage

## Invoking the script

Resolve `canon.py` relative to this skill's directory and run it against the project's substrate root (default `docs`, set in `schema.md`):

```
python3 <canon-skill-path>/canon.py --root <substrate-root> <subcommand>
```

## Subcommands

### compile — regenerate compiled blocks from frontmatter

Incremental (named blocks) in the routine write path; full-corpus (`all`, the default) as a maintenance repair. Recompiling an unchanged corpus writes nothing.

```
--block members --page <hub> …    one or more hubs a written page joined
--block taxonomy --block state    the root, after any page write
--block registers                 after any decision write or supersession
                                   (no flag = full recompile of everything)
```

One call carries several `--block`/`--page` flags.

### check — conformance and link integrity

```
--frontmatter    every page has a type; authored core present; type is registered
--links          root-anchored links resolve; file-relative .md links flagged
                 (no flag = both)
```

Non-zero exit on a blocking issue.

### sequence — hand out the next id

```
--kind decision    prints the next DR-NNNN atomically
```

Never pick a DR number by hand.

## What it reads

`schema.md` at the substrate root: the `## Settings` bullets, the `## Type registry` table, and the `## Tag vocabulary` table. The registry's `surfaces` column drives which types appear in hub member lists and taxonomy counts, so a new type becomes hub-visible with a registry row and no code change.
