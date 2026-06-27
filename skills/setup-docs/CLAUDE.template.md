# docs steering block

`setup-docs` adds this block to the project's `CLAUDE.md`. Keep it short. Add to it when a real preference shows up; re-run `setup-docs` to change it.

## New project

```markdown
## docs

- Check-in: [confirm each write | batch and show periodically]
- Grilling: relentless by default. One question at a time, each with a recommended answer.
- Changes to immutable evidence (the cleanup half of maintain-docs) always ask first, batched by related change, and log what changed.

To change how the skills behave, re-run setup-docs and say what is annoying.
```

## Linked repo

Add these bullets to the steering block. List any other loaded skill systems or plugins with their purpose.

```markdown
## docs

- Shared docs: symlinked from <upstream project path>
- Workspace: <name> (findings write to evidence/findings/<name>/)
- [Other plugin]: <one-line purpose, e.g. "manages experiment lifecycle in experiments/">
- Check-in: [confirm each write | batch and show periodically]
- Grilling: relentless by default. One question at a time, each with a recommended answer.
- Changes to immutable evidence (the cleanup half of maintain-docs) always ask first, batched by related change, and log what changed.

To change how the skills behave, re-run setup-docs and say what is annoying.
```
