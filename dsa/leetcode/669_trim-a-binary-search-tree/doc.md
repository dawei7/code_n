# Trim a Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 669 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/trim-a-binary-search-tree/) |

## Problem Description
### Goal
Given the root of a binary search tree and boundaries `low` and `high`, trim the tree so that every remaining node value lies in the inclusive range `[low, high]`.

Trimming must preserve the relative structure of all retained nodes: a node that was a descendant of another retained node must remain its descendant after out-of-range nodes are removed. Return the root of the uniquely determined trimmed binary search tree. The original root may be removed, so the returned root can differ from the input root or be null.

### Function Contract
**Inputs**

- `root`: the root of a binary search tree with distinct values
- `low`: the inclusive lower value bound
- `high`: the inclusive upper value bound, with `low <= high`

**Return value**

- The root of the tree containing exactly the original nodes whose values are between `low` and `high`, with their valid BST relationships preserved

### Examples
**Example 1**

- Input: `root = [1,0,2], low = 1, high = 2`
- Output: `[1,null,2]`

**Example 2**

- Input: `root = [3,0,4,null,2,null,null,1], low = 1, high = 3`
- Output: `[3,2,null,1]`

**Example 3**

- Input: `root = [2,1,3], low = 2, high = 2`
- Output: `[2]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(H)$

<details>
<summary>Approach</summary>

#### General

**Use the search-tree ordering to discard whole sides**

If a node value is below `low`, its left subtree is also below `low`; none of those nodes can survive. The trimmed result for that entire subtree is therefore obtained by trimming only the node's right child. Symmetrically, when a node value is above `high`, its right subtree can be discarded and only its left child can contain retained values.

**Reconnect both children of an in-range node**

A node within the interval must remain. Recursively trim its left and right subtrees, then replace its child pointers with the returned roots. Each returned subtree contains exactly the valid descendants from that original side, so these assignments bypass removed boundary nodes without disturbing the ordering among retained nodes.

**Why the returned tree has exactly the required structure**

Each recursive call handles one of three exhaustive value positions. An out-of-range node returns the only side that could still contain valid values; an in-range node retains itself and attaches the correctly trimmed results of both children. Induction over subtree height therefore shows that every returned subtree contains all and only its in-range original nodes. Because every surviving child remains on its original BST side, the relative ancestor structure and search-tree ordering are preserved.

#### Complexity detail

Every visited node is processed once, and discarded subtrees need not be traversed after the BST ordering proves that all their values are invalid. The worst case still visits all `N` nodes, so time is $O(N)$. Recursive calls occupy one frame per level, using $O(H)$ auxiliary space for tree height `H`; this is $O(\log N)$ for a balanced tree and $O(N)$ for a skewed tree.

#### Alternatives and edge cases

- **Iterative boundary repair:** move the root into range, then repair invalid left and right boundary chains with pointers; it also runs in $O(N)$ time and $O(1)$ auxiliary space, but its asymmetric pointer logic is easier to get wrong.
- **Filter preorder values and rebuild a BST:** can reproduce the retained structure when insertion follows the original preorder, but ordinary insertion can take $O(N^2)$ time on a skewed tree and allocates a new tree.
- **Inorder collection followed by balanced rebuilding:** returns a valid BST with the right values, but changes the required relative structure and is therefore not semantically equivalent.
- Bounds are inclusive, so nodes equal to `low` or `high` remain.
- If the original root is outside the interval, a descendant can become the new root.
- A one-node tree is returned unchanged when its value is in range.

</details>
