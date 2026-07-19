# Camelcase Matching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1023 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String, Trie, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/camelcase-matching/) |

## Problem Description

### Goal

You are given an array of query strings `queries` and a string `pattern`. A query matches when it can be formed by inserting zero or more lowercase English letters anywhere into `pattern`.

Return a boolean array aligned with the queries, where each value reports whether that query matches. Every pattern character must appear in order, and any query character not used to match the pattern must be lowercase. Consequently, an additional uppercase character makes a query invalid.

### Function Contract

**Inputs**

- `queries`: an array of $Q$ nonempty English-letter strings, where $1\le Q\le100$ and every query has length at most `100`.
- `pattern`: a nonempty English-letter string of length $P$, where $1\le P\le100$.

Define the total query length as

$$
S=\sum_{q\in\texttt{queries}}\lvert q\rvert.
$$

**Return value**

- A $Q$-element boolean array indicating whether each query can be produced from `pattern` by inserting only lowercase letters.

### Examples

**Example 1**

- Input: `queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern = "FB"`
- Output: `[True, False, True, True, False]`

**Example 2**

- Input: `queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern = "FoBa"`
- Output: `[True, False, True, False, False]`

**Example 3**

- Input: `queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern = "FoBaT"`
- Output: `[False, True, False, False, False]`
