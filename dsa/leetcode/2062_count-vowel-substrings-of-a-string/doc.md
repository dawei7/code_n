# Count Vowel Substrings of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2062 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-vowel-substrings-of-a-string/) |

## Problem Description

### Goal

A substring is a nonempty contiguous sequence of characters. Call a substring a vowel substring when every one of its characters is a vowel—`a`, `e`, `i`, `o`, or `u`—and all five different vowels occur at least once.

Given a lowercase English string `word`, return the number of its vowel substrings. Count different index ranges separately even when they contain the same text.

### Function Contract

**Inputs**

- `word`: a lowercase English string of length $n$, where $1 \le n \le 100$.

**Return value**

- Return the number of nonempty contiguous substrings that contain only vowels and include all five vowels.

### Examples

**Example 1**

- Input: `word = "aeiouu"`
- Output: `2`
- Explanation: The ranges spelling `"aeiou"` and `"aeiouu"` both satisfy the two conditions.

**Example 2**

- Input: `word = "unicornarihan"`
- Output: `0`
- Explanation: No all-vowel range contains all five distinct vowels.

**Example 3**

- Input: `word = "cuaieuouac"`
- Output: `7`
- Explanation: Seven contiguous ranges stay within the central vowel run and contain every vowel.
