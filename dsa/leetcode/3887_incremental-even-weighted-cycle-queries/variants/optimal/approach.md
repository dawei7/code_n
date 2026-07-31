## General

**Replace cycle sums with vertex potentials**

Because every weight is $0$ or $1$, a cycle has even total weight exactly when the XOR of its edge weights is $0$. A component satisfies this condition for every cycle if and only if its vertices can receive binary potentials such that every retained edge obeys

$$
\text{potential}(u) \mathbin{\mathtt{xor}} \text{potential}(v) = w.
$$

Along any path, intermediate potentials cancel, so the path's weight parity is the XOR of its endpoint potentials. Conversely, if every edge agrees with the potentials, XORing the equations around a cycle cancels every vertex twice and leaves cycle parity $0$.

**Store relative potential in a disjoint-set union**

Maintain the usual parent and component-size arrays. In addition, `parity[x]` is the XOR difference between vertex `x` and its current parent. After `find(x)` performs path compression, `parity[x]` is the difference between `x` and the returned root.

If a proposed edge joins different roots, it creates no cycle and must be accepted. Attach the smaller component to the larger one. If the endpoint-to-root parities are $p_u$ and $p_v$, the required difference between the two roots is

$$
p_u \mathbin{\mathtt{xor}} p_v \mathbin{\mathtt{xor}} w.
$$

Storing that value on the attached root makes the new edge equation true without changing any equation inside either old component.

**Validate edges that close a cycle**

When both endpoints already have the same root, the accepted graph fixes the parity of every path between them as $p_u \mathbin{\mathtt{xor}} p_v$. The new edge closes only even-weighted cycles precisely when its weight equals that value. Accept it in that case; otherwise reject it and leave the disjoint-set state unchanged.

Initially every isolated vertex has potential $0$, so the invariant holds. The merge argument preserves it across edges joining components, and the same-root test admits exactly the constraints consistent with the established potentials. By induction, every counted edge is safe and every rejected edge would create an odd-weight cycle.

## Complexity detail

Let $N$ be the vertex count and $M$ the number of proposals. Initialization takes $O(N)$ time. Union by size and path compression make the $O(M)$ find/union operations take $O(M\alpha(N))$ amortized time, for $O((N+M)\alpha(N))$ total time. The parent, size, and parity arrays use $O(N)$ space.

The benchmark defines size as the number $M$ of chain-edge proposals on $M+1$ vertices. Every edge is accepted. Parity DSU processes the sequence in near-linear time, while a correct implementation that searches the growing component for a path between each proposed pair performs $\Theta(M^2)$ total work.

## Alternatives and edge cases

- **Recolor the whole graph after each proposal:** A fresh BFS or DFS correctly detects inconsistent parity constraints, but repeatedly traversing the growing graph is quadratic on long accepted sequences.
- **Search for an existing endpoint path:** Deriving its parity by graph traversal works, yet unsuccessful searches between separate components can repeatedly scan large components before each merge.
- **Ordinary union-find without parity:** Connectivity alone detects whether an edge closes a cycle but cannot determine whether that cycle's weight sum is odd or even.
- **Edge between separate components:** It cannot form a cycle, so it is always accepted regardless of weight.
- **Redundant consistent edge:** An edge inside a component is still accepted when its weight agrees with the established endpoint parity; the DSU structure need not change.
- **Rejected proposal:** It contributes nothing and must not influence any later parity relation.
- **Disconnected graph:** Each root defines its own arbitrary potential offset, which does not affect relations inside that component.
- **Weight zero:** Its endpoints must have equal potentials; weight one requires different potentials.
