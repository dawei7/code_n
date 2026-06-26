# Sort Array by Increasing Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1636 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sorting |
| Official Link | [sort-array-by-increasing-frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) |

## Problem Description & Examples
### Goal
Sort numbers by increasing frequency. If two values have the same frequency,
place the larger value first.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The reordered array.

### Examples
**Example 1**

- Input: `nums = [1, 1, 2, 2, 2, 3]`
- Output: `[3, 1, 1, 2, 2, 2]`

**Example 2**

- Input: `nums = [2, 3, 1, 3, 2]`
- Output: `[1, 3, 3, 2, 2]`

**Example 3**

- Input: `nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]`
- Output: `[5, -1, 4, 4, -6, -6, 1, 1, 1]`

---

## Underlying Base Algorithm(s)
Count frequencies with a hash map, then sort using the key
`(frequency[value], -value)`.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(n)`.
