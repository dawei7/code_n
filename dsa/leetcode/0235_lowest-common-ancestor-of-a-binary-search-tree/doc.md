# Lowest Common Ancestor of a Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 235 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) |

## Problem Description
### Goal
Given a binary search tree with unique values and two distinct existing target nodes `p` and `q`, find their lowest common ancestor. A node is an ancestor of itself, and a common ancestor must have both targets within its subtree, including the possibility that it equals one target.

Return the value of the deepest node satisfying that condition. The binary-search ordering may be used to locate where the targets' search paths meet or split. Do not choose a higher ancestor when a descendant already contains both targets, and do not infer ancestry from numeric closeness alone; it comes from the tree structure.

### Function Contract
**Inputs**

- `root`: the root of a binary search tree with distinct values
- `p`: the value of the first target node
- `q`: the value of the second target node

**Return value**

The value of the lowest common ancestor of the two target nodes.

### Examples
**Example 1**

- Input: `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8`
- Output: `6`

**Example 2**

- Input: `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4`
- Output: `2`

**Example 3**

- Input: `root = [2,1], p = 2, q = 1`
- Output: `2`

### Required Complexity

- **Time:** $O(h)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compare both targets with the current split point**

At any node, all left-subtree values are smaller and all right-subtree values are larger. If both targets are smaller, continue left; if both are larger, continue right.

**The first split is the lowest shared ancestor**

The first node where the targets lie on different sides—or where one target equals the current value—is their lowest common ancestor.

Before every iteration, the current subtree contains both targets. Moving to one child is safe only when BST comparisons prove both targets lie in that child.

For targets `2` and `4` under root `6`, both are smaller, so move to `2`. Because `2` equals one target, it is an ancestor of both and is returned. Every skipped ancestor had both targets in one proper child; the first non-skipped node is therefore the lowest node containing both.

#### Complexity detail

The search follows one root-to-node path, taking $O(h)$ time and $O(1)$ iterative space.

#### Alternatives and edge cases

- **General binary-tree LCA:** works but may inspect every node and ignores ordering.
- **Stored root paths:** uses $O(h)$ extra space.
- One target may be an ancestor of the other; target order does not matter.

</details>
