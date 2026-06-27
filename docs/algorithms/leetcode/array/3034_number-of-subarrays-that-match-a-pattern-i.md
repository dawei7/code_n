# Number of Subarrays That Match a Pattern I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3034 |
| Difficulty | Medium |
| Topics | Array, Rolling Hash, String Matching, Hash Function |
| Official Link | [number-of-subarrays-that-match-a-pattern-i](https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums` and a pattern array `pattern` consisting of elements {-1, 0, 1}, determine how many contiguous subarrays of `nums` of length `m + 1` (where `m` is the length of `pattern`) satisfy the specified relationship sequence. A relationship is defined as: 1 if `nums[i+1] > nums[i]`, 0 if `nums[i+1] == nums[i]`, and -1 if `nums[i+1] < nums[i]`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to search within.
- `pattern`: A list of integers (values -1, 0, or 1) representing the target relationship sequence.

**Return value**

- An integer representing the total count of subarrays in `nums` that match the provided `pattern`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5, 6]`, `pattern = [1, 1]`
- Output: `4`

**Example 2**

- Input: `nums = [1, 4, 4, 1, 3, 5, 5, 3]`, `pattern = [1, 0, -1]`
- Output: `2`

**Example 3**

- Input: `nums = [1, 2, 3, 2, 1]`, `pattern = [1, -1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is a variation of the string matching problem. We first transform the `nums` array into a sequence of relationships (differences) of length `n-1`. Once transformed, the problem reduces to finding the number of occurrences of the `pattern` array within this new sequence, which can be solved using a sliding window approach or string matching algorithms like KMP.

---

## Complexity Analysis
- **Time Complexity**: `O(n * m)`, where `n` is the length of `nums` and `m` is the length of `pattern`. In each window of the transformed array, we compare `m` elements.
- **Space Complexity**: `O(n)`, used to store the transformed relationship array. This can be optimized to `O(1)` if we compute relationships on-the-fly.
