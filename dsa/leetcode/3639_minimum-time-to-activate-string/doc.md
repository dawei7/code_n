# Minimum Time to Activate String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3639 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-activate-string/) |

## Problem Description

### Goal

You are given a string `s` of length $n$ and a permutation `order` of its indices. At time $t$, beginning with $t=0$, replace the character at index `order[t]` by `"*"`. Replacements from earlier times remain in place.

A nonempty substring is valid when it contains at least one asterisk. The current string is active once the total number of valid substrings is at least `k`.

Return the earliest time when the string becomes active. If even replacing every character cannot provide `k` valid substrings, return `-1`.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$, where $1 \le n \le 10^5$.
- `order`: A permutation of all indices from 0 through $n-1$.
- `k`: The required number of valid substrings, where $1 \le k \le 10^9$.

**Return value**

Return the smallest zero-based activation time $t$ for which at least `k` substrings contain an activated position, or `-1` when impossible.

### Examples

#### Example 1

- **Input:** `s = "abc", order = [1, 0, 2], k = 2`
- **Output:** `0`
- **Explanation:** Activating the middle character immediately creates four valid substrings.

#### Example 2

- **Input:** `s = "cat", order = [0, 2, 1], k = 6`
- **Output:** `2`
- **Explanation:** All six substrings become valid only after every position is activated.

#### Example 3

- **Input:** `s = "xy", order = [0, 1], k = 4`
- **Output:** `-1`
- **Explanation:** A length-two string has only three nonempty substrings.
