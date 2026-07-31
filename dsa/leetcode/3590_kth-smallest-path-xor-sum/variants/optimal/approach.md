## General

The path XOR for a node depends only on its parent's path XOR:

$$
x_0=\texttt{vals[0]}, \qquad x_v=x_{\texttt{par[v]}}\mathbin{\mathrm{XOR}}\texttt{vals[v]}.
$$

Build the child lists and traverse outward from root `0` once to compute every $x_v$. Queries can then ignore the original node values and ask only for ranked distinct values among the $x_v$ values in a subtree.

Process nodes in reverse traversal order so every child subtree is complete before its parent. Associate each completed subtree with an ordered set containing its distinct path XORs. At a node, retain the largest child set, insert every value from each smaller child set into it, and finally insert the node's own path XOR. This is small-to-large merging: whenever a distinct value is copied from one retained set into another, the destination has at least the source's size, so the containing set's scale grows geometrically. A value can therefore participate in only $O(\log n)$ such migrations.

The ordered set supports membership, insertion, and zero-based order statistics in $O(\log n)$ time. After constructing node `u`'s set, a query `[u, k]` returns the element at index `k - 1` when that index exists, or `-1` otherwise. Group queries by their node before the postorder pass and write results to their original query indices.

Duplicate path XORs disappear at insertion, which is essential: subtree size is not the same as the number of available ranks. Reusing the largest set is also essential; merging every child into a fresh set could repeatedly copy large subtrees and become quadratic.

## Complexity detail

Let $n$ be the number of nodes and $q$ the number of queries. Tree construction, path-XOR computation, and query grouping take $O(n+q)$ time. Small-to-large merging moves each distinct value through at most $O(\log n)$ light merges, and each ordered-set membership or insertion costs $O(\log n)$, giving $O(n\log^2 n)$ merge time. Each order-statistic query costs $O(\log n)$, for total time $O(n\log^2 n+q\log n)$.

The accepted native implementation retains references to completed ordered sets, whose conservative worst-case storage is $O(n\log n)$ across the merge history; grouped queries and answers add $O(q)$. The self-contained app adapter releases child bags after merging and uses $O(n+q)$ live storage, but the branch bound remains the conservative $O(n\log n+q)$ shared guarantee.

## Alternatives and edge cases

- **Per-query subtree traversal:** Gathering, deduplicating, and sorting a subtree independently for every query can cost $O(qn\log n)$.
- **Unordered sets alone:** Hash sets merge efficiently but cannot return a $k$th smallest value without an additional ordering structure.
- **Euler tour plus range queries:** A subtree becomes an interval, but distinct order statistics over arbitrary intervals require substantially more involved offline structures such as Mo's algorithm or multidimensional counting.
- **Repeated XOR sums:** Multiple nodes with the same path XOR contribute one ordered-set entry and one rank.
- **Original-root semantics:** A query rooted below node `0` does not restart the XOR at its queried node.
- **Non-topological node numbers:** A parent may have a larger numeric index than its child; build child lists and traverse from `0` instead of assuming index order.
- **Input preservation requirement:** The native source stores `(par, vals, queries)` in `narvetholi` midway through the function.
