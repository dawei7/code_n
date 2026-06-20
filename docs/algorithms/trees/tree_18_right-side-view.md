# Binary Tree Right Side View

| | |
|---|---|
| **ID** | `tree_18` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(D)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) |

## Problem statement

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it. Return the values of the nodes you can see ordered from top to bottom.
In other words, return the rightmost node at every single depth level of the tree.

**Input:** A binary tree `root` node.
**Output:** An array of integers representing the right side view.

## When to use it

- To easily demonstrate your understanding of Level-Order (BFS) Traversal, or your cleverness with Depth-First Search.
- One of the most common variations of the standard Level-Order traversal.

## Approach

**1. The Level-Order (BFS) Approach:**
The most intuitive way to solve this is to slice the tree into horizontal levels.
We use a Queue to perform a standard Level-Order Traversal (`tree_05`).
At each level, we process all nodes from left to right. The very LAST node we process in that level is exactly the node that is visible from the right side! We simply append that last node's value to our result array before moving to the next level.

**2. The Clever DFS Approach (Reverse Pre-Order):**
BFS requires $O(W)$ space (where W is the maximum width of the tree). Can we do it with DFS?
Standard Pre-Order DFS goes: Root -> Left -> Right.
What if we reverse it? Root -> Right -> Left!
By going Right first, the VERY FIRST node we encounter at any new depth is mathematically guaranteed to be the rightmost node at that depth!
We just pass a `depth` variable down the recursion. We maintain an array of results.
If `depth == len(results)`, it means we have reached a depth we have never seen before! Because we prioritize the Right branch, this must be the rightmost node! We append it to `results`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_18: Right Side View.

BFS level-by-level; the rightmost node at each level is the
one visible from the right side. Return the list of those
nodes, top-to-bottom.
"""


def solve(children, root, n):
    """Right side view of a binary tree."""
    if root == -1:
        return []
    from collections import deque
    levels = []
    q = deque([(root, 0)])
    while q:
        u, d = q.popleft()
        while len(levels) <= d:
            levels.append([])
        levels[d].append(u)
        if children[u][0] != -1:
            q.append((children[u][0], d + 1))
        if children[u][1] != -1:
            q.append((children[u][1], d + 1))
    return [level[-1] for level in levels]
```

</details>

## Walk-through

Tree:
```text
      1
    /   \
   2     3
    \     \
     5     4
    /
   6
```

**DFS Walk-through:**
1. `dfs(1, depth=0)`: `0 == len([])`. Append `1`. `res = [1]`.
   - Call Right: `dfs(3, depth=1)`
2. `dfs(3, depth=1)`: `1 == len([1])`. Append `3`. `res = [1, 3]`.
   - Call Right: `dfs(4, depth=2)`
3. `dfs(4, depth=2)`: `2 == len([1, 3])`. Append `4`. `res = [1, 3, 4]`.
   - Call Right: `dfs(null)`
   - Call Left: `dfs(null)`
   - Returns back to 3.
   - Node 3 has no Left.
   - Returns back to 1.
   - Call Left from 1: `dfs(2, depth=1)`
4. `dfs(2, depth=1)`: `1 != len([1, 3, 4])`. Skip append. (It is blocked by 3!)
   - Call Right: `dfs(5, depth=2)`
5. `dfs(5, depth=2)`: `2 != len([1, 3, 4])`. Skip append. (Blocked by 4!)
   - Call Left: `dfs(6, depth=3)`
6. `dfs(6, depth=3)`: `3 == len([1, 3, 4])`. Wait, depth 3 is new! Append `6`.
   - `res = [1, 3, 4, 6]`.

Final Result: `[1, 3, 4, 6]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(\log N)$ |
| **Average** | $O(N)$ | $O(\log N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

For both BFS and DFS, every node is visited exactly once. Time complexity is $O(N)$.
Space complexity differs slightly based on tree shape:
- **DFS:** Bounded by tree height $O(H)$. For a balanced tree, space is $O(\log N)$. For a skewed tree, it degrades to $O(N)$.
- **BFS:** Bounded by tree width $O(W)$. For a balanced tree, the bottom level has N/2 nodes, so space is $O(N)$. For a skewed tree (linked list), the width is 1, so space is $O(1)$.
In Big-O terms, both are technically $O(N)$ worst-case space.

## Variants & optimizations

- **Left Side View:** Exactly the same BFS logic (check `if i == 0` instead of `level_length - 1`), or exact same DFS logic (traverse `node.left` before `node.right`).
- **Bottom View:** A much harder variation where you must track horizontal X-coordinates (like in Vertical Order Traversal) and overwrite a Hash Map with the last node seen at each X-coordinate.

## Real-world applications

- **2D Game Rendering:** Rendering 2.5D isometric trees or overlapping UI elements where only the "outermost" boundaries of hierarchical bounding boxes need to be drawn to the screen to save GPU cycles.

## Related algorithms in cOde(n)

- **[tree_05 - Level Order Traversal](tree_05_level-order-traversal.md)** — The BFS engine used for the iterative approach.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
