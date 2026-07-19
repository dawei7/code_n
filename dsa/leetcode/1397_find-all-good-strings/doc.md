# Find All Good Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1397 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/find-all-good-strings/) |

## Problem Description

### Goal

A good string has length $n$, contains only lowercase English letters, and does not contain `evil` as a substring. Two length-$n$ strings `s1` and `s2` define an inclusive lexicographic interval, with `s1` no greater than `s2`.

Count the good strings `s` for which `s1` is lexicographically less than or equal to `s` and `s` is less than or equal to `s2`. Because the number can be large, return it modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `n`: the common string length, where $1 \le n \le 500$.
- `s1` and `s2`: lowercase strings of length $n$ with `s1 <= s2` lexicographically.
- `evil`: a lowercase forbidden substring of length $m$, where $1 \le m \le 50$.

**Return value**

- The number of length-$n$ strings in the inclusive interval that do not contain `evil`, reduced modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `n = 2, s1 = "aa", s2 = "da", evil = "b"`
- Output: `51`

**Example 2**

- Input: `n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"`
- Output: `0`

**Example 3**

- Input: `n = 2, s1 = "gx", s2 = "gz", evil = "x"`
- Output: `2`
