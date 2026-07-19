# Merge Strings Alternately

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1768 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-strings-alternately/) |

## Problem Description

### Goal

You are given two strings, `word1` and `word2`. Construct a new string by taking characters alternately, beginning with the first character of `word1`, then the first character of `word2`, and continuing in that order.

If one input is longer, alternating stops after the shorter string is exhausted. Append all remaining characters of the longer string to the end without changing their order.

Return the resulting merged string.

### Function Contract

**Inputs**

- `word1`: a nonempty string of lowercase English letters, with $1 \le A \le 100$, where $A=\lvert\texttt{word1}\rvert$.
- `word2`: a nonempty string of lowercase English letters, with $1 \le B \le 100$, where $B=\lvert\texttt{word2}\rvert$.

**Return value**

- Return the length-$(A+B)$ string formed by alternating characters from `word1` and `word2`, starting with `word1`, followed by the unconsumed suffix of the longer input.

### Examples

**Example 1**

- Input: `word1 = "abc", word2 = "pqr"`
- Output: `"apbqcr"`
- Explanation: Both strings have the same length, so every character belongs to an alternating pair.

**Example 2**

- Input: `word1 = "ab", word2 = "pqrs"`
- Output: `"apbqrs"`
- Explanation: After `"apbq"`, the remaining suffix `"rs"` from `word2` is appended.

**Example 3**

- Input: `word1 = "abcd", word2 = "pq"`
- Output: `"apbqcd"`
- Explanation: After two alternating pairs, the suffix `"cd"` from `word1` remains.
