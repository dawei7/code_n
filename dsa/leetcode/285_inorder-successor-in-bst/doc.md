# Inorder Successor in BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 285 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/inorder-successor-in-bst/) |

## Problem Description
### Goal
Given a binary search tree with unique values and an existing target node `p`, find the node that appears immediately after `p` in an inorder traversal. Because inorder visits BST values in ascending order, this successor is the smallest stored value strictly greater than `p.val`.

Return the successor node under the native contract, or `null` when `p` is the tree's maximum and no successor exists. The app adapter receives and returns node values while preserving the same meaning. A successor may be the leftmost node of `p`'s right subtree or a higher ancestor; it is not necessarily an immediate child.

### Function Contract
**Inputs**

- `root`: the root of a BST with unique values
- `p`: the target node's value in the offline adapter; the native interface receives the target `TreeNode`

**Return value**

The successor value locally, or `null` when none exists. The native method returns the successor `TreeNode` or `None`.

### Examples
**Example 1**

- Input: `root = [2,1,3], p = 1`
- Output: `2`

**Example 2**

- Input: `root = [5,3,6,2,4,null,null,1], p = 6`
- Output: `null`

**Example 3**

- Input: `root = [5,3,6,2,4], p = 4`
- Output: `5`

### Required Complexity

- **Time:** $O(h)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Greater ancestors are successor candidates**

Whenever the current node is greater than `p`, it is a successor candidate; remember it and continue left for a smaller candidate. Otherwise continue right because neither the current node nor its left subtree can succeed `p`.

`successor` is the smallest visited value greater than `p`. The chosen child is the only remaining subtree that may contain a better candidate.

**Each branch discards values that cannot improve the candidate**

At a value greater than `p`, the node qualifies and everything in its right subtree is even larger, so only its left subtree might contain a better successor. At a value no greater than `p`, neither that node nor its left subtree can qualify, so only the right subtree remains relevant. The remembered minimum is therefore globally optimal when the path ends.

#### Complexity detail

The search visits at most one node per tree level for $O(h)$ time and stores only two node references.

#### Alternatives and edge cases

- **Full inorder traversal:** takes $O(n)$ time and extra traversal storage.
- The maximum node has no successor; a successor may be an ancestor rather than a child.

</details>
