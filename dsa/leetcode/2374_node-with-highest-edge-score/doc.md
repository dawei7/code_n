# Node With Highest Edge Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2374 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/node-with-highest-edge-score/) |

## Problem Description

### Goal

A directed graph has $n$ nodes labeled from $0$ through $n-1$, and every node has exactly one outgoing edge. The array `edges` represents those edges: node `i` points to node `edges[i]`.

The edge score of a target node is the sum of the labels of all source nodes pointing to it. Find the node whose edge score is greatest. If several nodes share that greatest score, return the smallest node index among them.

### Function Contract

**Inputs**

- `edges`: An integer array of length $n$, where $2 \le n \le 10^5$, $0 \le \texttt{edges[i]} < n$, and `edges[i] != i`.

**Return value**

- Return the index of the node with the greatest edge score, breaking ties in favor of the smallest index.

**Graph semantics**

- Every array position is a source-node label and contributes that label to exactly one target's score.
- A node may have any number of incoming edges, including none.
- The score is a sum of source labels, not the number of incoming edges.

### Examples

**Example 1**

- Input: `edges = [1,0,0,0,0,7,7,5]`
- Output: `7`
- Explanation: Node `0` has score $1+2+3+4=10$, while node `7` has score $5+6=11$, which is greatest.

**Example 2**

- Input: `edges = [2,0,0,2]`
- Output: `0`
- Explanation: Nodes `0` and `2` both have score $3$, so the smaller index `0` is returned.
