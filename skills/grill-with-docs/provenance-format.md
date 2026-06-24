# Provenance format

A provenance doc records why a parameter has the value it does. The why lives here in the wiki; the value itself, the what, lives in the model's code.

File: `docs/wiki/<name>.md`, type `provenance`.

**Frontmatter:**

```
---
type: provenance
title: <the parameter>
description: <one line: the value and how it was obtained>
timestamp: <ISO 8601, stamped once at creation>
---
```

**Record:**

- the parameter and what it represents
- how the value was obtained, one of:
  - `measured` : literature reports the parameter directly.
  - `derived` : no direct data; built from proxy evidence through an inference step.
  - `calibrated` : fit to model output against targets.
  - `assumed` : expert judgment, no data. Flag this one loudly as an assumption.
- the basis: the finding, source, or decision (DR) the value rests on, by relative link
- a pointer to where the value lives in code (path and symbol), so `audit-code-with-docs` can check the two against each other

**Do not record a lifecycle stage by hand.** The stage (prior, calibrated, frozen) is read off the evidence: sources only reads as a prior; a calibration finding existing reads as calibrated. There is no step that advances it.
