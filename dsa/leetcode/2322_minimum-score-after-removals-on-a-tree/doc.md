# Minimum Score After Removals on a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2322 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/) |

## Problem Description

### Goal

An undirected connected tree has $n$ nodes labeled from $0$ through $n-1$.
Each node `i` stores the positive integer `nums[i]`, and `edges` lists the
$n-1$ undirected connections. Remove exactly two distinct edges. Because the
original graph is a tree, these removals divide all nodes into exactly three
connected components.

For each component, XOR the values of all nodes that belong to it. The score of
the chosen edge pair is the largest of the three component XORs minus the
smallest. Return the minimum score obtainable over every valid pair of edge
removals. The removed edges may be nested relative to any chosen root or may
lead to two disjoint subtrees.

### Function Contract

**Inputs**

- `nums`: An array of $n$ node values, where $3 \le n \le 1000$ and
  $1 \le \texttt{nums[i]} \le 10^8$.
- `edges`: An array of $n-1$ distinct endpoint pairs. Every endpoint lies in
  $[0,n)$, the two endpoints of an edge differ, and all edges together form a
  valid tree.

**Return value**

The minimum possible difference between the largest and smallest component
XORs after removing exactly two distinct edges.

### Examples

**Example 1**

- Input: `nums = [1,5,5,4,11]`,
  `edges = [[0,1],[1,2],[1,3],[3,4]]`
- Output: `9`
- Explanation: Cutting the edges to nodes `0` and `2` leaves component XORs
  `10`, `1`, and `5`, whose spread is $10-1=9$. No cut pair has a smaller
  spread.

**Example 2**

- Input: `nums = [5,5,2,4,4,2]`,
  `edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]`
- Output: `0`
- Explanation: The tree can be split into components with node values
  `[4,4]`, `[5,5]`, and `[2,2]`. Every component XOR is zero, so the score is
  zero, the smallest possible value.
