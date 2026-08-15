# Most Profitable Path in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2467 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/most-profitable-path-in-a-tree/) |

## Problem Description

### Goal

An undirected tree has $n$ nodes numbered from $0$ through $n-1$ and is rooted at node $0$. Every node has a gate whose even-valued `amount` is either a reward when nonnegative or a price when negative.

Alice begins at node $0$ and chooses a path toward some leaf, while Bob begins at node `bob` and follows the unique path toward node $0$. Each second, both move to the next node on their respective paths. A traveler who reaches an unopened gate receives its reward or pays its price. An already opened gate has no further effect. If Alice and Bob first reach a gate simultaneously, they split its reward or price equally. Alice stops at her chosen leaf, Bob stops at node $0$, and either traveler may stop before the other.

Return the maximum net income Alice can obtain by choosing the best leaf-directed path.

### Function Contract

**Inputs**

- `edges`: The $n-1$ undirected edges of the valid tree, with each entry `[a, b]` joining nodes `a` and `b`.
- `bob`: Bob's starting node, where $1\le\texttt{bob}<n$.
- `amount`: The gate values for nodes $0$ through $n-1$.

The constraints are $2\le n\le10^5$. Every `amount[i]` is even and lies in the inclusive range $[-10^4,10^4]$.

**Return value**

- Alice's maximum possible net income upon reaching a leaf.

### Examples

#### Example 1

- **Input:** `edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]`
- **Output:** `6`
- **Explanation:** Alice pays $2$ at the root, shares the reward at node $1$, gets nothing at node $3$ after Bob opened it, and collects $6$ at leaf $4$.

#### Example 2

- **Input:** `edges = [[0,1]], bob = 1, amount = [-7280,2350]`
- **Output:** `-7280`
- **Explanation:** Alice opens the root gate before Bob arrives, while Bob opens node $1$ before Alice reaches it.
