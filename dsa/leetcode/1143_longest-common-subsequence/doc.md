# Longest Common Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1143 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-common-subsequence/) |

## Problem Description

### Goal

A subsequence is formed from a string by deleting zero or more characters without changing the relative order of those that remain. For example, `"ace"` is a subsequence of `"abcde"`; the selected characters do not need to occupy adjacent positions.

Given lowercase strings `text1` and `text2`, return the length of their longest common subsequence—a string that is a subsequence of both inputs. The empty string is always common, so return `0` when the inputs share no nonempty subsequence.

### Function Contract

**Inputs**

- `text1`: a lowercase English string of length $m$, where $1 \le m \le 1000$.
- `text2`: a lowercase English string of length $n$, where $1 \le n \le 1000$.

**Return value**

The maximum possible length of a string obtainable as a subsequence of both `text1` and `text2`.

### Examples

**Example 1**

- Input: `text1 = "abcde", text2 = "ace"`
- Output: `3`
- Explanation: `"ace"` appears in order in both strings.

**Example 2**

- Input: `text1 = "abc", text2 = "abc"`
- Output: `3`

**Example 3**

- Input: `text1 = "abc", text2 = "def"`
- Output: `0`
