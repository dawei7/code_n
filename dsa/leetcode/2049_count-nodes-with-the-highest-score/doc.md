# Count Nodes With the Highest Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2049 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-nodes-with-the-highest-score/) |

## Problem Description

### Goal

A binary tree contains $n$ nodes labeled from $0$ through $n-1$ and is rooted at node $0$. The array `parents` encodes its edges: `parents[i]` gives the parent of node `i`, while `parents[0]` is `-1`.

To score a node, remove that node and every edge incident to it. The remaining nodes separate into one or more non-empty connected subtrees. Multiply the sizes of all those components to obtain the removed node's score. Determine the maximum score achieved anywhere in the tree and return how many nodes attain that same maximum.

### Function Contract

**Inputs**

- `parents`: an integer array of length $n$, where $2 \le n \le 10^5$, `parents[0] = -1`, and every later entry is a valid node index.
- `parents` describes a valid rooted binary tree, so each node has at most two children.

**Return value**

- Return the number of nodes whose removal produces the largest component-size product.

### Examples

**Example 1**

- Input: `parents = [-1,2,0,2,0]`
- Output: `3`
- Explanation: Nodes `1`, `3`, and `4` each score $4$, which is the maximum.

**Example 2**

- Input: `parents = [-1,2,0]`
- Output: `2`
- Explanation: Removing node `0` or node `1` produces score $2$; node `2` scores $1$.
