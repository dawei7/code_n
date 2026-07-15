# All Nodes Distance K in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 863 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, a target node in that tree, and a nonnegative integer `k`, find every node whose distance from the target is exactly `k`. The distance between two nodes is the number of edges on their unique connecting path, which may travel through children, through parents, or in both directions.

Return the values of all qualifying nodes in any order. Every node value is unique, so the serialized target value identifies exactly one node. The target is guaranteed to belong to the tree; if no node is far enough away, return an empty array.

### Function Contract
**Inputs**

- `root`: the root of a non-empty binary tree containing $n$ nodes, where $1 \leq n \leq 500$.
- `target`: the target node. Authored app cases identify it by its unique value; the native LeetCode entrypoint receives the corresponding `TreeNode` object.
- `k`: the required edge distance, where $0 \leq k \leq 1000$.

Every node value is unique and lies in $[0,500]$.

**Return value**

Return an array containing the values of exactly the nodes at distance `k` from `target`. The values may appear in any order.

### Examples
**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2`
- Output: `[7,4,1]`

The nodes with values `7` and `4` are two edges below the target, while `1` is reached through the target's parent.

**Example 2**

- Input: `root = [1], target = 1, k = 3`
- Output: `[]`

**Example 3**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 0`
- Output: `[5]`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Expose the missing parent edges**

A binary-tree node directly references only its children, but a shortest path from the target may need to move upward. Traverse the entire tree once and record each node's parent. During the app-local traversal, also locate the node whose unique value equals the serialized `target`; the native artifact already receives that node object.

After this pass, treat every node as a vertex with up to three neighbors: `left`, `right`, and its recorded parent. These undirected connections represent exactly the legal one-edge steps in the original tree.

**Expand breadth-first from the target**

Begin a breadth-first search with only the target in layer zero. For each layer, add every unvisited child or parent to the next layer. A visited set prevents immediately walking back across an edge and ensures each node enters at most once.

Breadth-first layers are defined by shortest-path length: the initial layer is at distance zero, and every expansion adds one edge. Because a tree has one unique path between any pair of nodes, all nodes first reached in layer `d` are exactly distance $d$ from the target. After `k` expansions, return the values in the current layer. If the frontier becomes empty sooner, no qualifying nodes exist.

#### Complexity detail

Building parent links visits all $n$ nodes once. The breadth-first search also visits each node at most once and inspects at most three neighbors per node, so total time is $O(n)$. The parent map, visited set, traversal stack, and breadth-first frontiers together use $O(n)$ space.

#### Alternatives and edge cases

- **Rebuild a full adjacency matrix:** It supports breadth-first search but spends $O(n^2)$ time and space discovering edges that the tree already exposes.
- **Run a fresh root search for every candidate node:** Computing each candidate's path to the target separately is correct but can take $O(n^2)$ total time.
- **Recursive distance propagation:** A depth-first solution can return distances while collecting opposite subtrees, but its control flow and boundary calculations are more intricate.
- **Distance zero:** The answer contains only the target value.
- **`k` exceeds the tree diameter:** The frontier becomes empty and the result is `[]`.
- **Target is the root:** There is no parent neighbor, but downward breadth-first layers work unchanged.
- **Target is a leaf:** Parent edges allow the search to reach siblings, ancestors, and other branches.
- **Output order:** Any permutation of the qualifying unique values is valid.

</details>
