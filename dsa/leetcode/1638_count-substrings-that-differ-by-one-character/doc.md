# Count Substrings That Differ by One Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1638 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Dynamic Programming, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-substrings-that-differ-by-one-character/) |

## Problem Description
### Goal
Given two strings `s` and `t`, count the ways to choose one non-empty substring from each string such that the chosen substrings have equal length and differ at exactly one character position. Equivalently, replacing that one character of the substring from `s` with a different character must make it equal to the selected substring from `t`.

Every pair of starting positions and length is counted separately, even when the resulting substring texts are identical to those of another pair. A substring is a contiguous sequence of characters.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $m$, where $1 \le m \le 100$.
- `t`: a lowercase English string of length $n$, where $1 \le n \le 100$.

**Return value**

Return the number of equal-length, non-empty substring pairs—one selected from each input—that differ in exactly one aligned position.

### Examples
**Example 1**

- Input: `s = "aba", t = "baba"`
- Output: `6`

The six valid choices include four one-character `"a"`/`"b"` pairs and the two aligned one-character `"b"`/`"a"` pairs.

**Example 2**

- Input: `s = "ab", t = "bb"`
- Output: `3`

Two length-one choices compare `"a"` with either occurrence of `"b"`; the length-two pair `"ab"` and `"bb"` is also valid.

**Example 3**

- Input: `s = "a", t = "a"`
- Output: `0`

The only substring pair has no differing character, but exactly one is required.
