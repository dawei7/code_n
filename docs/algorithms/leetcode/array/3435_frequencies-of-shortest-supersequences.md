# Frequencies of Shortest Supersequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3435 |
| Difficulty | Hard |
| Topics | Array, String, Bit Manipulation, Graph Theory, Topological Sort, Enumeration |
| Official Link | [frequencies-of-shortest-supersequences](https://leetcode.com/problems/frequencies-of-shortest-supersequences/) |

## Problem Description & Examples
### Goal
Given a list of strings, determine the frequency of each character (from 'a' to 'z') across all possible shortest common supersequences (SCS) of the input strings. A shortest common supersequence is a string of minimum length that contains every input string as a subsequence. Since there may be multiple such supersequences, you must return the count of each character at every position across all valid SCSs, normalized or aggregated as required by the problem constraints.

### Function Contract
**Inputs**

- `words`: A list of strings consisting of lowercase English letters.

**Return value**

- A list of strings (or a structured format) representing the frequency distribution of characters in the shortest common supersequences.

### Examples
**Example 1**

- Input: `words = ["ab", "ba"]`
- Output: `["aba", "bab"]` (The SCSs are "aba" and "bab", frequencies are aggregated accordingly).

**Example 2**

- Input: `words = ["a", "b"]`
- Output: `["ab", "ba"]`

**Example 3**

- Input: `words = ["aa", "aa"]`
- Output: `["aa"]`

---

## Underlying Base Algorithm(s)
The problem is solved by modeling the dependencies between characters as a directed graph. Since we are looking for the shortest common supersequence, we identify the relative ordering constraints imposed by each word. We use topological sort to find valid orderings and dynamic programming (often involving bitmasking if the number of strings is small) to determine the length and structure of the SCS.

---

## Complexity Analysis
- **Time Complexity**: `O(2^N * N + L)`, where `N` is the number of unique characters (up to 26) and `L` is the total length of all strings. The exponential component arises from the state-space search for the shortest path in the dependency graph.
- **Space Complexity**: `O(2^N + L)` to store the DP table and the dependency graph.
