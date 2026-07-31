## Function Contract

**Inputs**

- `n`: The number of labeled tree nodes.
- `edges`: The undirected edges of the tree.
- `s`: The initial lowercase character at every node.
- `queries`: The ordered update and path-query command strings.

Let $T=(V,E)$ be the tree with $V=\{0,\ldots,n-1\}$. For nodes $u$ and $v$, let $P(u,v)$ be the unique inclusive path between them. Operations are stateful: an `update` replaces one node's current character but produces no output, while a `query` observes every update that precedes it.

A multiset of letters can be rearranged into a palindrome exactly when at most one letter has an odd frequency. Therefore, a path query returns `true` precisely when

$$
\left\lvert
\left\{c\in\{\texttt{a},\ldots,\texttt{z}\}
\mid \operatorname{count}_{P(u,v)}(c)\equiv 1\pmod 2\right\}
\right\rvert \le 1.
$$

**Return value**

Return the query results in chronological order. The returned array has one boolean for each command beginning with `"query"` and no entry for an `"update"` command.
