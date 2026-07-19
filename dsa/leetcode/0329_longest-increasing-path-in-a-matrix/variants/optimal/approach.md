## General
**Strict increases turn the matrix into a directed acyclic graph**

Treat each cell as a vertex and direct an edge from a cell to every orthogonal neighbor with a larger value. Along any directed edge the value strictly increases, so a directed cycle is impossible: returning to the starting cell would require its value to be both larger than and equal to itself.

The task is therefore the longest path length in this implicit DAG. It can be computed without recursion by peeling topological layers from local maxima downward.

**Start with cells that have no larger neighbor**

For every cell, count its outgoing edges to larger neighbors. Cells with outdegree zero are local maxima and form the first queue layer. Remove that entire layer conceptually. For each removed cell, inspect its smaller neighbors and decrement their outdegrees; a smaller neighbor enters the queue when all of its larger successors have been removed.

Repeat until the queue is empty and count the number of layers. Edges are traversed in reverse during removal, but the underlying increasing path direction remains from smaller to larger.

**Each layer adds one possible path cell**

Layer one contains cells whose longest increasing continuation has length one. After those are removed, a cell entering layer two has all larger continuations in earlier layers and can precede one of them, giving maximum continuation length two. Inductively, a cell removed in layer `d` begins an increasing path of length `d`, and no longer continuation exists because every outgoing neighbor was removed in an earlier layer.

Thus the final number of peeling rounds equals the maximum increasing-path length. Every cell enters the queue once and every orthogonal adjacency is examined only a constant number of times.

## Complexity detail
There are `mn` cells and at most four directed adjacencies per cell. Computing outdegrees and peeling all layers takes $O(mn)$ time. The outdegree matrix and queue contain at most `mn` entries, using $O(mn)$ space.

## Alternatives and edge cases
- **Memoized DFS:** also solves each cell once in $O(mn)$ time, but a very long path can exceed the language recursion limit unless implemented iteratively.
- **Uncached DFS from every cell:** repeatedly solves the same suffix paths and can take exponential time on branching inputs or $O((mn)^2)$ even on a single increasing chain.
- **Sort cells by value and run DP:** is correct but adds an $O(mn \log(mn))$ sorting cost.
- Equal-valued neighbors have no edge because the path must increase strictly. A uniform matrix and a one-cell matrix both return one.
