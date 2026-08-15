# Number of Beautiful Partitions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2478 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-beautiful-partitions/) |

## Problem Description

### Goal

You are given a digit string `s`, an integer `k`, and a minimum length `minLength`. Split the entire string into exactly `k` non-overlapping substrings that remain in their original order.

A partition is beautiful when every substring contains at least `minLength` characters, begins with a prime digit, and ends with a non-prime digit. The prime digits are `2`, `3`, `5`, and `7`; every other digit from `1` through `9` is non-prime.

Return the number of beautiful partitions modulo $10^9 + 7$. A substring is a contiguous segment, so every character of `s` belongs to exactly one part.

### Function Contract

**Inputs**

- `s`: A string of digits from `1` through `9`.
- `k`: The exact positive number of substrings required.
- `minLength`: The minimum positive length of every substring.

Let $n = \lvert\texttt{s}\rvert$. The constraints satisfy $1 \le k, \texttt{minLength} \le n \le 1000$.

**Return value**

Return the number of valid partitions modulo $10^9 + 7$.

### Examples

#### Example 1

- **Input:** `s = "23542185131", k = 3, minLength = 2`
- **Output:** `3`
- **Explanation:** The three valid splits are `2354 | 218 | 5131`, `2354 | 21851 | 31`, and `2354218 | 51 | 31`.

#### Example 2

- **Input:** `s = "23542185131", k = 3, minLength = 3`
- **Output:** `1`
- **Explanation:** Only `2354 | 218 | 5131` gives every part at least three characters.

#### Example 3

- **Input:** `s = "3312958", k = 3, minLength = 1`
- **Output:** `1`
- **Explanation:** The unique beautiful partition is `331 | 29 | 58`.
