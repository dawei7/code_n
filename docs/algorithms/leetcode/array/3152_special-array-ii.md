# Special Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3152 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Prefix Sum |
| Official Link | [special-array-ii](https://leetcode.com/problems/special-array-ii/) |

## Problem Description & Examples
### Goal
Determine whether specific subarrays within a given integer array are "special." A subarray is defined as special if every pair of adjacent elements within that subarray has different parity (i.e., one is even and the other is odd). You are provided with a list of queries, where each query specifies a range `[from, to]`, and you must return a boolean indicating if the subarray spanning that range satisfies the parity condition.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `queries`: A list of lists, where each inner list contains two integers `[from, to]` representing the start and end indices (inclusive) of the subarray.

**Return value**

- A list of booleans corresponding to each query, where `True` indicates the subarray is special and `False` otherwise.

### Examples
**Example 1**

- Input: `nums = [3, 4, 1, 2, 6]`, `queries = [[0, 4]]`
- Output: `[False]`

**Example 2**

- Input: `nums = [4, 3, 1, 6]`, `queries = [[0, 2], [2, 3]]`
- Output: `[False, True]`

**Example 3**

- Input: `nums = [1], queries = [[0, 0]]`
- Output: `[True]`

---

## Underlying Base Algorithm(s)
The optimal approach utilizes a **Prefix Sum** array to track parity violations. We pre-calculate an array where `violation[i]` is 1 if `nums[i]` and `nums[i+1]` have the same parity, and 0 otherwise. By computing the prefix sum of this violation array, we can determine if any violations exist within a range `[start, end]` in constant time by checking if the sum of violations between `start` and `end-1` is greater than zero.

---

## Complexity Analysis
- **Time Complexity**: `O(N + Q)`, where `N` is the length of `nums` and `Q` is the number of queries. We perform a single pass to build the prefix sum array and then answer each query in `O(1)`.
- **Space Complexity**: `O(N)` to store the prefix sum array.
