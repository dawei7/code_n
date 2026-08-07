## Description

Table: `Actions`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| post_id       | int     |
| action_date   | date    |
| action        | enum    |
| extra         | varchar |
+---------------+---------+
This table may have duplicate rows.
The action column is an ENUM (category) type of ('view', 'like', 'reaction', 'comment', 'report', 'share').
The extra column has optional information about the action, such as a reason for the report or a type of reaction.
```

Write a solution to report the number of posts reported yesterday for each report reason. Assume today is `2019-07-05`.

Return the result table in **any order**.

The result format is in the following example.
### Function Contract

**Input table**

- `Actions(user_id, post_id, action_date, action, extra)`: $R$ activity rows. Duplicate rows are allowed; `action` belongs to the exact six-value source domain, and `extra` contains optional action-specific information.

Filter to report actions dated `2019-07-04`. Within each `extra` value represented by those rows, count distinct `post_id` values rather than action rows or reporters.

**Return value**

- `report_reason`: the qualifying report row's `extra` value.
- `report_count`: the number of distinct posts reported for that reason yesterday.

Return one row for every represented report reason with a nonzero post count, in any order. If yesterday has no report rows, return an empty result.

### Examples
#### Example 1

```
**Input:**
Actions table:
+---------+---------+-------------+--------+--------+
| user_id | post_id | action_date | action | extra  |
+---------+---------+-------------+--------+--------+
| 1       | 1       | 2019-07-01  | view   | null   |
| 1       | 1       | 2019-07-01  | like   | null   |
| 1       | 1       | 2019-07-01  | share  | null   |
| 2       | 4       | 2019-07-04  | view   | null   |
| 2       | 4       | 2019-07-04  | report | spam   |
| 3       | 4       | 2019-07-04  | view   | null   |
| 3       | 4       | 2019-07-04  | report | spam   |
| 4       | 3       | 2019-07-02  | view   | null   |
| 4       | 3       | 2019-07-02  | report | spam   |
| 5       | 2       | 2019-07-04  | view   | null   |
| 5       | 2       | 2019-07-04  | report | racism |
| 5       | 5       | 2019-07-04  | view   | null   |
| 5       | 5       | 2019-07-04  | report | racism |
+---------+---------+-------------+--------+--------+
**Output:**
+---------------+--------------+
| report_reason | report_count |
+---------------+--------------+
| spam          | 1            |
| racism        | 2            |
+---------------+--------------+
**Explanation:** Note that we only care about report reasons with non-zero number of reports.
```