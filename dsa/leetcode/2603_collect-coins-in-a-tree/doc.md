# Collect Coins in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2603 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Tree, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/collect-coins-in-a-tree/) |

## Problem Description

### Goal

An undirected, unrooted tree has $n$ vertices numbered from $0$ through $n-1$. Each pair `edges[i] = [a_i, b_i]` connects two adjacent vertices, and `coins[i]` is $1$ exactly when vertex $i$ contains a coin.

Choose any vertex as the starting point. From the current vertex, you may collect every coin whose tree distance from it is at most $2$, or traverse one edge to an adjacent vertex. Both operations may be performed any number of times.

Find the minimum total number of edge traversals needed to collect every coin and return to the chosen starting vertex. Traversing the same edge more than once contributes once to the total on every traversal.

### Function Contract

**Inputs**

- `coins`: A length-$n$ list whose entries are either $0$ or $1$.
- `edges`: A list of $n-1$ pairs describing a valid undirected tree on vertices $0$ through $n-1$.

The tree size satisfies $1 \leq n \leq 3 \cdot 10^4$.

**Return value**

- The minimum number of edge traversals required to collect all coins and finish at the starting vertex.

### Examples

**Example 1**

- Input: `coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]`
- Output: `2`

Start at vertex $2$, collect the coin at vertex $0$, traverse to vertex $3$, collect the coin at vertex $5$, and return to vertex $2$.

**Example 2**

- Input: `coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]`
- Output: `2`

Starting at vertex $0$, the two coins in its nearby branch can be collected immediately. One round trip across edge $0$-$2$ brings the remaining coin within distance $2$.
