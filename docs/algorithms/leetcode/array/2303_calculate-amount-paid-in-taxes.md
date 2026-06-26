# Calculate Amount Paid in Taxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2303 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [calculate-amount-paid-in-taxes](https://leetcode.com/problems/calculate-amount-paid-in-taxes/) |

## Problem Description & Examples
### Goal
Calculate tax under progressive brackets. Each bracket's percentage applies only to income above the previous upper bound and at or below its own upper bound.

### Function Contract
**Inputs**

- `brackets`: increasing pairs `[upper, percent]`.
- `income`: the nonnegative taxable income.

**Return value**

The total tax paid as a decimal amount.

### Examples
**Example 1**

- Input: `brackets = [[3, 50], [7, 10], [12, 25]]`, `income = 10`
- Output: `2.65`

**Example 2**

- Input: `brackets = [[1, 0], [4, 25], [5, 50]]`, `income = 2`
- Output: `0.25`

**Example 3**

- Input: `brackets = [[5, 20]]`, `income = 0`
- Output: `0.0`

---

## Underlying Base Algorithm(s)
Traverse brackets while tracking the previous upper bound. Tax the portion `min(income, upper) - previous` at the current percentage when positive, then stop once the bracket reaches the income.

---

## Complexity Analysis
- **Time Complexity**: `O(b)`
- **Space Complexity**: `O(1)`
