# Source format

A source is something external you read: a paper, a dataset. The file itself lives in `docs/sources/`; the summary lives in the wiki.

File: `docs/wiki/<short-name>.md`, type `source`.

**Frontmatter:**

```
---
type: source
title: <the source's name>
description: <one line: what it is and what it bears on>
resource: <DOI or stable URL preferred; else the local path under sources/>
timestamp: <ISO 8601, stamped once at creation>
---
```

`resource` follows the ordering rule: prefer a web-accessible canonical identifier (DOI for academic works, else a stable URL); fall back to the local `docs/sources/...` path only when nothing web-accessible exists.

**Record:**

- what it is, and where the file sits (`docs/sources/...`)
- the points that matter to this project, in your own words. Paraphrase; do not paste long passages.
- what it bears on: the parameters, findings, or decisions it touches, by relative link
- any conflict with what the project already holds, stated plainly

A source summary is wiki: update it as your understanding improves. The source file itself does not change.
