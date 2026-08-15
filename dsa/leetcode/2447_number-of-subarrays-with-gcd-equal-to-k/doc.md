# Number of Subarrays With GCD Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2447 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Number of Subarrays With GCD Equal to K](https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/) |

## Problem Description

### Goal

You are given an integer array `nums` and a positive integer `k`. A subarray is a contiguous, nonempty sequence of elements from `nums`. The greatest common divisor of a subarray is the largest positive integer that divides every value in that subarray.

Count and return the number of subarrays whose greatest common divisor is exactly `k`. Subarrays are identified by their start and end positions, so overlapping occurrences count separately.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 1000$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `k`: The required greatest common divisor, where $1 \le k \le 10^9$.

**Return value**

- The number of contiguous nonempty subarrays whose GCD equals `k`.

### Examples

#### Example 1

- **Input:** `nums = [9, 3, 1, 2, 6, 3], k = 3`
- **Output:** `4`
- **Explanation:** The qualifying subarrays are the two singleton `[3]` occurrences, `[9, 3]`, and `[6, 3]`.

#### Example 2

- **Input:** `nums = [4], k = 7`
- **Output:** `0`
- **Explanation:** The only subarray has GCD 4.
