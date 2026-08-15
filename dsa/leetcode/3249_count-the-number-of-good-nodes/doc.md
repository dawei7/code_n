# Count the Number of Good Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3249 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-good-nodes/) |

## Problem Description

### Goal

An undirected tree has $n$ nodes labeled from $0$ through $n-1$ and is rooted at node $0$. Each pair `[a, b]` in `edges` connects nodes `a` and `b`.

Rooting the tree gives every non-root node one parent and makes its other adjacent nodes its children. The subtree rooted at a child contains that child and all of its descendants. A node is *good* when every one of its child subtrees has the same number of nodes. Leaves and nodes with only one child satisfy this condition because they have no unequal pair of child-subtree sizes.

Return the total number of good nodes in the tree.

### Function Contract

**Inputs**

- `edges`: The $n-1$ undirected edges of a valid tree on nodes $0$ through $n-1$, where $2 \le n \le 10^5$.

Each edge contains exactly two valid node labels. The tree is connected and contains no cycle.

**Return value**

- The number of nodes whose child subtrees all have equal size after the tree is rooted at node $0$.

### Examples

#### Example 1

- **Input:** `edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]`
- **Output:** `7`

Every internal node has equally sized child subtrees, so all seven nodes are good.

#### Example 2

- **Input:** `edges = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]`
- **Output:** `6`

#### Example 3

- **Input:** `edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]`
- **Output:** `12`

Only node `9` has child subtrees of different sizes.
