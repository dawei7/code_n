# Longest Palindrome by Concatenating Two Letter Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2131 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Greedy, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/) |

## Problem Description

### Goal

You are given an array whose elements are two-letter strings made from
lowercase English letters. Select any subset of the individual occurrences
and concatenate the selected words in any order. Each occurrence may be used
at most once.

Find the greatest possible character length of a concatenation that is a
palindrome, meaning it reads identically from left to right and right to left.
Return `0` when no selected word can form a non-empty palindrome.

### Function Contract

**Inputs**

- `words`: A list of $n$ lowercase two-letter strings, where
  $1\le n\le 10^5$.

**Return value**

The length in characters of the longest palindrome obtainable from the
available word occurrences.

### Examples

#### Example 1

- **Input:** `words = ["lc", "cl", "gg"]`
- **Output:** `6`
- **Explanation:** `"lc" + "gg" + "cl"` forms `"lcggcl"`.

#### Example 2

- **Input:** `words = ["ab", "ty", "yt", "lc", "cl", "ab"]`
- **Output:** `8`
- **Explanation:** The reverse pairs `"ty"`/`"yt"` and `"lc"`/`"cl"` use four
  words.

#### Example 3

- **Input:** `words = ["cc", "ll", "xx"]`
- **Output:** `2`
- **Explanation:** Any one equal-letter word can occupy the center.
