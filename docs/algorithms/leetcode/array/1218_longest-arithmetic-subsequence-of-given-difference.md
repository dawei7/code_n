# Longest Arithmetic Subsequence of Given Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1218 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Dynamic Programming |
| Official Link | [longest-arithmetic-subsequence-of-given-difference](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/) |

## Problem Description & Examples
### Goal
Find the longest subsequence where consecutive selected values differ by exactly `difference`.

### Function Contract
**Inputs**

- `arr`: integer array.
- `difference`: required difference between consecutive subsequence values.

**Return value**

The maximum length of such a subsequence.

### Examples
**Example 1**

- Input: `arr = [1,2,3,4]`, `difference = 1`
- Output: `4`

**Example 2**

- Input: `arr = [1,3,5,7]`, `difference = 1`
- Output: `1`

**Example 3**

- Input: `arr = [1,5,7,8,5,3,4,2,1]`, `difference = -2`
- Output: `4`

---

## Underlying Base Algorithm(s)
Hash-map dynamic programming.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
