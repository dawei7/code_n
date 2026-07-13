# Split BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 776 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Binary Search Tree, Recursion, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-bst/) |

## Problem Description

### Goal

Given the root of a binary search tree with distinct values and an integer `target`, split the tree into two binary search trees. The first must contain every original node whose value is less than or equal to `target`, and the second every node whose value is greater.

Preserve as much of the original parent-descendant structure as the split permits, changing only links needed to separate the value groups. Return the two component roots as `[small, large]`; either root may be null, and `target` does not need to occur in the input tree.

### Function Contract

**Inputs**

- `root`: the root node of a binary search tree with distinct values, represented in cases by level order.
- `target`: the split threshold, which need not occur in the tree.

**Return value**

- A two-element list `[small, large]` of component entry nodes, with all values `<= target` in `small` and all values `> target` in `large`; either entry may be `None`.

### Examples

**Example 1**

- Input: `root = [4,2,6,1,3,5,7]`, `target = 2`
- Output: `[[2,1],[4,3,6,null,null,5,7]]`
- Explanation: Node `3` becomes the left child of `4`, while `2` retains its left subtree.

**Example 2**

- Input: `root = [4,2,6,1,3,5,7]`, `target = 4`
- Output: `[[4,2,null,1,3],[6,5,7]]`
- Explanation: Splitting at the original root detaches its greater right component.

**Example 3**

- Input: `root = [2,1,3]`, `target = 0`
- Output: `[[],[2,1,3]]`
- Explanation: Every value is greater than the target.

### Required Complexity

- **Time:** $O(h)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Follow only the search path for the threshold**

At a node with `node.val <= target`, the node and its entire left subtree belong in the smaller component. Only its right subtree may contain values on both sides, so recursively split that subtree. Attach the returned smaller part back as `node.right`, then return `[node, greater_part]`.

When `node.val > target`, the node and its entire right subtree belong in the greater component. Recursively split only its left subtree, attach the returned greater part as `node.left`, and return `[smaller_part, node]`.

**Why the untouched side is already classified**

The BST ordering guarantees that every left-subtree value is below its node and every right-subtree value is above it. Therefore, each branch can classify one whole subtree without visiting it. The recursive result correctly partitions the only ambiguous child; reconnecting its same-side component preserves all original relative relationships except the one edge that must cross the split. Induction down the search path proves both returned components contain exactly the required nodes and remain BSTs.

#### Complexity detail

The recursion visits one node per level along a single search path, taking $O(h)$ time for tree height `h`. The call stack uses $O(h)$ space; all result nodes are reused rather than copied.

#### Alternatives and edge cases

- **Iterative path rewiring:** Two dummy chains can partition the same search path in $O(h)$ time and constant auxiliary pointer storage.
- **Copy the entire tree before splitting:** It preserves output values and shape but costs $O(n)$ time and space instead of reusing nodes along an $O(h)$ path.
- **Traverse and reinsert every value:** This loses the required relative structure and costs at least $O(n)$ work.
- **Target below every value:** Return an empty smaller component and the original entry as the greater component.
- **Target at or above every value:** Return the original entry as the smaller component and an empty greater component.
- **Missing target:** The ordering comparisons still identify the correct split boundary.
- **Skewed tree:** Height can equal the node count, making the worst case linear.

</details>
