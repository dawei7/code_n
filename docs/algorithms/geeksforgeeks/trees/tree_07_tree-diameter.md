# Diameter of a Binary Tree

| | |
|---|---|
| **ID** | `tree_07` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(H)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) |

## Problem statement

Given the `root` of a binary tree, return the length of the **diameter** of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.
The length of a path between two nodes is represented by the number of edges between them.

**Input:** A binary tree `root` node.
**Output:** An integer representing the diameter.

## When to use it

- A classic test of Bottom-Up Post-Order DFS traversal.
- It tests your ability to maintain a global state variable while simultaneously returning a different value up the recursive call stack.

## Approach

**1. The "Arch" Analogy:**
Imagine lifting the tree by its root. The longest path between any two nodes looks like a giant arch spanning from one leaf, going UP to some connecting node, and then going DOWN to another leaf.
For any arbitrary node in the tree, what is the longest path that "arches" directly through it?
It mathematically MUST be: `(Longest path going down its Left Subtree) + (Longest path going down its Right Subtree)`.

**2. The Bottom-Up Calculation:**
To find the global diameter, we must calculate this "Arch" value for EVERY SINGLE NODE in the tree, and keep track of the absolute maximum we ever see!
How do we know the longest path going down a subtree? That's just the **Height (`tree_04`)** of the subtree!
So, if we compute the Height of the tree using Post-Order DFS, at every single node, we will magically have the height of its left child `L` and the height of its right child `R`.
The Arch size through this node is `L + R`.
We just update a global `max_diameter` variable if `L + R` is bigger!

**3. The Dual-Purpose Recursion:**
The recursive function serves TWO different purposes simultaneously:
1. **To its parent:** It returns its own Height (`1 + max(L, R)`).
2. **To the global variable:** It calculates and updates the Diameter arch (`L + R`).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_07: Tree Diameter.

For each node, the longest path through it is the sum of the two
tallest subtree depths. The diameter is the max of that sum.
"""


def solve(children, root, n):
    if n == 0:
        return 0
    best = 0

    def depth(u):
        nonlocal best
        if not children[u]:
            return 0
        top_two = [0, 0]
        for v in children[u]:
            d = depth(v)
            if d >= top_two[0]:
                top_two = [d, top_two[0]]
            elif d > top_two[1]:
                top_two[1] = d
        through = top_two[0] + top_two[1]
        if through > best:
            best = through
        return 1 + top_two[0]

    depth(root)
    return best
```

</details>

## Walk-through

Tree:
```text
      1
     / \
    2   3
   / \
  4   5
```

1. **`height(4)`:**
   - Left is null -> 0. Right is null -> 0.
   - Local diameter: 0 + 0 = 0. `max_diameter = max(0, 0) = 0`.
   - Returns Height: 1 + \max(0, 0) = 1.
2. **`height(5)`:**
   - Left null -> 0. Right null -> 0.
   - Local diameter: 0 + 0 = 0. `max_diameter = 0`.
   - Returns Height: 1.
3. **`height(2)`:**
   - Left returned 1. Right returned 1.
   - Local diameter: 1 + 1 = 2. `max_diameter = max(0, 2) = 2`.
   - Returns Height: 1 + \max(1, 1) = 2.
4. **`height(3)`:**
   - Left null -> 0. Right null -> 0.
   - Local diameter: 0. `max_diameter = 2`.
   - Returns Height: 1.
5. **`height(1)` (Root):**
   - Left (from 2) returned 2. Right (from 3) returned 1.
   - Local diameter: 2 + 1 = 3. `max_diameter = max(2, 3) = 3`.
   - Returns Height: 1 + \max(2, 1) = 3.

Recursion ends. Return `max_diameter = 3`. ✓
(The path is `4 -> 2 -> 1 -> 3` which has 3 edges).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(\log N)$ |
| **Average** | $O(N)$ | $O(\log N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

The DFS traversal visits every single node exactly once. Doing $O(1)$ constant time addition and `max()` operations at each node.
Time complexity is exactly $O(N)$.
Space complexity is bounded by the recursive call stack, which equals the height of the tree $O(H)$. In the average/best case (balanced tree), space is $O(\log N)$. In the worst case (skewed tree), it degrades to $O(N)$.

## Variants & optimizations

- **Binary Tree Maximum Path Sum (`tree_10`):** The exact same architectural approach! But instead of counting edges (`left_height + right_height`), you sum the values of the nodes (`node.val + max_left_sum + max_right_sum`), with an extra check to ignore negative paths.

## Real-world applications

- **Network Routing:** Finding the absolute longest physical transmission path (latency bottleneck) within a tree-based network topology to determine packet timeouts.

## Related algorithms in cOde(n)

- **[tree_04 - Tree Height](tree_04_tree-height.md)** — The foundational recursive function that powers this entire algorithm.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
