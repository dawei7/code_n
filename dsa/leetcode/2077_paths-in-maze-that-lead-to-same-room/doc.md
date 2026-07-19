# Paths in Maze That Lead to Same Room

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2077 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/) |

## Problem Description

### Goal

A maze has `n` rooms numbered from $1$ through $n$. Each pair in `corridors` creates one undirected connection between two distinct rooms, and no corridor is repeated.

The maze's confusion score is the number of distinct cycles containing exactly three rooms. Traversing the same three rooms from another starting point or in the opposite direction does not create a different cycle; only the set of rooms matters. Return this number of triangular cycles.

### Function Contract

**Inputs**

- `n`: the number of rooms, where $2 \le n \le 1000$.
- `corridors`: a list of $E$ unique undirected pairs `[u, v]`, where $1 \le E \le 5\cdot10^4$, $1 \le u,v \le n$, and $u \ne v$.
- Let $d(v)$ denote the number of corridors incident to room $v$.

**Return value**

- Return the number of distinct unordered triples of rooms whose three pairwise corridors all exist.

### Examples

**Example 1**

- Input: `n = 5, corridors = [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]`
- Output: `2`
- Explanation: Rooms `{1,3,4}` and `{1,2,4}` form the two triangular cycles.

**Example 2**

- Input: `n = 4, corridors = [[1,2],[3,4]]`
- Output: `0`
- Explanation: Two disconnected corridors do not close any three-room cycle.

**Example 3**

- Input: `n = 3, corridors = [[1,2],[2,3],[1,3]]`
- Output: `1`
- Explanation: All three room pairs are connected, so the rooms form exactly one cycle.
