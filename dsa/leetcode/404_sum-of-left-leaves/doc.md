# Sum of Left Leaves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 404 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-left-leaves/) |

## Problem Description
### Goal
Given the root of a binary tree, identify leaves that are reached through the left-child pointer of their parent. A leaf must have neither a left nor a right child; an internal left child does not contribute merely because of its position.

Return the sum of all such left-leaf values. Negative values subtract normally, and leaves in different branches are counted independently. The root itself has no parent and is therefore not a left leaf when it is the tree's only node. A tree with no qualifying left leaves returns `0`.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, or `None`

**Return value**

- Return the sum of values from nodes that have no children and are reached through a parent's left edge.

### Examples
**Example 1**

- Input: `root = [3,9,20,null,null,15,7]`
- Output: `24`

**Example 2**

- Input: `root = [1]`
- Output: `0`

**Example 3**

- Input: `root = [1,2,3,4,5]`
- Output: `4`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Carry edge direction with each traversal entry**

Use a stack of pairs `(node, is_left)`. The Boolean records whether the node was reached from its parent's left pointer, information that cannot be inferred from the node value or shape alone. The root starts with `False` because it has no parent.

**Test leaf status before expanding children**

A node is a leaf only when both child pointers are absent. If it is also marked left, add its value. Otherwise push its right child with `False` and its left child with `True`, omitting absent children.

**Why each qualifying value is counted exactly once**

Every non-root node is pushed once from its unique parent with the exact direction of that edge. The leaf test accepts precisely childless nodes, and the direction flag filters those on left edges. Since a tree node has one parent and traversal visits it once, no left leaf is missed or duplicated.

#### Complexity detail

Every one of the `n` nodes is processed once, giving $O(n)$ time. The traversal stack holds at most $O(h)$ nodes for tree height `h` in a depth-first traversal, which is $O(n)$ in the worst-case skewed tree.

#### Alternatives and edge cases

- **Recursive depth-first search:** passes an `is_left` flag through calls with the same $O(n)$ time and $O(h)$ call-stack space.
- **Breadth-first search:** can inspect each node's left child directly, using $O(w)$ queue space for maximum tree width `w`.
- **Search from the root for each leaf's parent:** is correct but may revisit the tree and take $O(n^2)$ time.
- An empty tree has sum zero.
- The root is not a left leaf even when it has no children.
- A left child with descendants is not a leaf.
- Negative left-leaf values contribute their signed values.

</details>
