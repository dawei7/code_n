# Find Minimum Cost to Remove Array Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3469 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/) |

## Problem Description
### Goal
Given an integer array `nums`, remove every element through a sequence of charged operations. Whenever at least three elements remain, choose any two among the current first three elements and remove them. That operation costs the maximum of the two removed values, while the unchosen element stays at the front of the remaining array.

When fewer than three elements remain, remove all of them together in one final operation whose cost is their maximum value. The total cost is the sum paid by every operation. Return the smallest total obtainable by choosing which pair to remove at each step.

### Function Contract
**Inputs**

- `nums`: The array of positive values to remove.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $1\le n\le1000$ and $1\le\texttt{nums[i]}\le10^6$.

**Return value**

Return the minimum total cost required to remove all elements.

### Examples
**Example 1**

- Input: `nums = [6,2,8,4]`
- Output: `12`

Remove 6 and 8 from the first three for a cost of 8, then remove the remaining `[2,4]` for a cost of 4.

**Example 2**

- Input: `nums = [2,1,3,3]`
- Output: `5`

Remove 2 and 1 for a cost of 2, then pay 3 to remove the final two elements.

**Example 3**

- Input: `nums = [7]`
- Output: `7`

Fewer than three elements are present initially, so the single value is removed at its own cost.
