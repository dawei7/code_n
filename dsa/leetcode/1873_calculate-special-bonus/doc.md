# Calculate Special Bonus

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/calculate-special-bonus/) |
| Frontend ID | 1873 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Employees` table contains one row per employee, recording a unique `employee_id`, the employee's `name`, and their `salary`. Every employee must appear in the result with a calculated special bonus.

An employee receives a bonus equal to their full salary only when both conditions hold: the employee identifier is odd, and the name does not begin with the uppercase character `"M"`. If either condition fails, the bonus is zero. Return each identifier and calculated bonus, ordered by `employee_id` in ascending order.

### Function Contract

**Inputs**

- `Employees(employee_id, name, salary)`: one row per employee; `employee_id` is unique.
- Let $R$ be the number of employee rows.

**Return value**

- Return columns `employee_id` and `bonus`.
- Set `bonus` to `salary` exactly for odd identifiers whose names do not start with `"M"`; otherwise set it to `0`.
- Return all employees in ascending `employee_id` order.

### Examples

**Example 1**

- Input: employees `(2,"Meir",3000)`, `(3,"Michael",3800)`, `(7,"Addilyn",7400)`, `(8,"Juan",6100)`, `(9,"Kannon",7700)`
- Output: `[[2,0],[3,0],[7,7400],[8,0],[9,7700]]`

Even identifiers receive zero, as does Michael because his name starts with `"M"`.

**Example 2**

- Input: employee `(1,"Alice",5000)`
- Output: `[[1,5000]]`

The identifier is odd and the name does not start with `"M"`.

**Example 3**

- Input: employees `(5,"Mina",4200)` and `(6,"Noah",6100)`
- Output: `[[5,0],[6,0]]`

The first fails the name rule and the second fails the identifier rule.

### Required Complexity

- **Time:** $O(R\log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Project one result row per employee**

Select `employee_id` directly. A `CASE` expression tests `employee_id % 2 = 1` together with `name NOT LIKE 'M%'`. When both predicates hold, emit `salary`; the `ELSE` branch emits zero. Keeping the conditions in the projection, rather than in `WHERE`, ensures employees who receive no bonus still appear.

**Encode the name rule as a prefix pattern**

The pattern `'M%'` means an initial `"M"` followed by any suffix, including an empty suffix. Negating that match expresses exactly that the name does not start with `"M"`; searching for `"M"` elsewhere in the name would be incorrect.

**Apply the required result order**

Sort by `employee_id` ascending. Since the identifier is unique, this produces a deterministic order without a secondary key.

#### Complexity detail

The conditional projection examines each of the $R$ rows once. Without a usable preordered index, sorting the result by identifier takes $O(R\log R)$ time and $O(R)$ working space. A database that scans a suitable `employee_id` index in order can reduce the physical sort work, but the stated bound covers the general execution plan and returned rows.

#### Alternatives and edge cases

- **Boolean multiplication:** Multiplying `salary` by a Boolean condition is concise in some dialects, but `CASE` is clearer and more portable.
- **Filter qualifying employees:** A `WHERE` clause alone is wrong because zero-bonus employees must remain in the output.
- **`UNION ALL` branches:** Separate qualifying and nonqualifying queries can work but duplicate predicates and still require a final sort.
- **Odd ID with `"M"` name:** The name condition fails, so the bonus is zero.
- **Even ID with another name:** The parity condition fails, so the bonus is zero.
- **`"M"` inside the name:** Only the first character matters.
- **Output order:** `ORDER BY employee_id` is mandatory.

</details>
