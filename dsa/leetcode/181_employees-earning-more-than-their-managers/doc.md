# Employees Earning More Than Their Managers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 181 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/employees-earning-more-than-their-managers/) |

## Problem Description
### Goal
The `Employee` table stores each employee's identifier, name, salary, and an optional `managerId` that references another row in the same table. Compare each employee who has a recorded manager with that manager's salary.

Return one column named `Employee` containing the names of qualifying employees in any order. Employees earning the same amount as their manager do not qualify, and top-level employees with no manager have no comparison and must be excluded. Manager status does not otherwise affect eligibility: a manager may also qualify relative to their own manager.

### Function Contract
**Inputs**

- `Employee(id, name, salary, managerId)`: employees and their optional manager reference into the same table

**Return value**

One column named `Employee` containing each qualifying employee name.

### Examples
**Example 1**

Joe earns `70000` while manager Sam earns `60000`; Joe is returned.

**Example 2**

An employee earning exactly the manager's salary is not returned.

**Example 3**

Top-level employees with null managerId are not returned.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

Both sides of the relationship live in `Employee`, so give the table two roles with aliases: one row is the employee and the other is that employee's manager. Join them with

`employee.managerId = manager.id`.

This predicate is crucial. Joining on a salary or comparing arbitrary employee pairs would not preserve the reporting relationship. Once each subordinate is paired with the referenced manager, retain rows satisfying the strict comparison `employee.salary > manager.salary` and project the subordinate's name as `Employee`.

An inner join is appropriate because a top-level employee with `managerId = NULL` has no manager salary to exceed and therefore cannot qualify. Under the schema's manager reference, each joined row describes one concrete employee-manager edge in the organizational graph.

Every joined pair satisfies `employee.managerId = manager.id`, so it compares an employee with exactly the manager named by that employee's record. The `>` predicate retains the pair if and only if the employee earns more than that manager. Employees without a matching manager produce no inner-join row and correctly do not qualify. Projecting the employee alias therefore returns exactly the required names.

#### Complexity detail

With a primary-key index or hash structure on `Employee.id`, each of `n` employee rows can resolve its manager in $O(1)$ expected lookup time, for $O(n)$ logical work and up to $O(n)$ join/index storage. Without a useful access path, a naive nested-loop plan may be quadratic; physical costs depend on the database optimizer.

#### Alternatives and edge cases

- A correlated scalar subquery can fetch each manager's salary, but may repeat lookups and expresses the relationship less directly.
- A Cartesian product followed by salary comparison pairs unrelated employees and is both incorrect and potentially $O(n^2)$.
- A left join is unnecessary unless the query must also report employees lacking managers.
- Equal salaries do not satisfy the strict comparison. Null `managerId` values are naturally excluded.
- If manager references could be invalid, those employees likewise produce no joined pair.

</details>
