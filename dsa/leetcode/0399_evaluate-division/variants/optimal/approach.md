## General
**Attach a multiplicative weight to each parent link**

Use disjoint-set union over variables. For every variable `x`, store `weight[x] = x / parent[x]`, and for every root store its component size. A root is its own parent with weight one. During path compression, multiply weights along the old path so the compressed value becomes `x / root`.

**Translate an equation into a root-to-root ratio**

For `a / b = value`, first find both roots and their compressed weights. Let `r = value * weight[b] / weight[a]`, so `r = root_a / root_b`. Attach the smaller component below the larger one. If `root_a` becomes the child, store weight `r`; if `root_b` becomes the child, store the reciprocal `1 / r`. Either orientation preserves the supplied equation while union by size keeps parent trees shallow.

**Answer connected queries by dividing root weights**

If either queried variable is unknown or their roots differ, no relationship connects them and the result is `-1.0`. Otherwise both weights use the same root, so `a / b = (a / root) / (b / root) = weight[a] / weight[b]`.

**Why all implied equations remain consistent**

Each union adds exactly one equation-consistent link between two previously separate components. Path compression replaces a chain by a direct root link while preserving the product of its ratios. Inductively, every variable's stored root ratio equals the product implied by the input equations, so connected query quotients are correct.

## Complexity detail
Let `e` be the equation count, `q` the query count, and `v` the number of variables. Weighted find and union have amortized $O(\alpha(v))$ time with path compression and union by size, where `α` is the inverse Ackermann function. Total time is $O((e + q) \alpha(v))$, and the parent, weight, and size maps use $O(v)$ space.

## Alternatives and edge cases
- **Weighted graph plus DFS or BFS per query:** is straightforward but may traverse $O(v + e)$ relationships for every query.
- **Precompute every connected pair:** gives constant-time queries but can require $O(v^2)$ time and space.
- **Floyd-Warshall-style closure:** is convenient only for small variable sets and costs cubic preprocessing.
- A known variable divided by itself equals `1.0`.
- An unknown variable divided by itself still returns `-1.0`.
- Variables in different components have no derivable ratio.
- Reciprocal edges are implicit in each stored equation.
