# Partition Array Into Three Parts With Equal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1013 |
| Difficulty | Easy |
| Topics | Array, Greedy |
| Official Link | [partition-array-into-three-parts-with-equal-sum](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/) |

## Problem Description & Examples
### Goal
Determine whether an array can be split into three nonempty contiguous parts that all have the same sum.

### Function Contract
**Inputs**

- `arr`: List[int]

**Return value**

bool - `True` if such a three-way split exists

### Examples
**Example 1**

- Input: `arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]`
- Output: `True`

**Example 2**

- Input: `arr = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]`
- Output: `False`

**Example 3**

- Input: `arr = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]`
- Output: `True`

---

## Underlying Base Algorithm(s)
Prefix accumulation and greedy segment counting.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
