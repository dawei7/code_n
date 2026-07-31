# Find Number of Coins to Place in Tree Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2973 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/) |

## Problem Description
### Goal
An undirected tree has $N$ nodes labeled from `0` through `N - 1` and is rooted
at node `0`. Each edge in `edges` connects its two listed endpoints, and
`cost[i]` assigns a nonzero integer cost to node `i`.

Place coins independently at every node. If a node's rooted subtree contains
fewer than three nodes, place exactly one coin there. Otherwise, choose three
distinct nodes from that subtree and maximize the product of their costs. Place
that maximum product as the coin count, except that a negative maximum is
replaced by zero.

Return the coin count for every node in label order.

### Function Contract
**Inputs**

- `edges`: the `N - 1` undirected edges of the valid tree
- `cost`: the nonzero cost assigned to each node

The contract guarantees $2\le N\le2\cdot10^4$, valid endpoints from `0` to
`N - 1`, and $1\le\lvert\texttt{cost[i]}\rvert\le10^4$.

**Return value**

An array `coin` of length $N$ whose entry `coin[i]` follows the subtree rule
for node `i`.

### Examples
**Example 1**

- Input: `edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]`, `cost = [1,2,3,4,5,6]`
- Output: `[120,1,1,1,1,1]`
- Explanation: The root uses `6 * 5 * 4`; every other subtree is a singleton.

**Example 2**

- Input: `edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]]`, `cost = [1,4,2,3,5,7,8,-4,2]`
- Output: `[280,140,32,1,1,1,1,1,1]`
- Explanation: The best triples in the three nontrivial subtrees produce `280`, `140`, and `32`.

**Example 3**

- Input: `edges = [[0,1],[0,2]]`, `cost = [1,2,-2]`
- Output: `[0,1,1]`
- Explanation: The root's only triple has negative product, while both leaves receive one coin.
