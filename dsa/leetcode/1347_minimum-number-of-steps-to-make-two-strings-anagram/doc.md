# Minimum Number of Steps to Make Two Strings Anagram

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1347 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/) |

## Problem Description

### Goal

You are given two lowercase strings, `s` and `t`, of the same length. In one step, you may choose one character in `t` and replace it with any other lowercase English letter.

Return the minimum number of steps needed to make `t` an anagram of `s`. The order of characters does not matter in an anagram; the two strings must contain every letter with the same multiplicity.

### Function Contract

**Inputs**

- `s`: a nonempty string of lowercase English letters.
- `t`: a lowercase English string with the same length as `s`.
- Let $n$ be the common string length.

**Return value**

- Return the minimum number of character replacements in `t` needed to make its letter frequencies equal those of `s`.

### Examples

**Example 1**

- Input: `s = "bab", t = "aba"`
- Output: `1`
- Explanation: Replacing one `a` in `t` with `b` gives matching frequencies.

**Example 2**

- Input: `s = "leetcode", t = "practice"`
- Output: `5`

**Example 3**

- Input: `s = "anagram", t = "mangaar"`
- Output: `0`
