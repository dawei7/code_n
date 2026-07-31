## General

Row constraints and column constraints do not interact until placement. Treat each collection as a directed graph over values 1 through `k`, and compute one topological order for each graph.

**Order one dimension.** For every condition `[before, after]`, add a directed edge and increment `after`'s indegree. Kahn's algorithm repeatedly removes zero-indegree values and releases their outgoing neighbors. If fewer than `k` values are removed, that graph contains a cycle and no matrix can satisfy the corresponding strict order.

**Combine independent positions.** Map each value to its index in the row order and its index in the column order. Place value `x` at the intersection `(row_position[x], column_position[x])`. Because both orders are permutations, each value receives one cell and no two values share a row or column position pair.

Every row condition holds by the topological row order, and every column condition holds by the topological column order. Conversely, any valid matrix induces topological orders in both dimensions, so a cycle in either graph proves impossibility.

## Complexity detail

Let $r = \lvert\texttt{rowConditions}\rvert$ and $c = \lvert\texttt{colConditions}\rvert$. The two graph traversals take $O(k+r+c)$ time and space. Initializing the required $k \times k$ output takes $O(k^2)$ time and space, giving $O(k^2+r+c)$ overall for both.

## Alternatives and edge cases

- **Depth-first topological sort:** Color-based DFS also detects cycles, but an iterative implementation is needed to avoid recursion concerns.
- **Joint placement search:** Backtracking over matrix cells is exponential and ignores the independence of the two partial orders.
- **Cycle in one dimension:** Return `[]` even if the other graph is acyclic.
- **Duplicate conditions:** Parallel identical edges are harmless when indegrees and adjacency entries are updated consistently.
- **Unconstrained value:** It begins with zero indegree and may appear anywhere allowed by the selected topological order.
- **Multiple answers:** Output validation must check constraints rather than compare against one arbitrary matrix.
