## General
**Build the distinct post catalog.** Select distinct `sub_id` values from rows where `parent_id IS NULL`. Deduplication is required because the same post row may appear more than once, yet the output needs one row per post.

**Attach comments without losing empty posts.** Left join the post catalog to `Submissions` on `comments.parent_id = posts.post_id`. An inner join would remove posts that have no comments. Orphan comments find no post row and therefore never enter an output group.

**Count distinct comment identifiers.** Group by the post ID and use `COUNT(DISTINCT comments.sub_id)`. `COUNT` ignores the null placeholder produced by an unmatched left join, yielding zero for an empty post, while `DISTINCT` prevents duplicate comment rows from inflating the total. Finally, order by the post ID ascending.

## Complexity detail
With hash-based deduplication, aggregation, and joining, the query processes the $r$ submission rows in $O(r)$ logical time and stores up to $O(r)$ post, join, and grouping state. A physical database engine may choose a sort-based plan with an additional logarithmic factor.

## Alternatives and edge cases
- **Correlated count subquery:** Counting comments separately for every post is correct but can rescan the table per post and take $O(r^2)$ time.
- **Inner join:** It omits posts with zero comments and therefore violates the output contract.
- **`COUNT(*)`:** On an unmatched left join it reports one placeholder row instead of zero.
- **`COUNT(comments.sub_id)` without `DISTINCT`:** Duplicate comment rows inflate the result.
- **Duplicate post rows:** Deduplicate the post catalog before joining so each post appears once.
- **Orphan comment:** A non-null parent absent from the post catalog contributes to no output row.
- **Ordering:** Apply `ORDER BY post_id` explicitly rather than relying on grouping order.
