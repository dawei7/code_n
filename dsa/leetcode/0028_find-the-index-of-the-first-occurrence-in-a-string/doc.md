# Find the Index of the First Occurrence in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 28 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Two Pointers, String, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |

## Problem Description
### Goal
You are given two nonempty strings, `haystack` and `needle`. Search for an interval of `haystack` whose consecutive characters equal the complete `needle` in the same order. Matches may overlap, and characters cannot be skipped.

Return the zero-based starting index of the earliest such occurrence. If no contiguous occurrence exists, return `-1`. A match beginning at index zero takes precedence over every later match, and a needle equal to the entire haystack also begins at zero.

### Function Contract
**Inputs**

- `haystack`: non-empty `str`
- `needle`: non-empty `str`

**Return value**

An `int` containing the first match's zero-based start index, or `-1`.

### Examples
**Example 1**

- Input: `haystack = "sadbutsad", needle = "sad"`
- Output: `0`

**Example 2**

- Input: `haystack = "leetcode", needle = "leeto"`
- Output: `-1`

**Example 3**

- Input: `haystack = "mississippi", needle = "issip"`
- Output: `4`
