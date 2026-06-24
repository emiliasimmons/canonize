# Trace format

A trace is the trail behind one thing, written out end to end. It is regenerated on demand; keep one only if it is worth keeping.

File (if kept): `docs/wiki/<name>.md`, type `trace`.

**Frontmatter:**

```
---
type: trace
title: <what is being traced>
description: <one line: the trail in brief>
timestamp: <ISO 8601, stamped once at creation>
---
```

**Scope, by what is asked:**

- a parameter: value -> provenance -> the evidence under it
- a finding: -> its inputs and method
- a result or figure: -> its finding -> the parameter set as it was run -> each value's provenance

Always report an old result with the values as they were when it ran, and flag where the current provenance has since moved. The trace is what reconstructs a frozen set, so this honesty about then versus now is the whole point.
