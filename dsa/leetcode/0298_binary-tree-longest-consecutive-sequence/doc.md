# Binary Tree Longest Consecutive Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 298 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) |

## Problem Description
### Goal
Given a binary tree, find a downward path in which each next node is a direct child of the previous node and has value exactly one greater. The path may begin at any node and then follow either left or right child choices, but it cannot move upward or skip levels.

Return the maximum number of nodes in any valid path. A single node is a length-one consecutive path, repeated or decreasing values break the current sequence, and a later descendant may start a new one. Return `0` for an empty tree. The function reports only the length, not the node values or path itself.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

The number of nodes in the longest valid downward consecutive path, or zero for an empty tree.

### Examples
**Example 1**

- Input: `root = [1,null,3,2,4,null,null,null,5]`
- Output: `3`

**Example 2**

- Input: `root = [2,null,3,2,null,1]`
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

**Carry the only history a child needs**

Whether a path continues at a node depends only on its parent's value and the valid length ending at that parent. During depth-first traversal, carry those two pieces of state. If `node.val == parent_value + 1`, extend the length; otherwise start a new path of length one at the node.

Every node may be the endpoint of the global answer, so update a running maximum after computing its local length. Then pass the new value and length to both children. An explicit stack avoids recursion-depth limits while holding at most a traversal frontier.

**Direction and adjacency are strict**

The path must move from parent to child; a child with value one less does not form a reverse sequence. Values also cannot skip: `3 -> 5` resets even though it is increasing. Branches are evaluated independently, because a path cannot travel up from one child and down into its sibling.

For `[3,2,4,1,null,null,5]`, the left edges decrease and reset. The right branch follows `3 -> 4 -> 5`, so the answer is three.

**Why one traversal finds every candidate**

At each node, the carried length is exactly the longest valid consecutive path ending there: there is only one parent, so it either extends that unique incoming path or begins anew. Taking the maximum of these endpoint lengths considers every possible downward path, since every such path has a final node.

#### Complexity detail

Each of the `n` nodes is pushed, examined, and popped once, giving $O(n)$ time. The traversal stack uses $O(h)$ space on a skewed depth-first traversal when children are processed in depth order; in the iterative implementation it is bounded by the number of pending nodes and is $O(n)$ in the worst shape.

#### Alternatives and edge cases

- **Start a fresh search from every node:** is correct but revisits long descendant paths and can take $O(n^2)$ on a chain.
- **Inorder or sorted values:** lose parent-child adjacency and cannot establish a valid path.
- An empty tree returns zero. Duplicate, decreasing, or skipped values reset the current length to one.

</details>
