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
