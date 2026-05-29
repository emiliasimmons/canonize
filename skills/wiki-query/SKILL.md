---
name: wiki-query
description: Answer a question over the project's evidence, or trace a value, finding, or result back through its provenance. Use when the user asks why something is the way it is, asks to trace where a number came from, or wants the assumptions or open-decisions registers refreshed.
---

Answer questions over sources and evidence, and follow the trail back when asked. Everything you write here must trace to something in the sources or evidence layer.

Answering. Most questions just get answered in the conversation. When the answer is a real synthesis you would hate to re-derive in six months, offer to keep it as a page in `wiki/` (type `concept`). The user decides. The wiki stays made of things worth keeping.

Tracing. Follow the citation graph end to end, at whatever scope is asked:

- a parameter: value -> provenance -> the evidence under it
- a finding: -> its inputs and method
- a result or figure: -> its finding -> the parameter set as it was run -> each value's provenance

Be honest about history. For an old result, report the values as they were when it ran, and flag anywhere the current provenance has since moved. This is how a frozen set is rebuilt; there is no separate manifest to keep.

You also compile the two registers, both regenerable, never hand-kept: the assumptions register from accepted MDRs, and the open-decisions register from provisional MDRs.

Format is in this folder: `trace-format.md`.

When you file a page, append a line to `log.md` (`## [date] query | Title`) and update `index.md`.
