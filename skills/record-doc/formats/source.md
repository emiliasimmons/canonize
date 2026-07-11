# Source format

A source is something external you read: a paper, a dataset. The raw file lives in `sources/`; the summary — the knowledge object — lives under the topic it belongs to. Nobody browses PDFs; the summary is what the project knows.

File: `topics/<topic>/<short-name>.md`, type `source`.

**Frontmatter:**

```
---
type: source
title: <the source's name>
description: <one line: what it is and what it bears on>
resource: <DOI or stable URL preferred; else the local sources/ path>
timestamp: <ISO 8601, stamped once at creation>
tags: [<cross-cutting themes beyond its home topic>]
---
```

`resource` follows the ordering rule: a web-accessible canonical identifier first (DOI for academic works, else a stable URL), then the local `sources/...` path only when nothing web-accessible exists. The home topic is the directory the summary sits in; `tags` add any other hub it should surface in.

**Body:**

- **Summary** — what the source is, and where the raw file sits (`/sources/...`)
- **Key points** — the points that matter to this project, in your own words. Paraphrase; do not paste long passages.

Add sections beyond these two when the source and project warrant it — methodology, data description, limitations, or whatever structure fits the material.

A source summary is wiki: update it as understanding improves. The raw file does not change.
