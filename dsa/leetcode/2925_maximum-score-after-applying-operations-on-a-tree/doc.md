# Maximum Score After Applying Operations on a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2925 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/) |

## Problem Description

### Goal

An undirected tree with $n$ nodes is rooted at node 0. Node $i$ initially has
the positive integer `values[i]`. In one operation, choose a node, add its
current value to the score, and replace that node's value with zero. Any number
of nodes may be chosen, and each can contribute only its original value once.

After the operations, the tree must remain healthy: the sum of the remaining
values along every root-to-leaf path must be nonzero. Return the greatest score
obtainable while preserving that condition.

### Function Contract

**Inputs**

- `edges`: The $n-1$ undirected edges of the tree.
- `values`: The positive initial value of each corresponding node.

Let $n=\lvert\texttt{values}\rvert$. The constraints are
$2\le n\le20{,}000$, $\lvert\texttt{edges}\rvert=n-1$, and
$1\le\texttt{values[i]}\le10^9$. The edges form a valid tree rooted at
node 0 for path interpretation.

**Return value**

- The maximum score from selected nodes while every root-to-leaf path retains
  a positive sum.

### Examples

#### Example 1

- **Input:** `edges = [[0, 1], [0, 2], [0, 3], [2, 4], [4, 5]], values = [5, 2, 5, 2, 1, 1]`
- **Output:** `11`
- **Explanation:** Keep the root value and select nodes 1 through 5. Every
  root-to-leaf path remains positive because it contains the root.

#### Example 2

- **Input:** `edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], values = [20, 10, 9, 7, 4, 3, 5]`
- **Output:** `40`
- **Explanation:** Selecting nodes 0, 2, 3, and 4 leaves positive value on every
  path and earns 40.
