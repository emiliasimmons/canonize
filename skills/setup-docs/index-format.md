# Index format

The index is the map across all zones. It lives at `docs/index.md` and is updated as a tail step by every skill that writes a page.

Group entries by type, using these sections in order:

```
## MDRs
## Findings
## Sources
## Provenance
## Concepts
## Traces
```

Under each heading, one line per page: `- [title](relative/path)` with a short gloss if the title alone is not enough. Keep glosses to a few words.

Omit sections that have no entries yet. Add a section the first time a page of that type is created.

The glossary (`docs/wiki/glossary.md`) and the two compiled registers (assumptions, open decisions) are not indexed here; they are navigation targets themselves, linked from the top of the index if they exist.
