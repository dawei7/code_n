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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(d)$

<details>
<summary>Approach</summary>

#### General

**Group every department once.** Use `GROUP BY id` so all monthly rows belonging to one department contribute to a single output row.

**Route each month with conditional aggregation.** For `Jan_Revenue`, a `CASE` expression returns `revenue` only for a January row and `NULL` for every other month. `SUM` ignores those `NULL` values. Because `(id, month)` is unique, at most one value remains in each department-month group, so the sum is that exact revenue rather than a combination of several rows. Repeat the same expression for all twelve month labels and apply the required aliases.

If a department lacks a particular month, every input to that month's aggregate is `NULL`, so SQL returns `NULL` in the pivoted cell as required. Ordering by `id` is optional for the problem but makes local results deterministic.

#### Complexity detail

With hash aggregation, the query examines each of the $n$ source rows once, giving $O(n)$ logical time. It maintains one fixed set of twelve aggregate slots for each of the $d$ departments, so auxiliary aggregation state is $O(d)$. An engine may choose a sorted grouping plan with different physical costs.

#### Alternatives and edge cases

- **Twelve correlated scalar subqueries:** Looking up each month separately for every distinct department is correct, but without supporting indexes it can repeatedly rescan the table and take $O(dn)$ time.
- **Database-specific `PIVOT`:** Some systems provide a pivot operator, but conditional aggregation is portable to MySQL and the local SQL runtime.
- **Missing month:** The expression must yield `NULL`, not zero, because no revenue row exists for that department-month pair.
- **Zero revenue:** A stored revenue of `0` is a real value and must remain distinguishable from `NULL`.
- **Sparse department:** Even one source row creates a result row with all other month columns `NULL`.
- **Composite primary key:** Uniqueness of `(id, month)` ensures no monthly aggregate combines duplicate revenue rows.

</details>
