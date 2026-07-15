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

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compute each frequency in one scan.** Track the smallest character seen and how many times it has appeared. A smaller character resets the count to one; an equal character increments it. This produces $f(s)$ without separately calling `min` and `count`.

**Exploit the length bound.** Every string has length at most `10`, so every frequency is an integer from `1` through `10`. Count how many words have each possible frequency in an 11-slot bucket array. Then sweep frequencies downward to precompute `greater[k]`, the number of words whose frequency is strictly greater than $k$.

**Answer each query directly.** Compute `frequency(query)` and append `greater[frequency(query)]`. The suffix counts already exclude equal-frequency words, exactly matching the strict inequality. Each word and query is scanned once, and query order is unchanged.

#### Complexity detail

All string scans examine $S$ characters. Building the suffix counts touches only the fixed 10-frequency domain, so total time is $O(S)$. The two fixed-size arrays use $O(1)$ auxiliary space; the required result array is output storage.

#### Alternatives and edge cases

- **Sort word frequencies and binary search:** This is correct in $O(S+w\log w+q\log w)$ time, but the fixed frequency range permits direct counting.
- **Compare every query with every word:** This takes $O(qw)$ comparisons after frequency calculation and scales quadratically when both arrays grow.
- **Equal frequencies:** A word counts only when its frequency is strictly greater, not equal.
- **One-character string:** Its smallest character occurs once, so its frequency is `1`.
- **All characters equal:** The frequency is the full string length, up to `10`.
- **Smallest character not first:** The scan must reset when a later, lexicographically smaller character appears.

</details>
