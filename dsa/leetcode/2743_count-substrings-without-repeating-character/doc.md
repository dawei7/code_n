# Count Substrings Without Repeating Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2743 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/count-substrings-without-repeating-character/) |

## Problem Description

### Goal

A string `s` contains only lowercase English letters. A substring is special when every character inside that contiguous segment occurs exactly once within the segment; any repeated character makes it invalid.

Count all special substrings of `s`. Substrings are distinguished by their start and end positions, so equal text appearing at different locations contributes multiple times. Return the total over every non-empty contiguous segment.

### Function Contract

Let $n$ be the length of `s`.

**Inputs**

- `s`: A lowercase English string with $1 \le n \le 10^5$.

**Return value**

Return the number of non-empty substrings whose characters are all distinct.

### Examples

**Example 1**

- Input: `s = "abcd"`
- Output: `10`
- Explanation: Every substring is special, giving $4+3+2+1=10$ choices.

**Example 2**

- Input: `s = "ooo"`
- Output: `3`
- Explanation: Only the three one-character substrings avoid repetition.

**Example 3**

- Input: `s = "abab"`
- Output: `7`
- Explanation: The four length-one and three length-two substrings are special; every longer substring repeats a character.
