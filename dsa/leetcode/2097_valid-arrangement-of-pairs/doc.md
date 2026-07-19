# Valid Arrangement of Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2097 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Graph Theory, Eulerian Circuit |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/valid-arrangement-of-pairs/) |

## Problem Description

### Goal

You are given distinct directed pairs. In a pair `[start, end]`, the first value is its starting vertex and the second value is its ending vertex.

Reorder all pairs so that the ending vertex of every pair equals the starting vertex of the following pair. Every input pair must appear exactly once in the returned arrangement. At least one valid arrangement is guaranteed to exist, and any valid one may be returned.

### Function Contract

Let $P$ be the number of directed pairs.

**Inputs**

- `pairs`: a list of $P$ distinct two-element integer lists `[start, end]`, where $1 \le P \le 10^5$, $0 \le \texttt{start}, \texttt{end} \le 10^9$, and the two endpoints of each pair differ.

**Return value**

Return any ordering of all input pairs in which each pair's end equals the next pair's start.

### Examples

**Example 1**

- Input: `pairs = [[5,1],[4,5],[11,9],[9,4]]`
- Output: `[[11,9],[9,4],[4,5],[5,1]]`

**Example 2**

- Input: `pairs = [[1,3],[3,2],[2,1]]`
- Output: `[[1,3],[3,2],[2,1]]`
- Explanation: This arrangement closes a directed cycle. Rotating that cycle would also be valid.

**Example 3**

- Input: `pairs = [[1,2],[1,3],[2,1]]`
- Output: `[[1,2],[2,1],[1,3]]`
