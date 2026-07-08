---
name: ingest-source
description: Bring sources and findings into the project — a paper or dataset you read, or the result of an analysis you ran. Owns placement (which topic, which tags). Use when the user has read something worth keeping, dropped in one or many sources, or wants an analysis result recorded, including a validation result. Delegates every write to record-doc.
---

Read the taxonomy block, judge where a thing belongs, and hand the content and placement to /record-doc — it owns the writing. Never touch views; views are pull-only.

## A source you read

1. **Read the taxonomy block** at the top of `<root>/index.md` (a few hundred tokens): the topics with their one-line descriptions and member counts, and the tag vocabulary. This is the placement map.
2. **Judge fit.** Pick the one primary topic the summary belongs under (its home directory) and the cross-cutting tags. The primary topic is always also a tag — it is the membership mechanism that binds the page to its hub. When a source contributes meaningfully to a second topic, add that topic name as a secondary tag; the page will appear in both hubs but live in one directory. Drop the raw file into `sources/`; the summary is the knowledge object.
3. **Cross-check** against what the project already holds. If the source conflicts with something assumed — an accepted decision, a calibrated value — say so plainly and name what it conflicts with. An unresolved conflict becomes a provisional DR via /record-doc, which the open-decisions register then picks up; do not resolve the conflict yourself.
4. **When nothing fits,** say so. Explore just enough to confirm novelty, then propose a new topic — never place unilaterally, never force a bad fit. A new topic is a structural change: on approval, /record-doc scaffolds the hub and files the summary.
5. **Write** the summary through /record-doc (type `source`). It stamps frontmatter, writes root-anchored links, increments the hub staleness, regenerates the affected blocks, and commits `ingest: <title>`.

## Many sources (batch)

1. **Skim all before placing any.** At triage depth — title, abstract, what it bears on.
2. **Present one placement plan** for a single review: each source with its proposed topic and tags, flagged misfits, and aggregated new-topic proposals ("eight of these cluster; propose topic `vaccine-hesitancy`"). During adoption, with no topics yet, this plan *is* the proposed taxonomy.
3. **Amend once, then execute mechanically** through /record-doc, one page per source.
4. **Coalesce the regen:** run a single /canon compile at the end rather than per source, and commit per source or per batch at the user's preference.

## A finding you ran

Write it through /record-doc (type `finding`): the question, the method as a pointer to the re-runnable artifact (never paste the script), the inputs that mattered, and the result with its diagnostic. When the project has registered workspaces (in `schema.md`), the current repo's workspace — named in the `## docs` steering block — routes it to `evidence/findings/<workspace>/`. A validation result lands here like any other finding.

## Staleness

Adding a member increments the hub's staleness counter (/record-doc does this). Past the schema's nudge threshold you may say so once — one line — but never offer to rewrite a synthesis. Rewrites are /maintain-docs curation the user schedules.
