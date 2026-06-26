# Balanced Binary Tree Check

| | |
|---|---|
| **ID** | `tree_13` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(H)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) |

## Problem statement

*(Note: This is a duplicate file for the Balanced Binary Tree logic, originally identical to `tree_11`)*

Given a binary tree, determine if it is **height-balanced**.
A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of EVERY node differ in height by no more than 1.

**Input:** A binary tree `root` node.
**Output:** A boolean indicating whether it is balanced.

## When to use it

- To verify that a custom tree insertion algorithm (like AVL or Red-Black logic) is correctly maintaining its invariants.
- A classic interview question to test Top-Down vs Bottom-Up DFS efficiency.

## Approach

**1. The Naive Top-Down Approach ($O(N^2)$):**
The mathematical definition requires checking the height of the Left and Right subtrees. We already have a `height()` function (`tree_04`).
We could write a function that calculates `height(root.left)` and `height(root.right)`. If they differ by more than 1, return `False`.
Then, we recursively call the function on `root.left` and `root.right` to verify *their* subtrees.
**The Flaw:** Calculating the height takes $O(N)$ time. We are running an $O(N)$ calculation recursively N times! This takes $O(N^2)$ time!

**2. The Bottom-Up DFS Optimization ($O(N)$):**
Notice that to calculate the height of a node, the computer MUST travel all the way to the bottom of the tree anyway!
Instead of running a separate `isBalanced()` function and a `height()` function, what if we combine them?
We do a Post-Order DFS to calculate the height from the bottom up.
When a left child returns its height (e.g. `2`), and a right child returns its height (e.g. `4`), the parent instantly knows: "Wait! 4 - 2 = 2. My subtrees are unbalanced!"
Instead of returning its own height to the parent above it, it returns a special flag: `-1`!

**3. The Contagious Failure:**
If any node receives a `-1` from either of its children, it means the tree has failed the balance check deep down. It instantly stops calculating and just returns `-1` upwards. The `-1` propagates all the way to the root!
If the final call to the root returns `-1`, the tree is unbalanced. If it returns a normal positive integer (the height), the tree is balanced!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_13: Balanced Tree Check.

Return True iff the binary tree is height-balanced:
"""


def solve(children, root, n):
    """Return True iff the binary tree is height-balanced."""
    balanced = [True]

    def height(u):
        if u == -1:
            return 0
        l = height(children[u][0])
        r = height(children[u][1])
        if abs(l - r) > 1:
            balanced[0] = False
        return 1 + max(l, r)

    height(root)
    return balanced[0]
```

</details>

## Walk-through

Tree:
```text
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
```

1. **DFS reaches node `3` (the one on the left):**
   - It checks its left child `4`. It's a leaf. Left child returns `1`.
   - It checks its right child `4`. It's a leaf. Right child returns `1`.
   - Difference is 1 - 1 = 0. Balanced.
   - Node `3` returns its height: 1 + \max(1, 1) = 2.
2. **DFS evaluates node `2` (the one on the left):**
   - Left child `3` returned height `2`.
   - Right child `3` (the leaf) returns height `1`.
   - Difference is 2 - 1 = 1. Balanced!
   - Node `2` returns its height: 1 + \max(2, 1) = 3.
3. **DFS evaluates node `1` (Root):**
   - Left child `2` returned height `3`.
   - Right child `2` (the leaf on the far right) returns height `1`.
   - Difference is 3 - 1 = 2.
   - 2 > 1! Unbalanced!
   - Root returns `-1`.
4. The main function checks `check_height(root) != -1`. `-1 != -1` is False.
Returns `False`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(\log N)$ |
| **Average** | $O(N)$ | $O(\log N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

The DFS traversal visits every single node exactly once. The moment a violation is found, it immediately aborts further deep recursion (though it still bubbles up).
Time complexity is strictly $O(N)$.
Space complexity is bounded by the recursive call stack, which equals the height of the tree $O(H)$. In the average/best case (balanced tree), space is $O(\log N)$. In the worst case (skewed tree), it degrades to $O(N)$.

## Variants & optimizations

- **Top-Down Cache:** If you must use the $O(N^2)$ Top-Down approach for architectural reasons (e.g., using an external API to fetch height), you can use a Hash Map to memoize the height of each node, artificially bringing the time complexity back down to $O(N)$.

## Real-world applications

- **AVL Trees / Red-Black Trees:** This check is fundamentally embedded inside the insert/delete operations of self-balancing binary search trees. If the subtrees violate the `abs(left - right) <= 1` rule, a physical tree rotation is immediately triggered.

## Related algorithms in cOde(n)

- **[tree_04 - Tree Height](tree_04_tree-height.md)** — The foundational recursive function that powers this entire algorithm.
- **[tree_22 - AVL Insert](tree_22_avl-insert-simplified.md)** — How to physically fix the tree if this function returns `False`!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
