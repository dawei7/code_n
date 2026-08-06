## General
An island is a connected component in a graph whose vertices are land cells and whose edges connect horizontal or vertical neighbors. The task is therefore to count connected components without building an explicit graph.

Scan the grid in row-major order. Whenever a cell still contains `"1"`, it is the first encountered representative of a new island: increment the count and traverse from that seed. An explicit stack avoids recursion-depth limits. Change the seed to `"0"` before pushing it, then repeatedly inspect its four neighboring coordinates and do the same for each in-bounds land neighbor.

Marking at discovery time matters. If marking were delayed until a cell is popped, two adjacent cells could both push the same neighbor, increasing work and stack size. Reusing `"0"` as the visited marker avoids a separate coordinate set; this intentionally mutates the working grid, which the LeetCode method contract permits and the app runner isolates from stored inputs.

For

```text
1 1 0
1 0 0
0 0 1
```

the first `1` seeds a traversal that reaches the other two cells in the upper-left component. Those cells are then skipped by the outer scan. The bottom-right `1` remains unvisited, seeds a second traversal, and gives a total of two.

Diagonal cells are never considered neighbors. Two `1`s touching only at a corner therefore seed separate traversals and count as separate islands.

Starting from an unerased land seed, the traversal follows every allowed four-direction land edge. It therefore reaches every cell in that connected component and cannot reach a cell outside it. When the traversal finishes, that entire island has become water. No erased cell can seed another count, while every island has a first cell encountered by the complete grid scan and therefore seeds exactly one traversal. Consequently the counter equals the number of islands.

## Complexity detail
The outer scan examines `mn` cells. Each land cell is erased once, pushed and popped at most once, and checks four neighbors, so total time is $O(mn)$. The explicit stack can hold $O(mn)$ coordinates in the worst case. Marking inside the input grid uses no separate visited structure, though the required auxiliary-space bound remains $O(mn)$ because of the stack.

## Alternatives and edge cases
- A coordinate set preserves the caller's grid but adds up to $O(mn)$ stored entries; using a list instead makes membership checks linear and can make the whole scan quadratic.
- Recursive DFS is concise but can overflow the call stack on a large or snake-shaped island.
- Breadth-first search with a queue has the same asymptotic bounds and correctness.
- Union-find is valuable when connectivity changes dynamically, but adds parent/rank machinery for this static scan.
- All water returns zero; all connected land returns one. One-row and one-column grids use the same logic.
