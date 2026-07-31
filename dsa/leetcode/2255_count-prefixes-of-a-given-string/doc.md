# Count Prefixes of a Given String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2255 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/count-prefixes-of-a-given-string/) |

## Problem Description

### Goal

Given an array `words` and a string `s`, count the array entries that are a
prefix of `s`. A prefix must occupy a contiguous range beginning at index zero;
matching the same letters somewhere later in `s` does not qualify.

Every occurrence in `words` is considered separately. Consequently, if an
identical prefix appears multiple times, each copy contributes one to the
answer. A word equal to all of `s` is a prefix, while a word longer than `s`
cannot be one. All strings contain only lowercase English letters.

Return the total number of qualifying entries.

### Function Contract

**Inputs**

- `words`: An array of $1$ to $1000$ lowercase-English-letter strings, each with length from $1$ to $10$.
- `s`: A lowercase-English-letter string with length from $1$ to $10$.

Define

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

**Return value**

Return the number of indices $i$ for which `words[i]` matches the beginning of
`s` for the entirety of `words[i]`. Duplicate strings are counted at their
distinct array positions.

### Examples

**Example 1**

- Input: `words = ["a","b","c","ab","bc","abc"], s = "abc"`
- Output: `3`

**Example 2**

- Input: `words = ["a","a"], s = "aa"`
- Output: `2`

**Example 3**

- Input: `words = ["abcd","abc","abx"], s = "abc"`
- Output: `1`
