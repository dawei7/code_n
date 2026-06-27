# Count Pairs That Form a Complete Day I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3184 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [count-pairs-that-form-a-complete-day-i](https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/) |

## Problem Description & Examples
### Goal
Given an array of integers representing hours, identify the total number of pairs (i, j) such that i < j and the sum of the elements at these indices is exactly divisible by 24.

### Function Contract
**Inputs**

- `hours`: A list of integers where each element represents a duration in hours.

**Return value**

- An integer representing the total count of valid pairs whose sum is a multiple of 24.

### Examples
**Example 1**

- Input: `hours = [12, 12, 30, 24, 24]`
- Output: `2`

**Example 2**

- Input: `hours = [72, 48, 24, 5]`
- Output: `3`

**Example 3**

- Input: `hours = [1, 2, 3, 4, 5]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem can be solved using a frequency map (or an array of size 24) to store the remainders of each hour value when divided by 24. By iterating through the array and calculating `remainder = hour % 24`, we can determine how many previous numbers had a remainder that, when added to the current remainder, equals 24 (or 0). This reduces the problem to a single-pass counting approach.

---

## Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input array, as we iterate through the list exactly once.
- **Space Complexity**: O(1), because the frequency array used to store remainders is fixed at a size of 24, regardless of the input size.
