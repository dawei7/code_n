# Maximum Depth of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 104 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, measure how far the tree extends along its longest downward route. A route begins at the root, follows child pointers, and ends at a leaf, which is a node with no children.

Return the maximum number of nodes encountered on any such root-to-leaf route. Depth counts nodes rather than edges, so a tree containing only its root has depth `1`. An empty tree has no route and therefore has maximum depth `0`; an unbalanced branch may determine the answer even when most of the tree is shallow.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

The tree's maximum depth; an empty tree has depth `0`.

### Examples
**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `3`

**Example 2**

- Input: `root = [1, null, 2]`
- Output: `2`

**Example 3**

- Input: `root = []`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Propagate exact root-to-node depth with each stack entry**

If the root is absent, return zero. Otherwise push `(root, 1)`. Each time a pair is popped, update the maximum and push each existing child with `depth + 1`. Carrying depth explicitly avoids recomputing path lengths from parent pointers that tree nodes do not have.

**Explicit depth-first traversal avoids call-stack limits**

An explicit stack handles highly skewed trees without consuming the language call stack. Pushing right before left gives conventional root-left-right processing because the stack is last-in, first-out, but traversal order does not affect the maximum.

**Every pending depth is derived from one valid parent path**

Every pending pair contains the exact number of nodes on the root-to-node path. The stored maximum is the greatest depth among all nodes already processed.

**Trace leaves at different depths**

For `[3, 9, 20, null, null, 15, 7]`, the root establishes depth one, nodes `9` and `20` establish depth two, and children `15` and `7` establish depth three. No deeper node exists, so the answer is `3`.

**Parent-depth propagation labels every root path**

The root receives depth one, and every other node is reached from its unique parent with depth exactly one greater. The stored depth is therefore the number of nodes on that node's root path.

The traversal reaches every node, including every leaf, so the largest assigned value considers every root-to-leaf path. Its maximum is exactly the tree's maximum depth.

#### Complexity detail

Each of the `n` nodes is pushed and popped once, giving $O(n)$ time. A depth-first stack is bounded by $O(h)$ pending path-related nodes, where `h` is maximum depth.

#### Alternatives and edge cases

- **Recursive height formula:** `1 + max(left, right)` is concise and has the same bounds, but deep skew can exceed recursion limits.
- **Breadth-first levels:** also runs in $O(n)$ time but can require $O(w)$ queue space.
- **Count nodes:** cannot determine depth because trees with equal size can have different heights.
- Empty depth is zero and root depth is one, matching the problem's node-count definition rather than an edge-count convention.
- Balanced trees have $h = O(\log n)$; a completely skewed tree has $h = n$.

</details>
