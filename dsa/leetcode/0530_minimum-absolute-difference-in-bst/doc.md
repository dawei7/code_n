# Minimum Absolute Difference in BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 530 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-bst/) |

## Problem Description
### Goal
Given a binary search tree containing at least two nodes, consider every pair of distinct nodes and the absolute difference between their stored values. The BST ordering places node values in sorted order under inorder traversal.

Return the minimum absolute difference among all node pairs. The task compares values rather than node depths or path lengths, and the selected nodes need not have a parent-child relationship. Because the closest values in sorted order determine the minimum, meet the intended traversal complexity without explicitly enumerating every pair.

### Function Contract
**Inputs**

- `root`: the root of a binary search tree containing at least two nodes with distinct values

**Return value**

- The minimum absolute difference between any pair of node values

### Examples
**Example 1**

- Input: `root = [4, 2, 6, 1, 3]`
- Output: `1`

**Example 2**

- Input: `root = [1, 0, 48, null, null, 12, 49]`
- Output: `1`

**Example 3**

- Input: `root = [5, 3, 8]`
- Output: `2`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Use the ordering already stored in the tree**

An inorder traversal of a binary search tree visits its distinct values in strictly increasing order. This turns the tree problem into finding the smallest gap in a sorted sequence without first materializing or sorting that sequence.

**Compare each value with its predecessor**

Maintain the previously visited value during iterative inorder traversal. For every visit after the first, subtract the predecessor from the current value and minimize the answer. Then make the current value the predecessor for the next visit.

**Why adjacent values are sufficient**

For any two sorted values $a < b$ with another value `c` between them, both $c - a$ and $b - c$ are no greater than $b - a$. Therefore a globally minimum pair cannot require skipping an intervening inorder value. Since the traversal checks every adjacent pair exactly once, it finds the global minimum.

**Avoid recursion-depth dependence**

An explicit stack descends each left chain, visits the node, and then moves into its right subtree. This preserves inorder while handling a highly skewed tree without relying on the language call-stack limit.

#### Complexity detail

Every one of the `n` nodes is pushed and popped once, so time is $O(n)$. The explicit traversal stack contains at most the tree height `h`, giving $O(h)$ auxiliary space: $O(\log n)$ for a balanced tree and $O(n)$ in the worst case.

#### Alternatives and edge cases

- **Recursive inorder traversal:** uses the same adjacent-value reasoning and $O(h)$ call-stack space, but a skewed tree can exceed recursion limits.
- **Collect and sort all values:** works for an arbitrary binary tree but costs $O(n \log n)$ time and $O(n)$ extra space, discarding the BST ordering advantage.
- **Compare every pair:** is correct but takes $O(n^2)$ time.
- **Two nodes:** their single difference is necessarily the answer.
- **Minimum at non-parent nodes:** inorder adjacency, rather than tree-edge adjacency, is what matters.
- **Unbalanced tree:** iterative traversal prevents call-stack failure while retaining the same result.
- **First inorder value:** initializes the predecessor and does not form a difference by itself.

</details>
