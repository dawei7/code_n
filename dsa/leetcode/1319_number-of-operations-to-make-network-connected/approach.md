## General

The network consists of connected components. A cable whose endpoints are already connected through other cables is redundant: removing it does not split its component. Such a cable can be relocated to join two different components.

If there are `c` components, at least `c - 1` new inter-component links are necessary and sufficient to connect them. The exact Optimal solution uses disjoint-set union to count both:

- the number of components remaining, stored by repurposing local variable `n`; and
- the number of redundant cables, stored in `cnt`.

**Initial disjoint sets**

`p = list(range(n))` gives every computer itself as parent. Initially, all computers are separate components, so the initial component count is the original `n`.

`find(x)` follows parent pointers to a representative root. Its recursive assignment

`p[x] = find(p[x])`

performs path compression: after finding the root, every node on that search path points directly to it. Later searches through those nodes become faster.

**Processing one cable**

For cable `[a, b]`, the method finds representatives `pa` and `pb`.

If they differ, the cable joins two previously separate components. `p[pa] = pb` merges them, and `n -= 1` reduces the component count by one.

If the representatives are equal, `a` and `b` already have another path between them within the processed graph. This cable is not needed to preserve connectivity of that component. `cnt += 1` records it as available for relocation.

This classification is incremental but exact. Every accepted merge edge belongs to a spanning forest. Every rejected same-component edge creates a cycle relative to that forest and is redundant.

**Why components minus one operations are needed**

One relocated cable can join at most two components, reducing the component count by at most one. Starting with `c` components therefore requires at least `c - 1` operations.

If at least `c - 1` redundant cables exist, choose one component as a hub and use one cable to connect it to each other component. This uses exactly `c - 1` operations and connects the network.

The final expression is:

`-1 if n - 1 > cnt else n - 1`.

At this point, local `n` means `c`, not the original number of computers. If the number of required links exceeds spare cables, connection is impossible. Otherwise, the lower bound is achievable and returned.

**Why counting redundant edges is equivalent to checking total cables**

Suppose the original number of computers is $N$, the final component count is $c$, and there are $m$ cables. The spanning forest accepted exactly $N-c$ merge edges. All other cables are redundant:

$$
\texttt{cnt}=m-(N-c).
$$

The condition `cnt >= c - 1` simplifies to `m >= N - 1`. This is the familiar fact that any connected $N$-vertex graph needs at least $N-1$ edges.

The exact source derives feasibility through redundant counting rather than performing the total-edge check before union processing. Both views are equivalent.

**Following the first example**

For four computers and cables `[0,1]`, `[0,2]`, and `[1,2]`:

- the first cable merges two components;
- the second merges computer 2 into that component;
- the third finds both endpoints already connected, so it increments `cnt`.

Computer 3 remains alone. There are two components and one redundant cable. One operation is required and one spare is available, so the answer is one.

**Why the result is correct**

Disjoint-set representatives partition computers exactly according to connectivity created by processed merge edges. A merge reduces the component count; a same-root cable can be removed without harming that connectivity and becomes a spare.

After every cable is processed, local `n` is the true number of connected components and `cnt` is the number of cables outside a spanning forest. Connecting those components needs exactly `n - 1` cables. The final condition returns that number precisely when enough spares exist, otherwise $-1$.

## Complexity detail

Initializing `p` takes $O(N)$ time and space, where $N$ is the original computer count. Every one of $m$ cables performs two `find` operations and possibly one parent assignment.

The exact source uses path compression but does not use union by rank or union by size. The classic $O((N+m)\alpha(N))$ guarantee requires both path compression and a balancing union rule. Because `p[pa] = pb` always attaches the first root under the second regardless of tree shape, the manifest's inverse-Ackermann bound is stronger than the exact implementation justifies.

A safe broad bound for this unbalanced parent structure is $O((N+m)\log N)$ amortized for path-compression-only sequences, with worse individual finds possible before compression. The parent array and recursion paths use $O(N)$ space.

Adding rank or size and attaching the shallower tree under the deeper one yields the standard $O((N+m)\alpha(N))$ amortized time while preserving $O(N)$ space.

The recursive `find` can follow a deep unbalanced chain before compression and may encounter Python recursion limits on adversarial edge order near $N=10^5$. An iterative find or balanced union avoids that practical risk.

## Alternatives and edge cases

- **Early cable-count check plus component count:** If `len(connections) < N - 1`, return $-1$ immediately; otherwise count components and return `c - 1`. This avoids explicitly counting redundant cables.
- **DFS or BFS components:** Build an adjacency list, count connected components, and combine it with the total-edge feasibility check. Time is $O(N+m)$ but adjacency storage is $O(N+m)$.
- **Union by rank or size:** Pairing it with path compression provides the inverse-Ackermann complexity claimed by the manifest and prevents deep parent chains.
- **Already connected network:** Final component count is one, so zero operations are required regardless of additional redundant cables.
- **Exactly enough cables:** A forest with $N-1$ edges has no spare cycles if disconnected, which cannot occur; if total edges suffice, redundant cables balance the component gaps.
- **Too few cables:** The required `c - 1` exceeds `cnt` and the method returns $-1$.
- **Isolated computers:** Each remains its own disjoint-set component until connected by a merge edge.
- **Cycle edges:** Their endpoints have the same representative, so they increment the spare count.
- **Variable reuse:** After unions, local `n` no longer means the original computer count; it means the current component count. Renaming it `components` would improve clarity.
- **Single computer:** It is already connected and needs zero operations, even with no cables.
- **Recursive find depth:** Unbalanced unions can create a long chain before path compression. Python may fail before the theoretical memory limit.
- **No repeated input edges:** Redundancy still arises through cycles of three or more distinct cables, not only duplicate pairs.
