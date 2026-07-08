# Trace format

Stock-optional type. A trace is the trail behind one thing, written out end to end. Live traces are ephemeral `query-docs` output; store one only on an explicit freeze — a date-stamped snapshot you want to keep.

File (only when frozen): `wiki/topics/<topic>/<name>.md`, type `trace`.

**Frontmatter:**

```
---
type: trace
title: <what is being traced>
description: <one line: the trail in brief>
timestamp: <ISO 8601, the freeze date>
tags: [<topic names and cross-cutting themes>]
derived_from: [<root-anchored links to the evidence on the trail>]
---
```

**Scope, by what is asked:**

- a parameter: value → provenance → the evidence under it
- a finding: → its inputs and method
- a result or figure: → its finding → the parameter set as it was run → each value's provenance

A frozen trace is a snapshot: it reports the values as they were when it ran. A recomputed trace reflects current provenance; a stored one rots. That is why storage is the exception, not the routine — freeze only when the snapshot itself is the artifact worth keeping.
