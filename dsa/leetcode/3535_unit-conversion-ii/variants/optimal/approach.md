## General

Treat the conversions as a weighted graph. A stated conversion `[u, v, factor]` gives an edge from `u` to `v` with weight `factor`: one unit of `u` becomes `factor` units of `v`. Traversing that edge backward multiplies by the modular inverse of `factor`. Because every nonzero factor is invertible modulo the prime $10^9+7$, both directions are well-defined.

Define `from_root[x]` as the number of units of `x` equal to one unit of unit `0`. Set `from_root[0] = 1`, then traverse the graph once. If an edge from an already visited unit `u` to an unvisited unit `v` has weight `w`, assign `from_root[v] = from_root[u] * w` modulo $10^9+7$. The connectivity guarantee reaches every unit, and the unique conversion sequence prevents conflicting assignments.

For a query `[source, target]`, one unit of `0` equals `from_root[source]` units of `source` and `from_root[target]` units of `target`. Dividing these equal quantities shows that one unit of `source` equals

$$
\frac{\texttt{from_root[target]}}{\texttt{from_root[source]}}
$$

units of `target`. Modular division is multiplication by the denominator's inverse, so this ratio answers the query without another graph traversal.

## Complexity detail

Let $Q$ be the number of queries. Building and traversing the $n-1$ conversion edges takes $O(n)$ time, and each query takes $O(1)$ time with respect to the input size, for $O(n+Q)$ total time. Modular inverse exponentiation uses $O(\log(10^9+7))$ arithmetic operations; the modulus is fixed, so this is constant with respect to $n$ and $Q$. The adjacency list, traversal stack, and root factors use $O(n)$ space; the returned list uses $O(Q)$ output space.

## Alternatives and edge cases

- **Graph search for every query:** Following the unique path separately is correct but can take $O(nQ)$ time on a long chain.
- **Store only stated edge directions:** A query or root traversal may need to reverse a conversion, so every edge needs its inverse direction.
- **Multiply ordinary fractions directly:** Numerators and denominators can grow extremely large; modular multiplication and inverses keep every intermediate bounded.
- **Self-conversion:** The ratio of any root factor to itself is one.
- **Edges directed toward unit 0:** The reverse weighted edge lets the traversal proceed regardless of the orientation in `conversions`.
- **Factor equal to $10^9$:** It is nonzero modulo $10^9+7$ and therefore still has a valid modular inverse.
