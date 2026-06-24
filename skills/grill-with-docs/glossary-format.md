# Glossary format

The glossary pins down terms so the project speaks one language, kept inline as terms come up.

File: `docs/wiki/glossary.md`, type `glossary`. A single file, but a conformant page like any other — it carries frontmatter.

**Frontmatter:**

```
---
type: glossary
title: Glossary
description: Canonical terms for the project.
timestamp: <ISO 8601, stamped once at creation>
---
```

For each term: the canonical word, and a one-line meaning precise enough that two people could not read it two ways.

When a new term collides with one already in the glossary, flag it and pick a single canonical form rather than letting both run. When a term is vague or overloaded, propose the precise word ("you are saying account, do you mean the customer or the user").

Keep it short. A glossary earns its keep by being read, which means being brief.
