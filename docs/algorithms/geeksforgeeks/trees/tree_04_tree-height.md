# Tree Height (Maximum Depth)

| | |
|---|---|
| **ID** | `tree_04` |
| **Category** | trees |
| **Complexity (required)** | $O(n)$ |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |

## Problem statement

Given the `root` of a binary tree, return its **maximum depth** (or height).

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Input:** The root node of a binary tree.
**Output:** An integer representing the height.

**Example:**
Given the tree:
```
      3
     / \
    9  20
      /  \
     15   7
```
**Output:** `3` (The path 3 -> 20 -> 15 has 3 nodes).

## When to use it

- As a foundational subroutine for highly complex tree algorithms.
- To determine if a tree is balanced (by comparing the height of the left and right subtrees).
- To evaluate the worst-case lookup time for a Binary Search Tree (lookup is `O(h)`).

## Approach

Finding the height of a tree is a classic recursive **Divide and Conquer** problem, beautifully mapping to a **Post-order** traversal.

If you want to know the maximum depth of a tree starting at node `A`, you just need to ask two questions:
1. What is the maximum depth of my left subtree?
2. What is the maximum depth of my right subtree?

The height of `A` is simply the larger of those two numbers, plus `1` (to account for `A` itself).
If the node is `None` (empty), its depth is mathematically `0`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_04: Tree Height.

A leaf has height 0; a non-leaf has height 1 + max(child height).
"""


def solve(children, root, n):
    def depth(u):
        if not children[u]:
            return 0
        return 1 + max(depth(v) for v in children[u])
    return depth(root)
```

</details>

## Walk-through (Recursive)

Let the tree be:
```
    A
     \
      B
     /
    C
```

Call `max_depth(A)`:
- `left_depth = max_depth(None)` -> returns `0`.
- `right_depth = max_depth(B)`:
  - `left_depth = max_depth(C)`:
    - `left_depth = max_depth(None)` -> returns `0`.
    - `right_depth = max_depth(None)` -> returns `0`.
    - Returns `max(0, 0) + 1` = `1`. (Height of C is 1).
  - `right_depth = max_depth(None)` -> returns `0`.
  - Returns `max(1, 0) + 1` = `2`. (Height of B is 2).
- Returns `max(0, 2) + 1` = `3`.

Final output: `3`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n)$ | $O(log n)$ |
| **Average** | $O(n)$ | $O(log n)$ |
| **Worst** | $O(n)$ | $O(n)$ |

We must visit every single node to ensure we don't miss a deep, hidden branch, so time is strictly `O(n)`.
Space complexity is dictated by the recursion stack (for DFS) or the queue size (for BFS). In the worst case (a linked list), DFS takes `O(n)` stack space. For BFS, the queue holds at most N/2 nodes at the widest level, meaning BFS takes `O(n)` heap space in perfectly balanced trees.

## Variants & optimizations

- **Minimum Depth:** A highly similar algorithm that finds the shortest path to a leaf. Unlike Max Depth, you must be careful: if a node only has one child, the minimum depth is NOT `0` (the empty child), you must traverse down the valid child.
- **N-ary Trees:** Instead of `max(left, right)`, simply iterate over `node.children` and track the running maximum `depth`.

## Real-world applications

- **AVL Trees / Red-Black Trees:** Balancing mechanisms in self-balancing trees constantly check the relative heights of subtrees during insertions to know when to trigger rotation algorithms.

## Related algorithms in cOde(n)

- **[tree_11 - Balanced Tree Check](tree_11_balanced-tree-check.md)** — An algorithm that directly builds upon `max_depth` to assert the overall health of a tree structure.
- **[tree_05 - Level Order Traversal](tree_05_level-order-traversal.md)** — The BFS technique used in the iterative approach.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
