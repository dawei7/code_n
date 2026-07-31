## General

**Choose the middle edge**

Every valid sequence `[a, b, c, d]` has a unique middle edge `[b, c]`.
Therefore, examine each graph edge as that middle pair and choose one outer
neighbor of each endpoint. The four nodes must then be checked for
distinctness.

**Keep only three candidates per endpoint**

For each node, retain its three adjacent nodes with the greatest scores. When
choosing an outer neighbor for `b`, at most two otherwise desirable neighbors
can be forbidden: `c` and the outer node selected for `c`. Consequently, if
any legal neighbor exists, at least one of the three highest-scoring neighbors
is legal. The same argument applies symmetrically to `c`.

Try all at most nine pairs drawn from the two retained lists. Any accepted
combination is a valid four-node path because all three required edges exist
and the nodes are distinct. Conversely, take an optimal sequence and its
middle edge. If either outer endpoint were outside its middle node's top three,
one of the top three would remain distinct from the other three sequence nodes
and would have at least as large a score. Replacing the endpoint would preserve
validity without reducing the total. Thus some optimal sequence is examined.

## Complexity detail

Let $n=\lvert\texttt{scores}\rvert$ and $m=\lvert\texttt{edges}\rvert$.
Building adjacency lists and selecting three neighbors per node takes
$O(n+m)$ time because the retained count is constant. Each edge tests at most
nine outer pairs, so the total time is $O(n+m)$. Adjacency lists use
$O(n+m)$ space; all retained top-neighbor lists together use $O(n)$.

## Alternatives and edge cases

- **All neighbor pairs per middle edge:** This is correct but can take quadratic time when both endpoints have high degree.
- **Enumerate all four-node tuples:** Testing every ordered quadruple costs $O(n^4)$ before graph sparsity helps.
- **Keep only one best neighbor:** The best neighbor may be the opposite middle endpoint or may collide with the chosen outer node.
- **Keep only two neighbors:** Two candidates can both be forbidden by the other middle endpoint and outer endpoint; three are sufficient.
- **No four-node path:** Return `-1`, including for graphs with fewer than three connected edges in any simple chain.
- **Extra edges:** The four selected nodes may have connections beyond the three sequence edges.
- **Disconnected graph:** Components are handled independently as their edges are examined.
- **Positive scores:** Maximization never benefits from omitting a valid sequence once one exists.
