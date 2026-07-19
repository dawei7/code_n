# Shortest Path with Alternating Colors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1129 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/shortest-path-with-alternating-colors/) |

## Problem Description

### Goal

You are given a directed graph with `n` nodes labeled from `0` through `n - 1`. Every edge is either red or blue, and the graph may contain self-edges and parallel edges. Each `redEdges[i] = [a,b]` represents a directed red edge from `a` to `b`, while each `blueEdges[j] = [u,v]` represents a directed blue edge from `u` to `v`.

Return an array `answer` of length `n`. For every node `x`, `answer[x]` must be the length of the shortest directed path from node `0` to node `x` whose consecutive edges alternate colors. Either color may be used for the first edge. If no alternating path reaches `x`, set `answer[x] = -1`; the empty path makes `answer[0] = 0`.

### Function Contract

**Inputs**

- `n`: the number of nodes, where $1 \le n \le 100$.
- `redEdges`: a list of $r$ directed red edges, where $0 \le r \le 400$ and every endpoint lies in $[0,n-1]$.
- `blueEdges`: a list of $b$ directed blue edges, where $0 \le b \le 400$ and every endpoint lies in $[0,n-1]$.

**Return value**

An integer array of length $n$ containing each shortest alternating-path length from node `0`, or `-1` when unreachable.

### Examples

**Example 1**

- Input: `n = 3, redEdges = [[0,1],[1,2]], blueEdges = []`
- Output: `[0,1,-1]`

**Example 2**

- Input: `n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]`
- Output: `[0,1,-1]`
