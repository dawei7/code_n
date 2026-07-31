## General

Each requested result is a count of matching table rows, not a count of every textual occurrence. A `LIKE` pattern with a literal space on both sides expresses the contract directly: `% bull %` matches a file containing at least one `bull` with the required neighboring spaces, and `% bear %` does the same for `bear`.

Run one aggregate query per target. `COUNT(*)` counts every qualifying file exactly once regardless of how often the pattern occurs within that row. Each aggregate returns a row even when its count is zero. Combine the two labeled scalar results with `UNION ALL`; the labels differ, no deduplication is needed, and the contract permits either row order.

## Complexity detail

Let $R$ be the number of files and $S$ the total length of their text content. The two pattern predicates scan the table and inspect the contents, requiring $O(S)$ time overall; the constant factor of two is omitted. Apart from the database engine's scan buffers and the two result rows, the query uses $O(1)$ auxiliary space. The benchmark uses $R$ equal-length content rows, so its recorded size is proportional to $S$.

## Alternatives and edge cases

- **Conditional aggregation over target labels:** Cross joining two constant word labels with `Files` and grouping by the label also takes linear work, but constructs a larger intermediate relation.
- **Regular expression:** A regex can express the surrounding spaces, but word-boundary tokens would incorrectly admit punctuation and text boundaries under this problem's stricter rule.
- **Split content into tokens:** Expanding every file into words is unnecessary and risks treating punctuation as a separator when punctuation-adjacent targets must be rejected.
- A file contributes at most one to a target's count even when its content contains several valid occurrences.
- A content row may contribute to both output counts.
- `bull` or `bear` at the very beginning or end of the content is invalid because it lacks a space on one side.
- `bull.`, `bears`, `bullet`, and analogous forms do not match the literal space-delimited patterns.
- The query must still return both labeled rows when one or both counts are zero.
