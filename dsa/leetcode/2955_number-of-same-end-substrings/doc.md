# Number of Same-End Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2955 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-same-end-substrings/) |

## Problem Description
### Goal
You are given a 0-indexed lowercase English string `s` and an array `queries`.
Each query `[left, right]` selects the inclusive substring from index `left`
through index `right`.

A nonempty string is same-end when its first and last characters are equal.
This includes every single-character string, since its two ends are the same
position. For each selected range, count all contiguous substrings lying
entirely inside that range that are same-end. Return the counts in the same
order as the input queries.

### Function Contract
**Inputs**

- `s`: the lowercase English source string
- `queries`: inclusive `[left, right]` index pairs describing ranges of `s`

Let $N=\lvert\texttt{s}\rvert$ and $Q=\lvert\texttt{queries}\rvert$. The
contract guarantees $2\le N\le3\cdot10^4$, $1\le Q\le3\cdot10^4$, and
$0\le\texttt{left}\le\texttt{right}<N$ for every query.

**Return value**

An array whose entry at index `i` is the number of same-end substrings inside
the inclusive range described by `queries[i]`.

### Examples
**Example 1**

- Input: `s = "abcaab", queries = [[0,0],[1,4],[2,5],[0,5]]`
- Output: `[1,5,5,10]`
- Explanation: Each range counts its singletons plus longer substrings whose endpoint characters match.

**Example 2**

- Input: `s = "abcd", queries = [[0,3]]`
- Output: `[4]`
- Explanation: All letters differ, so only the four single-character substrings qualify.
