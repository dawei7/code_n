# Trapping Rain Water

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 42 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/trapping-rain-water/) |

## Problem Description
### Goal
The array `height` describes adjacent vertical bars of unit width standing on a common baseline. After rain, water may collect in depressions between taller bars; water beyond either outer edge escapes.

For each horizontal position, the stable water level is limited by the tallest boundary available on both its left and right. Sum the water units held above every bar and return the total volume. Bars have nonnegative integer heights, and empty or too-short profiles trap no water.

### Function Contract
**Inputs**

- `height`: `List[int]` of non-negative bar heights

**Return value**

An `int` equal to the total trapped water volume.

### Examples
**Example 1**

- Input: `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`
- Output: `6`

**Example 2**

- Input: `height = [4, 2, 0, 3, 2, 5]`
- Output: `9`

**Example 3**

- Input: `height = []`
- Output: `0`
