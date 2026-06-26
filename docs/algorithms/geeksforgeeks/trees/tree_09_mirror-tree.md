# Invert/Mirror Binary Tree

| | |
|---|---|
| **ID** | `tree_09` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(H)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) |

## Problem statement

Given the `root` of a binary tree, invert the tree, and return its root.
Inverting a binary tree means swapping the left and right children of EVERY node in the tree. The resulting tree should be a perfect mirror image of the original.

**Input:** A binary tree `root` node.
**Output:** The root node of the inverted tree.

## When to use it

- The most infamous interview question of all time, largely due to the viral tweet by Max Howell (creator of Homebrew): *"Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invert a binary tree on a whiteboard so f*** off."*
- To test basic recursive tree traversal and pointer swapping.

## Approach

**1. The "Top-Down Swap" Analogy:**
If you want to mirror an entire tree, you start at the root.
You physically swap the root's left child branch with its right child branch.
Now the top level is mirrored! But the subtrees themselves are still in their original order.
So, you walk down into the left subtree, and swap ITS children. Then you walk down into the right subtree, and swap ITS children.
You continue this process recursively until you hit the absolute bottom of the tree (a `null` leaf).

**2. The DFS Pre-Order Traversal:**
This logic perfectly matches a recursive Depth First Search (DFS).
At any given `node`:
1. Save the `node.left` pointer into a temporary variable.
2. Overwrite `node.left` with `node.right`.
3. Overwrite `node.right` with the temporary variable.
4. Recursively call the function on the new `node.left`.
5. Recursively call the function on the new `node.right`.

**3. The BFS Alternative:**
You can also do this iteratively using Breadth First Search (BFS) and a Queue!
Instead of a recursive call stack, you push the root into a Queue.
While the Queue isn't empty, pop a node, swap its children, and push any non-null children into the Queue to be swapped later.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_09: Mirror Tree.

Reverse every node's child list.
"""


def solve(children, root, n):
    return [list(reversed(c)) for c in children]
```

</details>

## Walk-through

Original Tree:
```text
      4
    /   \
   2     7
  / \   / \
 1   3 6   9
```

**Recursive DFS:**
1. **`invert(4)`:**
   - Swap children of 4. `4.left` becomes `7`, `4.right` becomes `2`.
   - Call `invert(7)`.
2. **`invert(7)`:** (Note: this is currently the *left* child of 4)
   - Swap children of 7. `7.left` becomes `9`, `7.right` becomes `6`.
   - Call `invert(9)`. `9` is a leaf, it swaps its `null` children and returns.
   - Call `invert(6)`. `6` is a leaf, returns.
3. **`invert(2)`:** (Note: this is currently the *right* child of 4)
   - Swap children of 2. `2.left` becomes `3`, `2.right` becomes `1`.
   - Call `invert(3)`. Returns.
   - Call `invert(1)`. Returns.

Resulting Tree:
```text
      4
    /   \
   7     2
  / \   / \
 9   6 3   1
```
Perfectly mirrored! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(\log N)$ |
| **Average** | $O(N)$ | $O(\log N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

Every single node in the tree must be visited exactly once to swap its children. Visiting a node takes $O(1)$ time. Time complexity is strictly $O(N)$.
Space complexity is bounded by the recursive call stack (or the BFS queue size).
For DFS, the maximum call stack depth is the height of the tree $O(H)$. In the worst case (a skewed linked-list-like tree), this is $O(N)$. In a balanced tree, it is $O(\log N)$.
For BFS, the maximum queue size is the width of the bottom level of the tree. In a perfectly balanced tree, this is N/2, which strictly simplifies to $O(N)$ space.

## Variants & optimizations

- **Symmetric Tree (`tree_12`):** A related problem that asks if a tree is a mirror of ITSELF. (i.e. is the left subtree an exact inversion of the right subtree?).

## Real-world applications

- **Computer Graphics / UI Rendering:** If a developer builds a complex UI element or 3D object represented as a Scene Graph (Tree), "flipping" the object horizontally requires an algorithmic tree inversion!

## Related algorithms in cOde(n)

- **[tree_01 - Pre-order Traversal](tree_01_preorder-traversal.md)** — The foundational recursive pattern used by the DFS solution.
- **[tree_05 - Level Order Traversal](tree_05_level-order-traversal.md)** — The foundational queue-based pattern used by the BFS solution.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
