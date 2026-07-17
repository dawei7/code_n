# Primary Department for Each Employee

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/primary-department-for-each-employee/) |
| Frontend ID | 1789 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Employee` table records the departments to which each employee belongs. An employee may have several rows, one for each department. For a multi-department employee, exactly one membership is identified as primary by `primary_flag = 'Y'`; other memberships use `'N'`.

An employee who belongs to only one department has no separate choice to make, so that sole row keeps `primary_flag = 'N'` even though its department must be reported as primary.

Return each employee's identifier together with the correct primary department: use the explicitly flagged department for employees with several memberships, and use the only department for employees with one membership. Result rows may appear in any order.

### Function Contract

**Input**

- `Employee(employee_id, department_id, primary_flag)`: membership rows whose composite primary key is `(employee_id, department_id)`.
- `primary_flag` is either `'Y'` or `'N'`. A multi-department employee has one `'Y'` row; a single-department employee's only row is `'N'`.

Let $R$ be the number of membership rows and $M$ the number of distinct employees.

**Return value**

- Return columns `employee_id` and `department_id`, with exactly one row per employee containing that employee's primary department.
- Result order is unrestricted.

### Examples

**Example 1**

- Input: `Employee = [[1,1,"N"],[2,1,"Y"],[2,2,"N"],[3,3,"N"],[4,2,"N"],[4,3,"Y"],[4,4,"N"]]`
- Output: `[[1,1],[2,1],[3,3],[4,3]]`

Employees `1` and `3` use their only departments; employees `2` and `4` use their `'Y'` rows.

**Example 2**

- Input: `Employee = [[7,42,"N"]]`
- Output: `[[7,42]]`

A sole membership is reported despite its `'N'` flag.

**Example 3**

- Input: `Employee = [[5,90,"N"],[5,3,"Y"],[5,40,"N"]]`
- Output: `[[5,3]]`

The primary department is selected by the flag, not by the smallest or largest identifier.

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(M)$

<details>
<summary>Approach</summary>

#### General

**Aggregate one output group per employee**

Group all membership rows by `employee_id`. This guarantees one result row for every employee regardless of how many departments they have.

**Extract the explicit primary when it exists**

Inside each group, use a conditional expression that returns `department_id` only when `primary_flag = 'Y'`, and aggregate it with `MAX`. A multi-department employee has one such row, so the aggregate yields that department. If no row is flagged, the conditional aggregate is `NULL`.

**Fall back only for the single-department rule**

Also compute `MAX(department_id)` across the group. `COALESCE` returns the conditional primary when present. Otherwise the contract guarantees that the employee has one membership, so the fallback aggregate returns that sole department.

The conditional branch selects every explicit primary exactly, and the fallback applies precisely when no explicit primary exists. Under the membership guarantees, that absence means the single row is the required department, so every employee receives exactly the correct result.

#### Complexity detail

A hash aggregation examines each of the $R$ membership rows once and performs constant work for its employee group, giving $O(R)$ expected logical time. The aggregation stores two scalar values for each of the $M$ employee groups, using $O(M)$ space.

#### Alternatives and edge cases

- **Window count plus filter:** Count memberships per employee and keep rows that are flagged or belong to a one-row partition. This is clear but may require partition sorting.
- **`UNION` of flagged and singleton rows:** Combine all `'Y'` rows with groups having count one. It is correct but scans or groups the source in separate branches and may require duplicate elimination unless `UNION ALL` is used carefully.
- **Correlated membership count:** Testing the row count separately for every source row can degrade to quadratic work without an appropriate index.
- **Single department with `'N'`:** It must be returned; filtering only for `'Y'` loses this employee.
- **Several departments:** Use the flagged row even when its department ID is not an extremum.
- **Input row order:** The primary row may occur before, after, or between nonprimary memberships.
- **Interleaved employees:** Grouping uses identifiers rather than relying on adjacent source rows.
- **Output order:** The platform accepts any order. The app-local query sorts by `employee_id` only for deterministic fixtures.

</details>
