---
name: onramp
description: Survey an existing project's sources and code, triage what needs capturing, and produce a phased plan for bringing it all into the project record. Use after setup-docs when the project has existing sources, code, or undocumented decisions. Re-runnable when new material appears.
---

Survey the project, decide what needs capturing, and produce a phased plan that dispatches to the right skills across multiple sessions.

Run this after `setup-docs` when the project has existing work: sources, code, informal notes, or decisions living only in someone's head. Re-run it any time new material appears; it checks what is already captured and plans only the remainder.

**Step 1: Survey.** Look at what exists before asking anything.

- Sources: scan `docs/sources/` and any directories the user points you at. Use sub-agents to skim sources at triage depth — title, abstract, key findings — not full ingestion depth. Assess relevance to the project's scope as described in the schema and any existing wiki/evidence.
- Code: surface scan the model codebase for undocumented modeling decisions — hardcoded parameter values, algorithm choices, structural patterns, configuration. Do not do a deep audit; inventory what is there and flag areas that look decision-heavy.
- Existing docs: check what the wiki and evidence layers already hold, so you do not plan to re-ingest what is already captured.

**Step 2: Clarify.** Ask the user clarifying questions about the project's scope, priorities, and any context that the survey could not answer on its own. Use the grilling style: one question at a time, provide your recommended answer. If the existing docs (from setup's initial grill) are sufficient, skip this step.

**Step 3: Triage and group.** Decide what to capture and in what order.

- Group related sources into batches of roughly 3-8, clustered by topic or by what they bear on in the model. Sources that conflict or address the same parameter should land in the same batch so the ingestion session can cross-reference them.
- Group code-discovered decisions by module or subsystem.
- Prioritize: what blocks current work goes first; historical record goes later.
- Flag sources that are not worth ingesting individually — background reading, superseded papers, duplicates — and say why. The user confirms what to skip.

**Step 4: Write the plan.** Produce a plan document at `docs/onramp-plan.md`. Each phase should include the information relevant to executing it: what to process, why it is grouped, which skills to use, and anything the session should watch for. Phases should be self-contained enough that a fresh session can read the plan, find the next unchecked phase, and execute it.

The plan is a suggestion, not a script. The user can reorder, skip, or split phases. Each phase gets a status that is updated as work completes. The final item in the plan should note that the document can be safely removed when all phases are done.

**On re-run:** read the existing plan (if any) and the current state of `docs/`. Subtract what has already been captured. Append new phases for the remainder, or note that the existing plan is still current.
