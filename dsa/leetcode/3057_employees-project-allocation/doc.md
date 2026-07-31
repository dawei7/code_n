# Employees Project Allocation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3057 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/employees-project-allocation/) |

## Problem Description

### Goal

Each employee belongs to a team and is assigned a project workload. A workload
is considered unusually high only relative to the workloads of employees on
that same team, not relative to the company as a whole.

Find every employee whose project workload is strictly greater than the
average workload among employees in their team. Return the employee and
project identifiers, the employee's name, and the workload. Order the rows by
`employee_id` ascending and then `project_id` ascending.

### Function Contract

**Inputs**

- `Project(project_id, employee_id, workload)`: records the project and
  workload assigned to each unique employee.
- `Employees(employee_id, name, team)`: records each unique employee's name
  and team.

Let $n$ be the number of project-allocation rows.

**Return value**

- An ordered table with columns `employee_id`, `project_id`, `employee_name`,
  and `project_workload` for allocations strictly above their team average.

### Examples

**Example 1**

Team A has workloads `45` and `68`, averaging `56.50`, so only employee `4`
qualifies. Team B has workloads `90` and `12`, averaging `51.00`, so only
employee `2` qualifies. Employee order places `2` before `4`.

**Example 2**

An employee whose workload equals the team average is excluded because the
comparison is strict.

**Example 3**

A team containing one employee has that employee's workload as its average,
so it contributes no result row.
