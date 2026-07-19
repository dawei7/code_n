# Shortest Way to Form String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1055 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/shortest-way-to-form-string/) |

## Problem Description

### Goal

A **subsequence** is formed from a string by deleting any number of characters, possibly none, without changing the relative order of the characters that remain. For example, `"ace"` is a subsequence of `"abcde"`, while `"aec"` is not.

Given `source` and `target`, concatenate subsequences chosen from reusable copies of `source` so that the concatenation equals `target`. Return the minimum number of source subsequences required. If no such construction is possible, return `-1`.

### Function Contract

**Inputs**

- `source`: a lowercase English string of length $S$, where $1 \le S \le 1000$.
- `target`: a lowercase English string of length $T$, where $1 \le T \le 1000$.
- The alphabet size is $A=26$.

**Return value**

- The minimum number of subsequences of `source` whose concatenation equals `target`, or `-1` if impossible.

### Examples

**Example 1**

- Input: `source = "abc", target = "abcbc"`
- Output: `2`
- Explanation: `"abc"` followed by `"bc"` forms the target.

**Example 2**

- Input: `source = "abc", target = "acdbc"`
- Output: `-1`
- Explanation: Character `"d"` never occurs in the source.

**Example 3**

- Input: `source = "xyz", target = "xzyxz"`
- Output: `3`
- Explanation: One optimal construction is `"xz" + "y" + "xz"`.
