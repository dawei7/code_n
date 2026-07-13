# Managers with at Least 5 Direct Reports

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 570 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/) |

## Problem Description
### Goal
Given an `Employee` table in which each row's `managerId` identifies that employee's direct manager, find every manager who has at least five direct reports. Employee identifiers are unique, and a null manager identifier means that the employee does not report directly to another employee in the table.

Return the qualifying managers' names in any order. Count only employees whose `managerId` equals the manager's `id`; employees farther down the reporting hierarchy are indirect reports and must not be included in that manager's count.

### Function Contract
**Inputs**

- `Employee(id, name, department, managerId)`: employees and the identifier of each employee's direct manager

**Return value**

- A result grid with one column, `name`, containing every qualifying manager

### Examples
**Example 1**

- Input: manager `John` is referenced by five employee rows
- Output: `John`

**Example 2**

- Input: a manager has only four direct reports
- Output: no rows

**Example 3**

- Input: two managers each have at least five direct reports
- Output: both manager names

### Required Complexity

- **Time:** $O(E \log E)$
- **Space:** $O(E)$

<details>
<summary>Approach</summary>

#### General

**Treat employee rows as direct-report edges**

A non-null `managerId` points from one employee directly to their manager. Grouping report rows by this identifier counts direct reports without following deeper hierarchy levels.

**Join counted identifiers to manager rows**

Join each report row to the employee whose `id` equals its `managerId`. Group by that manager's identifier and name, then retain groups whose row count is at least five.

**Return each qualifying manager once**

Aggregation collapses all report edges for one manager into one result row. A deterministic final order is added for local result comparison.

**Why every reported name qualifies**

Every joined row represents one distinct employee whose direct `managerId` equals the grouped manager's `id`. A group surviving `HAVING COUNT(*) >= 5` therefore has at least five direct reports. Conversely, all direct reports of any manager join into that manager's group, so every qualifying manager reaches the threshold and is returned.

#### Complexity detail

For `E` employee rows, a typical join and grouping plan uses hashing or sorting in $O(E \log E)$ time and $O(E)$ working space. Indexes on `id` and `managerId` can allow near-linear execution.

#### Alternatives and edge cases

- **Aggregate manager identifiers first:** a grouped subquery on `managerId` followed by a join has the same asymptotic behavior.
- **Correlated count per employee:** is concise but may rescan all reports for every possible manager and take $O(E^2)$ time.
- **Count indirect descendants:** is incorrect because only direct reports qualify.
- **Exactly five reports:** satisfies the inclusive threshold.
- **Null manager identifier:** represents a top-level employee and contributes to no manager's count.
- **Nonmanager employee:** has no report group and is absent from the output.
- **Department:** does not affect the direct-report relationship.

</details>
