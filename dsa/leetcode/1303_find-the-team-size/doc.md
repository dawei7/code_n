# Find the Team Size

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1303 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-team-size/) |

## Problem Description
### Goal
The `Employee` table records each employee's identifier and the identifier of the team to which that employee belongs. Every employee row belongs to exactly one recorded team, and multiple employees may share the same `team_id`.

Produce one result row for every employee. Alongside `employee_id`, report `team_size`: the total number of employees whose `team_id` matches that employee's team. The result may be returned in any order.

### Function Contract
**Input table**

`Employee`

| Column | Type | Meaning |
|---|---|---|
| `employee_id` | integer | Primary key identifying one employee. |
| `team_id` | integer | Identifier of the employee's team. |

Let $n$ be the number of rows in `Employee`.

**Return value**

A relation with columns `employee_id` and `team_size`, containing exactly one row per employee and the count of rows in that employee's team.

### Examples
**Example 1**

- Input: `Employee = [(1,8),(2,8),(3,8),(4,7),(5,9),(6,9)]`
- Output: `[(1,3),(2,3),(3,3),(4,1),(5,2),(6,2)]`
- Explanation: Team 8 has three members, team 7 has one, and team 9 has two.

**Example 2**

- Input: `Employee = [(10,4)]`
- Output: `[(10,1)]`

**Example 3**

- Input: `Employee = [(1,5),(2,6),(3,5),(4,6)]`
- Output: `[(1,2),(2,2),(3,2),(4,2)]`

### Required Complexity
- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Count a partition without collapsing its rows**

A `GROUP BY team_id` can calculate one size per team, but the requested output has one row per employee. Use a windowed `COUNT(*)` partitioned by `team_id`. The partition makes every row with the same team identifier share one counting frame, while the window operation preserves the original employee rows.

Select `employee_id` directly and name the window count `team_size`. Each employee therefore retains its own identifier and receives the size of exactly its team. An `ORDER BY employee_id` makes local verification deterministic even though the source contract permits any output order.

#### Complexity detail

A database engine can partition or sort the $n$ rows by `team_id` and order the output in $O(n \log n)$ time. The window and ordered result may require $O(n)$ working space. Physical plans can vary by engine and available indexes.

#### Alternatives and edge cases

- **Aggregate then join:** Grouping by `team_id` and joining the counts back to `Employee` is also correct, but requires an additional relational step.
- **Correlated count subquery:** Counting matching team rows separately for every employee is simple but can take $O(n^2)$ time without a supporting index.
- **Singleton team:** Its sole employee receives `team_size = 1`.
- **Noncontiguous identifiers:** Counts depend only on equal `team_id` values, not on numeric adjacency.
- **Several equal-size teams:** Each employee still receives the count from their own partition.
- **Output cardinality:** The query must return exactly one row per input employee rather than one row per team.

</details>
