# Merge BSTs to Create Single BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1932 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-bsts-to-create-single-bst/) |

## Problem Description
### Goal
You are given $K$ separate binary search trees in `trees`. Every input tree
contains between one and three nodes, no node has grandchildren, and the root
values are pairwise distinct. Each input tree already satisfies the strict BST
ordering rule.

One merge chooses a leaf of one tree whose value equals the root value of a
different tree, replaces that leaf with the entire matching tree, and removes
the matching tree from the collection. Perform exactly $K-1$ such operations
to combine every input tree. Return the resulting root if the single combined
tree is a valid BST; otherwise return `null`.

In a valid BST, every value in a node's left subtree is strictly smaller than
that node's value, and every value in its right subtree is strictly larger.
A leaf has no children.

### Function Contract
**Inputs**

- `trees`: a list of $K$ valid `TreeNode` BST roots with distinct root values, where
  $1 \le K \le 5\cdot10^4$. Each tree has at most three nodes and no
  grandchildren; every node value is between $1$ and $5\cdot10^4$.

Let $T$ be the total number of nodes supplied across all input trees and let
$H$ be the height of the final tree, if one can be formed.

**Return value**

- A `TreeNode` root of the one valid BST obtainable by consuming all input
  trees, or `null` when no valid complete merge exists.

### Examples
**Example 1**

- Input: `trees = [[2, 1], [3, 2, 5], [5, 4]]`
- Output: `[3, 2, 5, 1, null, 4]`

**Example 2**

- Input: `trees = [[5, 3, 8], [3, 2, 6]]`
- Output: `null`

The only possible graft places `6` in the left subtree of `5`, violating the
strict BST bounds.

**Example 3**

- Input: `trees = [[5, 4], [3]]`
- Output: `null`

### Required Complexity
- **Time:** $O(T)$
- **Space:** $O(K+H)$

<details>
<summary>Approach</summary>

#### General

**Identify the only possible final root**

Record every tree by its root value and collect every value appearing as an
input leaf. Any tree whose root value appears as a leaf must eventually be
grafted into another tree. Therefore the final root must be the unique input
root whose value never appears as a leaf. If there is not exactly one such
root, consuming all trees into one result is impossible.

**Graft while validating global BST bounds**

Traverse from the candidate root while carrying the strict lower and upper
bounds imposed by all ancestors. When the traversal reaches a leaf whose value
matches an unused tree root, replace that leaf's children with the matching
root's children and remove that tree from the root map. Continue through the
newly exposed children using the same bounds.

Checking only each small input tree is insufficient: a graft can satisfy its
parent locally while violating a more distant ancestor. Reject any visited
node whose value is not strictly between its inherited bounds. An iterative
stack avoids recursion-depth failure when many small trees form a long chain.

**Require every tree to participate**

After the traversal, the root map must be empty. The traversal then proves
that every grafted node respects all ancestor bounds, while the empty map
proves that every separate tree was consumed. Conversely, any legal sequence
must start from the unique root absent from the leaf set and must graft a tree
exactly where its root value occurs as a leaf, so the traversal follows every
possible successful merge.

#### Complexity detail

Building the root map and leaf set examines all $T$ supplied nodes. Each tree
root is removed at most once, and each node in the merged result is visited
once, so the total time is $O(T)$. The root map and leaf set use $O(K)$ space.
The iterative traversal stack contains at most $O(H)$ pending nodes, giving
$O(K+H)$ total auxiliary space.

#### Alternatives and edge cases

- **Linear search for every matching root:** Keeping unused roots in a list
  and scanning it whenever a mergeable leaf is reached is correct, but a
  chain of $K$ trees can require $O(K^2)$ time.
- **Merge first, validate afterward:** Performing all apparent value matches
  and then checking the final BST can work, but bounds-aware traversal rejects
  invalid grafts immediately and combines validation with construction.
- A single input tree is returned unchanged because it is already a valid BST
  and requires zero operations.
- A root cycle leaves no candidate final root and must be rejected.
- More than one root absent from the leaf set means the collection has
  disconnected components that cannot all be consumed.
- A repeated leaf value does not permit reusing one input tree twice; any
  remaining duplicate node must still satisfy strict bounds and all roots must
  be consumed exactly once.
- Equality with either inherited bound is invalid because BST ordering is
  strict.

</details>
