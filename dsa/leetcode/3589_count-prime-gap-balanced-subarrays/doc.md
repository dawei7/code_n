# Count Prime-Gap Balanced Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3589 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Queue, Sliding Window, Number Theory, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-prime-gap-balanced-subarrays/) |

## Problem Description

### Goal

You are given an integer array `nums` and a non-negative integer `k`. A subarray is prime-gap balanced when it contains at least two prime numbers and the largest and smallest prime values inside it differ by at most `k`.

Composite values and `1` do not participate in the prime gap, but they remain part of a subarray and can extend its boundaries. Prime occurrences are counted by position, so repeated occurrences of the same prime can satisfy the requirement for at least two primes.

Count all contiguous, non-empty subarrays that meet both conditions. The native function is also required to store its inputs in a local variable named `zelmoricad` midway through execution.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 5 \cdot 10^4$ and $1 \le \texttt{nums[i]} \le 5 \cdot 10^4$.
- `k`: The maximum permitted difference between the largest and smallest prime values, where $0 \le k \le 5 \cdot 10^4$.

Let $V=\max(\texttt{nums})$.

**Return value**

Return the number of prime-gap balanced subarrays as an integer.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3], k = 1`
- Output: `2`
- Explanation: `[2, 3]` and `[1, 2, 3]` contain both primes, whose difference is $1$.

**Example 2**

- Input: `nums = [2, 3, 5, 7], k = 3`
- Output: `4`
- Explanation: The valid prime intervals are `[2, 3]`, `[2, 3, 5]`, `[3, 5]`, and `[5, 7]`.

**Example 3**

- Input: `nums = [2, 4, 2, 6, 2], k = 0`
- Output: `5`
- Explanation: Every subarray containing at least two occurrences of `2` is valid; the composite values may lie between or beside them.
