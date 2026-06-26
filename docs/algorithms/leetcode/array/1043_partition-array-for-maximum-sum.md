# Partition Array for Maximum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1043 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [partition-array-for-maximum-sum](https://leetcode.com/problems/partition-array-for-maximum-sum/) |

## Problem Description & Examples
### Goal
Partition an array into contiguous groups of length at most `k`. Each group contributes its maximum value repeated for the group length. Return the largest possible total.

### Function Contract
**Inputs**

- `arr`: List[int]
- `k`: int maximum partition length

**Return value**

int - maximum transformed sum

### Examples
**Example 1**

- Input: `arr = [1, 15, 7, 9, 2, 5, 10], k = 3`
- Output: `84`

**Example 2**

- Input: `arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k = 4`
- Output: `83`

**Example 3**

- Input: `arr = [1], k = 1`
- Output: `1`

---

## Underlying Base Algorithm(s)
One-dimensional dynamic programming.

---

## Complexity Analysis
- **Time Complexity**: `O(n * k)`
- **Space Complexity**: `O(n)`
