# Last Substring in Lexicographical Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1163 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/last-substring-in-lexicographical-order/) |

## Problem Description

### Goal

You are given a string `s`. A substring is a contiguous, non-empty sequence of its characters, and substrings are compared in lexicographical order.

Consider every substring that can be taken from `s`. Return the one that appears last in lexicographical order—that is, the lexicographically largest substring. The input contains only lowercase English letters, and its length may be large enough that explicitly creating and sorting all substrings is not practical.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters with length $n$, where $1 \le n \le 4 \cdot 10^5$.

**Return value**

- The substring of `s` that is last in lexicographical order.

### Examples

**Example 1**

- Input: `s = "abab"`
- Output: `"bab"`

The distinct substrings include `"b"`, `"ba"`, and `"bab"`; `"bab"` is lexicographically largest.

**Example 2**

- Input: `s = "leetcode"`
- Output: `"tcode"`

**Example 3**

- Input: `s = "zzzz"`
- Output: `"zzzz"`
