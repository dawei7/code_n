## General

Root the tree at node 0. For each node $v$, the only information its parent needs is the best value in $v$'s subtree under two conditions: the parent edge is excluded, leaving all $k$ incident slots available for child edges, or the parent edge is included, leaving only $k-1$ child slots.

First suppose every edge from $v$ to a child $c$ is excluded. The resulting base is the sum of each child's optimum with its parent edge excluded. Including edge $(v,c)$ of weight $w$ changes the contribution for that child from `without_parent[c]` to $w+\texttt{with_parent[c]}$. Its incremental gain is therefore

$$
w+\texttt{with_parent[c]}-\texttt{without_parent[c]}.
$$

The child subtrees are otherwise independent. Sort these gains and add the largest positive $k$ gains when $v$'s parent edge is absent, or the largest positive $k-1$ gains when it is present. A non-positive gain is never useful because removing edges is allowed.

Processing nodes in reverse rooted order ensures both child states are known before their parent. The base covers the optimal choice that excludes every child edge. Any feasible choice can then include only as many child edges as the available slots, and its improvement is exactly the sum of their gains; selecting the largest positive gains is optimal. Thus both states are correct at every node, and the root's state without a parent edge is the required global optimum.

## Complexity detail

Let $d_v$ be the number of children of node $v$. Building and rooting the adjacency list takes $O(n)$ time. Sorting gains costs $O(d_v\log d_v)$ at each node, whose sum is $O(n\log n)$ in the worst case. The adjacency list, traversal order, parent array, gains, and two DP arrays use $O(n)$ space.

The benchmark defines `size` as $n$ and uses a star with $k=n/2$, so the center has $\Theta(n)$ competing gains. The reference sorts them. A correct baseline that repeatedly scans all remaining gains to select each of the best $k$ values requires $\Theta(n^2)$ work on these tiers.

## Alternatives and edge cases

- **Bounded min-heap:** Keeping only the best $k$ gains gives $O(n\log k)$ time and is useful when $k$ is much smaller than high node degrees.
- **Repeated maximum scans:** Selecting one best remaining gain at a time is correct but can take $O(n^2)$ time on a star.
- **Enumerate retained edge subsets:** This directly enforces degrees but has exponential time in the number of edges.
- **Greedy by raw edge weight:** An edge's real benefit includes the capacity it consumes in its child's subtree, so raw weights alone are insufficient.
- **Non-positive gain:** Exclude that child edge; retaining fewer than `k` edges is legal.
- **Parent-edge state:** When the parent edge is retained, exactly one of the node's degree slots is already occupied.
- **`k = 1`:** The retained edges form a weighted matching, which the same two-state recurrence handles.
- **Large depth:** Iterative rooting and reverse processing avoid recursion-depth failure on a path of $10^5$ nodes.
