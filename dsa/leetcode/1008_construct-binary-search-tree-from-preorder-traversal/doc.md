# Construct Binary Search Tree from Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1008 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Tree, Binary Search Tree, Monotonic Stack, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) |

## Problem Description

### Goal

You are given an integer array `preorder` representing the preorder traversal of a binary search tree. In preorder traversal, a node is visited before its left subtree and then its right subtree.

Construct and return the tree's root. In the required binary search tree, every descendant in `Node.left` has a value strictly less than `Node.val`, and every descendant in `Node.right` has a value strictly greater than `Node.val`. All traversal values are unique, and a tree satisfying the traversal is guaranteed to exist.

### Function Contract

**Inputs**

- `preorder`: an array of $N$ unique integers, where $1\le N\le100$ and $1\le\texttt{preorder[i]}\le1000$.

Let $H$ denote the height of the constructed tree, with a single-node tree having height $1$.

**Return value**

- The root `TreeNode` of the binary search tree whose preorder traversal is `preorder`.

### Examples

**Example 1**

- Input: `preorder = [8, 5, 1, 7, 10, 12]`
- Output: `[8, 5, 10, 1, 7, null, 12]`
- Explanation: The output uses level-order tree serialization; its preorder traversal is the given array.

**Example 2**

- Input: `preorder = [1, 3]`
- Output: `[1, null, 3]`
- Explanation: Since `3` is strictly greater than `1`, it is the root's right child.

**Example 3**

- Input: `preorder = [4, 2]`
- Output: `[4, 2]`
- Explanation: Since `2` is strictly less than `4`, it is the root's left child.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(H)$

<details>
<summary>Approach</summary>

#### General

**Interpret the stack as the active ancestor path:** Create the root from the first preorder value and keep a stack containing the path of nodes whose right subtree may still receive values. Each later value creates exactly one new node.

**Attach smaller values immediately on the left:** If `value < stack[-1].val`, preorder and the BST ordering imply that the new node begins the current node's left subtree. Assign it to `stack[-1].left` and push it, extending the active path downward.

**Pop completed subtrees before attaching right:** Otherwise, pop while the stack's top value is smaller than `value`. The last popped node is the deepest ancestor whose left subtree and any smaller nested subtrees are complete, so the new node is its right child. Push the new node as the new end of the active path.

Each attachment respects the strict BST inequalities. Preorder supplies a child only after its ancestors and supplies the entire left subtree before the right subtree; the pop step removes exactly the ancestors whose remaining right boundary the new value has crossed. Therefore every input value is attached at its unique valid position and the constructed tree reproduces the traversal.

#### Complexity detail

Each of the $N$ nodes is pushed once and popped at most once, so total time is $O(N)$. The stack contains at most the $H$ nodes on an active root-to-node path and uses $O(H)$ auxiliary space. The returned tree itself is output space.

#### Alternatives and edge cases

- **Recursive upper bound:** Consuming preorder with a moving index and subtree bound also achieves $O(N)$ time and $O(H)$ call-stack space.
- **Find each subtree split:** Scanning every recursive slice for the first value greater than its root is intuitive, but a skewed tree causes $O(N^2)$ work and repeated slicing.
- **Insert nodes one at a time:** Ordinary BST insertion reconstructs the same tree, yet also takes $O(N^2)$ time for sorted preorder input.
- **Strict inequalities:** Values are unique, so no duplicate-placement rule is needed.
- **Skewed traversal:** Increasing or decreasing input produces height $H=N$; an iterative stack avoids recursion-limit concerns.

</details>
