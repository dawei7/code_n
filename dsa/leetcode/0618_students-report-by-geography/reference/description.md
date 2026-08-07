## Description

Table: `Student`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
+-------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the name of a student and the continent they came from.
```

A school has students from Asia, Europe, and America.

Write a solution to <a href="https://en.wikipedia.org/wiki/Pivot_table" target="_blank">pivot</a> the continent column in the `Student` table so that each name is **sorted alphabetically** and displayed underneath its corresponding continent. The output headers should be `America`, `Asia`, and `Europe`, respectively.

The test cases are generated so that the student number from America is not less than either Asia or Europe.

The result format is in the following example.
### Function Contract

Execute one SQL query against the `Student` table.

### Inputs

- `Student(name, continent)`: Student names and their corresponding continents. Duplicate rows are permitted.

### Output

Return exactly three columns named `America`, `Asia`, and `Europe`, in that order. Sort the names within each continent alphabetically and align equal one-based ranks on the same output row. Preserve duplicate rows as repeated names at successive ranks, and use `NULL` after a shorter continent list is exhausted.

### Examples

#### Example 1

```
**Input:**
Student table:
+--------+-----------+
| name   | continent |
+--------+-----------+
| Jane   | America   |
| Pascal | Europe    |
| Xi     | Asia      |
| Jack   | America   |
+--------+-----------+
**Output:**
+---------+------+--------+
| America | Asia | Europe |
+---------+------+--------+
| Jack    | Xi   | Pascal |
| Jane    | null | null   |
+---------+------+--------+
```

**Follow up:** If it is unknown which continent has the most students, could you write a solution to generate the student report?