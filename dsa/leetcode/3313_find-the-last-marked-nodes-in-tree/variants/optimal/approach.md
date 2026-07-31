## General

Starting from node `i`, a node is marked after exactly its graph distance from `i` seconds. The requested last-marked node is therefore any vertex with maximum distance from `i`, so the problem is to find one farthest vertex for every possible source.

A standard tree property reduces all $n$ searches to one diameter. Run a breadth-first search from an arbitrary vertex to find a farthest vertex $A$. A second search from $A$ reaches a farthest vertex $B$, making $A$ and $B$ endpoints of a diameter. Record every distance from $A$, then run a third search from $B$ and record those distances too.

For every vertex $v$, at least one farthest vertex is a diameter endpoint, and its eccentricity is

$$
\max(\operatorname{dist}(v,A),\operatorname{dist}(v,B)).
$$

Choose $A$ when its recorded distance is larger and $B$ otherwise. Equal distances mean both endpoints are valid, so consistently choosing $B$ respects the contract. Breadth-first search is iterative, avoiding recursion-depth limits on a path-shaped tree.

## Complexity detail

Let $n$ be the number of vertices. A tree has $n-1$ edges, and each of the three breadth-first searches visits every vertex and traverses every edge at most twice. Constructing the answers is another linear pass. Total time is $O(n)$ and the adjacency list, distance arrays, and queue use $O(n)$ space.

## Alternatives and edge cases

- **Search from every starting node:** Running a separate traversal for every vertex costs $O(n^2)$ time on a tree and is too slow for $n=10^5$.
- **Rerooting dynamic programming:** Two tree-DP passes can compute every eccentricity, but retaining the responsible endpoint complicates tie handling without improving the asymptotic bounds.
- **Multiple farthest vertices:** The contract permits any tied answer; selecting one of the two fixed diameter endpoints is sufficient.
- **Two-node tree:** The two vertices are the diameter endpoints, and each is the unique last-marked node for the other.
- **Path-shaped tree:** Iterative traversal avoids a Python recursion overflow at the maximum depth.
