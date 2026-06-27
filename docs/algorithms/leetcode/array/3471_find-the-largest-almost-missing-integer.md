# Find the Largest Almost Missing Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3471 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [find-the-largest-almost-missing-integer](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and an integer `k`, identify the largest integer that appears in exactly one subarray of length `k`. If no such integer exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the length of the subarrays to consider.

**Return value**

- An integer representing the largest value that appears in exactly one subarray of length `k`, or -1 if no such value exists.

### Examples
**Example 1**

- Input: `nums = [3, 9, 2, 1, 7], k = 3`
- Output: `7`

**Example 2**

- Input: `nums = [3, 9, 7, 2, 1, 7], k = 2`
- Output: `3`

**Example 3**

- Input: `nums = [0, 0], k = 1`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem is solved using a frequency counting approach. We iterate through all possible subarrays of length `k` using a sliding window or simple slicing. For each subarray, we count the occurrences of its elements. We then track how many distinct subarrays each unique integer appears in. Finally, we filter for integers that appear in exactly one subarray and return the maximum among them.

---

## Complexity Analysis
- **Time Complexity**: O(n * k), where n is the length of the array. We iterate through n-k+1 subarrays, and for each, we process k elements.
- **Space Complexity**: O(n), as we store the frequency of each integer across the subarrays in a hash map.
