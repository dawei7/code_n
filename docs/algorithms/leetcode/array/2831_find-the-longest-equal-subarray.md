# Find the Longest Equal Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2831 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Sliding Window |
| Official Link | [find-the-longest-equal-subarray](https://leetcode.com/problems/find-the-longest-equal-subarray/) |

## Problem Description & Examples
### Goal
Given an array of integers and an integer `k`, determine the length of the longest subarray that can be formed by deleting at most `k` elements such that all remaining elements in the subarray are equal.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the maximum number of elements that can be removed.

**Return value**

- An integer representing the maximum possible length of an equal-element subarray after at most `k` deletions.

### Examples
**Example 1**

- Input: `nums = [1,3,2,3,1,3], k = 3`
- Output: `3`

**Example 2**

- Input: `nums = [1,1,2,2,1,1], k = 2`
- Output: `4`

**Example 3**

- Input: `nums = [1,2,3,4], k = 0`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Sliding Window** approach combined with a **Hash Map** (or dictionary). We store the indices of each unique number in the array. For each number, we treat its list of indices as a sequence and use a sliding window to find the longest subsequence of indices `[i_start, ..., i_end]` such that the number of elements between them that are *not* equal to the target value (calculated as `(indices[end] - indices[start]) - (end - start)`) is less than or equal to `k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. We iterate through the array once to group indices and then perform a linear scan over the index lists.
- **Space Complexity**: `O(n)` to store the indices of each element in the hash map.
