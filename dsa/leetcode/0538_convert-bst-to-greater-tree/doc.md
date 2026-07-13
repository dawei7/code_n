# Convert BST to Greater Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 538 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-bst-to-greater-tree/) |

## Problem Description
### Goal
Given a binary search tree with unique values, transform every node in place. Its new value must equal its original value plus the original values of all nodes whose values are greater.

Return the root of the transformed tree, preserving the existing node structure and child links. All sums are based on original values, so an earlier update must not be counted again as though it were another node. The maximum-valued node remains unchanged, while smaller nodes accumulate an increasingly large suffix of the BST's sorted values.

### Function Contract
**Inputs**

- `root`: the root of a binary search tree

**Return value**

- The root of the tree after every node has been replaced by its greater-or-equal value sum

### Examples
**Example 1**

- Input tree: `[4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]`
- Output tree: `[30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8]`

**Example 2**

- Input tree: `[1, 0, 2]`
- Output tree: `[3, 3, 2]`

**Example 3**

- Input tree: `[0, null, 1]`
- Output tree: `[1, null, 1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Traverse BST values from largest to smallest**

Ordinary inorder visits a BST in increasing order. Reverse the traversal order to right subtree, node, left subtree so every value greater than the current node has already been processed.

**Maintain the sum of all visited originals**

Keep a running total. At each visit, add the node's original value to the total and replace the node value with that total. The traversal then continues left while retaining the accumulated sum.

**Use an explicit reverse-inorder stack**

Push each right chain, pop and update its node, then move into the left child. This performs the same ordering as recursive reverse inorder without depending on the call stack for a highly skewed tree.

**Why every replacement is exact**

When a node with original value `v` is visited, BST ordering guarantees that all previously visited nodes have original values greater than `v`, and no unvisited node does. Adding `v` makes the running total equal the sum of `v` and every greater original value. Assigning that total therefore produces exactly the required replacement for each node.

#### Complexity detail

Every one of the `n` nodes is pushed, popped, and updated once, giving $O(n)$ time. The explicit stack holds at most one root-to-leaf path, so auxiliary space is $O(h)$ for tree height `h`.

#### Alternatives and edge cases

- **Recursive reverse inorder:** has the same $O(n)$ time and $O(h)$ call-stack space, but a skewed tree may exceed recursion limits.
- **Collect sorted values and suffix sums:** remains linear after traversal but uses $O(n)$ extra storage instead of $O(h)$.
- **Recompute greater values for every node:** is correct but takes $O(n^2)$ time.
- **Single node:** retains its original value because no greater node exists.
- **Negative values:** the running total may decrease; ordering, not positivity, establishes correctness.
- **Skewed tree:** the iterative stack avoids call-stack failure.
- **In-place update:** accumulation must use each node's original value at the moment it is visited.

</details>
