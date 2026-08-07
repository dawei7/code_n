## Description

Table: `Numbers`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
| frequency   | int  |
+-------------+------+
num is the primary key (column with unique values) for this table.
Each row of this table shows the frequency of a number in the database.
```

The <a href="https://en.wikipedia.org/wiki/Median" target="_blank">**median**</a> is the value separating the higher half from the lower half of a data sample.

Write a solution to report the **median** of all the numbers in the database after decompressing the `Numbers` table. Round the median to **one decimal point**.

The result format is in the following example.

**Example 1:**

```
**Input:**
Numbers table:
+-----+-----------+
| num | frequency |
+-----+-----------+
| 0   | 7         |
| 1   | 1         |
| 2   | 3         |
| 3   | 1         |
+-----+-----------+
**Output:**
+--------+
| median |
+--------+
| 0.0    |
+--------+
**Explanation:**
If we decompress the Numbers table, we will get [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3], so the median is (0 + 0) / 2 = 0.
```
