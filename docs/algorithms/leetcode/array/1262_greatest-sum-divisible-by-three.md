# Greatest Sum Divisible by Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1262 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy, Sorting |
| Official Link | [greatest-sum-divisible-by-three](https://leetcode.com/problems/greatest-sum-divisible-by-three/) |

## Problem Description & Examples
### Goal
Choose a subsequence of numbers with the largest possible sum that is divisible by `3`.

### Function Contract
**Inputs**

- `nums`: positive integer array.

**Return value**

The greatest sum divisible by `3`.

### Examples
**Example 1**

- Input: `nums = [3,6,5,1,8]`
- Output: `18`

**Example 2**

- Input: `nums = [4]`
- Output: `0`

**Example 3**

- Input: `nums = [1,2,3,4,4]`
- Output: `12`

---

## Underlying Base Algorithm(s)
Dynamic programming by remainder.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
