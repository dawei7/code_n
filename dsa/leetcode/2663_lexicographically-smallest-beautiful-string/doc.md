# Lexicographically Smallest Beautiful String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2663 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lexicographically-smallest-beautiful-string/) |

## Problem Description

### Goal

A string is called beautiful when it uses only the first `k` lowercase English letters and contains no palindromic substring whose length is at least $2$.

You are given a beautiful string `s` of length $n$ and an integer `k`. Find another beautiful string of the same length that is lexicographically larger than `s`. Among every string satisfying those conditions, return the lexicographically smallest one. If no such string exists, return the empty string.

For equal-length strings, lexicographic order is decided at their first differing position: the string having the larger character there is the larger string.

### Function Contract

**Inputs**

- `s`: A beautiful lowercase string with length $n$, where $1 \le n \le 10^5$.
- `k`: The number of permitted letters, so every character lies from `a` through the `k`th lowercase letter and $4 \le k \le 26$.

**Return value**

- Return the smallest beautiful length-$n$ string strictly greater than `s`, or `""` when no such string exists.

### Examples

**Example 1**

- Input: `s = "abcz", k = 26`
- Output: `"abda"`
- Explanation: Increasing the third character to `d` permits the suffix to restart at `a`; no closer larger beautiful string exists.

**Example 2**

- Input: `s = "dc", k = 4`
- Output: `""`
- Explanation: No length-two beautiful string over `a` through `d` is lexicographically larger than `dc`.
