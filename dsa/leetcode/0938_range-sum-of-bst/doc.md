# Range Sum of BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 938 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/range-sum-of-bst/) |

## Problem Description

### Goal

Given the `root` of a binary search tree and integers `low` and `high`, compute the sum of every node value in the inclusive interval from `low` through `high`.

The tree contains at least one node, all node values are unique, and its binary-search-tree ordering may be used: every value in a left subtree is smaller than its ancestor and every value in a right subtree is larger. Values equal to either boundary must be included.

### Function Contract

Let $N$ be the number of nodes, $h$ the tree height, $v$ the number of node values in the requested range, and $a$ and $b$ the values of `low` and `high`, respectively.

**Inputs**

- `root`: the root node of a binary search tree with $N$ nodes. Cases serialize the tree in level order.
- `low`, `high`: inclusive integer bounds satisfying $1 \le a \le b \le 10^5$.
- The tree has $1 \le N \le 2 \cdot 10^4$ unique values, each in $[1,10^5]$.

**Return value**

Return the sum of all node values $x$ such that $a \le x \le b$.

### Examples

**Example 1**

- Input: `root = [10,5,15,3,7,null,18], low = 7, high = 15`
- Output: `32`

**Example 2**

- Input: `root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10`
- Output: `23`

### Required Complexity

- **Time:** $O(h+v)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Traverse while exploiting BST order.** Keep a stack of nodes still to inspect. For a node whose value is below `low`, its entire left subtree is also below the range, so only push the right child. Symmetrically, when the value is above `high`, only its left subtree can contain qualifying values.

**Include both boundaries.** When `low <= node.val <= high`, add the value and push both children. The inclusive comparisons ensure values equal to either limit contribute. Every skipped subtree is proved irrelevant by BST ordering, while every subtree that could contain an in-range value remains reachable.

**Finish after all relevant nodes are resolved.** Each node enters the stack at most once. The running total therefore contains every qualifying value exactly once when the stack empties. An iterative traversal avoids recursion-depth failures on a highly unbalanced tree. Pruning can make many inputs faster, although a range covering the whole tree still requires visiting all $N$ nodes.

#### Complexity detail

The traversal visits the $v$ in-range nodes plus at most the boundary search paths around them, taking $O(h+v)$ time. A depth-first stack holds $O(h)$ nodes. Either $h$ or $v$ can equal $N$, so the time bound still becomes $O(N)$ in the worst case.

#### Alternatives and edge cases

- **Recursive pruned DFS:** Apply the same comparisons recursively. It has the same $O(h+v)$ time and $O(h)$ call-stack bounds but may exceed the language recursion limit on a skewed tree.
- **Full inorder traversal:** Visit every node and filter values. This always takes $O(N)$ time and misses beneficial pruning on narrow ranges.
- **Scan the tree once per candidate value:** Searching the entire tree separately for every integer in the range is correct but can require $O(N^2)$ time when the range width scales with $N$.
- **Boundary equality:** Values exactly equal to `low` or `high` are included.
- **Range outside most tree values:** BST pruning may reduce the work to a single root-to-leaf path.

</details>
