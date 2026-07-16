# Diameter of N-Ary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1522 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/diameter-of-n-ary-tree/) |

## Problem Description
### Goal

Given the root of an N-ary tree, find the tree's diameter: the greatest number of edges on a simple path between any two nodes. The longest path may pass through the supplied root, through another internal node, or end at the root.

The source tree contains between 1 and $10^4$ nodes and may have depth up to 1000. Return only the diameter length in edges, not the endpoints or the path itself.

### Function Contract
**Inputs**

Let $n$ be the node count.

- `tree`: The app-local tree as $n$ records `[value, child_values]`. Every non-root value appears in exactly one child list, values are unique, and $1 \leq n \leq 10^4$.
- The equivalent native interface receives the actual N-ary root node, whose `children` list contains child nodes.
- The maximum root-to-leaf depth is 1000.

**Return value**

Return the maximum number of edges on a path between any two nodes. A one-node tree has diameter 0.

### Examples
**Example 1**

- Input: `tree = [[1, [3, 2, 4]], [3, [5, 6]], [2, []], [4, []], [5, []], [6, []]]`
- Output: `3`
- Explanation: A longest path joins node 5 or 6 to node 2 or 4 using three edges.

**Example 2**

- Input: `tree = [[1, [2]], [2, [3, 4]], [3, [5]], [4, []], [5, [6]], [6, []]]`
- Output: `4`
- Explanation: The path from node 6 to node 4 contains four edges.

**Example 3**

- Input: `tree = [[7, []]]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Summarize each subtree by its greatest downward height**

For a node, define its height as the maximum number of edges from that node down to a descendant leaf. Once every child's height is known, the node's height is one plus the largest child height, or zero for a leaf.

Any path whose highest node is the current node uses at most two child branches. Its length is the sum of the two greatest values `child_height + 1`; when fewer than two children exist, the missing branch contributes zero. Taking the maximum of this sum over all nodes considers every possible diameter path, including paths that do not pass through the root.

**Evaluate children before parents without recursion**

First traverse from the root and record nodes in parent-before-child order. Process that list in reverse, so every child height is available before its parent. At each node, retain only the two largest downward candidates rather than sorting all children.

The native Accepted artifact applies this logic to node objects. The app-local adapter infers the root as the only value absent from all child lists and performs the same postorder calculation over value records. An explicit stack avoids recursion failure near the permitted depth of 1000.

#### Complexity detail

The initial traversal and reverse postorder each visit every node and child edge once. Selecting the two largest child branches is constant work per edge, so total time is $O(n)$.

The traversal order, stack, and height map each store at most $n$ entries, giving $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Two graph sweeps:** from any node, find a farthest endpoint, then find the farthest node from that endpoint. This also computes a tree diameter in linear time but requires treating child links as undirected edges.
- **All-pairs searches:** running a traversal from every node is correct but takes $O(n^2)$ time.
- **Recursive height DFS:** concise, but the maximum legal depth is close to Python's default recursion limit.
- **Single node:** no edge exists, so the diameter is zero.
- **Chain:** the diameter is the chain's edge count, $n-1$.
- **Wide star:** the two deepest branches are two leaves, giving diameter 2 when at least two leaves exist.
- **One child:** the second branch is zero, so a root-to-leaf path may be the diameter.
- **Node values:** values do not influence distance; only parent-child structure matters.

</details>
