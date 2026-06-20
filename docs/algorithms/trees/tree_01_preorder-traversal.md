# Pre-order Traversal

| | |
|---|---|
| **ID** | `tree_01` |
| **Category** | trees |
| **Complexity (required)** | $O(n)$ |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) |

## Problem statement

Given the `root` of a binary tree, return an array containing the values of its nodes using **Pre-order Traversal**.

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
**Output:** `[1, 2, 3]`

## When to use it

- To create a **copy** (clone) of a tree. Pre-order traversal perfectly serializes the root first, allowing you to easily reconstruct the tree from top to bottom.
- When evaluating prefix expressions (e.g., `+ * A B C`) in an expression tree.
- When exploring directory structures in an operating system (you want to visit the parent directory before exploring its child folders).

## Approach

There are three primary Depth-First Search (DFS) traversals for binary trees: Pre-order, In-order, and Post-order.
The name specifies exactly when the **Current Node (Root)** is processed relative to its children.

**Pre**-order means the root is processed **before** its subtrees:
1. Process the Current Node (`Root`).
2. Recursively traverse the `Left` subtree.
3. Recursively traverse the `Right` subtree.

Mnemonic: **N L R** (Node, Left, Right).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_01: Preorder Traversal.

Multi-way tree: children[i] is the list of i's children. Visit
the node, then recurse on each child left-to-right.
"""


def solve(children, root, n):
    out = []

    def walk(u):
        out.append(u)
        for v in children[u]:
            walk(v)

    walk(root)
    return out
```

</details>

## Walk-through (Iterative)

Let the tree be:
```
      A
    /   \
   B     C
  / \   /
 D   E F
```

1. Init: `Stack = [A]`. `Result = []`
2. Pop `A`. `Result = [A]`. Push `A.right` (C), then `A.left` (B). `Stack = [C, B]`.
3. Pop `B`. `Result = [A, B]`. Push `E`, then `D`. `Stack = [C, E, D]`.
4. Pop `D`. `Result = [A, B, D]`. `D` has no children. `Stack = [C, E]`.
5. Pop `E`. `Result = [A, B, D, E]`. `E` has no children. `Stack = [C]`.
6. Pop `C`. `Result = [A, B, D, E, C]`. Push `C.right` (None), then `F`. `Stack = [F]`.
7. Pop `F`. `Result = [A, B, D, E, C, F]`. No children. `Stack = []`.

Loop finishes. Output: `A -> B -> D -> E -> C -> F`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n)$ | $O(log n)$ |
| **Average** | $O(n)$ | $O(log n)$ |
| **Worst** | $O(n)$ | $O(n)$ |

We visit every single node exactly once, taking strictly `O(n)` time.
The space complexity depends on the height of the tree `h`. In a perfectly balanced tree, the maximum depth (and thus the maximum size of the recursion stack or explicit stack) is `O(log n)`. In the worst case (a completely unbalanced, linked-list-like tree), the stack depth grows to `O(n)`.

## Variants & optimizations

- **Morris Traversal:** A brilliant `O(1)` space algorithm that temporarily modifies the tree structure by creating links from the leaves back up to their ancestors. It eliminates the need for both the call stack and explicit stacks, though it mutates the tree during traversal.

## Real-world applications

- **DOM Rendering:** When a browser parses HTML, it renders the parent tags (like `<div>`) before recursively stepping inside to render the child tags (like `<p>`).
- **Tree Serialization:** JSON parsing/stringification effectively works via pre-order DFS traversals of an object graph.

## Related algorithms in cOde(n)

- **[tree_02 - In-order Traversal](tree_02_inorder-traversal.md)** — Traverse L, N, R.
- **[tree_03 - Post-order Traversal](tree_03_postorder-traversal.md)** — Traverse L, R, N.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
