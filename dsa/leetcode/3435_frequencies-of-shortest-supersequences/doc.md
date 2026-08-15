# Frequencies of Shortest Supersequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3435 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Bit Manipulation, Graph Theory, Topological Sort, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/frequencies-of-shortest-supersequences/) |

## Problem Description

### Goal

Given a collection of distinct two-letter lowercase strings, find the frequency descriptions of all shortest common supersequences. A common supersequence contains every input word as a subsequence, and it is shortest when no common supersequence has fewer characters.

Supersequences that are permutations of each other have the same letter frequencies and count as one result. Return one 26-entry array for every distinct frequency pattern attainable by a shortest common supersequence. Entry zero records the count of `a`, entry one the count of `b`, and so on; the arrays may be returned in any order.

### Function Contract

**Inputs**

- `words`: Between 1 and 256 unique lowercase strings, each of length exactly two.

Across all words, at most 16 distinct letters occur.

**Return value**

Return all distinct 26-letter frequency arrays corresponding to shortest common supersequences, in any order.

### Examples

#### Example 1

- **Input:** `words = ["ab","ba"]`
- **Output:** `[[1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]`

#### Example 2

- **Input:** `words = ["aa","ac"]`
- **Output:** `[[2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]`

#### Example 3

- **Input:** `words = ["aa","bb","cc"]`
- **Output:** `[[2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]`
