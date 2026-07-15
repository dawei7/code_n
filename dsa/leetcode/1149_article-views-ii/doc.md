# Article Views II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1149 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/article-views-ii/) |

## Problem Description

### Goal

The `Views` table records article-view events: which article was viewed, who wrote it, who viewed it, and on which date the view occurred. The table may contain duplicate rows, and equal author and viewer IDs merely indicate that those roles belong to the same person.

Find every person who viewed more than one distinct article on at least one single date. Multiple events for the same article and viewer on that date still represent only one article. Return each qualifying viewer once, name the column `id`, and sort the result by `id` in ascending order.

### Function Contract

**Input table**

- `Views(article_id, author_id, viewer_id, view_date)`:
  - `article_id`: the integer ID of the viewed article.
  - `author_id`: the article author's integer ID.
  - `viewer_id`: the viewer's integer ID.
  - `view_date`: the date of the event.
  - Duplicate rows are permitted.
- Let $r$ be the number of input rows.

**Return value**

A one-column relation named `id` containing each viewer who viewed at least two distinct articles on one date, listed once in ascending order.

### Examples

**Example 1**

`Views`

| article_id | author_id | viewer_id | view_date |
|---:|---:|---:|---|
| 1 | 3 | 5 | 2019-08-01 |
| 3 | 4 | 5 | 2019-08-01 |
| 1 | 3 | 6 | 2019-08-02 |
| 2 | 7 | 7 | 2019-08-01 |
| 2 | 7 | 6 | 2019-08-02 |
| 4 | 7 | 1 | 2019-07-22 |
| 3 | 4 | 4 | 2019-07-21 |
| 3 | 4 | 4 | 2019-07-21 |

Output:

| id |
|---:|
| 5 |
| 6 |

### Required Complexity

- **Time:** $O(r\log r)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Form one group per viewer and date.** The condition must hold within a single calendar date, so group rows by both `viewer_id` and `view_date`. Grouping by the viewer alone would incorrectly combine articles seen on different dates.

**Count articles rather than events.** Use `COUNT(DISTINCT article_id)` inside each group because duplicate rows or repeated views of one article do not establish that the person viewed more than one article. Retain only groups whose distinct count exceeds `1`.

**Collapse multiple qualifying dates.** One viewer may satisfy the condition on several dates, but the requested output contains people, not viewer-date pairs. Select `DISTINCT viewer_id AS id` from the retained groups, then explicitly sort by `id` ascending.

#### Complexity detail

A comparison-based grouping and distinct-count plan can sort the $r$ rows in $O(r\log r)$ time and retain $O(r)$ grouping state. Hash aggregation may achieve expected linear work, and indexes may change the physical plan, without changing the query's logical result.

#### Alternatives and edge cases

- **Self-join on viewer and date:** Pairing different article IDs is correct, but a busy viewer-date can generate quadratically many row pairs before deduplication.
- **Count all rows:** `COUNT(*) > 1` is wrong when the table repeats one article's event.
- **Group only by viewer:** This incorrectly combines different dates.
- **Same article on several dates:** The viewer does not qualify unless some one date contains another distinct article.
- **Several qualifying dates:** The viewer appears only once in the final output.
- **Author identity:** Whether the viewer authored an article is irrelevant to this problem.

</details>
