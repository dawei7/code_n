# Number of Substrings Containing All Three Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1358 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/) |

## Problem Description

### Goal

Given a string `s` made only from the characters `a`, `b`, and `c`, count its contiguous substrings that contain at least one occurrence of every one of those three characters.

Occurrences beyond the first do not change whether a substring qualifies, but substrings with different start or end positions are counted separately. Return the total number of qualifying contiguous substrings.

### Function Contract

**Inputs**

- `s`: a string of length $n$ whose characters all belong to `a`, `b`, and `c`.

**Return value**

- The number of contiguous substrings of `s` that contain `a`, `b`, and `c` at least once each.

### Examples

**Example 1**

- Input: `s = "abcabc"`
- Output: `10`
- Explanation: qualifying substrings occur at several lengths and positions; all ten are counted.

**Example 2**

- Input: `s = "aaacb"`
- Output: `3`
- Explanation: a valid substring must end at the final `b`, and it may begin at any of the first three positions.

**Example 3**

- Input: `s = "abc"`
- Output: `1`
- Explanation: only the complete string contains all three characters.
