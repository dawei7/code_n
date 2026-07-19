# Remove Boxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 546 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-boxes/) |

## Problem Description
### Goal
Given a row of colored boxes, one move selects a contiguous group of $k \ge 1$ boxes having the same color and removes the complete group. That move earns $k^{2}$ points, and boxes on the two sides close together after removal.

Remove all boxes and return the maximum total score obtainable. The current grouping changes after every move, so separating equal colors temporarily may allow them to join into a larger and more valuable group later. Each box is removed exactly once, and the function returns only the optimal score rather than the sequence of groups chosen.

### Function Contract
**Inputs**

- `boxes`: a non-empty list of integers representing box colors

**Return value**

- The greatest score achievable by choosing the removal order optimally

### Examples
**Example 1**

- Input: `boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]`
- Output: `23`

**Example 2**

- Input: `boxes = [1, 1, 1]`
- Output: `9`

**Example 3**

- Input: `boxes = [1]`
- Output: `1`
