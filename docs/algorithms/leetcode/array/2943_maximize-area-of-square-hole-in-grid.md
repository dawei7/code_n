# Maximize Area of Square Hole in Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2943 |
| Difficulty | Medium |
| Topics | Array, Sorting |
| Official Link | [maximize-area-of-square-hole-in-grid](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/) |

## Problem Description & Examples
### Goal
Given a grid defined by horizontal and vertical bars, identify the largest possible square hole that can be formed by removing a contiguous sequence of bars. A square hole is created by removing $k$ consecutive horizontal bars and $k$ consecutive vertical bars, resulting in a square of side length $k+1$.

### Function Contract
**Inputs**

- `n`: An integer representing the number of horizontal bars (excluding the boundary).
- `m`: An integer representing the number of vertical bars (excluding the boundary).
- `hBars`: A list of integers representing the positions of horizontal bars.
- `vBars`: A list of integers representing the positions of vertical bars.

**Return value**

- An integer representing the maximum area of the square hole that can be formed.

### Examples
**Example 1**

- Input: `n = 2, m = 1, hBars = [2, 3], vBars = [2]`
- Output: `4`

**Example 2**

- Input: `n = 1, m = 1, hBars = [2], vBars = [2]`
- Output: `4`

**Example 3**

- Input: `n = 2, m = 3, hBars = [2, 3], vBars = [2, 3, 4]`
- Output: `9`

---

## Underlying Base Algorithm(s)
The problem reduces to finding the longest sequence of consecutive integers in the provided bar lists. By sorting the bars and identifying the maximum number of consecutive segments, we determine the maximum side length $k+1$ of a square. The area is then the square of the minimum of the maximum consecutive horizontal and vertical segments.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N + M \log M)$, where $N$ and $M$ are the lengths of `hBars` and `vBars` respectively, due to the sorting step.
- **Space Complexity**: $O(1)$ (excluding the input storage), as we only track the current and maximum consecutive sequences.
