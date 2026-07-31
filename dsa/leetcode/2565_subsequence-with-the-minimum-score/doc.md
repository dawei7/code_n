# Subsequence With the Minimum Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2565 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [subsequence-with-the-minimum-score](https://leetcode.com/problems/subsequence-with-the-minimum-score/) |

## Problem Description

### Goal

You are given two lowercase English strings `s` and `t`. You may remove any number of characters from `t`, after which the characters that remain must form a subsequence of `s`: they must appear in the same relative order, but they do not need to occupy adjacent positions in `s`.

Removing nothing has score $0$. Otherwise, let `left` and `right` be the smallest and largest original indices in `t` from which a character was removed. The score is the length of that inclusive index span, `right - left + 1`, even if some characters inside the span were retained. Return the minimum score obtainable while making the remaining string a subsequence of `s`. Removing every character is allowed, because the empty string is a subsequence of any string.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$, where $1 \le n \le 10^5$.
- `t`: A lowercase English string of length $m$, where $1 \le m \le 10^5$.

**Return value**

- The minimum possible score after removing characters from `t` so that the remaining characters form a subsequence of `s`.

### Examples

**Example 1**

- Input: `s = "abacaba", t = "bzaa"`
- Output: `1`
- Explanation: Removing the `z` at index $1$ leaves `"baa"`, which is a subsequence of `s`, and the removed span has length $1$.

**Example 2**

- Input: `s = "cde", t = "xyz"`
- Output: `3`
- Explanation: No character can be retained, so removing all of `t` gives the minimum score $3$.

**Example 3**

- Input: `s = "abcde", t = "ace"`
- Output: `0`
- Explanation: `t` is already a subsequence of `s`, so no removal is necessary.
