# Employee Bonus

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 577 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/employee-bonus/) |

## Problem Description
### Goal
Given an `Employee` table and a `Bonus` table keyed by the unique employee identifier `empId`, find every employee whose bonus is less than `1000`. An employee may have no matching row in `Bonus`; that missing bonus also satisfies the requested condition and must not cause the employee to disappear from the result.

Return each qualifying employee's `name` and `bonus` in any order. Preserve `NULL` as the bonus for employees without a bonus record, and exclude a recorded bonus of exactly `1000` because the comparison is strictly less than `1000`.

### Function Contract
**Inputs**

- `Employee(empId, name, supervisor, salary)`: employee details
- `Bonus(empId, bonus)`: optional bonus amounts keyed by employee identifier

**Return value**

- A result grid with columns `name` and `bonus`
- Include employees whose bonus is below 1000 and employees with no matching bonus row; the latter have `NULL` in `bonus`

### Examples
**Example 1**

- Input: an employee has bonus `500`
- Output: that employee's name and `500`

**Example 2**

- Input: an employee has no row in `Bonus`
- Output: that employee's name and `NULL`

**Example 3**

- Input: an employee has bonus `1000`
- Output: no row for that employee

### Required Complexity

- **Time:** $O((E + B) \log(E + B))$
- **Space:** $O(E + B)$

<details>
<summary>Approach</summary>

#### General

**Preserve employees without bonuses**

Start from `Employee` and left join `Bonus` on `empId`. An inner join would discard the employees whose absent bonus records are part of the requested output.

**Distinguish a small bonus from no bonus**

After the left join, a matching amount below 1000 satisfies `bonus < 1000`. A missing match produces `NULL`, which does not satisfy an ordinary comparison, so the filter must separately accept `bonus IS NULL`.

**Why every output row qualifies**

Each joined row retains one employee and either supplies that employee's bonus or `NULL` when none exists. The disjunction keeps exactly the two permitted states: a present amount strictly below the threshold, or an absent bonus. Amounts at or above 1000 satisfy neither branch and are excluded.

#### Complexity detail

For `E` employee rows and `B` bonus rows, a typical indexed, hashed, or sorted join takes $O((E + B) \log(E + B))$ time in the general model and $O(E + B)$ working space. Suitable indexes can make the join near-linear.

#### Alternatives and edge cases

- **Correlated bonus lookup:** can express both the value and filter, but may rescan `Bonus` for every employee and take $O(EB)$ time.
- **Inner join plus union:** one branch can select small bonuses and another employees without matches, but it duplicates join logic.
- **`COALESCE(bonus, 0) < 1000`:** works only if treating missing as zero cannot conflict with the data semantics; the explicit null branch is clearer.
- **Bonus exactly 1000:** is excluded because the comparison is strict.
- **No bonus row:** remains present because of the left join and qualifies through `IS NULL`.
- **Zero or negative bonus:** is below 1000 and qualifies.
- **High bonus:** is excluded even though the employee row itself remains valid.
- **Null comparison:** `NULL < 1000` is unknown, not true, so `IS NULL` is necessary.

</details>
