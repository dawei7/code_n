# Shortest String That Contains Three Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2800 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-string-that-contains-three-strings/) |

## Problem Description

### Goal

Given three strings `a`, `b`, and `c`, construct a string of minimum possible length that contains each of the three inputs as a substring. A substring occupies consecutive positions, so separated characters do not satisfy the requirement.

More than one minimum-length answer may exist. In that case, return the lexicographically smallest candidate: at the first position where two equal-length candidates differ, choose the one whose character appears earlier in the alphabet.

### Function Contract

**Inputs**

- `a`: A lowercase English string with length between $1$ and $100$.
- `b`: A lowercase English string with length between $1$ and $100$.
- `c`: A lowercase English string with length between $1$ and $100$.

The strings may overlap, may be equal, and one may already occur inside another.

**Return value**

Return the shortest string containing `a`, `b`, and `c` as substrings. Break equal-length ties by lexicographic order.

### Examples

#### Example 1

- **Input:** `a = "abc"`, `b = "bca"`, `c = "aaa"`
- **Output:** `"aaabca"`
- **Explanation:** The result contains `"aaa"` at the start, `"abc"` from indices $2$ through $4$, and `"bca"` from indices $3$ through $5$; no shorter answer exists.

#### Example 2

- **Input:** `a = "ab"`, `b = "ba"`, `c = "aba"`
- **Output:** `"aba"`
- **Explanation:** The third string already contains the first two as substrings.
