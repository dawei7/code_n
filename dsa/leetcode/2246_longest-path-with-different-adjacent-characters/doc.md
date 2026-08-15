# Longest Path With Different Adjacent Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2246 |
| Difficulty | Hard |
| Topics | Array, String, Tree, Depth-First Search, Graph Theory, Topological Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-path-with-different-adjacent-characters/) |

## Problem Description

### Goal

A connected, undirected, acyclic graph with $n$ nodes is rooted at node $0$.
The 0-indexed array `parent` describes that rooted tree: `parent[0]` is `-1`,
and for every other node `i`, `parent[i]` is the node directly above it. A
string `s` assigns lowercase character `s[i]` to node `i`.

Consider any simple path in the tree. It is valid when every pair of adjacent
nodes on the path has different assigned characters; nonadjacent nodes may
share a character. Return the greatest possible number of nodes in such a
path.

### Function Contract

**Inputs**

- `parent`: A length-$n$ array representing a valid tree rooted at `0`, where $1\le n\le10^5$, `parent[0] = -1`, and every later entry is a node index.
- `s`: A length-$n$ string of lowercase English letters, with `s[i]` assigned to node `i`.

**Return value**

Return the number of nodes in the longest simple tree path whose adjacent
characters are all different.

### Examples

#### Example 1

- **Input:** `parent = [-1,0,0,1,1,2], s = "abacbe"`
- **Output:** `3`

#### Example 2

- **Input:** `parent = [-1,0,0,0], s = "aabc"`
- **Output:** `3`

#### Example 3

- **Input:** `parent = [-1], s = "z"`
- **Output:** `1`
