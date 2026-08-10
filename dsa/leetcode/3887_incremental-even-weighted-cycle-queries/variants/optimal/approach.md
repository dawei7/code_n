## General

**Even binary-weight sums are XOR constraints**

Every edge weight is zero or one. A cycle has even total weight exactly when the XOR of its edge weights is zero.

A graph has even weight on every cycle precisely when each vertex can be assigned a binary potential `color[v]` such that every accepted edge `(u,v,w)` satisfies

$$
color[u]\mathbin{\mathrm{XOR}}color[v]=w.
$$

If such potentials exist, XORing the edge equations around a cycle cancels every vertex potential twice, leaving zero, so the cycle weight parity is even.

Conversely, within a connected component, choose a root potential and define every vertex's potential as the XOR weight along a path from the root. All cycles being even makes this definition independent of which path is chosen.

The source maintains these relative potentials with a weighted union-find.

**Meaning of the arrays**

`parent[v]` and `size[v]` have their ordinary disjoint-set meanings.

`parity[v]` stores the XOR potential difference from `v` to its current parent:

$$
parity[v]=color[v]\mathbin{\mathrm{XOR}}color[parent[v]].
$$

After `find(v)` completes path compression, `parent[v]` is the component root and `parity[v]` becomes

$$
color[v]\mathbin{\mathrm{XOR}}color[root].
$$

Roots have parity zero to themselves.

**Path compression must update parity**

Suppose `v` currently points to `p`. Before recursion,

`parity[v]` is the XOR from `v` to `p`.

Recursive `find(p)` compresses `p` to the root and leaves `parity[p]` as the XOR from `p` to that root. Therefore the XOR from `v` to the root is

`parity[v] ^ parity[p]`.

The source saves `previous_parent` before changing the parent pointer, recursively finds the root, then applies that XOR update. This ordering preserves the meaning of weighted paths through compression.

**Proposal inside one connected component**

After finding both endpoints, `left_parity` and `right_parity` are their XOR differences to the same root. The existing path parity between them is

$$
leftParity\mathbin{\mathrm{XOR}}rightParity.
$$

Adding edge weight `w` creates a cycle whose total parity is

$$
leftParity\mathbin{\mathrm{XOR}}rightParity\mathbin{\mathrm{XOR}}w.
$$

It is even exactly when

`left_parity ^ right_parity == weight`.

If equal, the edge is accepted. It adds a redundant consistent constraint but does not change union-find structure. If unequal, accepting it would create an odd cycle, so the source rejects it and leaves all state unchanged.

**Proposal between different components**

When roots differ, no path currently connects the endpoints. Adding the edge creates no cycle, so it is always safe and the accepted count increases.

The union must establish a root-to-root parity that makes the new edge equation true. Let `L` and `R` be roots. We know

$$
color[left]\mathbin{\mathrm{XOR}}color[L]=leftParity
$$

and the analogous right equation. Required root difference is

$$
color[L]\mathbin{\mathrm{XOR}}color[R]
=leftParity\mathbin{\mathrm{XOR}}rightParity\mathbin{\mathrm{XOR}}weight.
$$

The source calls this `root_parity`.

XOR is symmetric, so the same bit represents `L` relative to `R` or `R` relative to `L`. Whether union by size attaches left root under right or right under left, assigning `root_parity` to the attached root establishes the constraint.

**Why preserving constraints preserves every cycle**

Initially each isolated vertex has a trivial potential assignment.

Joining components with one edge cannot create a cycle and the chosen root parity combines their potential systems consistently.

Adding a same-component edge is accepted only when it agrees with the potentials already implied by the component. Therefore the potential invariant exists after every accepted proposal. As shown initially, this guarantees every cycle—not only the newest fundamental cycle—has even weight.

Rejected edges do not enter the graph and do not alter the invariant.

**Examples**

After accepting weights one on edges zero-one and one-two, the existing path from zero to two has parity `1^1=0`. A proposed zero-two edge of weight one disagrees and would form an odd cycle, so it is rejected.

If that final edge has weight zero, it matches the existing path parity. The resulting cycle XOR is zero and all three edges are accepted.

Consistent extra edges inside a component still increase the returned accepted count even though they do not merge components.

## Complexity detail

Initializing arrays takes `O(N)` time. Each of `M` proposals performs a constant number of union-find operations. Path compression and union by size give amortized `O(\alpha(N))` time per operation, for

$$
O((N+M)\alpha(N))
$$

total time.

The parent, size, and parity arrays each have `N` entries, so auxiliary space is `O(N)`. These bounds match the manifest.

Recursive `find` depth is kept small by union by size and path compression. All parity values remain one bit.

## Alternatives and edge cases

- **Rebuild the graph and search cycles after every proposal:** Correct but can take quadratic or worse total time. Weighted DSU checks only the newly imposed parity relation.
- **Ordinary union-find without parity:** It knows whether endpoints are connected but not the XOR weight of their existing path, so it cannot judge a same-component edge.
- **BFS coloring per proposal:** Maintain or recompute binary potentials with graph traversal. This is conceptually direct but costs linear component work per query.
- **Duplicate-vertex expansion:** Represent each vertex's two parity states in a `2N`-node DSU. It can enforce XOR constraints but uses more nodes than weighted parity storage.
- **Weight zero:** Endpoints must have equal potentials.
- **Weight one:** Endpoints must have opposite potentials.
- **Different components:** Always accept because no cycle is created.
- **Same component, consistent edge:** Accept and count it without union.
- **Same component, inconsistent edge:** Reject without modifying state.
- **Multiple cycles from one edge:** Potential consistency ensures all cycles involving it are even, not only one chosen path cycle.
- **Distinct edge guarantee:** The source does not need duplicate-edge handling, though a repeated consistent edge would also satisfy the parity test.
- **Undirected symmetry:** XOR root relation is identical whichever root becomes parent.
- **Path-compression update order:** Save the old parent and combine its compressed parity; overwriting too early loses the intermediate relation.
- **AI-generated source comment:** The weighted-union invariant independently establishes correctness regardless of provenance.
