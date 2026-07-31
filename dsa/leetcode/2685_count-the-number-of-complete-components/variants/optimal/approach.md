## General

Build an adjacency list and discover each connected component with an iterative depth-first search. During that traversal, count both the component's vertices and the sum of their degrees.

**Why the degree sum identifies completeness**

If a component has $k$ vertices, each vertex in a complete component has degree $k-1$. Its degree sum must therefore be $k(k-1)$. Conversely, a simple connected component cannot contain more than one edge per vertex pair. Reaching the maximum possible degree sum means that none of the $k(k-1)/2$ pairs is missing, so the component is complete. This criterion also handles an isolated vertex: for $k=1$, both sides are zero.

Every vertex is assigned to exactly one traversal. Each incident edge contributes once to the degree of each endpoint, so the accumulated sum is twice the component's edge count. Count the component exactly when that sum equals $k(k-1)$.

## Complexity detail

Let $n$ be the number of vertices and $e$ the number of edges. Building the adjacency list and traversing all components take $O(n+e)$ time. The adjacency list, visited array, and traversal stack use $O(n+e)$ space.

## Alternatives and edge cases

- **Union-find with component statistics:** Union all edges, then aggregate vertex and edge counts by representative. It has near-linear time but needs more bookkeeping than a graph traversal.
- **Check every vertex pair:** After finding a component, testing every possible pair is correct but can take $O(k^2)$ time for a component of $k$ vertices even when the input is sparse.
- **Isolated vertices:** A one-vertex component is complete because there is no pair that could be missing an edge.
- **Degree double-counting:** The traversal sums degrees, so compare against $k(k-1)$ rather than $k(k-1)/2$.
- **Disconnected input:** Reset the per-component counters for every unseen starting vertex while retaining the global visited array.
