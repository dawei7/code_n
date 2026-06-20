# Post-order Traversal

| | |
|---|---|
| **ID** | `tree_03` |
| **Category** | trees |
| **Complexity (required)** | $O(n)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) |

## Problem statement

Given the `root` of a binary tree, return an array containing the values of its nodes using **Post-order Traversal**.

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
**Output:** `[3, 2, 1]`

## When to use it

- To safely **delete** a tree. You MUST delete a node's children before you can safely free the memory of the node itself. Post-order guarantees children are processed first.
- To calculate the space/size/height of a directory. A folder's total size is the sum of its files + the sum of all its subfolders. You must fully calculate the subfolders (children) before calculating the parent.
- When evaluating postfix expressions (Reverse Polish Notation, e.g. `A B C * +`).

## Approach

Post-order means the root is processed **after** its subtrees:
1. Recursively traverse the `Left` subtree.
2. Recursively traverse the `Right` subtree.
3. Process the Current Node (`Root`).

Mnemonic: **L R N** (Left, Right, Node).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_03: Postorder Traversal.

Multi-way tree: recurse on each child subtree, then visit the node.
"""


def solve(children, root, n):
    out = []

    def walk(u):
        for v in children[u]:
            walk(v)
        out.append(u)

    walk(root)
    return out
```

</details>

## Walk-through (Two-Stack Method)

Tree:
```
      A
    /   \
   B     C
```

1. `stack1 = [A]`, `stack2 = []`.
2. Pop `A`. Push to `stack2`. `stack2 = [A]`.
3. Push `A.left` (B). Push `A.right` (C). `stack1 = [B, C]`.
4. Pop `C`. Push to `stack2`. `stack2 = [A, C]`.
5. `C` has no children.
6. Pop `B`. Push to `stack2`. `stack2 = [A, C, B]`.
7. `B` has no children.
8. `stack1` is empty.
9. Pop `stack2` into array: Pop `B`, Pop `C`, Pop `A`.

Output: `[B, C, A]`. (Left, Right, Node). ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n)$ | $O(log n)$ |
| **Average** | $O(n)$ | $O(log n)$ |
| **Worst** | $O(n)$ | $O(n)$ |

*(Note: The Two-Stack method uses `O(n)` space strictly, but a true 1-stack solution scales based on height).*
We visit every node once, taking `O(n)` time. A proper 1-stack implementation uses `O(h)` memory, which ranges from `O(log n)` to `O(n)` depending on tree balance.

## Variants & optimizations

- **1-Stack Approach:** To use just 1 stack, you must keep a `last_visited` pointer. When peeking at the top of the stack, if its `right` child is `None` or equals `last_visited`, it means you have fully explored both branches and can safely pop and process it. Otherwise, you must push its `right` child and dive.

## Real-world applications

- **AST Code Generation:** When a compiler turns an Abstract Syntax Tree into machine code or bytecode, it uses post-order traversal. You cannot emit the `ADD` assembly instruction until you have emitted the code that loads both operand variables into the CPU registers.

## Related algorithms in cOde(n)

- **[tree_01 - Pre-order Traversal](tree_01_preorder-traversal.md)** — Traverse N, L, R.
- **[tree_02 - In-order Traversal](tree_02_inorder-traversal.md)** — Traverse L, N, R.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
