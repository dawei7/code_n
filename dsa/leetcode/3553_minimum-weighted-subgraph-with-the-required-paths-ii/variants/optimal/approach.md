## General

For query nodes $a$, $b$, and $c$, the minimum valid subtree is the union of their three unique pairwise paths. Every edge in this union separates one of the three terminals from the other two, so exactly two of the pairwise paths cross that edge. Consequently, if $d(x,y)$ is the weighted tree distance between two nodes, the answer is

$$
\frac{d(a,b)+d(a,c)+d(b,c)}{2}.
$$

Efficient queries therefore reduce to efficient tree distances. Root the tree at node `0`, and compute each node's depth, parent, and weighted distance from the root with one iterative traversal. Build a binary-lifting table in which `ancestors[k][v]` is the $2^k$-th ancestor of node `v`.

To find the lowest common ancestor of two nodes, first lift the deeper node until their depths match. Then examine powers of two from largest to smallest, lifting both nodes whenever their proposed ancestors differ. Their common parent after this process is the LCA. Root distances then give

$$
d(x,y)=f(x)+f(y)-2f(\operatorname{LCA}(x,y)),
$$

where $f(v)$ is the weighted distance from the chosen root to $v$. Three such distance queries and the half-sum formula produce each answer. The choice of root affects individual LCAs but not the resulting pairwise distances or subtree weight.

## Complexity detail

Let $n$ be the number of nodes and $q$ the number of queries. The tree traversal costs $O(n)$, and constructing $O(\log n)$ ancestor levels costs $O(n\log n)$. Each LCA and distance query costs $O(\log n)$; three distances per request therefore cost $O(q\log n)$ overall. Total time is $O((n+q)\log n)$ and the ancestor table uses $O(n\log n)$ space. All other stored arrays and the adjacency list use $O(n)$ space.

## Alternatives and edge cases

- **Per-query tree traversal:** Explicitly finding and uniting the two source-to-destination paths is correct but costs $O(nq)$ in the worst case.
- **Euler tour with range-minimum queries:** This can support constant-time LCAs after heavier preprocessing, but binary lifting is simpler and already satisfies the constraints.
- **Unweighted depth:** Edge counts cannot replace `root_distance`; the positive weights may differ substantially.
- **One node between the other two:** The union is just the path between the two outer terminals, and the pairwise half-sum still counts every edge once.
- **Three separate branches:** The formula includes all three arms from their branching point without double-counting shared prefixes.
- **Large totals:** A path may contain nearly $10^5$ edges of weight $10^4$, so implementations need integer storage beyond 32-bit signed range; Python integers grow automatically.
- **Root node in a query:** Its root distance is zero, and the same LCA formulas apply without a special case.
