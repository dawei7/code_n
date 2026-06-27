# Find the Maximum Factor Score of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3334 |
| Difficulty | Medium |
| Topics | Array, Math, Number Theory |
| Official Link | [find-the-maximum-factor-score-of-array](https://leetcode.com/problems/find-the-maximum-factor-score-of-array/) |

## Problem Description & Examples
### Goal
Given an array of integers, calculate its "factor score," defined as the product of the greatest common divisor (GCD) of all elements and the least common multiple (LCM) of all elements. You are permitted to remove exactly one element from the array (or none at all) to maximize this score. Return the highest possible factor score achievable.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- An integer representing the maximum possible factor score (GCD * LCM) after removing at most one element.

### Examples
**Example 1**

- Input: `nums = [2, 4, 8, 16]`
- Output: `64`
- Explanation: The original score is gcd(2,4,8,16) * lcm(2,4,8,16) = 2 * 16 = 32. Removing 2 gives gcd(4,8,16) * lcm(4,8,16) = 4 * 16 = 64.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `60`
- Explanation: Removing 1 gives gcd(2,3,4,5) * lcm(2,3,4,5) = 1 * 60 = 60.

**Example 3**

- Input: `nums = [10, 20]`
- Output: `200`
- Explanation: The original score is gcd(10,20) * lcm(10,20) = 10 * 20 = 200.

---

## Underlying Base Algorithm(s)
The solution relies on the properties of the Greatest Common Divisor (GCD) and Least Common Multiple (LCM). Since the array size is typically small in such problems, we can iterate through the array, temporarily removing each element one by one, and calculate the GCD and LCM of the remaining elements. We use the Euclidean algorithm for GCD and the relationship `lcm(a, b) = (a * b) // gcd(a, b)` for LCM.

---

## Complexity Analysis
- **Time Complexity**: `O(n * log(max(nums)))`, where `n` is the length of the array. We perform `n` iterations, and each GCD calculation takes logarithmic time relative to the values.
- **Space Complexity**: `O(1)`, as we only store a few integer variables regardless of the input size.
