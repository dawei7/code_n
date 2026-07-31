## General

Write each positive integer as a product of prime powers. Its **square-free kernel** is the product of exactly those primes whose exponents are odd. In a product of two integers, every prime exponent is even exactly when the two integers have identical square-free kernels. Therefore `nums[node] * nums[ancestor]` is a perfect square if and only if the two assigned values have the same kernel.

**Precompute every bounded kernel.** Let $M=\max(\texttt{nums})$. Sieve the primes through $\sqrt M$ and initialize `kernel[value] = value`. For each prime $p$, divide $p^2$ from every value containing it; repeat at powers $p^4,p^6,\ldots$ so every pair of $p$ factors is removed. What remains has exactly the primes with odd original exponents and is therefore the square-free kernel. Slice-based updates keep this bounded preprocessing app-friendly without changing its asymptotic work.

**Count only the active root path.** Build the undirected adjacency list and traverse from root `0`. Maintain a map from kernel to the number of nodes with that kernel currently on the ancestor path. On entry to a node, that map count is exactly its $t_i$, so add it to the answer before inserting the current node. On exit, remove the node's contribution. Explicit enter/exit stack events avoid recursion-depth limits.

The active map never contains a sibling or descendant, only strict ancestors of the entering node. Kernel equality is equivalent to the perfect-square product test, so every added count is valid and every valid ancestor is represented. Summing these entry counts gives precisely the requested total.

## Complexity detail

Let $M=\max(\texttt{nums})$. The sieve takes $O(M\log\log M)$ time, the kernel recurrence takes $O(M)$, and adjacency construction plus DFS takes $O(n)$. Overall time is $O(M\log\log M+n)$. The sieve and kernel arrays use $O(M)$ space, while the graph, traversal stack, and active counts use $O(n)$, for $O(M+n)$ total auxiliary space.

## Alternatives and edge cases

- **Test every ancestor product directly:** Walking the complete ancestor chain for each node can take $O(n^2)$ time on a path-shaped tree.
- **Factor every node independently:** Trial division up to $\sqrt M$ repeats work across equal and related values and can cost $O(n\sqrt M)$.
- **Global kernel frequencies:** Counting all nodes with a matching kernel incorrectly includes siblings, descendants, and nodes in other branches; only the active root path is relevant.
- **Recursive DFS:** A valid tree may be a path of $10^5$ nodes, which can exceed language recursion limits.
- **Root-only tree:** When `n = 1`, there are no non-root nodes or ancestor pairs, so the answer is `0`.
- **Sibling matches:** Even if two sibling values have a perfect-square product, neither node is the other's ancestor and the pair must not be counted.
- **All kernels equal on a chain:** Every earlier node is valid for every later node, so the result can reach $n(n-1)/2$ and requires a wide integer.
