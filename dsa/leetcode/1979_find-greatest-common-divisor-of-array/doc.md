# Find Greatest Common Divisor of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1979 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-greatest-common-divisor-of-array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-greatest-common-divisor-of-array/).

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

## Solution
### Approach
Scan once to find the minimum and maximum values, then apply the Euclidean algorithm to those two numbers.

### Complexity Analysis
- **Time Complexity**: `O(n + log M)`, where `M` is the larger endpoint value.
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
