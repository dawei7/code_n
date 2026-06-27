# Minimum Cost for Cutting Cake I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3218 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Dynamic Programming, Greedy, Sorting |
| Official Link | [minimum-cost-for-cutting-cake-i](https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/) |

## Problem Description & Examples
### Goal
Given a cake of size `m x n`, you must cut it into `1 x 1` individual squares. You are provided with the costs to perform horizontal cuts and vertical cuts. Each cut spans the entire current piece of cake. When you make a cut, the cost of that cut is multiplied by the number of pieces of that dimension currently existing. The objective is to determine the minimum total cost to reduce the entire cake into `1 x 1` units.

### Function Contract
**Inputs**

- `m`: An integer representing the number of rows.
- `n`: An integer representing the number of columns.
- `horizontalCut`: A list of integers where `horizontalCut[i]` is the cost of the `i`-th horizontal cut.
- `verticalCut`: A list of integers where `verticalCut[j]` is the cost of the `j`-th vertical cut.

**Return value**

- An integer representing the minimum total cost to cut the cake into `1 x 1` squares.

### Examples
**Example 1**

- Input: `m = 3, n = 2, horizontalCut = [1, 3], verticalCut = [5]`
- Output: `13`

**Example 2**

- Input: `m = 2, n = 2, horizontalCut = [7], verticalCut = [4]`
- Output: `15`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy strategy**. The key insight is that a cut made earlier is multiplied by more pieces later. Therefore, we should always prioritize the most expensive cuts first. By sorting both `horizontalCut` and `verticalCut` in descending order, we can iterate through the cuts and pick the largest available cost. If we pick a horizontal cut, it increases the number of vertical segments (pieces) we have, and vice versa.

---

## Complexity Analysis
- **Time Complexity**: `O(M log M + N log N)`, where `M` and `N` are the lengths of the horizontal and vertical cut arrays, respectively, due to the sorting step.
- **Space Complexity**: `O(1)` (excluding the space required for sorting), as we only maintain counters for the number of horizontal and vertical pieces.
