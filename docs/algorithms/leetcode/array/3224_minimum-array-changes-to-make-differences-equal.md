# Minimum Array Changes to Make Differences Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3224 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [minimum-array-changes-to-make-differences-equal](https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/) |

## Problem Description & Examples
### Goal
Given an array of even length `nums` and an integer `k`, we want to make all pairs `(nums[i], nums[n-1-i])` have the same absolute difference `x` by modifying elements in the array. Each modification allows changing an element to any integer between `0` and `k` (inclusive). We need to find the minimum number of modifications required to achieve this target difference `x` for all pairs.

### Function Contract
**Inputs**

- `nums`: A list of integers where the length is even.
- `k`: An integer representing the upper bound for any element in the array.

**Return value**

- An integer representing the minimum number of modifications required to make all pairs have the same absolute difference.

### Examples
**Example 1**

- Input: `nums = [1, 0, 1, 2, 4, 3], k = 4`
- Output: `2`

**Example 2**

- Input: `nums = [0, 1, 2, 3], k = 3`
- Output: `1`

**Example 3**

- Input: `nums = [1, 1, 1, 1], k = 0`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using a difference array (or sweep-line) technique combined with frequency counting. For each pair `(a, b)`, the maximum possible difference we can achieve with one change is `max(max(a, b), k - min(a, b))`. We count the occurrences of each possible difference `d = abs(a - b)`. Then, we use a difference array to track how many operations are needed for any target difference `x`. Specifically, for each pair, 0 changes are needed if `x == abs(a - b)`, 1 change is needed if `x <= max_diff`, and 2 changes are needed otherwise.

---

## Complexity Analysis
- **Time Complexity**: `O(n + k)`, where `n` is the length of the array and `k` is the maximum value allowed. We iterate through the array once and then iterate through the difference array of size `k`.
- **Space Complexity**: `O(k)`, used to store the frequency counts and the difference array.
