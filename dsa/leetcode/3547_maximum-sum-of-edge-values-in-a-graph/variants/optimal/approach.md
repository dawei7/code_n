## General

Because the graph is connected and every degree is at most two, its shape is forced. It is a simple path when `len(edges) == n - 1`, and a simple cycle when `len(edges) == n`. The identities and ordering of the supplied node labels do not otherwise affect the maximum: any path can receive the values in any linear order, and any cycle can receive them in any cyclic order.

**The maximizing path order.** An exchange argument on four values shows that large values should be adjacent to other large values while the smallest values are pushed to the two endpoints, where each participates in only one product. Repeatedly applying that exchange yields, up to reversal, the order

$$
1,3,5,\ldots,\text{largest odd},\text{largest even},\ldots,6,4,2.
$$

This order also gives a convenient recurrence. Let $P_n$ be its path score. When the new largest value $n$ is inserted into the central edge of the order for $n-1$, that edge's contribution is replaced by two products and the score increases by $n^2-2$. The same local exchange inequality proves that no other insertion can gain more. Since $P_1=0$,

$$
P_n=\sum_{k=2}^{n}(k^2-2)
=\frac{n(n+1)(2n+1)}{6}-2n+1.
$$

**Closing a cycle.** The corresponding optimal cyclic order places values $1$ and $2$ next to each other as well as at the two ends of the maximizing path order. Closing that path therefore adds exactly $1\cdot2=2$. The same exchange rule rules out a better cyclic arrangement, so a cycle's maximum is $P_n+2$.

The formula uses only `n`; the edge count selects whether the graph is the path or cycle case. Python's arbitrary-precision integers safely hold the result.

## Complexity detail

The calculation performs a fixed number of arithmetic operations and reads the stored edge-list length, so it takes $O(1)$ time and $O(1)$ auxiliary space. The input has already been constructed before `solve` is called; the algorithm neither traverses nor copies it.

## Alternatives and edge cases

- **Construct the maximizing order:** Building the odd-ascending/even-descending sequence and summing adjacent products is correct, but takes $O(n)$ time and space instead of evaluating its sum directly.
- **Traverse and classify the graph:** Degree counting or graph walking also distinguishes a path from a cycle, but connectivity and the degree bound make `len(edges)` sufficient.
- **Try every assignment:** Enumerating node-value permutations takes $O(n!)$ time and is infeasible even for modest `n`.
- **Path endpoints:** Values `1` and `2` occupy the two degree-one positions so larger values each contribute to two products.
- **Cycle closure:** A connected degree-two cycle has exactly `n` edges and gains the additional product $2$ over the optimal path score.
- **Smallest legal graph:** For `n = 2`, the connected simple graph has one edge and the formula returns `2`.
- **Node labels and edge order:** Relabeling nodes or reordering `edges` cannot change the graph's path-or-cycle shape or the answer.
