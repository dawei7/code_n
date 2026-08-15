# Find the Maximum Divisibility Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2644 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-maximum-divisibility-score/) |

## Problem Description

### Goal

You are given integer arrays `nums` and `divisors`. The divisibility score of a candidate `divisors[i]` is the number of indices $j$ for which `nums[j]` is evenly divisible by that candidate.

Return a divisor having the greatest score. When several divisor values attain the same maximum score, return the smallest of them. A candidate can win with score zero when no supplied number is divisible by any candidate.

### Function Contract

**Inputs**

- `nums`: A positive-integer array of length $n$.
- `divisors`: A positive-integer array of length $d$.

Both lengths are between 1 and 1000, and every value is between 1 and $10^9$, inclusive.

**Return value**

- Return the smallest divisor among those maximizing the number of divisible values in `nums`.

### Examples

#### Example 1

- **Input:** `nums = [2, 9, 15, 50]`, `divisors = [5, 3, 7, 2]`
- **Output:** `2`
- **Explanation:** Divisors 5, 3, and 2 each score two; the smallest tied divisor is 2.

#### Example 2

- **Input:** `nums = [4, 7, 9, 3, 9]`, `divisors = [5, 2, 3]`
- **Output:** `3`

#### Example 3

- **Input:** `nums = [20, 14, 21, 10]`, `divisors = [10, 16, 20]`
- **Output:** `10`
