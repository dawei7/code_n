# Subsequences with a Unique Middle Mode I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3395 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Combinatorics |
| Official Link | [subsequences-with-a-unique-middle-mode-i](https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the number of subsequences of length 5 such that the middle element (the third element) is the unique mode of the subsequence. A unique mode is defined as the element that appears more frequently than any other element in the subsequence.

### Function Contract
**Inputs**

- `nums`: A list of integers where the length is at least 5.

**Return value**

- An integer representing the total count of subsequences of length 5 that satisfy the unique middle mode condition, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 1, 1, 1]`
- Output: `6`

**Example 2**

- Input: `nums = [1, 2, 2, 3, 3, 4]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 2, 3, 4, 3, 2, 1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using combinatorics and prefix/suffix frequency tracking. For each element `nums[i]` acting as the potential middle element, we calculate the number of ways to choose two elements from the left (indices `0` to `i-1`) and two elements from the right (indices `i+1` to `n-1`) such that `nums[i]` appears more times than any other value in the 5-element subsequence. We use inclusion-exclusion to subtract cases where other elements appear with equal or greater frequency than the middle element.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array a constant number of times using precomputed frequency maps.
- **Space Complexity**: `O(n)` to store frequency counts and prefix/suffix arrays.
