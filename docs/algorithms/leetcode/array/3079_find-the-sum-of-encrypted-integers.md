# Find the Sum of Encrypted Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3079 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [find-the-sum-of-encrypted-integers](https://leetcode.com/problems/find-the-sum-of-encrypted-integers/) |

## Problem Description & Examples
### Goal
Given an array of integers, "encrypt" each integer by replacing every digit in the number with the largest digit present in that same number. After transforming all integers in the array according to this rule, return the sum of the resulting encrypted values.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- An integer representing the sum of all encrypted values in the array.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `6`

**Example 2**

- Input: `nums = [10, 21, 31]`
- Output: `66`
*(Explanation: 10 becomes 11, 21 becomes 22, 31 becomes 33. 11 + 22 + 33 = 66)*

**Example 3**

- Input: `nums = [5, 9, 12]`
- Output: `32`
*(Explanation: 5 becomes 5, 9 becomes 9, 12 becomes 22. 5 + 9 + 22 = 36)*

---

## Underlying Base Algorithm(s)
The solution utilizes digit extraction and transformation. For each number, we determine the maximum digit by repeatedly applying the modulo operator (`% 10`) and integer division (`// 10`). Once the maximum digit is found, we reconstruct the encrypted number by calculating the number of digits (or converting to string) and creating a value consisting of the maximum digit repeated that many times.

---

## Complexity Analysis
- **Time Complexity**: `O(n * d)`, where `n` is the number of elements in the array and `d` is the average number of digits in the integers. We iterate through each number and process each digit once.
- **Space Complexity**: `O(1)` (excluding the space required for input/output), as we only use a few integer variables to track the maximum digit and the running sum.
