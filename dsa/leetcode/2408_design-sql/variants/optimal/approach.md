## General

**Separate schema, identity, and live rows.** Give each table one record containing its column count, the next unused row ID, and a map from live IDs to rows. A top-level map from name to this record makes invalid-table checks and valid-table access expected $O(1)$ operations.

**Advance IDs only after successful validation.** An insertion first finds the table and checks the row width. If either check fails, it returns `false` without touching the counter. Otherwise it stores a copy at `next_id` and increments that counter. Removing a row only deletes its map entry, so no deletion can recycle an ID or disturb a later insertion.

**Answer directly from live state.** Selection looks up the table and row, validates the one-indexed column, and returns the corresponding value; any failed lookup returns `"<null>"`. Since IDs are assigned in increasing order and never reinserted, the row map's insertion order is ID order even after deletions. Export can therefore traverse the surviving entries once and prefix each joined row with its ID.

## Complexity detail

Building the table map costs $O(n)$. Apart from the data it returns, each insertion, removal, and selection takes expected $O(1)$ time; copying an inserted row is bounded by ten columns. An export is linear in its emitted cells, so an entire trace costs $O(n + q + E)$. The maps and live row values occupy $O(n + S)$ space.

## Alternatives and edge cases

- **Dense row arrays:** Indexing rows by ID is simple and fast, but many deletions leave unused slots; a sparse ID-to-row map releases those slots while preserving expected constant-time access.
- **Linear table-name search:** Parallel arrays can represent the schema, but finding the named table on every operation makes a trace quadratic when both the table count and operation count grow.
- **Failed insertions:** An unknown table or wrong row width must not consume an ID.
- **Deleted latest row:** The next successful insertion still uses one more than the last assigned ID.
- **Invalid selection:** Unknown tables, missing rows, column 0, and columns beyond the table width all return `"<null>"`.
- **Export order:** Deletion creates gaps but does not renumber or reorder the remaining increasing IDs.
