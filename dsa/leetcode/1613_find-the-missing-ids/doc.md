# Find the Missing IDs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1613 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-missing-ids/) |

## Problem Description
### Goal
Table `Customers` contains existing customer identifiers and their names, but the positive identifier sequence may have gaps. Let $m$ be the greatest `customer_id` currently present.

Find every integer ID from 1 through $m$ that does not occur in `Customers`. Return those absent IDs in ascending order. Values above the current maximum are outside the requested range and must not be generated.

### Function Contract
**Inputs**

- `Customers(customer_id, customer_name)`, with one row per existing customer and a unique positive `customer_id`.
- Let $c$ be the number of customer rows and $m=\max(\texttt{customer_id})$.

**Return value**

Return a relation with one column named `ids`, containing every missing integer in the inclusive range from 1 through $m$, sorted ascending.

### Examples
**Example 1**

- Input: customer IDs `[1, 4, 5]`
- Output: IDs `[2, 3]`

**Example 2**

- Input: customer IDs `[1, 2, 3]`
- Output: no rows, because the range is consecutive.

**Example 3**

- Input: the only customer ID is `5`
- Output: IDs `[1, 2, 3, 4]`
