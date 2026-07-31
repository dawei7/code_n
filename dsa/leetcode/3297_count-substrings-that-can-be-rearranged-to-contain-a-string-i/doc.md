# Count Substrings That Can Be Rearranged to Contain a String I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3297 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/) |

## Problem Description

### Goal

You are given two lowercase English strings, `word1` and `word2`. A substring of `word1` is valid when its characters can be rearranged so that the resulting string begins with `word2`. Characters after that prefix may appear in any order and do not need to match anything else.

Rearrangement changes only character order, so validity means that the substring contains at least the required number of every character appearing in `word2`. Count all valid substrings of `word1`. Substrings are identified by their positions, so equal text taken from different ranges contributes separately.

### Function Contract

**Inputs**

- `word1`: The lowercase source string whose contiguous substrings are counted.
- `word2`: The lowercase string whose character multiset every valid substring must contain.

The length of `word1` is from 1 through $10^5$, and the length of `word2` is from 1 through $10^4$.

**Return value**

- The number of substrings of `word1` that can be rearranged to have `word2` as a prefix.

### Examples

**Example 1**

- Input: `word1 = "bcca"`, `word2 = "abc"`
- Output: `1`
- Explanation: Only the whole string contains an `a`, a `b`, and a `c`; it can be rearranged to begin with `"abc"`.

**Example 2**

- Input: `word1 = "abcabc"`, `word2 = "abc"`
- Output: `10`
- Explanation: Every substring of length at least three contains the required characters except no additional ranges beyond those ten qualify.

**Example 3**

- Input: `word1 = "abcabc"`, `word2 = "aaabc"`
- Output: `0`
- Explanation: The source contains only two copies of `a`, fewer than the three required copies.
