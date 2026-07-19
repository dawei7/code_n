# Longest Subsequence Repeated k Times

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2014 |
| Difficulty | Hard |
| Topics | Hash Table, Two Pointers, String, Backtracking, Counting, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-subsequence-repeated-k-times/) |

## Problem Description

### Goal

A subsequence is obtained from a string by deleting zero or more characters
without changing the order of those retained. A candidate `seq` is repeated
`k` times in `s` when concatenating `k` copies of `seq` produces another
subsequence of `s`.

Find the longest candidate satisfying that repetition condition. When several
candidates share the maximum length, return the lexicographically largest one.
Return the empty string if no nonempty candidate can be repeated `k` times.

### Function Contract

Let $N=\lvert s\rvert$, let $L$ be the maximum candidate length, and let $C$
be the number of candidate extensions tested by the search. The constraints
imply $L\le7$.

**Inputs**

- `s`: a lowercase English string of length $N$, where
  $2\le N<\min(2001,8k)$.
- `k`: the required repetition count, where $2\le k\le2000$.

**Return value**

Return the longest repeated subsequence, breaking equal-length ties by
lexicographically larger value.

### Examples

**Example 1**

- Input: `s = "letsleetcode", k = 2`
- Output: `"let"`
- Explanation: Both `"let"` and `"ete"` have maximum length three, and
  `"let"` is lexicographically larger.

**Example 2**

- Input: `s = "bb", k = 2`
- Output: `"b"`
- Explanation: Two copies of `"b"` form the complete string.

**Example 3**

- Input: `s = "ab", k = 2`
- Output: `""`
- Explanation: Neither character occurs often enough to appear in two copies.

### Required Complexity

- **Time:** $O(NC)$
- **Space:** $O(CL)$

<details>
<summary>Approach</summary>

#### General

**Restrict the candidate alphabet by frequency.** A character occurring fewer
than `k` times cannot appear even once in a repeated candidate. Keep only
characters whose source frequency reaches `k`. Moreover, if a candidate has
length $L$, its `k` copies use $kL$ source characters. Since $N<8k$, every
valid candidate has $L\le7$.

**Grow only prefixes that already repeat.** Start a breadth-first search from
the empty prefix. Extend every current prefix by each eligible character, and
retain an extension only when scanning `s` confirms that `k` complete copies
appear in order. If a string is repeatable, all its prefixes are repeatable,
so pruning a failed extension cannot remove any valid longer answer.

Each nonempty breadth-first level contains candidates of one length. Whenever
a level is nonempty, record its lexicographically largest candidate. The last
nonempty level has maximum possible length, and taking its maximum applies the
required tie-break. The subsequence check advances through `s`, resetting the
candidate position whenever one complete copy has been matched, and succeeds
after the `k`th completion.

#### Complexity detail

Testing one candidate scans at most $N$ characters, so testing $C$ extensions
takes $O(NC)$ time. A frontier can retain $O(C)$ candidate strings, each of
length at most $L\le7$, for $O(CL)$ space. The official relation $N<8k$
strictly bounds the candidate depth, but the number of viable prefixes varies
non-monotonically with character frequencies and order.

#### Alternatives and edge cases

- **Enumerate source subsequences:** Generating all $2^N$ subsequences ignores
  the seven-character answer bound and is infeasible.
- **Depth-first lexicographic search:** Descending-character DFS can find the
  tie-break winner, but it must still prove that no longer valid candidate
  exists; breadth-first levels make the length priority explicit.
- A frequent character can still fail in a longer candidate because source
  order, not frequency alone, determines subsequence repetition.
- Repeated occurrences of one character may fill all seven positions of the
  answer.
- The empty string is returned when every single-character candidate fails.

</details>
