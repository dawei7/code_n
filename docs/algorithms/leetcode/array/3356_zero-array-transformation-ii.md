# Zero Array Transformation II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3356 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Prefix Sum |
| Official Link | [zero-array-transformation-ii](https://leetcode.com/problems/zero-array-transformation-ii/) |

## Problem Description & Examples
### Goal
Determine the minimum prefix of a given list of operations (queries) required to reduce all elements in an integer array `nums` to zero or less. Each query consists of a range `[l, r]` and a value `val`, which subtracts `val` from every element in `nums` within that index range. If it is impossible to reduce all elements to zero even using all queries, return -1.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers representing the target values to be reduced.
- `queries`: A list of lists, where each inner list `[l, r, val]` defines an operation to subtract `val` from `nums[i]` for all `l <= i <= r`.

**Return value**

- An integer representing the smallest index `k` (1-indexed) such that applying the first `k` queries results in all elements of `nums` being <= 0. If no such `k` exists, return -1.

### Examples
**Example 1**

- Input: `nums = [2, 0, 2]`, `queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]`
- Output: `2`

**Example 2**

- Input: `nums = [4, 3, 2, 1]`, `queries = [[1, 3, 2], [0, 2, 1]]`
- Output: `-1`

**Example 3**

- Input: `nums = [1, 2, 3]`, `queries = [[0, 2, 1], [0, 2, 1], [0, 2, 1]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem exhibits a monotonic property: if the first `k` queries can zero out the array, then any number of queries greater than `k` will also satisfy the condition. This allows for **Binary Search** on the answer `k`. To efficiently check if a given `k` is valid, we use a **Difference Array** (or Prefix Sum) technique to apply range updates in $O(N + K)$ time, where $N$ is the length of `nums` and $K$ is the number of queries.

---

## Complexity Analysis
- **Time Complexity**: $O((N + Q) \log Q)$, where $N$ is the length of `nums` and $Q$ is the number of queries. The binary search runs $\log Q$ times, and each check takes $O(N + Q)$ time.
- **Space Complexity**: $O(N)$ to store the difference array used during the validation check.
