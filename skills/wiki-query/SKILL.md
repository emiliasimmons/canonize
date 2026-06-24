---
name: wiki-query
description: Answer a question over the project's evidence, or trace a value, finding, or result back through its provenance. Use when the user asks why something is the way it is, asks to trace where a number came from, or wants the assumptions or open-decisions registers refreshed.
---

Everything you write here must trace to something in the sources or evidence layer.

Answering. Most questions just get answered in the conversation. When the answer is a real synthesis you would hate to re-derive in six months, offer to keep it as a page in `docs/wiki/` (type `concept`). The user decides. The wiki stays made of things worth keeping.

Tracing. Follow the citation graph end to end, at whatever scope is asked:

- a parameter: value -> provenance -> the evidence under it
- a finding: -> its inputs and method
- a result or figure: -> its finding -> the parameter set as it was run -> each value's provenance

Be honest about history. For an old result, report the values as they were when it ran, and flag anywhere the current provenance has since moved. This is how a frozen set is rebuilt; there is no separate manifest to keep.

You also compile the two registers: the assumptions register from accepted DRs, and the open-decisions register from provisional DRs. Each register is a wiki page of type `register` whose body is regenerated on each compile (read the DRs' `status` frontmatter to sort them). Never hand-append to a register — manual lines are overwritten on recompile.

Every page you file — concept, trace, or register — is conformant: it carries the authored-core frontmatter (`type`, `title`, `description`, a birth `timestamp` stamped once) and links with relative markdown links. Format is in this folder: `trace-format.md`.

When you file a page, append a line to `docs/log.md` (`## [date] query | Title`) and update `docs/index.md`.
