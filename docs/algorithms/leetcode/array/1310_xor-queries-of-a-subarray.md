# XOR Queries of a Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1310 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation, Prefix Sum |
| Official Link | [xor-queries-of-a-subarray](https://leetcode.com/problems/xor-queries-of-a-subarray/) |

## Problem Description & Examples
### Goal
For each query `[left, right]`, return the bitwise XOR of `arr[left]` through `arr[right]`.

### Function Contract
**Inputs**

- `arr`: integer array.
- `queries`: inclusive index ranges.

**Return value**

The XOR value for each query in order.

### Examples
**Example 1**

- Input: `arr = [1,3,4,8]`, `queries = [[0,1],[1,2],[0,3],[3,3]]`
- Output: `[2,7,14,8]`

**Example 2**

- Input: `arr = [4,8,2,10]`, `queries = [[2,3],[1,3],[0,0],[0,3]]`
- Output: `[8,0,4,4]`

**Example 3**

- Input: `arr = [5]`, `queries = [[0,0]]`
- Output: `[5]`

---

## Underlying Base Algorithm(s)
Prefix XOR.

---

## Complexity Analysis
- **Time Complexity**: `O(n + q)`
- **Space Complexity**: `O(n)`
