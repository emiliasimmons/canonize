# docs steering block

`setup-canon` adds this block to the project's agent instructions file (`AGENTS.md`, or `CLAUDE.md` if that is what the project already uses). Keep it short. Add to it when a real preference shows up; re-run `setup-canon` to change it. Check-in cadence and grilling intensity live here; the rest of the config lives in `schema.md`.

## New project

```markdown
## docs

- Substrate root: <root> (single OKF bundle; canon compiles the spine)
- Check-in: [confirm each write | batch and show periodically]
- Grilling: relentless by default. One question at a time, each with a recommended answer.
- Structural changes (new topic, new type, split/merge/rename) need sign-off; tag minting is unilateral but registered in the same write.

To change how the skills behave, re-run setup-canon and say what is annoying.
```

## Linked repo

Add these bullets and list any other loaded skill systems or plugins with their purpose.

```markdown
## docs

- Shared docs: symlinked from <upstream project path>
- Workspace: <name> (findings write to findings/<name>/)
- [Other plugin]: <one-line purpose>
- Check-in: [confirm each write | batch and show periodically]
- Grilling: relentless by default. One question at a time, each with a recommended answer.
- Structural changes need sign-off; tag minting is unilateral but registered.

To change how the skills behave, re-run setup-canon and say what is annoying.
```
