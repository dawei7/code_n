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
