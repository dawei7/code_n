# Matchsticks to Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 473 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/matchsticks-to-square/) |

## Problem Description
### Goal
Given positive matchstick lengths, determine whether all sticks can be assigned to four sides of one square. Every stick must be used exactly once, no stick may be broken, and side length is the sum of sticks assigned to that side.

Return `True` only when the four side sums can be equal and positive. The complete length must therefore be divisible by four, and no individual stick may exceed the required side length, though those conditions alone are not sufficient. Stick order inside a side is irrelevant, duplicate lengths remain separate occurrences, and the function need not return the grouping.

### Function Contract
**Inputs**

- `matchsticks`: positive integer stick lengths

**Return value**

- `True` if the sticks can be partitioned into four groups with equal sums; otherwise `False`

### Examples
**Example 1**

- Input: `matchsticks = [1, 1, 2, 2, 2]`
- Output: `True`

**Example 2**

- Input: `matchsticks = [3, 3, 3, 3, 4]`
- Output: `False`

**Example 3**

- Input: `matchsticks = [2, 2, 2, 1, 1]`
- Output: `True`
