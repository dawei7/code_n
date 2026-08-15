# Take K of Each Character From Left and Right

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2516 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/) |

## Problem Description

### Goal

You are given a string `s` containing only the characters `'a'`, `'b'`, and `'c'`, together with a non-negative integer `k`.

During one minute, you may remove exactly one character from either end of the current string: the leftmost character or the rightmost character. Characters removed in different minutes may come from different ends.

Return the minimum number of minutes needed to collect at least `k` copies of each of the three characters. If the original string does not contain enough copies of some character, return `-1`.

### Function Contract

**Inputs**

- `s`: A non-empty string of length $n$ whose characters are all `'a'`, `'b'`, or `'c'`, where $1 \le n \le 10^5$.
- `k`: The minimum required count of each character, where $0 \le k \le n$.

**Return value**

Return the smallest total number of removals from the two ends that collects at least `k` occurrences of `'a'`, `'b'`, and `'c'`; return `-1` when that is impossible.

### Examples

#### Example 1

- **Input:** `s = "aabaaaacaabc", k = 2`
- **Output:** `8`
- **Explanation:** Removing three characters from the left and five from the right collects at least two copies of every character, and no choice using fewer than eight removals can do so.

#### Example 2

- **Input:** `s = "a", k = 1`
- **Output:** `-1`
- **Explanation:** The string contains no `'b'` or `'c'`, so the required collection cannot be formed.
