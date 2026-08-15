# Find Longest Special Substring That Occurs Thrice I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2981 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Binary Search, Sliding Window, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/) |

## Problem Description

### Goal

You are given a string `s` containing only lowercase English letters. A string
is **special** when all of its characters are the same; for example, `"ddd"`,
`"zz"`, and `"f"` are special, while `"abc"` is not.

Among the non-empty contiguous substrings of `s`, find the greatest length for
which one special substring occurs at least three times. Occurrences are
identified by their positions and may overlap. Return that greatest length, or
return `-1` when no special substring has three occurrences.

### Function Contract

**Inputs**

- `s`: a lowercase English string

Let $N=\lvert\texttt{s}\rvert$. The contract guarantees $3\le N\le50$.

**Return value**

Return the length of the longest special substring occurring at least three
times, or `-1` if none exists.

### Examples

#### Example 1

- **Input:** `s = "aaaa"`
- **Output:** `2`
- **Explanation:** `"aa"` begins at indices `0`, `1`, and `2`; these overlapping occurrences all count.

#### Example 2

- **Input:** `s = "abcdef"`
- **Output:** `-1`

#### Example 3

- **Input:** `s = "abcaba"`
- **Output:** `1`
- **Explanation:** The one-character substring `"a"` occurs three times.
