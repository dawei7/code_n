## Description

Table: `Point`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
+-------------+------+
In SQL, x is the primary key column for this table.
Each row of this table indicates the position of a point on the X-axis.
```

Find the shortest distance between any two points from the `Point` table.

It is guaranteed that the `Point` table contains **at least **two rows.

The result format is in the following example.

**Example 1:**

```
**Input:**
Point table:
+----+
| x  |
+----+
| -1 |
| 0  |
| 2  |
+----+
**Output:**
+----------+
| shortest |
+----------+
| 1        |
+----------+
**Explanation:** The shortest distance is between points -1 and 0 which is |(-1) - 0| = 1.
```

**Follow up:** How could you optimize your solution if the `Point` table is ordered **in ascending order**?
