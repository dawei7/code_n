## General
**Identify self-views directly.** The problem defines the author and viewer as the same person when `author_id = viewer_id`, so filter on that equality. Neither the article nor the date changes whether the row qualifies.

**Collapse repeated qualifying authors.** A single author may view several own articles, view one article repeatedly, or have an identical row duplicated because the table has no primary key. `DISTINCT author_id` turns all such rows into one output entry and aliases that value as `id`.

**Make the requested order explicit.** SQL relations do not otherwise promise row order. Apply `ORDER BY id` after deduplication so every engine returns the qualifying IDs in ascending order.

## Complexity detail
A logical scan examines $r$ rows. Deduplicating the qualifying IDs can use $O(a)$ hash state, and sorting those $a$ IDs costs $O(a\log a)$, giving $O(r+a\log a)$ time and $O(a)$ auxiliary space. A database may choose a different physical plan or exploit an index while preserving the same result.

## Alternatives and edge cases
- **Group by author:** Filtering first and using `GROUP BY author_id` is equivalent, but no aggregate is needed, so `DISTINCT` states the intent more directly.
- **Self-join:** Joining the table to find a matching self-view can reproduce the answer but creates unnecessary row pairs and may require quadratic work.
- **Duplicate rows:** They must not duplicate an author in the output.
- **Several own articles:** An author still appears exactly once.
- **No self-view:** The query returns an empty relation with the `id` column.
- **Date and article identity:** They do not constrain qualification; only equality of the author and viewer IDs matters.
