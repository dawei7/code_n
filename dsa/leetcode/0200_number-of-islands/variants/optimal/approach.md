## General
An island is a connected component in a graph whose vertices are land cells and whose edges connect horizontal or vertical neighbors. The task is therefore to count connected components without building an explicit graph.

Scan the grid in row-major order. When a land cell has not been visited, it is the first encountered representative of a new island: increment the count and traverse from that seed. An explicit stack avoids recursion-depth limits. Mark the seed visited before pushing or immediately when discovered, then repeatedly inspect its four neighboring coordinates and add each in-bounds, unvisited land neighbor.

Marking at discovery time matters. If marking were delayed until a cell is popped, two adjacent cells could both enqueue the same neighbor, increasing work and stack size. The visited set separates discovery state from grid contents and preserves the input.

For

```text
1 1 0
1 0 0
0 0 1
```

the first `1` seeds a traversal that reaches the other two cells in the upper-left component. Those cells are then skipped by the outer scan. The bottom-right `1` remains unvisited, seeds a second traversal, and gives a total of two.

Diagonal cells are never considered neighbors. Two `1`s touching only at a corner therefore seed separate traversals and count as separate islands.

Starting from an unvisited land seed, the traversal follows every allowed four-direction land edge. It therefore visits every cell reachable from the seed and cannot visit a cell outside that connected component. When the traversal finishes, that entire island is marked. No marked cell can seed another count, while every island has a first cell encountered by the complete grid scan and therefore seeds exactly one traversal. Consequently the counter equals the number of islands.

## Complexity detail
The outer scan examines `mn` cells. Each land cell is marked once, pushed and popped at most once, and checks four neighbors, so total time is $O(mn)$. The visited set and explicit stack can each hold $O(mn)$ coordinates in the worst case, matching the required $O(mn)$ auxiliary-space bound.

## Alternatives and edge cases
- Mutating visited land from `"1"` to `"0"` removes the separate visited set and can reduce auxiliary storage, but changes the caller's grid.
- Recursive DFS is concise but can overflow the call stack on a large or snake-shaped island.
- Breadth-first search with a queue has the same asymptotic bounds and correctness.
- Union-find is valuable when connectivity changes dynamically, but adds parent/rank machinery for this static scan.
- All water returns zero; all connected land returns one. One-row and one-column grids use the same logic.
