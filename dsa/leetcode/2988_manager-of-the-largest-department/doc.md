# Manager of the Largest Department

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2988 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/manager-of-the-largest-department/) |

## Problem Description
### Goal
The `Employees` table stores each uniquely identified employee's name,
department, and position. A department's size is the number of employee rows
having its `dep_id`.

Find the largest department size and return the manager of every department
that attains it. Several departments may tie and all of their managers must be
included. Output the manager's name as `manager_name` together with `dep_id`,
ordered by ascending department ID.

### Function Contract
**Inputs**

- `Employees(emp_id, emp_name, dep_id, position)`: uniquely identified employees and their departments and positions

Let $R$ be the number of employee rows.

**Return value**

Return the manager name and department ID for every largest department,
ordered by `dep_id` ascending.

### Examples
**Example 1**

- Input: Departments `100` and `101` contain four employees each; department `107` contains three.
- Output: `[("Joseph",100),("Isabella",101)]`

**Example 2**

- Input: A single department with one manager and two other employees.
- Output: That manager and department.

**Example 3**

- Input: Three departments tied at the same size.
- Output: All three managers in ascending department order.
