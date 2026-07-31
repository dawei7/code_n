# Find the String with LCP

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2573 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming, Greedy, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [find-the-string-with-lcp](https://leetcode.com/problems/find-the-string-with-lcp/) |

## Problem Description

### Goal

For a 0-indexed string `word` of $n$ lowercase English letters, its LCP matrix is an $n \times n$ grid. The entry `lcp[i][j]` is the length of the longest common prefix shared by the two suffixes that begin at indices `i` and `j`: `word[i:n]` and `word[j:n]`.

Given such an $n \times n$ integer matrix `lcp`, construct the lexicographically smallest `word` whose suffixes produce exactly that matrix. If the supplied values cannot be the LCP matrix of any lowercase English string, return the empty string.

For two strings of equal length, lexicographic order is determined at their first differing position: the string using the alphabetically earlier letter there is smaller.

### Function Contract

**Inputs**

- `lcp`: An $n \times n$ matrix whose entry at row $i$ and column $j$ claims the common-prefix length of the suffixes beginning at those indices.

The matrix dimension satisfies $1 \le n \le 1000$, and every entry lies between $0$ and $n$, inclusive.

**Return value**

- Return the lexicographically smallest lowercase English string of length $n$ that generates `lcp`, or `""` if no such string exists.

### Examples

**Example 1**

- Input: `lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]`
- Output: `"abab"`
- Explanation: The matrix requires two alternating character groups. Assigning the earliest possible letters to those groups gives `"abab"`.

**Example 2**

- Input: `lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]`
- Output: `"aaaa"`
- Explanation: Every pair of suffixes shares as much prefix as their remaining lengths allow, so all positions contain the same character.

**Example 3**

- Input: `lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]`
- Output: `""`
- Explanation: A suffix starting at the final position has length one, so `lcp[3][3]` cannot equal three.
