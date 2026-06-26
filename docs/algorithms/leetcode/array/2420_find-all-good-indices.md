# Find All Good Indices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2420 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Official Link | [find-all-good-indices](https://leetcode.com/problems/find-all-good-indices/) |

## Problem Description & Examples
### Goal
Identify all indices `i` in an array `nums` such that the `k` elements immediately preceding `i` are in non-increasing order, and the `k` elements immediately following `i` are in non-decreasing order. The index `i` itself is excluded from these checks.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to analyze.
- `k`: An integer representing the required length of the non-increasing and non-decreasing subarrays.

**Return value**

- A list of integers representing all valid "good" indices in ascending order.

### Examples
**Example 1**

- Input: `nums = [2,1,1,1,3,4,1], k = 2`
- Output: `[2, 3]`

**Example 2**

- Input: `nums = [2,1,1,2], k = 2`
- Output: `[]`

**Example 3**

- Input: `nums = [1,2,3,4,5], k = 1`
- Output: `[1, 2, 3]`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming (or Prefix/Suffix arrays). We precompute two boolean arrays: `non_increasing` and `non_decreasing`. `non_increasing[i]` tracks how many consecutive elements ending at `i` are non-increasing, and `non_decreasing[i]` tracks how many consecutive elements starting at `i` are non-decreasing. An index `i` is "good" if `non_increasing[i-1] >= k` and `non_decreasing[i+1] >= k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a constant number of linear passes over the data.
- **Space Complexity**: `O(n)` to store the precomputed prefix and suffix counts.
