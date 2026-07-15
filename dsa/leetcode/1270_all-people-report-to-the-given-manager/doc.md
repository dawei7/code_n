# All People Report to the Given Manager

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1270 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/all-people-report-to-the-given-manager/) |

## Problem Description

### Goal

The `Employees` table describes a small company's reporting hierarchy. Each row gives one employee's unique identifier and name together with the identifier of that employee's direct manager. The company head has `employee_id = 1`; that row reports to itself.

Find the identifiers of all employees whose chain of direct managers eventually reaches the company head, whether they report to the head directly or through other managers. Do not include the head. A reporting chain contains at most three managers, and employees belonging to a separate self-managed hierarchy must be excluded. Return the qualifying identifiers in any order without duplicates.

### Function Contract

**Inputs**

- `Employees(employee_id, employee_name, manager_id)`: one row per employee, with `employee_id` unique and `manager_id` naming the direct manager.
- Let $n$ be the number of rows in `Employees`.

**Return value**

- Return a one-column table named `employee_id` containing every non-head employee who reports directly or indirectly to employee `1`.

### Examples

**Example 1**

- Input: employees `2` and `77` report to `1`, employee `4` reports to `2`, employee `7` reports to `4`, and a separate hierarchy is rooted at self-managed employee `3`.
- Output: employee identifiers `2`, `4`, `7`, and `77` in any order.

**Example 2**

- Input: the table contains only the head row `(1, "Boss", 1)`.
- Output: an empty result.

**Example 3**

- Input: `2 -> 1`, `3 -> 2`, and `4 -> 3`.
- Output: employee identifiers `2`, `3`, and `4`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Resolve the bounded manager chain with self-joins**

Alias `Employees` three times. The first alias is the candidate employee, the second is that employee's direct manager, and the third is the next manager. Join each `manager_id` to the following alias's `employee_id`. Because a chain contains at most three managers, checking whether the third alias's `manager_id` is `1` covers direct reports, reports through one intermediate manager, and reports through two intermediate managers.

The head's self-reference makes shorter chains naturally fill the remaining joins with employee `1`. For example, a direct report follows candidate -> head -> head, while a three-manager chain follows candidate -> manager -> manager -> head. Explicitly exclude candidate `1` so that this useful self-reference does not place the head in its own result.

Every returned employee has a concrete joined chain ending at `1`, so no unrelated hierarchy can pass. Conversely, any allowed reporting chain has at most three manager edges; padding a shorter chain with the head's self-reference satisfies the same joins and condition, so every qualifying employee is returned.

#### Complexity detail

With indexed lookup on the unique `employee_id`, each of the $n$ candidate rows performs a constant number of manager lookups, giving $O(n)$ logical time. The result and database join state can contain $O(n)$ rows, so the space bound is $O(n)$. A physical engine without usable indexes may choose a slower join plan.

#### Alternatives and edge cases

- **Recursive common table expression:** Traversing outward from the head generalizes to arbitrary hierarchy depth, but the source's three-manager bound makes fixed self-joins simpler.
- **Unconstrained cross joins:** Filtering a Cartesian product can produce the same rows but may examine $O(n^3)$ combinations.
- **Direct reports only:** Testing `manager_id = 1` misses employees reached through intermediate managers.
- **Head row:** Employee `1` must be excluded even though its self-reference reaches `1`.
- **Separate self-managed hierarchy:** A chain rooted at an employee other than `1` never satisfies the final head condition.
- **Maximum-depth chain:** A candidate three manager edges from the head is still included.
- **Output order:** The contract accepts any order; the app-local query orders identifiers only for deterministic display.

</details>
