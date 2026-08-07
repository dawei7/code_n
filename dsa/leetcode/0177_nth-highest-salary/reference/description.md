## Description

Table: `Employee`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
```

Write a solution to find the $$n^{\text{th}}$$ highest **distinct** salary from the `Employee` table. If there are less than `n` distinct salaries, return `null`.

The result format is in the following example.
### Function Contract

**Inputs**

- `N`: The positive, 1-based rank requested by the native database function. App fixtures expose the same value through `Request(N)`.

`Employee(id, salary)` contains employee rows whose salary values may repeat.

**Return value**

Return the $N$th-highest distinct salary under the column `getNthHighestSalary`, or null when that rank does not exist.

### Examples
#### Example 1

```
**Input:**
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
**Output:**
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```
#### Example 2

```
**Input:**
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
**Output:**
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
```