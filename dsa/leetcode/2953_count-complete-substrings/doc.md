# Count Complete Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2953 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-complete-substrings/) |

## Problem Description

### Goal

You are given a lowercase English string `word` and a positive integer `k`.
A nonempty substring is complete only when every distinct character present in
that substring occurs exactly `k` times; characters absent from it impose no
frequency requirement.

The substring must also be locally alphabetically smooth. For every pair of
adjacent characters inside it, the absolute difference between their alphabet
positions must be at most `2`. Return the total number of contiguous substrings
of `word` that satisfy both the exact-frequency and adjacency conditions.

### Function Contract

**Inputs**

- `word`: the lowercase English source string
- `k`: the exact required occurrence count for each character present in a complete substring

Let $N=\lvert\texttt{word}\rvert$. The contract guarantees
$1\le N\le10^5$ and $1\le\texttt{k}\le N$.

**Return value**

The number of nonempty contiguous substrings satisfying both completeness
conditions.

### Examples

#### Example 1

- **Input:** `word = "igigee", k = 2`
- **Output:** `3`
- **Explanation:** `"igig"`, `"ee"`, and `"igigee"` each use every present letter exactly twice and respect the adjacency limit.

#### Example 2

- **Input:** `word = "aaabbbccc", k = 3`
- **Output:** `6`
- **Explanation:** The three single-letter blocks, the two adjacent pairs of blocks, and the whole string are complete.
