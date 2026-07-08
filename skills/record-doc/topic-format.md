# Topic format

A topic hub is the level-2 browsing surface: the primary reading path into everything the project knows about one theme. It is a sibling page of its member directory (`wiki/topics/seasonality.md` describes `wiki/topics/seasonality/`), the pattern OKF's own appendix models, so it carries frontmatter where an index file could not.

File: `wiki/topics/<topic>.md`, type `topic`. Its directory `wiki/topics/<topic>/` holds the member source summaries and concepts.

**Frontmatter:**

```
---
type: topic
title: <the topic, title case>
description: <one line: what this topic covers — this is the taxonomy entry>
timestamp: <ISO 8601, stamped once at creation>
staleness: 0
tags: [<cross-cutting themes the hub itself belongs to>]
---
```

`description` is the line the root taxonomy block prints, so it earns its brevity. `staleness` counts members added since the synthesis was last rewritten; `record-doc` increments it on member addition, a synthesis rewrite (a `maintain-docs` curation) resets it to 0.

**Body:** two parts.

1. An **authored synthesis** on top: a genuine several-paragraph account of what the project knows about this topic — not a link list. This is the reading payload. Nothing regenerates it mechanically.
2. A **compiled member block** below, owned by `canon`:

```
<!-- compiled:members -->
<!-- /compiled:members -->
```

`canon compile --block members --page wiki/topics/<topic>.md` fills it: the topic's source summaries and concepts (physically in its directory) plus every finding and decision tagged to it, listed by root-anchored link, grouped by type. Never hand-edit inside the markers.

New topics are always a proposal, never unilateral — minting one is a structural change requiring sign-off. Target 8 to 15 topics for a 150-source project; a page has one primary parent and everything else is a tag.
