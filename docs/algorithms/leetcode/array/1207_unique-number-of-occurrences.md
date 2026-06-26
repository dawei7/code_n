# Unique Number of Occurrences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1207 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [unique-number-of-occurrences](https://leetcode.com/problems/unique-number-of-occurrences/) |

## Problem Description & Examples
### Goal
Determine whether every distinct value in the array appears a unique number of times.

### Function Contract
**Inputs**

- `arr`: integer array.

**Return value**

`true` if no two distinct values have the same frequency, otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [1,2,2,1,1,3]`
- Output: `true`

**Example 2**

- Input: `arr = [1,2]`
- Output: `false`

**Example 3**

- Input: `arr = [-3,0,1,-3,1,1,1,-3,10,0]`
- Output: `true`

---

## Underlying Base Algorithm(s)
Hash-map frequency counting.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(k)` for `k` distinct values.
