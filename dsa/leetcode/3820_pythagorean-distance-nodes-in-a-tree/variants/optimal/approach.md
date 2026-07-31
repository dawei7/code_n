## General

In an unweighted tree, one breadth-first traversal from a source computes that source's distance to every node. Build an undirected adjacency list, then run BFS separately from `x`, `y`, and `z`. Store the three resulting distance arrays.

For each node, read its entries from those arrays, sort the three values, and call them `a`, `b`, and `c`. Count the node when $a^2+b^2=c^2$. Sorting is important because the target order does not identify which distance is the potential hypotenuse.

Each BFS assigns a node its shortest edge-count distance from its target. A tree has exactly one path between any two nodes, so this shortest distance is also the length of that unique path required by the statement. Therefore, the three stored values for a node are exactly `dx`, `dy`, and `dz`. The final test is the definition of a Pythagorean triplet applied after ascending sorting, so a node is counted if and only if it is special.

## Complexity detail

Let $N$ be the number of nodes. A tree has $N-1$ edges. Building the adjacency list and each of the three traversals takes $O(N)$ time; testing all nodes also takes $O(N)$ because sorting three values is constant work. The total running time is $O(N)$.

The adjacency list, three distance arrays, and BFS queue use $O(N)$ space.

The benchmark defines size as $N$ and uses a path with targets at both endpoints and the midpoint. Each target traversal is linear. A slower definition-direct method that launches a fresh tree traversal from every candidate node to discover its three target distances performs $O(N^2)$ work on the path.

## Alternatives and edge cases

- **Depth-first traversal from each target:** Iterative DFS also computes tree distances in $O(N)$ time per target because every node has a unique path from the source.
- **Traverse from every candidate node:** Recomputing distances for each node is correct but repeats almost the same work and can take $O(N^2)$ time.
- **LCA preprocessing:** Lowest-common-ancestor data can answer many arbitrary distance queries, but three complete traversals are simpler and already linear for this fixed set of targets.
- **Use the target order as `a`, `b`, `c`:** This is incorrect because the largest distance can correspond to any of `x`, `y`, or `z`; sort before applying the equation.
- **Zero distances:** A target's distance to itself is zero, and triples such as $(0,d,d)$ satisfy the stated equation. Positivity is not required.
- **Pairwise-distinct targets:** The targets are different nodes, but their distances from a candidate node may still be equal.
- **Deep trees:** Use an iterative traversal so a legal path of length near $10^5$ does not overflow Python's recursion limit.
- **Squared distances:** The maximum distance is $N-1$; Python integers represent its square exactly without overflow.
