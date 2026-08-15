# Find Longest Self-Contained Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3104 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [find-longest-self-contained-substring](https://leetcode.com/problems/find-longest-self-contained-substring/) |

## Problem Description

### Goal

Given a lowercase string `s`, choose a substring `t` whose characters are isolated from the rest of the string. More precisely, `t` is **self-contained** when it is not the whole string and every character that occurs in `t` occurs nowhere outside `t` in `s`.

The substring must be contiguous. Characters that do not appear in the chosen interval impose no restriction, while every occurrence in `s` of each character used by the interval must lie inside it.

Return the length of the longest self-contained substring. If no proper substring satisfies the condition, return `-1`.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $2 \le n \le 5 \cdot 10^4$, consisting only of lowercase English letters.

**Return value**

- The maximum length of a self-contained substring that is not equal to `s`, or `-1` if no such substring exists.

### Examples

#### Example 1

- **Input:** `s = "abba"`
- **Output:** `2`
- **Explanation:** The substring `"bb"` contains every occurrence of `b`, and `b` does not occur in the remaining characters.

#### Example 2

- **Input:** `s = "abab"`
- **Output:** `-1`
- **Explanation:** Every proper substring containing `a` or `b` leaves another occurrence of that character outside the substring.

#### Example 3

- **Input:** `s = "abacd"`
- **Output:** `4`
- **Explanation:** The prefix `"abac"` contains all occurrences of `a`, `b`, and `c`; the only outside character is `d`.
