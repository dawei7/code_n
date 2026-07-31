# Sort Vowels in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2785 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-vowels-in-a-string/) |

## Problem Description

### Goal

You are given a 0-indexed string `s` containing uppercase and lowercase English letters. Permute only its vowels to form a new string `t`.

Every consonant must remain at its original index. Across the indices that originally contain vowels, place the same vowel characters in non-decreasing order of their ASCII values. Consequently, uppercase vowels precede lowercase vowels when their code points demand it; sorting is case-sensitive rather than alphabetical without regard to case.

The vowels are `a`, `e`, `i`, `o`, and `u`, in either uppercase or lowercase. Every other English letter is a consonant. Return the resulting string.

### Function Contract

**Inputs**

- `s`: A string of $n$ uppercase or lowercase English letters, where $1 \le n \le 10^5$.

**Return value**

Return a string of length $n$ in which consonants occupy their original indices and the vowels, read from left to right across their original positions, are in non-decreasing ASCII order.

### Examples

**Example 1**

- Input: `s = "lEetcOde"`
- Output: `"lEOtcede"`
- Explanation: The vowels are `E`, `e`, `O`, and `e`; their ASCII order is `E`, `O`, `e`, `e`, while `l`, `t`, `c`, and `d` stay fixed.

**Example 2**

- Input: `s = "lYmpH"`
- Output: `"lYmpH"`
- Explanation: The string has no vowels, so no position changes.

**Example 3**

- Input: `s = "aeiouAEIOU"`
- Output: `"AEIOUaeiou"`
- Explanation: All characters are vowels, and uppercase ASCII codes precede the lowercase codes.
