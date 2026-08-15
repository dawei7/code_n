# Find the Shortest Superstring II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3571 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-shortest-superstring-ii/) |

## Problem Description

### Goal

Given two strings `s1` and `s2`, construct the shortest possible string that contains each input as a substring. A substring occupies consecutive positions, so the strings may share characters only where a suffix of one exactly matches a prefix of the other.

If one input already occurs anywhere inside the other, the containing input is itself optimal. Otherwise, either input may come first, and their compatible boundary overlap should be reused rather than duplicated. When both orders yield the same minimum length, either resulting string is valid.

### Function Contract

**Inputs**

- `s1`: A non-empty lowercase English string of length at most $100$.
- `s2`: A non-empty lowercase English string of length at most $100$.

Let $m=\lvert\texttt{s1}\rvert$ and $n=\lvert\texttt{s2}\rvert$.

**Return value**

Return any minimum-length string containing both `s1` and `s2` as substrings.

### Examples

#### Example 1

- **Input:** `s1 = "aba", s2 = "bab"`
- **Output:** `"abab"`
- **Explanation:** The suffix `"ba"` of the first string matches the prefix of the second, so only one new character is needed. `"baba"` is another valid minimum-length answer.

#### Example 2

- **Input:** `s1 = "aa", s2 = "aaa"`
- **Output:** `"aaa"`
- **Explanation:** The longer string already contains the shorter one.

---
