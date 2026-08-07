## Description

Table: `Sales`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| sale_date     | date    |
| fruit         | enum    |
| sold_num      | int     |
+---------------+---------+
(sale_date, fruit) is the primary key (combination of columns with unique values) of this table.
This table contains the sales of "apples" and "oranges" sold each day.
```

Write a solution to report the difference between the number of **apples** and **oranges** sold each day.

Return the result table **ordered** by $\text{sale}_{date}$.

The result format is in the following example.
### Function Contract

**Input**

- `Sales(sale_date, fruit, sold_num)` records a daily quantity for `apples` or `oranges`;
- (`sale_date`, `fruit`) uniquely identifies a row.

Let $R$ be the number of rows in `Sales`, and let $D$ be the number of distinct sale dates.

**Return value**

Return `sale_date` and `diff` for every recorded date, where

$$
\texttt{diff}=\text{apples sold}-\text{oranges sold}.
$$

Order the $D$ result rows by `sale_date` ascending.

### Examples
#### Example 1

```
**Input:**
Sales table:
+------------+------------+-------------+
| sale_date  | fruit      | sold_num    |
+------------+------------+-------------+
| 2020-05-01 | apples     | 10          |
| 2020-05-01 | oranges    | 8           |
| 2020-05-02 | apples     | 15          |
| 2020-05-02 | oranges    | 15          |
| 2020-05-03 | apples     | 20          |
| 2020-05-03 | oranges    | 0           |
| 2020-05-04 | apples     | 15          |
| 2020-05-04 | oranges    | 16          |
+------------+------------+-------------+
**Output:**
+------------+--------------+
| sale_date  | diff         |
+------------+--------------+
| 2020-05-01 | 2            |
| 2020-05-02 | 0            |
| 2020-05-03 | 20           |
| 2020-05-04 | -1           |
+------------+--------------+
**Explanation:**
Day 2020-05-01, 10 apples and 8 oranges were sold (Difference  10 - 8 = 2).
Day 2020-05-02, 15 apples and 15 oranges were sold (Difference 15 - 15 = 0).
Day 2020-05-03, 20 apples and 0 oranges were sold (Difference 20 - 0 = 20).
Day 2020-05-04, 15 apples and 16 oranges were sold (Difference 15 - 16 = -1).
```