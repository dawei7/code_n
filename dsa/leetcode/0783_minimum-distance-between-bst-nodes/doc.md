# Minimum Distance Between BST Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 783 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-distance-between-bst-nodes/) |

## Problem Description

### Goal

Given the root of a binary search tree containing at least two nodes with distinct integer values, consider every pair of different nodes.

Return the minimum absolute difference between their values. Distance here is numerical value difference, not the number of tree edges between nodes. The binary-search-tree ordering determines how values are arranged, but the answer may come from nodes at any depths or branches.

### Function Contract

**Inputs**

- `root`: the root node of a binary search tree with at least two nodes and no duplicate values.

**Return value**

- The minimum absolute difference between any pair of node values.

### Examples

**Example 1**

- Input: `root = [4,2,6,1,3]`
- Output: `1`
- Explanation: Consecutive values such as `1` and `2` differ by one.

**Example 2**

- Input: `root = [1,0,48,null,null,12,49]`
- Output: `1`
- Explanation: The values `0` and `1`, as well as `48` and `49`, attain the minimum.

**Example 3**

- Input: `root = [10,5,15]`
- Output: `5`
- Explanation: Both adjacent values in sorted order differ by five.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Use the BST's sorted traversal**

An inorder traversal of a binary search tree visits its distinct values in strictly increasing order. Maintain the previously visited value and update the best difference when the next node is reached.

**Why only neighbors matter**

For sorted values, the difference between two nonadjacent entries contains one or more positive adjacent gaps. It cannot be smaller than every gap inside that interval. Therefore the globally closest pair must appear consecutively in the inorder sequence, and comparing each node only with its predecessor is sufficient.

An explicit stack descends left until it reaches the next smallest unvisited node, then moves into that node's right subtree. This produces exactly the sorted order without storing all values. Every candidate adjacent gap is examined once, so the smallest recorded gap is the required answer.

#### Complexity detail

Every one of the `n` nodes is pushed, popped, and processed once, taking $O(n)$ time. The traversal stack holds at most the tree height `h`, giving $O(h)$ auxiliary space.

#### Alternatives and edge cases

- **Recursive inorder traversal:** Carry the previous value and current minimum through recursion; this has the same $O(n)$ time and $O(h)$ call-stack space.
- **Collect and sort values:** A traversal followed by sorting works for any binary tree but takes $O(n \log n)$ time and $O(n)$ space.
- **Compare every pair:** Directly testing all node pairs is correct but takes $O(n^2)$ time.
- **Exactly two nodes:** Their absolute difference is the answer.
- **Skewed tree:** The explicit stack may grow to $O(n)$, matching $h = n$.
- **First inorder node:** It initializes the predecessor and does not form a gap by itself.
- **Distinct values:** The minimum is positive; duplicates do not need special handling under the contract.

</details>
