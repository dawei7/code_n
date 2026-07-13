# Diameter of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 543 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, a path may connect any two nodes by following parent-child edges without visiting an edge or node twice. The path may lie within one subtree and does not have to pass through the root.

Return the tree's diameter, defined as the greatest number of edges on any such path. A one-node tree has diameter zero because its longest path contains no edge, while an empty tree also yields zero under the app contract. Return only the edge count, not the endpoint nodes or the number of nodes on the path.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

- An integer equal to the maximum number of edges on any path between two nodes

### Examples
**Example 1**

- Input tree: `[1, 2, 3, 4, 5]`
- Output: `3`

**Example 2**

- Input tree: `[1, 2]`
- Output: `1`

**Example 3**

- Input tree: `[1]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Connect diameter to subtree heights**

For any node, the longest path whose highest point is that node descends through the deepest node in its left subtree and the deepest node in its right subtree. If those subtree heights are measured in nodes, that path contains `left_height + right_height` edges. A missing child contributes height zero.

**Compute children before their parent**

A postorder traversal first obtains both child heights. It can then update the best diameter with their sum and return `1 + max(left_height, right_height)` as the current subtree's height. One traversal therefore supplies both pieces of information without recalculating a subtree.

**Keep only one root-to-current path**

An explicit stack frame stores a node, which child should be visited next, and the two returned child heights. When a frame finishes, its height is written into its parent frame. This simulates recursive postorder while avoiding recursion-depth failures on a highly skewed tree.

**Why considering every node finds the global path**

Every simple path in a tree has a unique highest node: the first common ancestor of its endpoints. At that node, the path uses at most the deepest available branch on each side, so its length is no greater than the candidate formed from the two child heights. Conversely, each recorded candidate is itself a valid path. Taking the maximum candidate over all nodes is therefore exactly the tree's diameter.

#### Complexity detail

Each of the `n` nodes is pushed and removed once and does constant work, so the traversal takes $O(n)$ time. The stack contains at most one frame per level, giving $O(h)$ auxiliary space for tree height `h`.

#### Alternatives and edge cases

- **Recursive postorder:** expresses the same height recurrence compactly with $O(n)$ time and $O(h)$ call-stack space, but a long chain may exceed the language's recursion limit.
- **Recompute height at every node:** produces the right diameter but revisits descendants and degrades to $O(n^2)$ time on a skewed tree.
- **Build an undirected graph:** two graph searches can find the diameter in linear time, but storing every adjacency list costs $O(n)$ additional space.
- **Single node:** has diameter zero because a path containing one node has no edges.
- **Empty tree:** returns zero defensively even though the platform contract supplies at least one node.
- **Diameter below the root:** every node contributes a candidate, so the maximum is not restricted to paths through the root.
- **Node values:** do not affect the answer; only the tree's shape matters.

</details>
