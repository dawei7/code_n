# Compare Strings by Frequency of the Smallest Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1170 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/) |

## Problem Description

### Goal

For a non-empty string $s$, define $f(s)$ as the frequency of its lexicographically smallest character. For example, `f("dcce") = 2` because `'c'` is the smallest character and occurs twice.

You are given an array `words` and an array `queries`. For every `queries[i]`, count the words $W$ for which $f(\texttt{queries[i]}) < f(W)$. Return an integer array whose $i$-th entry is that count for the $i$-th query, preserving query order.

### Function Contract

**Inputs**

- `queries`: Between $1$ and $2000$ non-empty lowercase English strings.
- `words`: Between $1$ and $2000$ non-empty lowercase English strings.
- Every query and word has length from $1$ through $10$.
- Let $q=\lvert\texttt{queries}\rvert$, $w=\lvert\texttt{words}\rvert$, and define

$$
S = \sum_{s \in \texttt{queries}} \lvert s \rvert + \sum_{s \in \texttt{words}} \lvert s \rvert.
$$

**Return value**

- A length-$q$ array where entry $i$ is the number of words with smallest-character frequency strictly greater than that of `queries[i]`.

### Examples

**Example 1**

- Input: `queries = ["cbd"]`, `words = ["zaaaz"]`
- Output: `[1]`

Here `f("cbd") = 1` and `f("zaaaz") = 3`.

**Example 2**

- Input: `queries = ["bbb","cc"]`, `words = ["a","aa","aaa","aaaa"]`
- Output: `[1,2]`

**Example 3**

- Input: `queries = ["abcd","aabb"]`, `words = ["zzzz","abc","aa"]`
- Output: `[2,1]`
