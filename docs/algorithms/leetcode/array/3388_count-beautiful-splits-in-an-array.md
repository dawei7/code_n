# Count Beautiful Splits in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3388 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [count-beautiful-splits-in-an-array](https://leetcode.com/problems/count-beautiful-splits-in-an-array/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the number of ways to partition the array into three non-empty contiguous subarrays (let's call them `nums1`, `nums2`, and `nums3`) such that either `nums1` is a prefix of `nums2`, or `nums2` is a prefix of `nums3`.

### Function Contract
**Inputs**

- `nums`: A list of integers where $1 \le \text{nums.length} \le 5000$.

**Return value**

- An integer representing the total count of valid partitions $(i, j)$ such that the array is split at indices $i$ and $j$ ($0 < i < j < n$).

### Examples
**Example 1**

- Input: `nums = [1, 1, 2, 1]`
- Output: `3`
- Explanation: Valid splits are at indices (1, 2), (1, 3), and (2, 3).

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 3**

- Input: `nums = [2, 2, 2, 2, 2]`
- Output: `12`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming combined with Longest Common Prefix (LCP) precomputation. We precompute an LCP table where `lcp[i][j]` stores the length of the longest common prefix between the suffix starting at `i` and the suffix starting at `j`. This allows $O(1)$ verification of whether one subarray is a prefix of another.

---

## Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the length of the array. The LCP table takes $O(n^2)$ to build, and the nested loops to count splits also take $O(n^2)$.
- **Space Complexity**: $O(n^2)$ to store the LCP table.
