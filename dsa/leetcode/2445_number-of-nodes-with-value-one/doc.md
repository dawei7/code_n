# Number of Nodes With Value One

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2445 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Number of Nodes With Value One](https://leetcode.com/problems/number-of-nodes-with-value-one/) |

## Problem Description

### Goal

An undirected connected tree has nodes labeled 1 through `n`, with node 1 as its root. For every node labeled `v > 1`, its parent is labeled $\lfloor v/2\rfloor$. Initially, every node stores the value 0.

For each label in `queries`, flip the value of that node and every node in its rooted subtree: 0 becomes 1 and 1 becomes 0. Process the queries in order, then return how many nodes finally store 1.

### Function Contract

**Inputs**

- `n`: The number of nodes, with $1 \le n \le 10^5$.
- `queries`: A list of $q$ node labels, where $1 \le q \le 10^5$ and $1 \le \texttt{queries[i]} \le n$.

Node 1 is the root, and node $v>1$ has parent $\lfloor v/2\rfloor$.

**Return value**

- The number of nodes whose value is 1 after every subtree flip.

### Examples

#### Example 1

- **Input:** `n = 5, queries = [1, 2, 5]`
- **Output:** `3`
- **Explanation:** Nodes 1, 3, and 5 finish with value 1.

#### Example 2

- **Input:** `n = 3, queries = [2, 3, 3]`
- **Output:** `1`
- **Explanation:** The two flips at node 3 cancel, leaving only node 2 equal to 1.
