# Find Center of Star Graph

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/find-center-of-star-graph/) |
| Frontend ID | 1791 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An undirected star graph has $n$ nodes labeled from $1$ through $n$. It contains one center node and exactly $n-1$ edges, each connecting that center to one of the other nodes. Every non-center node is therefore a leaf incident to only its edge with the center.

You are given the graph as `edges`, where each pair `edges[i] = [u_i, v_i]` represents an undirected edge between its two endpoints. The input is guaranteed to describe a valid star graph. Return the label of its center node.

### Function Contract

**Inputs**

- `edges`: a list of exactly $n-1$ two-element integer lists, where $3 \le n \le 10^5$.
- Every endpoint is a node label from $1$ through $n$, the endpoints of an edge differ, and all edges together form a valid undirected star graph.

**Return value**

- Return the integer label of the unique center node.

### Examples

**Example 1**

- Input: `edges = [[1, 2], [2, 3], [4, 2]]`
- Output: `2`

Node `2` is incident to every edge.

**Example 2**

- Input: `edges = [[1, 2], [5, 1], [1, 3], [1, 4]]`
- Output: `1`

Every other node has its sole connection to node `1`.

**Example 3**

- Input: `edges = [[1, 3], [2, 3]]`
- Output: `3`

The minimum valid star has two edges, and their shared endpoint is the center.
