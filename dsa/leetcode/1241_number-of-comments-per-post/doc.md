# Number of Comments per Post

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1241 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-comments-per-post/) |

## Problem Description

### Goal

The `Submissions` table stores both posts and comments. A row whose `parent_id` is `NULL` represents a post identified by `sub_id`; a row with a non-null `parent_id` represents a comment on the post whose identifier equals that parent value. Duplicate rows may occur.

For every distinct post, report how many distinct comment identifiers refer directly to it. A post with no comments must still appear with a count of zero. Ignore comments whose parent does not identify a listed post, and return the result ordered by `post_id` in ascending order.

### Function Contract

**Input tables**

- `Submissions(sub_id, parent_id)`: `parent_id IS NULL` marks a post; otherwise the row is a comment referring to `parent_id`.
- Let $r$ be the number of rows in `Submissions`.

**Return value**

- One row per distinct post with columns `post_id` and `number_of_comments`, ordered by `post_id ASC`.

### Examples

**Example 1**

`Submissions`

| sub_id | parent_id |
|---:|---:|
| 1 | NULL |
| 2 | NULL |
| 1 | NULL |
| 12 | NULL |
| 3 | 1 |
| 5 | 2 |
| 3 | 1 |
| 4 | 1 |
| 9 | 1 |
| 10 | 2 |
| 6 | 7 |

Output:

| post_id | number_of_comments |
|---:|---:|
| 1 | 3 |
| 2 | 2 |
| 12 | 0 |

**Example 2**

A distinct post with no matching comment rows is returned with `number_of_comments = 0`.

**Example 3**

Repeated rows for the same comment identifier count only once for that post.

### Required Complexity

- **Time:** $O(r)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Build the distinct post catalog.** Select distinct `sub_id` values from rows where `parent_id IS NULL`. Deduplication is required because the same post row may appear more than once, yet the output needs one row per post.

**Attach comments without losing empty posts.** Left join the post catalog to `Submissions` on `comments.parent_id = posts.post_id`. An inner join would remove posts that have no comments. Orphan comments find no post row and therefore never enter an output group.

**Count distinct comment identifiers.** Group by the post ID and use `COUNT(DISTINCT comments.sub_id)`. `COUNT` ignores the null placeholder produced by an unmatched left join, yielding zero for an empty post, while `DISTINCT` prevents duplicate comment rows from inflating the total. Finally, order by the post ID ascending.

#### Complexity detail

With hash-based deduplication, aggregation, and joining, the query processes the $r$ submission rows in $O(r)$ logical time and stores up to $O(r)$ post, join, and grouping state. A physical database engine may choose a sort-based plan with an additional logarithmic factor.

#### Alternatives and edge cases

- **Correlated count subquery:** Counting comments separately for every post is correct but can rescan the table per post and take $O(r^2)$ time.
- **Inner join:** It omits posts with zero comments and therefore violates the output contract.
- **`COUNT(*)`:** On an unmatched left join it reports one placeholder row instead of zero.
- **`COUNT(comments.sub_id)` without `DISTINCT`:** Duplicate comment rows inflate the result.
- **Duplicate post rows:** Deduplicate the post catalog before joining so each post appears once.
- **Orphan comment:** A non-null parent absent from the post catalog contributes to no output row.
- **Ordering:** Apply `ORDER BY post_id` explicitly rather than relying on grouping order.

</details>
