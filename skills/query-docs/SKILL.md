---
name: query-docs
description: Answer a question over the project's evidence, or trace a value, finding, or result back through its provenance. Use when the user asks why something is the way it is, asks where a number came from, or wants a value traced end to end. Read-only; offers to keep an expensive answer as a page.
---

Read-only. Answer over the corpus; compile nothing. Everything you say traces to sources or evidence.

## Answering

Most questions get answered in the conversation. Read the taxonomy block at the top of `<root>/index.md` to find the relevant topic hubs, then the hub syntheses and their members. When an answer is a real synthesis you would hate to re-derive in six months, offer to keep it — on acceptance, /record-doc files a `concept` page into the right topic. The user decides; the wiki stays made of things worth keeping.

## Tracing

Compute traces **live** by walking the typed relations in frontmatter — `derived_from`, `bears_on`, `supersedes` — end to end, at whatever scope is asked:

- a parameter: value → its provenance → the evidence under it
- a finding: → its inputs and method
- a result or figure: → its finding → the parameter set as it was run → each value's provenance

**Be honest about history.** For an old result, report the values as they were when it ran, and flag anywhere the provenance has since moved. Repeated queries recompute. Store a trace only on an explicit freeze — the stock-optional `trace` type, a date-stamped snapshot filed through /record-doc.

Do not recompile registers; route a stale-register request to /maintain-docs.
