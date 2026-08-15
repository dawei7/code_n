# Maximum Points After Collecting Coins From All Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2920 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/) |

## Problem Description

### Goal

An undirected tree with $n$ nodes is rooted at node 0. The nodes are labeled
from 0 through $n-1$, `edges` describes its $n-1$ connections, and
`coins[i]` is the initial number of coins at node `i`. Starting from the
root, collect every node's coins; a node may be collected only after all of its
ancestors have been collected.

At each node, choose exactly one of two methods. The first awards the node's
current coin count minus `k`; this score may be negative. The second awards
the floor of half the current coin count and also replaces every coin count in
that node's rooted subtree by its floor after division by two. Multiple second
methods along an ancestor chain compound. Return the maximum total score after
all nodes have been collected.

### Function Contract

**Inputs**

- `edges`: The $n-1$ undirected edges of the tree.
- `coins`: A list whose entry `coins[i]` is node $i$'s initial coin count.
- `k`: The penalty charged by the first collection method.

Let $n=\lvert\texttt{coins}\rvert$. The constraints are
$2\le n\le 10^5$, $0\le\texttt{coins[i]}\le 10^4$,
$\lvert\texttt{edges}\rvert=n-1$, and $0\le\texttt{k}\le10^4$.
The edges form a tree and every endpoint lies in $[0,n-1]$.

**Return value**

- The maximum total points obtainable after collecting every node.

### Examples

#### Example 1

- **Input:** `edges = [[0, 1], [1, 2], [2, 3]], coins = [10, 10, 3, 3], k = 5`
- **Output:** `11`
- **Explanation:** Use the first method at nodes 0 and 1 for five points each.
  Use the second method at node 2 for one point; it halves node 3 to one coin,
  whose second method then yields zero.

#### Example 2

- **Input:** `edges = [[0, 1], [0, 2]], coins = [8, 4, 4], k = 0`
- **Output:** `16`
- **Explanation:** With no penalty, using the first method at all three nodes
  collects their full values.
