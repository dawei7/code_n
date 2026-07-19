# Department Highest Salary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 184 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/department-highest-salary/) |

## Problem Description
### Goal
The `Employee` table records each employee's name, salary, and department identifier, and the `Department` table supplies the corresponding department name. Determine the maximum salary independently inside every department that has employees.

Return columns named `Department`, `Employee`, and `Salary` for every employee whose salary equals their own department's maximum, in any order. If several employees tie for the highest salary in one department, include all of them. Do not compare salaries across department boundaries, return lower-paid employees, or manufacture a row for a department with no employee.

### Function Contract
**Inputs**

- `Employee(id, name, salary, departmentId)`: employees and their departments
- `Department(id, name)`: department names

**Return value**

Columns `Department`, `Employee`, and `Salary`. Ties for a department's highest salary must all be returned.

### Examples
**Example 1**

- IT salaries: `Joe 85000, Max 90000`
- Sales salaries: `Randy 85000, Sam 60000`
- Output: `IT, Max, 90000` and `Sales, Randy, 85000`

**Example 2**

- IT salaries: `Ada 10, Lin 10`
- Output: both Ada and Lin

**Example 3**

- A department has no employees
- Output: no row for that department
