# Increasing Order Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 897 |
| Difficulty | Easy |
| Topics | Stack, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/increasing-order-search-tree/) |

## Problem Description
### Goal
Given the `root` of a binary search tree, rearrange its nodes in in-order sequence.

The leftmost node of the original tree must become the new root. Every node in the result must have no left child, and successive in-order nodes must be connected through right-child pointers. Consequently, the result is a single rightward chain whose values appear in increasing order.

Return the root of this rearranged tree.

### Function Contract
Let $n$ be the number of nodes and $h$ be the height of the input tree.

**Inputs**

- `root`: the root node of a binary search tree containing $1 \leq n \leq 100$ nodes.
- Every node value satisfies $0 \leq \texttt{Node.val} \leq 1000$.

**Return value**

Return the leftmost original node as the root of a tree in which every left pointer is `None` and each right pointer leads to the next node in in-order sequence.

### Examples
**Example 1**

- Input: `root = [5,3,6,2,4,null,8,1,null,null,null,7,9]`
- Output: `[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]`

**Example 2**

- Input: `root = [5,1,7]`
- Output: `[1,null,5,null,7]`

**Example 3**

- Input: `root = [2,1]`
- Output: `[1,null,2]`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Visit nodes in the required order**

An in-order traversal of a binary search tree visits values in increasing order: traverse the left subtree, visit the node, and then traverse the right subtree. Use an explicit stack to perform this traversal without losing access to pending ancestors.

**Rewire one node at a time**

Keep a dummy node and a `tail` pointer to the last node placed in the result. When a node is popped from the traversal stack, save its original right child before changing links. Set its left child to `None`, connect `tail.right` to this node, advance `tail`, and continue the traversal from the saved right child. Finally set the last right pointer to `None` and return `dummy.right`.

After each visited node, the chain beginning at `dummy.right` contains exactly the already visited in-order prefix, with no left children and with `tail` at its final node. The next stack pop is the next node in in-order sequence, so appending it preserves this property. Once traversal ends, every original node appears exactly once. Because a binary search tree's in-order sequence is increasing, the completed rightward chain has precisely the required order and shape.

#### Complexity detail

Each of the $n$ nodes is pushed onto and popped from the traversal stack once, giving $O(n)$ time. The stack holds at most one root-to-leaf path, so it uses $O(h)$ auxiliary space. Rewiring reuses the existing nodes and does not allocate an $O(n)$ output copy.

#### Alternatives and edge cases

- **Recursive in-order traversal:** Carrying a shared tail pointer gives the same $O(n)$ time and $O(h)$ call-stack space, but recursion hides the rewiring order.
- **Collect values and build new nodes:** An in-order value list followed by reconstruction is simple, but it uses $O(n)$ extra storage and discards reusable nodes.
- **Sort all values first:** A general traversal plus sorting is correct for a binary search tree, but costs $O(n \log n)$ time and ignores the in-order ordering guarantee.
- **Repeated minimum selection:** Selecting the next smallest remaining value by scanning all candidates can take $O(n^2)$ time.
- **One node:** Clear its left and right pointers and return the same node.
- **Already right-skewed tree:** The traversal preserves the increasing order while ensuring every left pointer is empty.
- **Left-skewed tree:** The deepest left node becomes the new root, and every former ancestor is appended to its right.
- **Saved right child:** Preserve `current.right` before assigning links, or rewiring can lose the unvisited right subtree.

</details>
