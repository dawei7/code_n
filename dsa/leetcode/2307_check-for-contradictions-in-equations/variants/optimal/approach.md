## General

Treat every variable as a graph vertex and every equation $a/b=k$ as a weighted relationship. The important question is not merely whether two variables are connected, but what ratio their existing component already implies.

A weighted disjoint-set structure stores `parent[x]` together with `ratio[x]`, where `ratio[x]` is the value of $x / \texttt{parent[x]}$. During `find`, path compression multiplies the ratios along the path. Afterward, `ratio[x]` directly represents $x / \texttt{root}$.

For a new equation $a/b=k$, first find both roots. If the roots differ, the equation joins two previously independent components. Attaching $a$'s root below $b$'s root requires the new root weight

$$
\frac{\texttt{root}_a}{\texttt{root}_b}
= k \cdot \frac{b/\texttt{root}_b}{a/\texttt{root}_a}.
$$

If the roots are already equal, the component implies $a/b = \texttt{ratio[a]} / \texttt{ratio[b]}$. Comparing that result with $k$ detects exactly the equations that close a cycle inconsistently. Relationships in separate components cannot contradict one another, so processing every equation this way is sufficient.

## Complexity detail

Let $m$ be the number of equations and $v$ the number of distinct variables. Path compression gives amortized $O(\alpha(v))$ work per disjoint-set operation, so all equations take $O(m\alpha(v))$ time. The parent and ratio maps store one entry per variable, using $O(v)$ space.

## Alternatives and edge cases

- **Weighted graph search:** Add reciprocal edges and search for an existing path before inserting each equation. This is correct, but repeated searches can take $O(mv)$ time.
- **Logarithmic potentials:** Storing logarithms turns products into sums and can reduce overflow concerns, but the problem guarantees that ordinary double precision is enough and logarithms introduce their own rounding behavior.
- **Disconnected variables:** Independent components impose no relationship on each other and can be joined by any first equation between them.
- **Repeated or reversed equations:** Once both variables share a root, the implied ratio check handles either orientation without special cases.
- **Tolerance boundary:** A difference below $10^{-5}$ is accepted; a difference equal to or above that threshold is a contradiction.
