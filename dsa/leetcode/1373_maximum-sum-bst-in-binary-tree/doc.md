# Maximum Sum BST in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1373 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/) |

## Problem Description

### Goal

Given a binary tree, consider every subtree consisting of a node and all of its descendants. A subtree is a binary search tree when every value in its left subtree is strictly smaller than the root value, every value in its right subtree is strictly greater, and both child subtrees satisfy the same rule.

Find the greatest sum of node values among all subtrees that are binary search trees. If every nonempty BST subtree has a negative sum, return zero, corresponding to selecting no positive-sum subtree.

### Function Contract

**Inputs**

- `root`: the root of a nonempty binary tree containing $N$ nodes.

**Return value**

- The maximum node-value sum of any BST subtree, or `0` when no BST subtree has a positive sum.

### Examples

**Example 1**

- Input: `root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]`
- Output: `20`

**Example 2**

- Input: `root = [4,3,null,1,2]`
- Output: `2`

**Example 3**

- Input: `root = [-4,-2,-5]`
- Output: `0`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Summarize children before their parent.** Traverse the tree in iterative postorder. For every completed subtree, store whether it is a BST, its minimum and maximum values, and its total sum. An empty child is a valid BST with sum zero, minimum $+\infty$, and maximum $-\infty$.

**Combine summaries with strict boundaries.** A node forms a BST exactly when both child summaries are valid and
$$
\text{left maximum} < \text{node value} < \text{right minimum}.
$$
When valid, add both child sums and the node value, update the global answer, and propagate the combined minimum and maximum. When invalid, mark the parent summary invalid so no ancestor can treat that entire subtree as a BST.

Postorder guarantees both child summaries are exact before combination. The boundary inequalities are necessary and sufficient for every descendant on the left and right to respect the root, while child validity supplies the recursive BST property. Thus every valid subtree sum is considered once and invalid subtrees are never admitted.

#### Complexity detail

Each of the $N$ nodes is entered and completed once, with constant work at completion, so time is $O(N)$. The explicit traversal stack and stored summaries use $O(N)$ space in the worst case.

#### Alternatives and edge cases

- **Validate every subtree independently:** Run a bounded BST traversal and sum from each possible root. It is correct but can take $O(N^2)$ time.
- **Recursive postorder:** Return the same four-field summary from recursive calls. It uses $O(H)$ call space but may exceed the runtime recursion limit on a deep tree.
- **Strict inequality:** Equal values violate the BST rule; use `<`, not `<=`.
- **Invalid root:** A child or deeper descendant may still form the maximum BST subtree.
- **All negative:** Initialize the global answer to zero so negative subtree sums do not replace it.
- **Single node:** Every leaf is a BST, but a negative leaf still leaves the returned maximum at zero.
- **Whole tree valid:** The root summary includes every node, allowing the full-tree sum to win.

</details>
