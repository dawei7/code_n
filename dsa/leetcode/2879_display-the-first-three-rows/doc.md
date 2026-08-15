# Display the First Three Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2879 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/display-the-first-three-rows/) |

## Problem Description

### Goal

The pandas `DataFrame` named `employees` stores employee records in their current row order. Its four columns are `employee_id`, `name`, `department`, and `salary`; each output row must retain all four values and the original column labels.

Return a DataFrame containing only the first three rows of `employees`, without sorting or otherwise changing their order. If the input contains fewer than three rows, return every available row. Rows after the third position must not appear in the result.

### Function Contract

**Inputs**

- `employees`: A pandas `DataFrame` with columns `employee_id`, `name`, `department`, and `salary`.

**Return value**

A pandas `DataFrame` containing the first `min(3, len(employees))` rows with the original columns and order.

### Examples

#### Example 1

- **Input:** six employee rows beginning with Bob, Alice, and Tatiana.
- **Output:** the three rows for Bob, Alice, and Tatiana, with all four columns preserved.

#### Example 2

- **Input:** exactly three employee rows.
- **Output:** all three rows in their original order.

#### Example 3

- **Input:** one employee row.
- **Output:** that single row with the original schema.
