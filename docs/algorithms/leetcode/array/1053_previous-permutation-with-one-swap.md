# Previous Permutation With One Swap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1053 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [previous-permutation-with-one-swap](https://leetcode.com/problems/previous-permutation-with-one-swap/) |

## Problem Description & Examples
### Goal
Given an array of positive integers, make at most one swap to produce the lexicographically largest array that is still strictly smaller than the original.

### Function Contract
**Inputs**

- `arr`: List[int]

**Return value**

List[int] - previous permutation after at most one swap

### Examples
**Example 1**

- Input: `arr = [3, 2, 1]`
- Output: `[3, 1, 2]`

**Example 2**

- Input: `arr = [1, 1, 5]`
- Output: `[1, 1, 5]`

**Example 3**

- Input: `arr = [1, 9, 4, 6, 7]`
- Output: `[1, 7, 4, 6, 9]`

---

## Underlying Base Algorithm(s)
Greedy previous-permutation pivot selection.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
