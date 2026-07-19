# Swap For Longest Repeated Character Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1156 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/) |

## Problem Description

### Goal

You are given a string `text` consisting only of lowercase English characters. You may swap two characters at any two positions in the string, or leave the string unchanged.

After using at most one swap, consider every substring whose characters are all the same. Return the greatest possible length of such a repeated-character substring. A swap only relocates characters already present in `text`; it cannot create another copy of the character used by the chosen substring.

### Function Contract

**Inputs**

- `text`: A lowercase English string of length $n$, where $1 \le n \le 2 \cdot 10^4$.

**Return value**

- The maximum length of a one-character substring obtainable after at most one swap.

### Examples

**Example 1**

- Input: `text = "ababa"`
- Output: `3`

**Example 2**

- Input: `text = "aaabaaa"`
- Output: `6`

**Example 3**

- Input: `text = "aaaaa"`
- Output: `5`
