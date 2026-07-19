# Frog Position After T Seconds

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1377 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/frog-position-after-t-seconds/) |

## Problem Description

### Goal

An undirected tree has `n` vertices numbered from `1` through `n`. A frog starts at vertex `1`. Every second, if the current vertex has any adjacent vertex that the frog has not visited, the frog chooses uniformly among those unvisited neighbors and jumps to one of them.

The frog never revisits a vertex. If no unvisited neighbor is available, it remains at its current vertex for every later second. Given a time `t` and a `target` vertex, return the probability that the frog is at `target` after exactly `t` seconds.

### Function Contract

**Inputs**

- `n`: the number of vertices, with $1 \le n \le 100$.
- `edges`: the `n - 1` undirected edges of the tree.
- `t`: the number of elapsed seconds, with $1 \le t \le 50$.
- `target`: the vertex whose probability is requested.

**Return value**

- The probability that the frog occupies `target` after exactly `t` seconds.

### Examples

**Example 1**

- Input: `n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4`
- Output: `0.16666666666666666`

**Example 2**

- Input: `n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7`
- Output: `0.3333333333333333`

**Example 3**

- Input: `n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6`
- Output: `0.16666666666666666`
