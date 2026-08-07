## Description

Table: `Logs`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| log_id        | int     |
+---------------+---------+
log_id is the column of unique values for this table.
Each row of this table contains the ID in a log Table.
```

Write a solution to find the start and end number of continuous ranges in the table `Logs`.

Return the result table ordered by $\text{start}_{id}$.

The result format is in the following example.
### Function Contract

**Input**

- `Logs`: a table containing one row for each unique integer `log_id`.

Let $n$ be the number of input rows and $r$ the number of maximal continuous ranges.

**Output**

Return a table with these columns:

- `start_id`: the smallest identifier in a maximal range.
- `end_id`: the largest identifier in that same range.

Return exactly one row for each of the $r$ ranges, ordered by `start_id` in ascending order. A range containing one identifier has equal start and end values.

### Examples
#### Example 1

```
**Input:**
Logs table:
+------------+
| log_id     |
+------------+
| 1          |
| 2          |
| 3          |
| 7          |
| 8          |
| 10         |
+------------+
**Output:**
+------------+--------------+
| start_id   | end_id       |
+------------+--------------+
| 1          | 3            |
| 7          | 8            |
| 10         | 10           |
+------------+--------------+
**Explanation:**
The result table should contain all ranges in table Logs.
From 1 to 3 is contained in the table.
From 4 to 6 is missing in the table
From 7 to 8 is contained in the table.
Number 9 is missing from the table.
Number 10 is contained in the table.
```