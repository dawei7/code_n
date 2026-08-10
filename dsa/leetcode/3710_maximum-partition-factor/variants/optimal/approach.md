## General

The objective maximizes a minimum distance, which suggests asking a feasibility question:

> For a proposed factor $D$, can the points be divided into two groups so every pair in the same group has Manhattan distance at least $D$?

Any pair whose distance is **less than** $D$ is too close to share a group. Its two endpoints must receive opposite group labels.

This creates a graph:

- one vertex per point;
- an edge between every pair with distance below $D$;
- every edge requires opposite colors.

Such a two-group assignment exists exactly when this graph is bipartite.

The exact source does not binary-search $D$. It sorts all pair distances and adds opposite-color constraints from smallest to largest using a parity-aware disjoint-set union structure. The first distance that creates a contradiction is the optimal partition factor.

**Why close pairs become opposite constraints**

Suppose a split has partition factor at least $D$. By definition, every intra-group pair has distance at least $D$. Therefore, any pair at distance below $D$ cannot lie in the same group and must be opposite.

Conversely, if every pair below $D$ is assigned opposite colors, any pair that remains in one color group has distance at least $D$. The coloring therefore defines a split with factor at least $D$.

For $n\ge3$, assigning two colors can always produce two nonempty groups when the constraint graph is bipartite. If an edge exists, its endpoints already use both colors. If there are no edges, any one point can be placed in the second group.

The special $n=2$ case is handled separately because both required groups are singletons and contain no intra-group pair. The statement defines its factor as zero.

**Generating distance constraints**

For every unordered pair $i<j$, the source computes:

$$
\lvert x_i-x_j\rvert+\lvert y_i-y_j\rvert
$$

and stores tuple:

`(distance, i, j)`.

There are $n(n-1)/2$ tuples. Sorting them means constraints are processed from closest pairs to farthest pairs.

At the moment distance $d$ is reached, all constraints with distance below $d$ have already been incorporated.

**Parity-aware disjoint-set meaning**

Ordinary DSU records whether two vertices are connected. This version also records their relative colors.

`parity[node]` represents the XOR difference between the color of `node` and the color of its parent:

- zero means the same color;
- one means opposite colors.

After `find(node)` compresses the path, `parity[node]` becomes the color difference directly between `node` and its component root.

Two nodes in the same component then have:

$$
\operatorname{color}(a)\mathbin{\mathrm{XOR}}\operatorname{color}(b)
=
\texttt{parity}[a]\mathbin{\mathrm{XOR}}\texttt{parity}[b].
$$

**Path compression while preserving parity**

If `node` has a non-root parent `previous`, recursive `find(previous)` first attaches `previous` to the root and updates its parity to that root.

The source then performs:

`parity[node] ^= parity[previous]`.

Before this operation, `parity[node]` describes node-to-previous color difference. XOR-ing previous-to-root difference produces node-to-root difference, because relative binary colors compose with XOR.

Only after preserving this relationship can the parent pointer safely be compressed to the root.

**Checking an edge inside one component**

Every distance edge requires:

$$
\operatorname{color}(\textit{first})
\mathbin{\mathrm{XOR}}
\operatorname{color}(\textit{second})
=1.
$$

After both finds, if roots match, their relative color is already determined.

- If `first_parity != second_parity`, they are already opposite and the new edge is compatible.
- If the parities are equal, the component already forces them to the same color, but the new edge requires opposite colors. This closes an odd cycle and makes the graph non-bipartite.

The source immediately returns the current `distance` on this contradiction.

**Merging two components with an opposite relation**

If roots differ, the edge can connect the components consistently. Union by size attaches the smaller root under the larger root, keeping trees shallow.

The required parity between the two roots is derived from:

$$
(\textit{first}\oplus\textit{rootFirst})
\oplus
(\textit{rootFirst}\oplus\textit{rootSecond})
\oplus
(\textit{rootSecond}\oplus\textit{second})
=1.
$$

Solving for the root-to-root relation gives:

`first_parity ^ second_parity ^ 1`.

That value is assigned to `parity[root_first]` when `root_first` becomes a child of `root_second`.

If the roots are swapped for union by size, the corresponding endpoint parities are swapped too. XOR is symmetric, so the same formula remains valid.

**Why the first contradictory distance is the answer**

Suppose the first contradiction occurs while processing an edge of distance $d$.

Before any distance-$d$ contradiction, all edges with distance strictly below $d$ formed a bipartite graph. A valid two-coloring of those lower-distance edges places every pair closer than $d$ in opposite groups. Hence a partition factor of at least $d$ is attainable.

Once the contradictory distance-$d$ edges are required, the graph is non-bipartite. Any factor strictly greater than $d$ would require **all** pairs at distance $d$ to be opposite as well as all closer pairs, which is impossible.

Therefore:

- $d$ is feasible because pairs at distance exactly $d$ are allowed to share a group;
- anything larger than $d$ is infeasible.

So $d$ is the maximum partition factor.

Processing equal-distance edges in any order is safe. A contradiction may occur partway through one distance group, but the graph using only smaller distances was feasible, and the subset of current-distance edges already suffices to show that every larger threshold is impossible.

**Square example**

For the four corners of a $2\times2$ square, side-neighbor distances are two and diagonal distances are four.

The distance-two constraints form an even cycle and are bipartite. They color opposite corners the same. When a diagonal distance-four edge is added, it demands opposite colors for two points already forced equal, creating the first contradiction at four.

A partition into diagonal pairs has intra-group distance four, so returning four is exact.

**Why a contradiction must eventually occur for $n\ge3$**

After all pair edges are included, the constraint graph is the complete graph $K_n$. Any three vertices form a triangle, which is not bipartite. Thus the loop necessarily finds a contradiction and returns for every $n\ge3$.

The trailing `return 0` is only a defensive fallback; the explicit $n=2$ branch handles the one contractual case without a contradictory triangle.

## Complexity detail

There are:

$$
E=\frac{n(n-1)}{2}=O(n^2)
$$

pair edges. Computing them takes $O(n^2)$ time, and sorting takes:

$$
O(E\log E)=O(n^2\log n).
$$

Parity-DSU processing performs a constant number of find/union operations per edge. With path compression and union by size, this costs $O(E\alpha(n))$, dominated by sorting.

Total time is $O(n^2\log n)$.

The edge list stores $O(n^2)$ tuples. DSU arrays use $O(n)$ space. Total auxiliary space is $O(n^2)$.

## Alternatives and edge cases

- **Binary search the factor:** For each candidate, build the graph of closer pairs and test bipartiteness in $O(n^2)$. This also works but repeats distance comparisons; sorted incremental constraints reuse prior work.
- **Rebuild graph coloring after every distance:** Repeated BFS coloring can lead to cubic work. Parity DSU maintains color relations incrementally.
- **Ordinary DSU without parity:** Connectivity alone cannot distinguish same-color from opposite-color relationships or detect odd cycles.
- **Exactly two points:** Both groups must be singletons, and the statement defines the factor as zero.
- **Duplicate points:** Their distance is zero. Three mutually coincident points create a zero-distance triangle, so the maximum factor can be zero.
- **Equal edge distances:** Their processing order does not affect the returned distance; the first contradiction within the group still certifies that threshold.
- **Singleton group:** It contributes no pair, so only distances inside the other group constrain the factor.
- **Negative coordinates:** Absolute differences compute Manhattan distance normally.
- **Large coordinates:** A distance can reach $4\cdot10^8$, which fits standard signed 32-bit range but is handled safely by Python integers.
- **Complete bipartite lower graph:** It remains feasible until an edge requiring two already same-colored vertices to differ creates an odd cycle.
