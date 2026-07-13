# Verify Preorder Sequence in Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 255 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Tree, Binary Search Tree, Recursion, Monotonic Stack, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/) |

## Problem Description
### Goal
Given an array of distinct integers, decide whether it could be the preorder traversal of some binary search tree. Preorder visits a root before all nodes in its left subtree and then all nodes in its right subtree, while binary-search ordering places smaller values left and larger values right.

Return `True` when one valid tree structure can produce the entire sequence and `False` otherwise. Every array value must be used exactly once in the proposed tree; a later value cannot return to a completed left-side range after traversal has entered a right subtree. Meet the required linear-time and constant-extra-space target for verification.

### Function Contract
**Inputs**

- `preorder`: distinct node values in proposed root-left-right order

**Return value**

`True` exactly when some binary search tree has that preorder traversal.

### Examples
**Example 1**

- Input: `preorder = [5,2,1,3,6]`
- Output: `true`

**Example 2**

- Input: `preorder = [5,2,6,1,3]`
- Output: `false`

**Example 3**

- Input: `preorder = [1,2,3]`
- Output: `true`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**The stack represents unfinished ancestor paths**

Keep a monotonic stack of ancestors whose right subtrees have not been closed. When a value exceeds the stack top, pop ancestors until locating the subtree that now owns the value; the last popped value becomes a strict lower bound.

The stack is decreasing and represents the active root-to-current path. Every future value must exceed `lower_bound`, because preorder has already entered the right subtree of that ancestor.

**Entering a right subtree creates a permanent lower bound**

Whenever a value exceeds an ancestor on the stack, preorder has finished that ancestor's left side and entered its right subtree. The last popped ancestor becomes a lower bound for every later value until an even higher transition replaces it. A value below that bound would violate BST ordering and must be rejected. Otherwise, popping exactly the smaller ancestors identifies the valid active path, and pushing the value preserves the representation.

#### Complexity detail

Each value is pushed once and popped at most once, giving $O(n)$ time. The stack holds at most `n` values.

#### Alternatives and edge cases

- **Recursively partition each range:** mirrors the tree definition but repeatedly scans skewed ranges and can take $O(n^2)$.
- Empty, singleton, increasing, and decreasing sequences are valid; distinctness removes equality handling.

</details>
