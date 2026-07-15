# Leaf-Similar Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 872 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/leaf-similar-trees/) |

## Problem Description
### Goal
Read the leaves of a binary tree from left to right. Their values, in that order, form the tree's leaf value sequence. For example, a tree whose leaves are encountered with values `6`, `7`, `4`, `9`, and `8` has leaf value sequence `[6,7,4,9,8]`; values stored at internal nodes do not appear in the sequence.

Two binary trees are leaf-similar exactly when their leaf value sequences are identical. Given the head nodes `root1` and `root2`, return `true` if and only if the two trees are leaf-similar.

### Function Contract
**Inputs**

- `root1`: the root of the first nonempty binary tree.
- `root2`: the root of the second nonempty binary tree.
- Each tree contains between $1$ and $200$ nodes, and every node value is between $0$ and $200$.
- Let $n_1$ and $n_2$ be the numbers of nodes in the first and second trees, and let $h_1$ and $h_2$ be their respective heights.

**Return value**

Return `true` when the two left-to-right leaf value sequences contain the same values in the same order; otherwise, return `false`.

### Examples
**Example 1**

- Input: `root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]`
- Output: `true`

Both trees have leaf value sequence `[6,7,4,9,8]`.

**Example 2**

- Input: `root1 = [1,2,3], root2 = [1,3,2]`
- Output: `false`

The first sequence is `[2,3]`, while the second is `[3,2]`.

**Example 3**

- Input: `root1 = [1,2,3], root2 = [7,8,3,2]`
- Output: `true`

The tree shapes and internal values differ, but both leaf sequences are `[2,3]`.

### Required Complexity
- **Time:** $O(n_1+n_2)$
- **Space:** $O(h_1+h_2)$

<details>
<summary>Approach</summary>

#### General

**Generate leaves in their structural order**

Perform a depth-first traversal of each tree that always explores the left child before the right child. A node is a leaf only when both of its children are absent; yield its value at that moment and ignore the values of internal nodes. An explicit stack can preserve the required order by pushing the right child before the left child.

**Compare the two streams without storing either sequence**

Advance the two leaf generators together. Corresponding yielded values must be equal, and the generators must finish at the same time. A private sentinel supplied to a zip-with-padding operation distinguishes exhaustion from every legal node value, including `0`.

Every leaf is emitted in left-to-right order because depth-first traversal completely visits a node's left subtree before its right subtree. Therefore each generator produces exactly its tree's leaf value sequence. Pairwise equality plus simultaneous exhaustion is precisely the definition of leaf similarity, so the returned result is correct.

#### Complexity detail

Each node of both trees is pushed and removed once, so the total time is $O(n_1+n_2)$. Each traversal stack holds at most a root-to-leaf frontier, requiring $O(h_1)$ and $O(h_2)$ space respectively; the two lazy generators therefore use $O(h_1+h_2)$ auxiliary space.

#### Alternatives and edge cases

- **Materialize both sequences:** Collecting two leaf arrays and comparing them is simple and still uses linear time, but it requires $O(n_1+n_2)$ space instead of space proportional to tree height.
- **Recursive depth-first search:** Recursion yields leaves naturally in left-to-right order, with the same asymptotic bounds, but a highly skewed tree consumes one call-stack frame per level.
- **Compare node-by-node traversals:** Internal structure and values are irrelevant, so ordinary preorder or inorder sequences can disagree even when the leaves match.
- **Single-node trees:** The root is also the only leaf, so the answer depends solely on the two root values.
- **Equal prefix with different lengths:** Matching yielded values are insufficient if one tree has an additional leaf; simultaneous exhaustion is required.
- **Repeated and zero values:** Values are compared by position, and the exhaustion sentinel must not collide with any valid value.

</details>
