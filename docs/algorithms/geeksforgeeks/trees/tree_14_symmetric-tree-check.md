# Symmetric Tree Check

| | |
|---|---|
| **ID** | `tree_14` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(H)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) |

## Problem statement

*(Note: This is a duplicate file for the Symmetric Tree logic, originally identical to `tree_12`)*

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

**Input:** A binary tree `root` node.
**Output:** A boolean indicating whether the tree is symmetric.

## When to use it

- To test your ability to traverse two different trees (or two different branches of the same tree) simultaneously.
- A natural evolution of checking if two trees are identical (`Same Tree`).

## Approach

**1. The "Two Pointer" Tree Traversal:**
If we want to check if the left side of the tree is a mirror image of the right side, we can just run two simultaneous DFS traversals!
We start one pointer `left_ptr` on `root.left`, and another pointer `right_ptr` on `root.right`.

**2. The Mirror Conditions:**
For the tree to be symmetric at this current level, three things MUST be true:
1. `left_ptr.val` MUST equal `right_ptr.val`.
2. The LEFT child of the `left_ptr` MUST mirror the RIGHT child of the `right_ptr`. (Outside edges).
3. The RIGHT child of the `left_ptr` MUST mirror the LEFT child of the `right_ptr`. (Inside edges).

**3. The Recursive Base Cases:**
- If BOTH pointers are `null`, we've reached the bottom perfectly. Return `True`.
- If ONE pointer is `null` but the other is NOT, they mismatched structural shapes! Return `False`.
- If their values do not match, return `False`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_14: Symmetric Tree Check.

Return True iff the binary tree is symmetric around
"""


def solve(children, root, n):
    """True iff the binary tree is a mirror of itself around the root."""
    if root == -1:
        return True

    def is_mirror(a, b):
        if a == -1 and b == -1:
            return True
        if a == -1 or b == -1:
            return False
        return (
            is_mirror(children[a][0], children[b][1])
            and is_mirror(children[a][1], children[b][0])
        )

    return is_mirror(children[root][0], children[root][1])
```

</details>

## Walk-through

Tree:
```text
      1
     / \
    2   2
   / \ / \
  3  4 4  3
```

1. **`is_mirror(2 (left), 2 (right))`:**
   - Values match (`2 == 2`).
   - Recursively call:
     - `is_mirror(3 (left), 3 (right))` -> Outer edges
     - `is_mirror(4 (left), 4 (right))` -> Inner edges
2. **`is_mirror(3, 3)`:**
   - Values match (`3 == 3`).
   - Calls `is_mirror(null, null)` and `is_mirror(null, null)`. Both return `True`.
   - Returns `True`.
3. **`is_mirror(4, 4)`:**
   - Values match (`4 == 4`).
   - Calls `is_mirror(null, null)` and `is_mirror(null, null)`. Both return `True`.
   - Returns `True`.
4. The first call returns `True AND True` => `True`.

Returns `True`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(\log N)$ |
| **Average** | $O(N)$ | $O(\log N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

We traverse every single node in the tree exactly once (or half the nodes twice, mathematically equivalent to $O(N)$). Time complexity is strictly $O(N)$.
Space complexity is bounded by the recursive call stack (DFS) or the queue (BFS).
For DFS, maximum call stack depth is $O(H)$. In the worst case (a completely skewed tree), this degrades to $O(N)$. For a balanced symmetric tree, it is $O(\log N)$.
For BFS, the queue holds at most N/2 pairs at the bottom level, strictly $O(N)$ space.

## Variants & optimizations

- **Same Tree:** Exactly the same algorithm, but instead of crossing the branches (`t1.left, t2.right`), you check identical branches (`t1.left, t2.left`).
- **Subtree of Another Tree:** A two-part algorithm where you do a standard DFS on the main tree, and at every node, you trigger the `Same Tree` algorithm against the target subtree!

## Real-world applications

- **Computer Vision / 3D Modeling:** Checking if a generated 3D mesh (often stored as a BSP tree or Octree) is perfectly symmetrical across an axis before applying physics or rendering optimizations.

## Related algorithms in cOde(n)

- **[tree_09 - Mirror Tree](tree_09_mirror-tree.md)** — The active algorithm to physically mutate a tree into its mirror image.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
