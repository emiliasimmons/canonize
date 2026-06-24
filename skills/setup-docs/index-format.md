# Index and log format

`index.md` and `log.md` are reserved files. They are not concept pages: they carry no `type` and never appear as nodes in a compiled view.

## Index

The index is the map across all zones. It lives at `docs/index.md` and is updated as a tail step by every skill that writes a page.

The **root** `index.md` is the one place index frontmatter is permitted, and only for the version declaration:

```
---
okf_version: "0.1"
---
```

Group entries by type, using these sections in order:

```
## Decisions
## Findings
## Sources
## Provenance
## Concepts
## Traces
```

Under each heading, one line per page: `- [title](relative/path)` with a short gloss if the title alone is not enough. Take the title and gloss from the page's frontmatter `title` and `description`. Keep glosses to a few words.

Omit sections that have no entries yet. Add a section the first time a page of that type is created.

The glossary (`docs/wiki/glossary.md`) and the two compiled registers (assumptions, open decisions) are not listed by type here; they are navigation targets themselves, linked from the top of the index if they exist.

## Log

`docs/log.md` is an append-only changelog, newest first, one line per write: `## [date] verb | Title`.
