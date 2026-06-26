# Moving Stones Until Consecutive II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1040 |
| Difficulty | Medium |
| Topics | Array, Math, Sliding Window, Sorting |
| Official Link | [moving-stones-until-consecutive-ii](https://leetcode.com/problems/moving-stones-until-consecutive-ii/) |

## Problem Description & Examples
### Goal
Given stone positions on a number line, each move relocates an endpoint stone to an unoccupied non-endpoint position. Return the minimum and maximum number of moves needed to make all stones occupy consecutive positions.

### Function Contract
**Inputs**

- `stones`: List[int] distinct stone positions

**Return value**

List[int] - `[minimum_moves, maximum_moves]`

### Examples
**Example 1**

- Input: `stones = [7, 4, 9]`
- Output: `[1, 2]`

**Example 2**

- Input: `stones = [6, 5, 4, 3, 10]`
- Output: `[2, 3]`

**Example 3**

- Input: `stones = [100, 101, 102, 103, 104]`
- Output: `[0, 0]`

---

## Underlying Base Algorithm(s)
Sorting plus sliding window.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space if sorting in place
