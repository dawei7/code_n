# Longest Common Suffix Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3093 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-common-suffix-queries/) |

## Problem Description

### Goal

Two arrays of lowercase strings are given: `wordsContainer`, which supplies candidate words, and `wordsQuery`, which supplies independent queries. For every query, select the container word sharing the longest possible suffix with it. The empty suffix is shared when no final character matches.

If several container words attain the same longest common suffix length, prefer the shortest complete word. If that still leaves a tie, prefer the word appearing at the smallest index in `wordsContainer`.

Return one container index for each query, preserving the order of `wordsQuery`.

### Function Contract

**Inputs**

- `wordsContainer`: a nonempty list of lowercase English strings.
- `wordsQuery`: a nonempty list of lowercase English query strings.

Each list contains at most $10^4$ strings, and each string has length from $1$ through $5\cdot10^3$. Define

$$
C=\sum_{w\in\texttt{wordsContainer}}\lvert w\rvert
\qquad\text{and}\qquad
Q=\sum_{w\in\texttt{wordsQuery}}\lvert w\rvert.
$$

Both $C$ and $Q$ are at most $5\cdot10^5$.

**Return value**

Return a list of indices. For each `wordsQuery[i]`, choose the index maximizing common-suffix length, then minimizing the container word's length, then minimizing its index.

### Examples

#### Example 1

- **Input:** `wordsContainer = ["abcd", "bcd", "xbcd"]`, `wordsQuery = ["cd", "bcd", "xyz"]`
- **Output:** `[1, 1, 1]`
- **Explanation:** All three words match `"cd"` and `"bcd"`, so shortest word `"bcd"` wins. No final character matches `"xyz"`, and the same globally shortest word wins the empty-suffix tie.

#### Example 2

- **Input:** `wordsContainer = ["abcdefgh", "poiuygh", "ghghgh"]`, `wordsQuery = ["gh", "acbfgh", "acbfegh"]`
- **Output:** `[2, 0, 2]`
- **Explanation:** The shortest word wins the two-character `"gh"` ties, but index 0 uniquely matches the longer suffix `"fgh"` for the middle query.

#### Example 3

- **Input:** `wordsContainer = ["za", "ya", "b"]`, `wordsQuery = ["qa", "x"]`
- **Output:** `[0, 2]`
- **Explanation:** Equal-length `"a"` matches use the earlier index, while no match for `"x"` falls back to the globally shortest word.
