## Description

Table: `Departments`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
In SQL, id is the primary key of this table.
The table has information about the id of each department of a university.
```

Table: `Students`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
| department_id | int     |
+---------------+---------+
In SQL, id is the primary key of this table.
The table has information about the id of each student at a university and the id of the department he/she studies at.
```

Find the id and the name of all students who are enrolled in departments that no longer exist.

Return the result table in **any order**.

The result format is in the following example.
### Function Contract

**Input**

- `Departments`: the current university-department table described above.
- `Students`: the student and recorded-department table described above.

Let $D$ be the number of department rows, $S$ the number of student rows, and $N=D+S$.

**Return value**

Return a table with these columns:

- `id`: the primary-key ID from an invalid student's `Students` row.
- `name`: that student's name from the same row.

A row qualifies exactly when its `department_id` does not equal the `id` of any current department. The result order is unrestricted.

### Examples
#### Example 1

```
**Input:**
Departments table:
+------+--------------------------+
| id   | name                     |
+------+--------------------------+
| 1    | Electrical Engineering   |
| 7    | Computer Engineering     |
| 13   | Bussiness Administration |
+------+--------------------------+
Students table:
+------+----------+---------------+
| id   | name     | department_id |
+------+----------+---------------+
| 23   | Alice    | 1             |
| 1    | Bob      | 7             |
| 5    | Jennifer | 13            |
| 2    | John     | 14            |
| 4    | Jasmine  | 77            |
| 3    | Steve    | 74            |
| 6    | Luis     | 1             |
| 8    | Jonathan | 7             |
| 7    | Daiana   | 33            |
| 11   | Madelynn | 1             |
+------+----------+---------------+
**Output:**
+------+----------+
| id   | name     |
+------+----------+
| 2    | John     |
| 7    | Daiana   |
| 4    | Jasmine  |
| 3    | Steve    |
+------+----------+
**Explanation:**
John, Daiana, Steve, and Jasmine are enrolled in departments 14, 33, 74, and 77 respectively. department 14, 33, 74, and 77 do not exist in the Departments table.
```