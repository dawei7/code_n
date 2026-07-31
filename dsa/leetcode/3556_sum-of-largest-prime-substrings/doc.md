# Sum of Largest Prime Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3556 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Sorting, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-largest-prime-substrings/) |

## Problem Description

### Goal

Given a decimal digit string `s`, consider every nonempty contiguous substring. Convert each substring to an integer; leading zeros do not affect that value. Keep the values that are prime, counting a prime only once even when several substrings produce it.

Return the sum of the three largest distinct primes. When fewer than three distinct primes are available, return their total instead. If no substring represents a prime number, return zero.

### Function Contract

**Inputs**

- `s`: A string containing only decimal digits.

Let $n=\lvert\texttt{s}\rvert$. The constraint is $1 \le n \le 10$.

**Return value**

Return the sum of the largest three unique prime values represented by substrings of `s`, or the sum of every available unique prime when fewer than three exist. Return `0` if the set is empty.

### Examples

**Example 1**

- Input: `s = "12234"`
- Output: `1469`
- Explanation: The distinct primes are `2`, `3`, `23`, `223`, and `1223`; the largest three sum to `1223 + 223 + 23 = 1469`.

**Example 2**

- Input: `s = "111"`
- Output: `11`
- Explanation: The only prime value formed by a substring is `11`.

---
