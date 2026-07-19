# Determine if String Halves Are Alike

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1704 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/determine-if-string-halves-are-alike/) |

## Problem Description
### Goal

You are given an even-length string `s` containing uppercase and lowercase English letters. Split it exactly in the middle: `a` is the first half and `b` is the second half, so both halves contain the same number of characters.

Two strings are considered alike when they contain the same number of vowels. The vowels are `a`, `e`, `i`, `o`, and `u` in either letter case; repeated occurrences are counted separately. Return whether the two fixed halves of `s` are alike.

### Function Contract
**Inputs**

- `s`: an even-length string of uppercase and lowercase English letters
- Its length $n$ satisfies $2 \le n \le 1000$.

**Return value**

`True` when `s[:n // 2]` and `s[n // 2:]` contain equal numbers of vowels, and `False` otherwise.

### Examples
**Example 1**

- Input: `s = "book"`
- Output: `True`

The halves `bo` and `ok` each contain one vowel.

**Example 2**

- Input: `s = "textbook"`
- Output: `False`

The first half `text` contains one vowel, while `book` contains two occurrences of `o`.

**Example 3**

- Input: `s = "AAee"`
- Output: `True`

Uppercase vowels count as vowels, so both halves contain two.
