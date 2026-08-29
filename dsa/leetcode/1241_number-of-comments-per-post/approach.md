## General

**Use the table once as posts and once as comments**

Posts and comments share the same `Submissions` table. A row is a post when `parent_id IS NULL`; a comment row names its parent post in `parent_id`.

The query self-joins the table:

- `s1` represents candidate post rows;
- `s2` represents comment rows whose `parent_id` equals `s1.sub_id`.

The join condition `s1.sub_id = s2.parent_id` attaches each comment to its post.

**Why the join is a left join**

An inner join would omit posts that have no comments. The output must include them with count zero, so `LEFT JOIN` preserves each `s1` post even when no matching `s2` row exists. In that case, the comment-side columns are `NULL`.

The filter `WHERE s1.parent_id IS NULL` ensures only genuine post rows drive the result. A comment whose parent post is absent cannot find a qualifying `s1` row and is ignored.

**Remove duplicate posts and duplicate comments together**

The table may duplicate both kinds of rows. If a post row appears twice and one of its comments appears twice, the raw self-join can create four copies of the same post-comment relationship.

The common table expression selects:

`DISTINCT s1.sub_id AS post_id, s2.sub_id AS sub_id`.

`DISTINCT` collapses every repeated relationship to one pair. It also collapses duplicate no-comment post rows to a single pair `(post_id, NULL)`.

This is why the outer query can use ordinary `COUNT(sub_id)` instead of `COUNT(DISTINCT sub_id)`. Uniqueness has already been established per post-comment pair.

**Why `COUNT(sub_id)` gives zero for an empty post**

SQL `COUNT(expression)` counts only non-null expression values. A post with no comment has one preserved CTE row whose `sub_id` is null. Grouping that row by `post_id` and evaluating `COUNT(sub_id)` returns zero.

Using `COUNT(*)` would incorrectly return one for that preserved placeholder row.

**The grouping step**

After deduplication, the outer query groups rows by `post_id`. Each distinct non-null `sub_id` is one unique comment for that post, so its count is the required `number_of_comments`.

`ORDER BY post_id` produces ascending post identifiers as required.

**Following the example**

Post 1 occurs twice. Comment 3 on post 1 also occurs twice, while comments 4 and 9 occur once. The raw join contains repeated combinations, but `DISTINCT` reduces them to `(1,3)`, `(1,4)`, and `(1,9)`. Their count is three.

Post 2 produces distinct pairs with comments 5 and 10, giving two.

Post 12 has no match, so its left-join pair is `(12,NULL)`. `COUNT(sub_id)` returns zero.

Comment 6 points to post ID 7, but no row with `sub_id = 7` and null parent exists. It never obtains a qualifying post-side row and does not appear in the CTE.


For every distinct post ID, the left side contains at least one qualifying row. The left join associates it with every comment row whose parent is that ID, or a null placeholder if none exists. `DISTINCT` maps this multiset to exactly one row per unique comment ID, while preserving one null row for an empty post.

Grouping by post collects precisely those unique relationships. Counting non-null comment IDs yields the number of unique comments, including zero for an empty group. No absent parent can create a group because only null-parent rows are accepted on the post side.

**Why the CTE is useful**

Deduplicating pairs before aggregation separates two concerns cleanly. The CTE establishes the set of post-comment relationships; the outer query counts them. An equivalent single-level query could group directly and use `COUNT(DISTINCT s2.sub_id)`, but duplicate post rows can make reasoning less visible.

## Complexity detail

Let \(r\) be the number of input rows. With hash-based join, duplicate elimination, and grouping, the logical work can be expected \(O(r)\) plus output ordering, matching the manifest under favorable indexing and execution planning.

SQL engines may instead use sorting for `DISTINCT`, grouping, or the final order, yielding \(O(r\log r)\) comparison work in a conventional worst-case plan. Working tables, hash structures, or sort buffers can hold \(O(r)\) rows, so space is \(O(r)\). Actual physical complexity is optimizer- and index-dependent.

## Alternatives and edge cases

- **`COUNT(DISTINCT s2.sub_id)` directly:** Group post-side IDs after a left join and count distinct comment IDs. This can express the same result in one query level.
- **Pre-deduplicate posts and comments separately:** Build one CTE for unique posts and another for unique comment pairs, then left join them. It is more verbose but makes duplicate handling explicit.
- **Use of `COUNT(*)`:** Incorrect for posts without comments because the left join supplies one null-extended row.
- **Duplicate post rows:** `DISTINCT` collapses the repeated post-comment pairs.
- **Duplicate comment rows:** The same comment ID for the same post is counted once.
- **Post with no comments:** The null placeholder survives and counts as zero.
- **Comment with deleted parent:** No qualifying post-side row exists, so it is ignored.
- **Same comment ID under different posts:** Pair-level distinctness treats those as separate relationships, one per post.
- **Null semantics:** `parent_id IS NULL` must be used; equality to `NULL` is not valid SQL filtering.
- **Ordering:** The final sort is by numeric `post_id` ascending, independent of join or grouping order.
