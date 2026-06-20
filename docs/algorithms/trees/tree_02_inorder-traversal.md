# In-order Traversal

| | |
|---|---|
| **ID** | `tree_02` |
| **Category** | trees |
| **Complexity (required)** | $O(n)$ |
| **Difficulty** | 3/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) |

## Problem statement

Given the `root` of a binary tree, return an array containing the values of its nodes using **In-order Traversal**.

**Input:** The root node of a binary tree.
**Output:** An array of node values.

**Example:**
Given the tree:
```
    1
     \
      2
     /
    3
```
**Output:** `[1, 3, 2]`

## When to use it

- **Binary Search Trees (BST):** This is the absolute most important traversal for a BST. An in-order traversal of a perfectly formed BST will **always yield elements in strictly sorted ascending order**.
- To flatten a tree into an array for easy `k-th` smallest element lookups.
- When evaluating infix expressions (e.g., `A + B * C`) in an expression tree.

## Approach

In-order means the root is processed **in the middle** of its subtrees:
1. Recursively traverse the `Left` subtree.
2. Process the Current Node (`Root`).
3. Recursively traverse the `Right` subtree.

Mnemonic: **L N R** (Left, Node, Right).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_02: Inorder Traversal.

Multi-way tree: first-child subtree, then the node, then each
remaining child subtree left-to-right.
"""


def solve(children, root, n):
    out = []

    def walk(u):
        if children[u]:
            walk(children[u][0])
        out.append(u)
        for v in children[u][1:]:
            walk(v)

    walk(root)
    return out
```

</details>

## Walk-through (Iterative)

Let the tree be a BST:
```
      4
    /   \
   2     6
  / \   / \
 1   3 5   7
```

1. `current = 4`. `Stack = []`.
2. Dive left. Push 4, Push 2, Push 1. `current` is None. `Stack = [4, 2, 1]`.
3. Pop 1. Process **1**. Go right (`current = None`).
4. Dive left (skipped since None).
5. Pop 2. Process **2**. Go right (`current = 3`).
6. Dive left on 3. Push 3. `Stack = [4, 3]`.
7. Pop 3. Process **3**. Go right (`None`).
8. Dive left (skipped).
9. Pop 4. Process **4**. Go right (`current = 6`).
10. Dive left on 6. Push 6, Push 5. `Stack = [6, 5]`.
11. Pop 5. Process **5**. Go right (`None`).
12. Pop 6. Process **6**. Go right (`current = 7`).
13. Dive left on 7. Push 7. `Stack = [7]`.
14. Pop 7. Process **7**. Go right (`None`).
15. Loop terminates.

Final Output: `[1, 2, 3, 4, 5, 6, 7]`. It is perfectly sorted! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n)$ | $O(log n)$ |
| **Average** | $O(n)$ | $O(log n)$ |
| **Worst** | $O(n)$ | $O(n)$ |

We visit every single node exactly once, yielding strictly `O(n)` time.
The space complexity depends on the tree height `h`. In a balanced BST, the maximum stack depth is `O(log n)`. If the tree is entirely skewed to the left, the inner loop pushes every single node before a single pop, resulting in `O(n)` memory usage.

## Variants & optimizations

- **Reverse In-order Traversal:** If you traverse `Right -> Node -> Left`, you will output the elements of a BST in strictly **descending** order. This is incredibly useful for finding the K-th *largest* element.

## Real-world applications

- **Database Range Queries:** When a SQL query asks for `SELECT * WHERE ID BETWEEN 10 AND 50`, the B-Tree index resolves the bounds and then simply executes an in-order traversal to fetch the sorted range.

## Related algorithms in cOde(n)

- **[tree_01 - Pre-order Traversal](tree_01_preorder-traversal.md)** — Traverse N, L, R.
- **[tree_06 - BST Search](tree_06_bst-search.md)** — Understanding BST invariants.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
