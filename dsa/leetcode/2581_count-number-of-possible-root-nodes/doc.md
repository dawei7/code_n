# Count Number of Possible Root Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2581 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Count Number of Possible Root Nodes](https://leetcode.com/problems/count-number-of-possible-root-nodes/) |

## Problem Description

### Goal

Alice has an undirected tree with $n$ nodes labeled from $0$ through $n-1$. The array `edges` contains its $n-1$ undirected edges.

Bob does not know which node is the root. Each entry `[u, v]` in `guesses` records his claim that, after a root is chosen, `u` is the parent of its adjacent node `v`. Every guess refers to an actual tree edge, and no directed guess is repeated.

Alice reveals only that at least `k` of Bob's guesses are true. Return the number of node labels that could be the root while making at least `k` guesses correct. Return `0` when no node meets that threshold.

### Function Contract

**Inputs**

- `edges`: The $n-1$ undirected edges of a valid tree on nodes $0$ through $n-1$.
- `guesses`: Unique directed pairs `[u, v]`, each asserting that `u` is the parent of adjacent node `v`.
- `k`: The minimum number of guesses that must be true.

The tree has $2 \leq n \leq 10^5$ nodes, `guesses` has between $1$ and $10^5$ entries, and $0 \leq k \leq \lvert\texttt{guesses}\rvert$.

**Return value**

- The number of nodes that can serve as the root while satisfying at least `k` guesses.

### Examples

**Example 1**

- Input: `edges = [[0,1],[1,2],[1,3],[4,2]], guesses = [[1,3],[0,1],[1,0],[2,4]], k = 3`
- Output: `3`
- Explanation: Roots `0`, `1`, and `2` each make three guesses true; the other roots make only two true.

**Example 2**

- Input: `edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1`
- Output: `5`
- Explanation: Every possible root makes at least one of the guesses true.
