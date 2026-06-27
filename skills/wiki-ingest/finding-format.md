# Finding format

A finding is the result of an analysis you ran. It must carry enough detail that someone could understand the claim, cite the key numbers, and act on the implications without opening the full analysis record.

This format is the shared contract between canonize and any external tool that produces findings (e.g. a calibration plugin's experiment-close step). An agent with canonize loaded handles index, log, and zone rules; the template below specifies only the page format.

File: `docs/evidence/findings/<short-name>.md`, type `finding`. When the project uses workspaces, findings go in the workspace subdirectory: `docs/evidence/findings/<workspace>/<short-name>.md`. The filename should mirror the analysis artifact it came from (e.g. `02_syph_observability.md` for an experiment directory of the same name).

**Frontmatter:**

```yaml
---
type: finding
title: <the question the analysis answered, as a short phrase>
description: <one-line result>
timestamp: <ISO 8601, stamped once at creation>
tags: [<flat, composable tags — e.g. calibration, zimbabwe>]
resource: <path to the full analysis record, e.g. experiments/02_syph_observability/SUMMARY.md>
---
```

`tags` (optional, defaults to `[]`) are flat and composable. A Zimbabwe calibration finding is tagged `calibration, zimbabwe` — the intersection gives you what you need. No hierarchy.

`resource` (optional) points to the full analysis record (an experiment SUMMARY, a notebook, a script output), relative to the repository root. The finding is the distilled claim; the resource is one click away for figures, scorecard, and full detail. Omit for simple findings with no backing artifact.

**Record body:**

```markdown
## Question

<What did this analysis ask? One paragraph.>

## Method

<Pointer to the re-runnable artifact — committed script or notebook path.
Never paste the code.>

## Inputs

<Data sources, settings, parameter values as they were run.
Enough to let a trace rebuild the result without a separate manifest.>

## Result

<Headline result with key numbers. One to three sentences.>

## Key observations

<The 2-3 observations that bear on downstream decisions.
Not the full analysis — just what matters for the evidence trail.>
```

Content level: enough to write an email or brief a colleague from the finding alone, without opening the full analysis record. Not a mirror of the full record — just the distilled claim, the numbers, and the implications. For simple findings, Inputs and Key observations may be omitted if the Result section is self-contained.

A finding is immutable unless you re-run it. A validation result, whether the model reproduces a real-world target, is a finding like any other.
