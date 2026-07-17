# Find Distance in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1740 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-distance-in-a-binary-tree/) |

## Problem Description

### Goal

You are given the root of a binary tree whose node values are unique, together with two values `p` and `q` that both occur in the tree. The distance between two nodes is the number of edges on the shortest route connecting them.

Return the distance between the node whose value is `p` and the node whose value is `q`. The two values may identify the same node, and neither target is required to be a leaf.

### Function Contract

**Inputs**

- `root`: the root of a nonempty binary tree with unique integer node values.
- `p`: a value present in the tree.
- `q`: another value present in the tree; it may equal `p`.

Let $N$ be the number of nodes in the tree.

**Return value**

- Return the number of tree edges on the unique path between the two target nodes.

### Examples

**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0`
- Output: `3`
- Explanation: The route is `5 -> 3 -> 1 -> 0`.

**Example 2**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7`
- Output: `2`
- Explanation: The route is `5 -> 2 -> 7`.

**Example 3**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5`
- Output: `0`
- Explanation: A node has distance zero from itself.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Record how every node reaches the root**

Traverse the tree once. For each unique node value, store its parent's value and its depth from the root. The root has no parent and depth zero. An explicit stack keeps this traversal safe even when the tree is a long chain.

**Raise the deeper target first**

Start from values `p` and `q`. If one target is deeper, repeatedly replace it with its parent and count each traversed edge until both current nodes have equal depth. Every shortest route between the original targets must include those upward edges because the shallower node cannot occur below its own depth.

**Climb together to the meeting point**

If the equal-depth values differ, move both to their respective parents and add two edges to the distance. Their first shared value is their lowest common ancestor: below it the two ancestor chains are disjoint, while from it upward they coincide. The edges counted before and during this joint climb are therefore exactly the unique path between the targets. When `p == q`, no climb occurs and the result is zero.

#### Complexity detail

The traversal visits all $N$ nodes once, and the two ancestor chains contain at most $N$ edges in total. The time is $O(N)$. Parent and depth maps plus the explicit traversal stack store $O(N)$ entries.

#### Alternatives and edge cases

- **Recursive lowest common ancestor:** Find the common ancestor and target depths with depth-first search; this is also $O(N)$ but a skewed legal tree can exceed Python's recursion limit.
- **Undirected adjacency plus breadth-first search:** Convert every parent-child edge into two graph edges and search from one target. It is correct but stores a larger graph than the parent/depth representation.
- **Repeated parent searches:** Finding each next ancestor by rescanning from the root can degrade to $O(N^2)$ on a chain.
- **Equal targets:** When `p == q`, the unique path has no edges.
- **Ancestor target:** If one target is an ancestor of the other, depth alignment reaches it directly.
- **Targets in opposite root subtrees:** Their meeting point is the root.
- **Single-node tree:** Both target values identify the root and the answer is zero.

</details>
