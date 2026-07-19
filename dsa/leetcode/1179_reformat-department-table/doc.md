# Reformat Department Table

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1179 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/reformat-department-table/) |

## Problem Description

### Goal

The `Department` table stores monthly revenue in row form: each row identifies a department, one calendar month, and the revenue reported for that pair. The pair `(id, month)` is unique, but a department may have no row for some months.

Reformat this data into one row per department. Keep the department `id` and create twelve columns named `Jan_Revenue` through `Dec_Revenue`, placing each available monthly revenue in its corresponding column and `NULL` where that department has no row for the month. The result may be returned in any order.

### Function Contract

**Input table**

- `Department(id, revenue, month)`: `(id, month)` is the primary key. `month` is one of `"Jan"`, `"Feb"`, `"Mar"`, `"Apr"`, `"May"`, `"Jun"`, `"Jul"`, `"Aug"`, `"Sep"`, `"Oct"`, `"Nov"`, or `"Dec"`.
- Let $n$ be the number of input rows and $d$ the number of distinct department IDs.

**Return value**

- One row per department with columns `id`, `Jan_Revenue`, `Feb_Revenue`, `Mar_Revenue`, `Apr_Revenue`, `May_Revenue`, `Jun_Revenue`, `Jul_Revenue`, `Aug_Revenue`, `Sep_Revenue`, `Oct_Revenue`, `Nov_Revenue`, and `Dec_Revenue`.

### Examples

**Example 1**

`Department`

| id | revenue | month |
|---:|---:|---|
| 1 | 8000 | Jan |
| 2 | 9000 | Jan |
| 3 | 10000 | Feb |
| 1 | 7000 | Feb |
| 1 | 6000 | Mar |

Output, showing the populated leading months:

| id | Jan_Revenue | Feb_Revenue | Mar_Revenue |
|---:|---:|---:|---:|
| 1 | 8000 | 7000 | 6000 |
| 2 | 9000 | null | null |
| 3 | null | 10000 | null |

The actual result also contains the remaining monthly columns through `Dec_Revenue`, all `NULL` for these rows.

**Example 2**

A department represented only by a December row has `NULL` in the first eleven revenue columns and its value in `Dec_Revenue`.

**Example 3**

A department with all twelve month rows produces a completely populated output row.
