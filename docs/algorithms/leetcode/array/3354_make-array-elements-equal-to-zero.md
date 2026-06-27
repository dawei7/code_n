# Make Array Elements Equal to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3354 |
| Difficulty | Easy |
| Topics | Array, Simulation, Prefix Sum |
| Official Link | [make-array-elements-equal-to-zero](https://leetcode.com/problems/make-array-elements-equal-to-zero/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine how many starting positions allow a "selection" process to eventually reduce all elements in the array to zero. Starting at a chosen index, you move left or right. If the current element is non-zero, you decrement it and reverse your direction. If the current element is zero, you continue moving in the same direction. The process ends when you move out of the array bounds. A starting position is valid if all elements are zero when the process terminates.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the array state.

**Return value**

- An integer representing the count of indices `i` such that starting at `i` results in all elements becoming zero.

### Examples
**Example 1**

- Input: `nums = [1, 0, 2, 0, 3]`
- Output: `2`

**Example 2**

- Input: `nums = [2, 3, 4, 0, 4, 1]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 0, 1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem can be solved by observing that the simulation only succeeds if the sum of elements to the left of the starting index equals the sum of elements to the right (or differs by exactly 1 if the starting element is non-zero). By pre-calculating the total sum and using a prefix sum approach, we can evaluate each potential starting index in constant time.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the array to calculate sums and then once more to check each index.
- **Space Complexity**: `O(1)`, as we only store a few integer variables regardless of the input size.
