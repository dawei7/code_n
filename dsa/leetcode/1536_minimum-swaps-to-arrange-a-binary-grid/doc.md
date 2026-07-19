# Minimum Swaps to Arrange a Binary Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1536 |
| Difficulty | Medium |
| Topics | Array, Greedy, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/) |

## Problem Description
### Goal

Given an $n\times n$ binary grid, one step may swap two adjacent complete rows. A grid is valid when every cell strictly above the main diagonal is zero.

Return the minimum number of adjacent-row swaps needed to produce a valid grid. If no ordering of the existing rows can satisfy the requirement, return `-1`; columns and the contents within each row cannot be rearranged.

### Function Contract
**Inputs**

- `grid`: An $n\times n$ matrix of zeros and ones, where $1\leq n\leq200$.

**Return value**

Return the minimum adjacent-row swap count that makes every position $(i,j)$ with $j>i$ equal to zero, or `-1` if this is impossible.

### Examples
**Example 1**

- Input: `grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]`
- Output: `3`
- Explanation: The row with two trailing zeros must move to the top, requiring two swaps, and the row with one trailing zero then moves to the middle.

**Example 2**

- Input: four identical rows `[0, 1, 1, 0]`
- Output: `-1`
- Explanation: No row has the three trailing zeros required at the top.

**Example 3**

- Input: `grid = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]`
- Output: `0`
- Explanation: The grid already has only zeros above its main diagonal.
