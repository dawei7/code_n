# Find Greatest Common Divisor of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1979 |
| Difficulty | Easy |
| Topics | Array, Math, Number Theory |
| Official Link | [find-greatest-common-divisor-of-array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) |

## Problem Description & Examples
### Goal
Find the greatest common divisor of the smallest and largest values in the array.

### Function Contract
**Inputs**

- `nums`: a non-empty list of positive integers.

**Return value**

Return `gcd(min(nums), max(nums))`.

### Examples
**Example 1**

- Input: `nums = [2,5,6,9,10]`
- Output: `2`

**Example 2**

- Input: `nums = [7,5,6,8,3]`
- Output: `1`

**Example 3**

- Input: `nums = [3,3]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Scan once to find the minimum and maximum values, then apply the Euclidean algorithm to those two numbers.

---

## Complexity Analysis
- **Time Complexity**: `O(n + log M)`, where `M` is the larger endpoint value.
- **Space Complexity**: `O(1)`
