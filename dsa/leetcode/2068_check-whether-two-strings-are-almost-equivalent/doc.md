# Check Whether Two Strings are Almost Equivalent

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2068 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/) |

## Problem Description

### Goal

The frequency of a letter in a string is its number of occurrences. Two equal-length lowercase English strings are almost equivalent when, for every letter from `a` through `z`, the absolute difference between its two frequencies is at most $3$.

Given `word1` and `word2`, return whether they are almost equivalent. A difference of exactly $3$ is allowed; any single letter whose frequency differs by $4$ or more makes the result false.

### Function Contract

**Inputs**

- `word1`: a lowercase English string of length $n$.
- `word2`: another lowercase English string of the same length, where $1 \le n \le 100$.

**Return value**

- Return `true` if every letter's two frequencies differ by at most $3$; otherwise return `false`.

### Examples

**Example 1**

- Input: `word1 = "aaaa", word2 = "bccb"`
- Output: `false`
- Explanation: The frequency of `a` differs by $4$, exceeding the limit.

**Example 2**

- Input: `word1 = "abcdeef", word2 = "abaaacc"`
- Output: `true`
- Explanation: The largest frequency difference is $3$, which is allowed.

**Example 3**

- Input: `word1 = "cccddabba", word2 = "babababab"`
- Output: `true`
- Explanation: Every letter's frequency difference is at most $3$.
