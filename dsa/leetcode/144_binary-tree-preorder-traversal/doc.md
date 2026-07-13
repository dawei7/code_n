# Binary Tree Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 144 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Stack, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/) |

## Problem Description
### Goal
Given the root of a binary tree, traverse every reachable node in preorder. For each subtree, visit its root first, then completely traverse its left subtree, and finally completely traverse its right subtree.

Return the encountered node values in that exact root-left-right order. Missing children contribute no placeholder values, but their absence still determines which existing branch is left or right. Each node must appear exactly once even when values repeat. An empty tree has no visits and therefore produces an empty list, while a single-node tree produces a one-value list.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order list with `null` placeholders in app cases

**Return value**

A list of node values in root-left-right preorder.

### Examples
**Example 1**

- Input: `root = [1,null,2,3]`
- Output: `[1,2,3]`

**Example 2**

- Input: `root = []`
- Output: `[]`

**Example 3**

- Input: `root = [1,2,3,4,5,null,8]`
- Output: `[1,2,4,5,3,8]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Record a node immediately when its subtree is selected**

If the root exists, push it. Pop the next subtree root, append its value before either child, and schedule existing children for later processing. This explicit stack stores the work that recursive calls would otherwise hold.

**LIFO order requires scheduling the right subtree first**

A stack is last-in, first-out. Push the right child before the left child, leaving the left subtree root on top. All descendants pushed while processing that left subtree likewise remain ahead of the previously stored right subtree, so the entire left side finishes first.

**Stack order is the remaining preorder frontier**

The output contains exactly the already visited preorder prefix. Reading the stack from top to bottom gives the roots of all pending subtrees in the order preorder must process them.

**Trace a node with only a right child and then a left descendant**

For `[1,null,2,3]`, visit `1` and push `2`. Visit `2`, push its left child `3`, then visit `3`, producing `[1,2,3]`.

**Right-before-left pushing recreates preorder stack frames**

Popping a node records it before either child, satisfying preorder's root-first rule. Pushing the right child before the left places the left child on top, so the complete left subtree is processed before the pending right subtree.

Each child is pushed once by its parent and popped once. The explicit stack therefore reproduces the same node-left-right order as recursive preorder while visiting every node exactly once.

#### Complexity detail

Every node is processed once, giving $O(n)$ time. The explicit stack stores at most $O(h)$ pending nodes for a tree of height `h`; the returned list itself contains `n` values.

#### Alternatives and edge cases

- **Recursive DFS:** mirrors the definition but uses $O(h)$ call-stack space and can exceed recursion limits on a deep tree.
- **Morris traversal:** achieves $O(1)$ auxiliary space by temporarily threading the tree, but is more intricate and mutates links during traversal.
- **Breadth-first search:** visits by level, not in preorder.
- An empty tree returns an empty list. Skewed trees still visit every node exactly once, and duplicate values remain as separate output entries.
- Use node identity/structure for traversal; equal values do not imply duplicate nodes.

</details>
