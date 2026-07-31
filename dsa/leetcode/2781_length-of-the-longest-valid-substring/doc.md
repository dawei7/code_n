# Length of the Longest Valid Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2781 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/length-of-the-longest-valid-substring/) |

## Problem Description

### Goal

You are given a lowercase string `word` and an array `forbidden` whose entries are also lowercase strings. A string is valid when none of its contiguous substrings equals any entry in `forbidden`.

Consider every substring of `word`, including the empty substring. Return the greatest length among those that are valid. A forbidden occurrence anywhere inside a candidate invalidates the entire candidate, even when that occurrence is shorter than the candidate or overlaps another forbidden occurrence.

### Function Contract

**Inputs**

- `word`: A lowercase English string of length $n$, where $1 \le n \le 10^5$.
- `forbidden`: An array containing between $1$ and $10^5$ lowercase strings; every entry has length from $1$ through $10$.

Let

$$
S = \sum_{f \in \texttt{forbidden}} \lvert f \rvert
$$

denote the total number of characters stored across the forbidden strings.

**Return value**

Return the maximum length of a contiguous substring of `word` that contains no member of `forbidden` as one of its own substrings. Return `0` when every non-empty substring is invalid.

### Examples

**Example 1**

- Input: `word = "cbaaaabc"`, `forbidden = ["aaa","cb"]`
- Output: `4`
- Explanation: The substring `"aabc"` has length four and contains neither forbidden pattern. Every longer candidate contains either `"aaa"` or `"cb"`.

**Example 2**

- Input: `word = "leetcode"`, `forbidden = ["de","le","e"]`
- Output: `4`
- Explanation: `"tcod"` is valid and has length four. Extending it in either relevant direction introduces a forbidden occurrence.

**Example 3**

- Input: `word = "abc"`, `forbidden = ["a","b","c"]`
- Output: `0`
- Explanation: Every single character is forbidden, so no non-empty substring is valid.
