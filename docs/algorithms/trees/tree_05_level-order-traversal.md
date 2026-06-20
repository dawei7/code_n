# Level-Order Traversal

| | |
|---|---|
| **ID** | `tree_05` |
| **Category** | trees |
| **Complexity (required)** | $O(n)$ |
| **Difficulty** | 3/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) |

## Problem statement

Given the `root` of a binary tree, return the **level-order traversal** of its nodes' values. (i.e., from left to right, level by level).

**Input:** The root node of a binary tree.
**Output:** A 2D array, where each inner array represents a single level of the tree.

**Example:**
Given the tree:
```
      3
     / \
    9  20
      /  \
     15   7
```
**Output:** `[[3], [9, 20], [15, 7]]`

## When to use it

- To find the shortest path from the root to a specific node (in an unweighted tree).
- To print a tree visually in a terminal console.
- To serialize/deserialize a tree into a flat array structure (like LeetCode's standard tree representation `[3, 9, 20, null, null, 15, 7]`).

## Approach

Level-order traversal is fundamentally exactly the same as **Breadth-First Search (BFS)**.

Unlike DFS (which plunges deep using a Stack), BFS expands evenly in ripples using a **Queue** (First-In, First-Out).
1. Enqueue the root node.
2. While the Queue is not empty:
   - Determine how many nodes are currently in the queue. This number `M` represents the exact size of the current "level".
   - Loop exactly `M` times. In each loop, dequeue a node, process its value, and enqueue its left and right children.
   - All the children you just enqueued will wait patiently at the back of the queue to be processed in the *next* level.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_05: Level-Order Traversal.

BFS, return a list of lists — one row per depth.
"""


def solve(children, root, n):
    from collections import deque
    levels = []
    q = deque()
    q.append((root, 0))
    while q:
        u, d = q.popleft()
        while len(levels) <= d:
            levels.append([])
        levels[d].append(u)
        for v in children[u]:
            q.append((v, d + 1))
    return levels
```

</details>

## Walk-through

Let the tree be:
```
      A
     / \
    B   C
   /     \
  D       E
```

1. Init: `queue = [A]`. `result = []`.
2. Loop 1: `level_size = 1`.
   - Dequeue `A`. `current_level = [A]`.
   - Enqueue `B`, `C`. `queue = [B, C]`.
   - End inner loop. `result = [[A]]`.
3. Loop 2: `level_size = 2`.
   - Dequeue `B`. `current_level = [B]`. Enqueue `D`. `queue = [C, D]`.
   - Dequeue `C`. `current_level = [B, C]`. Enqueue `E`. `queue = [D, E]`.
   - End inner loop. `result = [[A], [B, C]]`.
4. Loop 3: `level_size = 2`.
   - Dequeue `D`. `current_level = [D]`. No children.
   - Dequeue `E`. `current_level = [D, E]`. No children.
   - End inner loop. `result = [[A], [B, C], [D, E]]`.
5. Loop terminates (`queue` is empty). ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n)$ | $O(1)$ |
| **Average** | $O(n)$ | $O(n)$ |
| **Worst** | $O(n)$ | $O(n)$ |

We visit every node exactly once, which takes strictly `O(n)` time.
The space complexity is defined by the maximum size of the queue. In a perfectly balanced binary tree, the absolute widest level is the very bottom row of leaves. In a binary tree, the last row contains roughly N/2 nodes. Therefore, the queue will hold at most `N/2` nodes simultaneously, making the worst-case space complexity `O(n)`. The best-case `O(1)` space occurs when the tree is a skewed linked list (width of 1).

## Variants & optimizations

- **Zig-Zag Level Order Traversal:** Every time you finish a level, check a boolean flag. If `True`, append `current_level` to the result normally. If `False`, append the `reverse()` of the `current_level`. Toggle the flag. This is a very common interview twist.

## Real-world applications

- **Network Routing:** OSPF (Open Shortest Path First) protocols use BFS to map out network topology, ensuring data packets take the shortest possible number of router hops to reach their destination.

## Related algorithms in cOde(n)

- **[search_03 - BFS on Grid](../searching/search_03_bfs-grid.md)** — The exact same algorithm logic applied to a 2D matrix instead of a pointer-based tree structure.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
