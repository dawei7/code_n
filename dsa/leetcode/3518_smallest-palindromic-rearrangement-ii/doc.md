# Smallest Palindromic Rearrangement II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3518 |
| Difficulty | Hard |
| Topics | Hash Table, Math, String, Combinatorics, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/) |

## Problem Description

### Goal

You are given a palindromic lowercase English string `s` and a positive integer `k`. Consider every distinct palindrome that can be formed by rearranging all characters of `s`, and order those strings lexicographically.

Return the $k$-th string in that ordering, using one-based rank. Rearrangements that produce the same final string count only once, even when equal character occurrences could be exchanged in multiple ways. If the multiset of `s` produces fewer than `k` distinct palindromes, return the empty string.

### Function Contract

**Inputs**

- `s`: A palindromic lowercase English string with $1 \le \lvert s \rvert \le 10^4$.
- `k`: The requested one-based lexicographic rank, where $1 \le k \le 10^6$.

**Return value**

Return the $k$-th lexicographically smallest distinct palindromic permutation of `s`, or `""` when that rank does not exist.

### Examples

#### Example 1

- **Input:** `s = "abba", k = 2`
- **Output:** `"baab"`
- **Explanation:** The distinct palindromes are `"abba"` and `"baab"` in lexicographic order.

#### Example 2

- **Input:** `s = "aa", k = 2`
- **Output:** `""`
- **Explanation:** Only `"aa"` can be formed, so rank 2 is absent.

#### Example 3

- **Input:** `s = "bacab", k = 1`
- **Output:** `"abcba"`
- **Explanation:** `"abcba"` precedes the other distinct palindrome, `"bacab"`.
