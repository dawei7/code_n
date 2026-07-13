# Flatten Binary Tree to Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 114 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Stack, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) |

## Problem Description
### Goal
Given the root of a binary tree, transform that same tree into a linear structure using its existing nodes. The final order must match a preorder traversal of the original structure: visit a node, then its left subtree, then its right subtree.

Perform the transformation in place. Each node's `right` pointer must lead to the next node in preorder, every `left` pointer must be set to `null`, and the final node's `right` pointer must also be `null`. Do not allocate a replacement list or return copied values; callers observe the rewired tree through the original root, with an empty tree remaining unchanged.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

`None`; mutate the `TreeNode` structure in place. The app displays the resulting right-skewed tree.

### Examples
**Example 1**

- Input: `root = [1, 2, 5, 3, 4, null, 6]`
- Output tree: `[1, null, 2, null, 3, null, 4, null, 5, null, 6]`

**Example 2**

- Input: `root = []`
- Output tree: `[]`

**Example 3**

- Input: `root = [0]`
- Output tree: `[0]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Preorder determines where the old right subtree must be spliced**

When the current node has a left child, find the rightmost node of that left subtree—the last node visited within it in preorder. Attach the current right subtree after that predecessor.

**Promote the left subtree and clear the obsolete link**

Set `current.right` to the former left child and clear `current.left`. Then advance along the right pointer, which now follows the next node in preorder.

The old right subtree must be attached to the predecessor before `current.right` is overwritten; otherwise that entire subtree can become unreachable. If no left child exists, no splice is necessary and the existing right child is already the next preorder node.

**The processed prefix is final while the suffix stays reachable**

All nodes before `current` form a finalized right-only preorder prefix with null left pointers. Nodes from `current` onward remain reachable in their required preorder sequence, although later left subtrees may still need promotion.

**Trace a splice that preserves both subtrees**

At root `1` in `[1, 2, 5, 3, 4, null, 6]`, the rightmost node of the left subtree is `4`. Attach subtree `5 -> 6` after `4`, move subtree `2` to the root's right, and continue, producing `1 -> 2 -> 3 -> 4 -> 5 -> 6`.

**Splicing after the left predecessor preserves preorder**

When a node has a left subtree, preorder requires that complete subtree before the old right subtree. The rightmost node of the left subtree is the last node reached before preorder would return to the old right side, so attaching the old right subtree there preserves that boundary.

Moving the left subtree to `right` and clearing `left` makes the next pointer follow preorder directly. Repeating along the new right chain preserves every node and eventually produces the complete node-left-right sequence using only right links.

#### Complexity detail

Each edge is followed only a constant number of times across the sequence of predecessor searches and rightward advances, giving $O(n)$ time. Rewiring uses only node pointers, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Explicit preorder stack:** is straightforward and $O(n)$ time but uses $O(h)$ space.
- **Reverse-preorder recursion:** rewires cleanly but consumes $O(h)$ call-stack space.
- **Create new list nodes:** violates the in-place requirement and discards tree-node identity.
- Empty and one-node trees require no rewiring. Trees already containing only right children remain unchanged.
- Every left pointer must be cleared; merely adding right links would leave a graph rather than the required linked-list shape.

</details>
