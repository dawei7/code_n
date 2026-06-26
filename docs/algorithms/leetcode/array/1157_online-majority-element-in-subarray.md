# Online Majority Element In Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1157 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Design, Binary Indexed Tree, Segment Tree |
| Official Link | [online-majority-element-in-subarray](https://leetcode.com/problems/online-majority-element-in-subarray/) |

## Problem Description & Examples
### Goal
Design a structure that answers range queries asking for a value that appears at least `threshold` times in `arr[left:right+1]`.

### Function Contract
**Inputs**

- Constructor receives `arr`.
- `query(left, right, threshold)` receives an inclusive range and a required frequency.

**Return value**

A value meeting the threshold inside the range, or `-1` if no such value exists.

### Examples
**Example 1**

- Input: `arr = [1,1,2,2,1,1]`; `query(0,5,4)`
- Output: `1`

**Example 2**

- Input: `arr = [1,1,2,2,1,1]`; `query(0,3,3)`
- Output: `-1`

**Example 3**

- Input: `arr = [2,2,1,1,1,2,2]`; `query(2,4,2)`
- Output: `1`

---

## Underlying Base Algorithm(s)
Segment tree with majority-candidate merging and binary-search verification.

---

## Complexity Analysis
- **Time Complexity**: constructor `O(n log n)` including position indexes, each query `O(log n + log f)` where `f` is the candidate's global frequency.
- **Space Complexity**: `O(n)`
