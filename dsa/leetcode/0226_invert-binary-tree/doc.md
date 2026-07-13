# Invert Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 226 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/invert-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, invert its structure to form a mirror image. At every existing node, the original left subtree must become the right subtree and the original right subtree must become the left subtree, with the same transformation applied recursively throughout both branches.

Return the root of the inverted tree, reusing the original node values and preserving every node exactly once. Missing children swap positions just like present subtrees. An empty tree returns `null`, and a single-node tree remains structurally unchanged. The operation changes child links rather than merely reversing values within each level.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

The root of the inverted binary tree.

### Examples
**Example 1**

- Input: `[4,2,7,1,3,6,9]`
- Output: `[4,7,2,9,6,3,1]`

**Example 2**

- Input: `[2,1,3]`
- Output: `[2,3,1]`

**Example 3**

- Input: `[]`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Visit every structural decision once**

Begin an explicit depth-first traversal with the root. Whenever a node is removed from the stack, exchange its left and right references, then schedule the children that now occupy those positions.

The traversal order is irrelevant: a node's local swap does not depend on whether its parent, children, or nodes on another branch were processed first.

**Local swaps compose into the global mirror**

After a node is processed, its two outgoing edges have their final mirrored orientation. Both original subtrees are still reachable—the swap changes only which side points to each one—and every reachable child is scheduled exactly once.

Applying this local transformation at every node exchanges the left and right subtrees recursively throughout the entire tree. The returned root therefore heads the complete mirror image.

#### Complexity detail

Every node is processed once for $O(n)$ time. The explicit stack can hold $O(n)$ nodes in the worst case.

#### Alternatives and edge cases

- **Recursive DFS:** is concise but uses call-stack depth.
- **Level-order queue:** has the same bounds.
- **Swap values only:** does not invert structure.
- Empty and single-node trees are unchanged. An absent child is simply swapped to the other side, so asymmetric trees need no special branch.

</details>
