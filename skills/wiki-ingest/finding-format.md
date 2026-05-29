# Finding format

A finding is the result of an analysis you ran. It must describe itself well enough that someone could understand and re-run it without hunting.

File: `evidence/findings/<short-name>.md`

**Record:**

- the question the analysis answered
- the method, as a pointer to the re-runnable artifact (the committed script or notebook). Never paste the code.
- the inputs that mattered, as data: the source pages used, the settings as they were run. This is what lets a trace rebuild a result later without a separate manifest.
- the result, with its fit or diagnostic

A finding is immutable unless you re-run it. A validation result, whether the model reproduces a real-world target, is a finding like any other.
