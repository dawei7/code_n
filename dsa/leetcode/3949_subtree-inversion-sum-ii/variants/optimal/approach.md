## General

**Represent a configuration by its nearest selected node.** Root the tree at `0`. For a node $u$ and distance $d\in[0,k]$, store the greatest and smallest final sums attainable inside $u$'s subtree when the nearest selected inversion node in that subtree is at exact distance $d$ from $u$. Distances of $k$ or more are capped at $k$. The capped state also covers a subtree with no selected node.

Both extrema are necessary. Selecting $u$ negates every final value in its subtree, including the effects of compatible inversions already chosen below it. Consequently, the best selected-$u$ result is the negation of the smallest compatible unflipped sum, while the smallest result is the negation of the largest one.

**Merge sibling subtrees without a quadratic distance loop.** Lift a child's distance by one edge before combining it with the children already processed at $u$. Suppose the nearest selected nodes on the two sides are at distances $a$ and $b$ from $u$. Their path passes through $u$, so compatibility requires

$$
a+b\ge k.
$$

If the merged nearest distance is $d=\min(a,b)$, the other distance must be at least $\max(d,k-d)$. Suffix maxima and minima over the distance arrays answer this range query in constant time for each $d$. A complete child merge therefore costs $O(k)$ rather than enumerating all $O(k^2)$ distance pairs.

**Add the option to invert the current root.** After all children have been merged without selecting $u$, selecting $u$ is compatible only with the capped distance-$k$ state: every selected descendant must be at least $k$ edges away. This produces distance state zero. Negate the prior minimum to obtain the new maximum, and negate the prior maximum to obtain the new minimum.

An iterative traversal establishes parent links. Processing its order in reverse ensures that every child state is ready before its parent. Finished child arrays are merged directly into a pending parent accumulator, avoiding recursion and retaining only states still needed by unfinished ancestors or sibling groups.

Every DP state represents exactly the valid configurations with its capped nearest distance. The sibling check enforces the distance rule across child subtrees, child states already enforce it internally, and the distance-$k$ restriction makes selecting $u$ compatible with every descendant. Taking the greatest root state therefore considers every legal inversion subset and returns its maximum sum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each of the $n-1$ child edges is merged once. Lifting, building four suffix-extremum arrays, and evaluating every distance state take $O(k)$ work per merge, so the total running time is $O(nk)$.

Each active node accumulator contains two arrays of length $k+1$. In the worst tree and traversal shape, $O(n)$ accumulators may coexist, giving $O(nk)$ auxiliary space; the graph, parent array, and traversal order use an additional $O(n)$ space.

The benchmark tiers use chains with $(n,k)=(8,8),(16,16),(32,32)$ and record the governing product $nk$ as sizes 64, 256, and 1024. The accepted suffix-extremum merge is linear in that workload. A correct implementation that enumerates every pair of distance states takes $O(nk^2)$ time and should fail only the scaling verdict.

## Alternatives and edge cases

- **Pair every distance state:** The direct child merge is easier to state, but its $O(k^2)$ work per edge becomes $O(nk^2)$ overall.
- **Track only the maximum sum:** This loses the best configuration to negate when the current node is inverted; maximum and minimum sums are dual requirements.
- **Track only inverted ancestors:** The restriction also applies to selected nodes in different child subtrees, so ancestor distance alone cannot validate a merge.
- **Uncapped distances:** Exact distances above `k` are interchangeable for every later compatibility test; capping them prevents the state space from depending on tree height.
- **Nested inversions:** An ancestor and descendant may both be selected when their distance is at least `k`; the descendant region is then negated twice.
- **Sibling inversions:** Two child-subtree selections are compatible precisely when the sum of their lifted nearest distances is at least `k`.
- **`k = 1`:** Any distinct nodes are far enough apart, including adjacent nodes, so many overlapping inversions may be selected.
- **Large `k`:** If the tree diameter is smaller than `k`, at most one inversion node may be selected, but the empty set remains legal.
- **Zero values:** Negation leaves them unchanged, yet their nodes still matter as possible inversion roots and as distances on tree paths.
- **Wide sums:** Up to $5\cdot10^4$ values of magnitude $4\cdot10^4$ may contribute, so fixed-width implementations need a wide integer type.
