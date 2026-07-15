# Article Views I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1148 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/article-views-i/) |

## Problem Description

### Goal

The `Views` table records that a viewer opened an article written by an author on a particular date. The table has no primary key, so the same view record may appear more than once. An author and a viewer represent the same person exactly when their IDs are equal.

Find every author who viewed at least one of their own articles. Each qualifying author must appear only once regardless of how many self-views or duplicate rows exist. Name the output column `id` and return the result in ascending order by that value.

### Function Contract

**Input table**

- `Views(article_id, author_id, viewer_id, view_date)`:
  - `article_id`: the viewed article's integer ID.
  - `author_id`: the integer ID of that article's author.
  - `viewer_id`: the integer ID of the person who viewed it.
  - `view_date`: the date of the view.
  - Rows are not unique and may be duplicated.
- Let $r$ be the number of input rows and $a$ the number of distinct authors whose `author_id` equals `viewer_id` on at least one row.

**Return value**

A one-column relation named `id`, containing each qualifying author ID once and sorted in ascending order.

### Examples

**Example 1**

`Views`

| article_id | author_id | viewer_id | view_date |
|---:|---:|---:|---|
| 1 | 3 | 5 | 2019-08-01 |
| 1 | 3 | 6 | 2019-08-02 |
| 2 | 7 | 7 | 2019-08-01 |
| 2 | 7 | 6 | 2019-08-02 |
| 4 | 7 | 1 | 2019-07-22 |
| 3 | 4 | 4 | 2019-07-21 |
| 3 | 4 | 4 | 2019-07-21 |

Output:

| id |
|---:|
| 4 |
| 7 |

### Required Complexity

- **Time:** $O(r+a\log a)$
- **Space:** $O(a)$

<details>
<summary>Approach</summary>

#### General

**Identify self-views directly.** The problem defines the author and viewer as the same person when `author_id = viewer_id`, so filter on that equality. Neither the article nor the date changes whether the row qualifies.

**Collapse repeated qualifying authors.** A single author may view several own articles, view one article repeatedly, or have an identical row duplicated because the table has no primary key. `DISTINCT author_id` turns all such rows into one output entry and aliases that value as `id`.

**Make the requested order explicit.** SQL relations do not otherwise promise row order. Apply `ORDER BY id` after deduplication so every engine returns the qualifying IDs in ascending order.

#### Complexity detail

A logical scan examines $r$ rows. Deduplicating the qualifying IDs can use $O(a)$ hash state, and sorting those $a$ IDs costs $O(a\log a)$, giving $O(r+a\log a)$ time and $O(a)$ auxiliary space. A database may choose a different physical plan or exploit an index while preserving the same result.

#### Alternatives and edge cases

- **Group by author:** Filtering first and using `GROUP BY author_id` is equivalent, but no aggregate is needed, so `DISTINCT` states the intent more directly.
- **Self-join:** Joining the table to find a matching self-view can reproduce the answer but creates unnecessary row pairs and may require quadratic work.
- **Duplicate rows:** They must not duplicate an author in the output.
- **Several own articles:** An author still appears exactly once.
- **No self-view:** The query returns an empty relation with the `id` column.
- **Date and article identity:** They do not constrain qualification; only equality of the author and viewer IDs matters.

</details>
