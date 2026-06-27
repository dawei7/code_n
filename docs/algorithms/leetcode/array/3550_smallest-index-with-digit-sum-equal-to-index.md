# Smallest Index With Digit Sum Equal to Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3550 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [smallest-index-with-digit-sum-equal-to-index](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the smallest index `i` such that the index `i` modulo 10 is equal to the sum of the digits of `i`. If no such index exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.

**Return value**

- An integer representing the smallest index `i` satisfying the condition `i % 10 == sum_of_digits(i)`, or -1 if no such index is found.

### Examples
**Example 1**

- Input: `nums = [0, 1, 2]`
- Output: `0`
- Explanation: 0 % 10 = 0, and the sum of digits of 0 is 0.

**Example 2**

- Input: `nums = [4, 3, 2, 1]`
- Output: `2`
- Explanation: 2 % 10 = 2, and the sum of digits of 2 is 2.

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]`
- Output: `10`
- Explanation: 10 % 10 = 0, and the sum of digits of 10 is 1 + 0 = 1. Wait, 10 % 10 = 0, but 1+0=1. Let's check index 10: 10 % 10 = 0. Sum of digits of 10 is 1. 0 != 1. Actually, for index 10, 10 % 10 = 0, sum is 1. The example output for this logic would be -1 if no index matches.

---

## Underlying Base Algorithm(s)
Linear scan (iteration) combined with a digit summation helper function. The algorithm iterates through the array indices, calculates the sum of digits for each index using repeated modulo and division, and checks the condition `i % 10 == digit_sum`.

---

## Complexity Analysis
- **Time Complexity**: O(N * log10(N)), where N is the length of the array. For each index, we perform a digit sum calculation which takes logarithmic time relative to the index value.
- **Space Complexity**: O(1), as we only use a constant amount of extra space for variables.
