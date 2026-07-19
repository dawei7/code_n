# Find the Longest Substring Containing Vowels in Even Counts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1371 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Bit Manipulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/) |

## Problem Description

### Goal

Given a lowercase English string `s`, find the maximum length of a contiguous substring in which each vowel—`a`, `e`, `i`, `o`, and `u`—appears an even number of times.

Zero is an even count, so a qualifying substring may omit any or all vowels. Consonant frequencies are unrestricted. Return only the greatest valid substring length, not the substring itself.

### Function Contract

**Inputs**

- `s`: a lowercase string of length $n$.

**Return value**

- The maximum length among contiguous substrings whose count of every vowel is even.

### Examples

**Example 1**

- Input: `s = "eleetminicoworoep"`
- Output: `13`

**Example 2**

- Input: `s = "leetcodeisgreat"`
- Output: `5`

**Example 3**

- Input: `s = "bcbcbc"`
- Output: `6`
