# Count Substrings With K-Frequency Characters II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3329 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/) |

## Problem Description

### Goal

Given a lowercase English string `s` and a positive integer `k`, consider every nonempty contiguous substring of `s`. A substring qualifies when at least one character occurs at least `k` times inside that substring. The character that reaches the threshold may differ between substrings, and no particular character is designated beforehand.

Return the total number of qualifying substrings. Substrings are distinguished by their start and end indices, so equal text at different positions contributes more than once. Once a substring qualifies, extending it to the right cannot make it invalid because existing character frequencies never decrease.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$.
- `k`: The inclusive frequency threshold.

The constraints are $1\leq n\leq3\cdot10^5$ and $1\leq k\leq n$.

**Return value**

Return the number of pairs $(i,j)$ with $0\leq i\leq j<n$ for which some character appears at least `k` times in `s[i..j]`.

### Examples

#### Example 1

- **Input:** `s = "abacb", k = 2`
- **Output:** `4`
- **Explanation:** `"aba"`, `"abac"`, and `"abacb"` qualify through `a`; `"bacb"` qualifies through `b`.

#### Example 2

- **Input:** `s = "abcde", k = 1`
- **Output:** `15`
- **Explanation:** Every nonempty substring contains a character at least once, so all $5\cdot6/2$ substrings qualify.
