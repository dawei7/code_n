# Smallest Palindromic Rearrangement I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3517 |
| Difficulty | Medium |
| Topics | String, Sorting, Counting Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-i/) |

## Problem Description

### Goal

You are given a string `s` that consists only of lowercase English letters. The string is guaranteed to be palindromic, so its character multiset can be arranged symmetrically around a center.

Rearrange all characters of `s` into a palindrome and return the lexicographically smallest palindrome obtainable this way. Every occurrence must be used exactly once. Lexicographic order is determined at the first position where two candidate strings differ, so choosing the smallest possible left half also fixes the smallest possible complete palindrome.

### Function Contract

**Inputs**

- `s`: A palindromic lowercase English string with $1 \le \lvert s \rvert \le 10^5$.

**Return value**

Return the lexicographically smallest palindromic permutation of `s`.

### Examples

#### Example 1

- **Input:** `s = "z"`
- **Output:** `"z"`
- **Explanation:** The only character is already the unique possible palindrome.

#### Example 2

- **Input:** `s = "babab"`
- **Output:** `"abbba"`
- **Explanation:** The two `a` characters occupy the outermost positions, producing the smallest possible first character.

#### Example 3

- **Input:** `s = "daccad"`
- **Output:** `"acddca"`
- **Explanation:** The ascending left half is `"acd"`; mirroring it gives the smallest palindrome.
