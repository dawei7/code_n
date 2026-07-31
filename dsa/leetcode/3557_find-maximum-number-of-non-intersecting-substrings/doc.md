# Find Maximum Number of Non Intersecting Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3557 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/) |

## Problem Description

### Goal

You are given a lowercase English string `word`. Select as many pairwise non-intersecting substrings as possible, subject to two requirements: every selected substring has length at least four, and its first and last characters are equal.

Selected substrings may have unused characters between them, but they cannot share any position. In particular, an index can belong to at most one selection. Return the maximum possible number of selected substrings.

### Function Contract

**Inputs**

- `word`: A string containing only lowercase English letters.

Let $n=\lvert\texttt{word}\rvert$. The constraint is $1 \le n \le 2\cdot10^5$.

**Return value**

Return the greatest number of pairwise non-intersecting substrings of length at least four whose first and last characters match.

### Examples

**Example 1**

- Input: `word = "abcdeafdef"`
- Output: `2`
- Explanation: Choose `"abcdea"` followed by `"fdef"`.

**Example 2**

- Input: `word = "bcdaaaab"`
- Output: `1`
- Explanation: Choosing `"aaaa"` prevents also choosing the surrounding `"bcdaaaab"`, so at most one valid substring can be selected.

---
