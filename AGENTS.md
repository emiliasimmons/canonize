Composable agent skills for computational modelers — structured evidence trails behind every modeling decision. Pure Markdown, no runtime code.

## Architecture pointers

- For the skill system design and zone model (`docs/sources`, `docs/evidence`, `docs/wiki`, `docs/views`): `README.md`
- For individual skill behavior: `skills/<skill-name>/SKILL.md`
- For the LLM Wiki substrate pattern: `references/llm-wiki.md`
- For the upstream skills pattern: `references/skills/`

## Code conventions

Skills follow this pattern: each skill lives in `skills/<name>/` with a `SKILL.md` and optional format docs. Names describe what you are doing, not which system they belong to:

```
skills/grill-with-docs/
├── SKILL.md            # skill behavior and triggers
├── mdr-format.md       # format reference used by this skill
├── provenance-format.md
└── glossary-format.md
```

Format documents are reference material for their parent skill, not standalone specs.

## Boundaries

- **Always**: evidence layer is append-only — append, re-run, or supersede; never quietly rewrite existing entries.
- **Always**: wiki content must trace back to sources or evidence; if the backing material is removed, the wiki claim is invalid.
- **Ask first**: any modification to immutable evidence. `maintain-docs` prefers supersession; direct rewrites require user confirmation and a log entry.
- **Ask first**: changes to `docs/schema.md` or the `## docs` steering block.
- **Never** edit files under `references/` directly → re-vendor (replace the local copy) or add new reference files at `references/` root.

## Gotchas

- `references/` is **gitignored** vendor/reference material (`.gitignore` is literally `references`; no submodule, no `.gitmodules`). It is not tracked — anything built under `references/` is invisible to git, which is why substrate is vendored into `skills/` rather than built in place.
- Three zones have different mutability: `docs/sources/` is immutable and human-managed, `docs/evidence/` is immutable (append/supersede only), `docs/wiki/` is mutable and built incrementally from sources and evidence. Workspace subdirectories under `evidence/findings/` are governed by the same immutability rules as the rest of evidence.
- Parameter lifecycle stage (prior/calibrated/etc.) is **read from evidence**, never set by hand — the wiki compiles it.
- `audit-code-with-docs` is the only skill that reads model code, and it is strictly read-only (reports, never fixes).
