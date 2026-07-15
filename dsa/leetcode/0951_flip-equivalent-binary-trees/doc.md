# Flip Equivalent Binary Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 951 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/flip-equivalent-binary-trees/) |

## Problem Description

### Goal

A flip operation on a binary tree chooses any node and swaps its entire left and right child subtrees. Any number of nodes, including none, may be flipped.

Two binary trees are flip equivalent exactly when some sequence of these operations can make their node values and structure identical. Flipping changes only the ordering of child subtrees; it never changes a node value, creates a node, or removes one. Given `root1` and `root2`, determine whether they are flip equivalent and return the corresponding boolean result.

### Function Contract

Let $n$ be the total number of nodes across both trees, and let $h$ be the greater tree height.

**Inputs**

- `root1`: the root of a binary tree, or `None`.
- `root2`: the root of a binary tree, or `None`.
- Each tree has from $0$ through $100$ nodes, with unique values within that tree from $0$ through $99$.

**Return value**

Return `true` if flips can make the trees identical; otherwise return `false`.

### Examples

**Example 1**

- Input: `root1 = [1, 2, 3, 4, 5, 6, null, null, null, 7, 8]`, `root2 = [1, 3, 2, null, 6, 4, 5, null, null, null, null, 8, 7]`
- Output: `true`

Flips at nodes with values `1`, `3`, and `5` make the trees identical.

**Example 2**

- Input: `root1 = []`, `root2 = []`
- Output: `true`

**Example 3**

- Input: `root1 = []`, `root2 = [1]`
- Output: `false`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Match one pair of roots at a time.** Two missing nodes match. If exactly one node is missing, or their values differ, the subtrees cannot be flip equivalent. Otherwise their roots already agree, and only their children remain to be matched.

**Try the two meanings of a flip.** The subtrees match if either the left children match and the right children match without flipping, or the first left child matches the second right child and the first right child matches the second left child after a flip. Apply this rule recursively.

The base cases exactly characterize empty and unequal roots. For equal roots, every valid transformation either flips that root or does not; the two recursive alternatives cover those exhaustive choices. By induction on subtree size, a branch returns `true` exactly when its paired subtrees are flip equivalent. Unique values cause an incorrectly paired child root to fail immediately, so nodes are not repeatedly explored.

#### Complexity detail

Across successful and failed orientations, unique node values let the recursion examine $O(n)$ nodes. The call stack follows at most one root-to-leaf path at a time and uses $O(h)$ space.

#### Alternatives and edge cases

- **Canonical subtree serialization:** Recursively canonicalize the two child strings into a fixed order and compare the root serializations. It is correct, but repeated immutable-string concatenation can take $O(n^2)$ time on a skewed tree.
- **Repeated value lookup:** With unique values, find each matching node in the other tree and compare its unordered pair of child values. Repeating a full tree search for every node is correct but takes $O(n^2)$ time.
- **Canonical child ordering by root value:** With unique values, treat a missing child as a sentinel and compare smaller-root children together. This also yields a linear recursive test but relies directly on the uniqueness guarantee.
- **Breadth-first paired states:** A queue can process corresponding subtree pairs iteratively, though it still must choose flipped or unflipped child alignment.
- **Both trees empty:** They are flip equivalent without any operation.
- **Only one tree empty:** No flip can create or remove a node.
- **Different root values:** Flips change child positions only, never node values.
- **One child:** A flip may move that child from left to right or conversely.

</details>
