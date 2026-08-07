## Description

Table: `Point2D`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
+-------------+------+
(x, y) is the primary key column (combination of columns with unique values) for this table.
Each row of this table indicates the position of a point on the X-Y plane.
```

The distance between two points $p_{1}(x_{1}, y_{1})$ and $p_{2}(x_{2}, y_{2})$ is $sqrt((x_{2} - x_{1})^2 + (y_{2} - y_{1})^2)$.

Write a solution to report the shortest distance between any two points from the `Point2D` table. Round the distance to **two decimal points**.

The result format is in the following example.
### Function Contract

**Input**

`Point2D(x, y)` contains unique integer coordinate pairs. Let $P$ be the number of stored points.

**Return value**

Return one row with one column named `shortest`. Its value is the minimum Euclidean distance over all unordered pairs of distinct rows, rounded to two digits after the decimal point.

### Examples

#### Example 1

```
**Input:**
Point2D table:
+----+----+
| x  | y  |
+----+----+
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |
+----+----+
**Output:**
+----------+
| shortest |
+----------+
| 1.00     |
+----------+
**Explanation:** The shortest distance is 1.00 from point (-1, -1) to (-1, 2).
```