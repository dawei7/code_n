# Height of Binary Tree After Subtree Removal Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2458 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/) |

## Problem Description

### Goal

You are given the root of a binary tree containing $n$ nodes. Every node has a distinct value from $1$ through $n$. An array `queries` specifies node values, and no query names the root.

For each query independently, remove the entire subtree rooted at the node whose value equals that query. Measure the remaining tree's height as the number of edges in the longest simple path from the original root to any remaining node. Restore the original tree before processing the next query, and return the resulting heights in query order.

### Function Contract

**Inputs**

- `root`: The root of a non-empty binary tree whose node values are unique.
- `queries`: A list of values other than the root's value, identifying subtrees to remove independently.

Let $n$ be the number of nodes and $m=\lvert\texttt{queries}\rvert$. The constraints are $2\le n\le10^5$ and $1\le m\le\min(n,10^4)$. Every node and query value lies between $1$ and $n$.

**Return value**

- A list of $m$ integers, where position $i$ is the remaining tree height after removing the subtree rooted at `queries[i]`.

### Examples

#### Example 1

- **Input:** `root = [1, 3, 4, 2, null, 6, 5, null, null, null, null, null, 7], queries = [4]`
- **Output:** `[2]`
- **Explanation:** Removing node `4` and its descendants leaves the path `1 -> 3 -> 2`, which has two edges.

#### Example 2

- **Input:** `root = [5, 8, 9, 2, 1, 3, 7, 4, 6], queries = [3, 2, 4, 8]`
- **Output:** `[3, 2, 3, 2]`
- **Explanation:** Each removal starts from the original tree; earlier queries do not alter later ones.
