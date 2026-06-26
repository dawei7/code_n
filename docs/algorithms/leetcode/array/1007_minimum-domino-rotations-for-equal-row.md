# Minimum Domino Rotations For Equal Row

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1007 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [minimum-domino-rotations-for-equal-row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/) |

## Problem Description & Examples
### Goal
Each domino has a top and bottom value. You may rotate individual dominoes to swap top and bottom. Return the minimum rotations needed so all top values are equal or all bottom values are equal, or `-1` if impossible.

### Function Contract
**Inputs**

- `tops`: List[int]
- `bottoms`: List[int]

**Return value**

int - minimum rotations, or `-1`

### Examples
**Example 1**

- Input: `tops = [2, 1, 2, 4, 2, 2], bottoms = [5, 2, 6, 2, 3, 2]`
- Output: `2`

**Example 2**

- Input: `tops = [3, 5, 1, 2, 3], bottoms = [3, 6, 3, 3, 4]`
- Output: `-1`

**Example 3**

- Input: `tops = [1, 1, 1], bottoms = [1, 2, 3]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Greedy candidate validation.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
