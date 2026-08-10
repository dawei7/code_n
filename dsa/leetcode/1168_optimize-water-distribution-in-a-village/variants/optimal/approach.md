## General

**Turn wells and pipes into one graph problem**

Pipes are ordinary undirected weighted edges between houses. A well is different on the surface because it supplies one house directly rather than connecting two houses.

Introduce a virtual vertex zero representing the water source. Building a well at house `i` is now modeled as selecting an edge

`(0, i, wells[i - 1])`.

If house `i` connects to zero, it has a well. If it reaches zero through other houses and pipes, water flows from some selected well through those connections. Supplying every house is therefore equivalent to connecting vertices zero through `n` in one graph.

The minimum-cost connected subgraph with positive or zero edge costs can be reduced to a tree: any cycle edge can be removed without disconnecting the graph and without increasing cost. The task is exactly a minimum spanning tree over the virtual-source graph.

**Add all well choices as virtual edges**

`enumerate(wells, 1)` pairs the first well cost with house one and so on. Each virtual edge `[0, i, w]` is appended directly to `pipes`.

After this loop, the list contains every choice: the original pipe offers plus one well edge for each house. Parallel pipe offers remain separate edges, which is correct because Kruskal's algorithm can consider their different costs independently.

The exact source mutates the caller-provided `pipes` list by appending virtual edges and then sorting it. This is acceptable for a one-shot judge call, but a caller needing the original order or contents would have to pass a copy.

**Process edges from cheapest to most expensive**

`pipes.sort(key=lambda x: x[2])` orders all well and pipe edges by cost. Kruskal's algorithm scans them in this order.

For edge `(a, b, c)`, `find(a)` and `find(b)` return the current disjoint-set representatives of its endpoints. If the representatives are equal, the endpoints are already connected; adding the edge would form a cycle and provide no new water reachability.

If the representatives differ, the edge joins two components. The code sets `p[pa] = pb`, adds `c` to `ans`, and reduces the number of remaining required unions.

The `find` helper uses path compression. When a vertex's parent is not itself, it recursively finds the root and writes that root back into `p[x]`. Later representative queries along the same path become faster.

The implementation does not keep rank or component size, so it attaches `pa` directly below `pb`. Path compression still avoids repeatedly following unchanged long paths, while edge sorting dominates the documented overall bound.

**Why decrementing `n` counts completion**

The augmented graph has `n + 1` vertices: the virtual source plus `n` houses. A spanning tree on those vertices contains exactly `n` accepted edges.

The method reuses the parameter `n` as the number of successful unions still needed. Every accepted edge decreases the component count by one and decrements `n`. When it reaches zero, exactly `n_original` unions have connected all vertices, so the current edges form a spanning tree and the accumulated cost can be returned immediately.

Virtual well edges guarantee connectivity even if the original pipe graph is disconnected: every house has its own possible edge to vertex zero. Thus the loop must eventually accept enough edges to return.

**Why Kruskal's greedy choice is optimal**

Consider the cheapest scanned edge whose endpoints lie in different current components. Any complete water-supply solution must eventually connect those components, directly or indirectly.

By the minimum-spanning-tree cut property, the cheapest edge crossing a component cut is safe: there exists an MST containing it. If an optimal tree used another more expensive crossing edge, replacing that edge with the cheaper one would preserve connectivity and would not increase cost.

Kruskal repeatedly accepts only such safe edges and rejects only cycle-forming edges. Inductively, every accepted set can be extended to an MST. Once all vertices are connected, the accepted edges themselves are a spanning tree and have minimum possible total cost.

Because well choices are edges in the same graph, this proof simultaneously decides how many wells to build, which houses get them, and which pipes carry their water.

**Trace the first example**

The augmented edges include well edges from zero to houses one, two, and three with costs one, two, and two. Pipe edges one-two and two-three each cost one.

Kruskal can select the well at house one for cost one and both cost-one pipes. Those three edges connect all four augmented vertices for total cost three. More wells would not improve that total.

## Complexity detail

Let `p` be the original number of pipe offers and `e = n + p` be the augmented edge count. Appending well edges takes `O(n)` time. Sorting all edges takes `O(e log e)` time.

The scan performs a constant number of disjoint-set operations per edge. With path compression, this work is below the sorting term for the stated bound, so total time is `O(e log e)`.

The parent array has `n + 1` entries. The augmented edge list contains `e` records; `n` of them are appended to the input list. Total storage associated with the algorithm is `O(e)`.

## Alternatives and edge cases

- **Prim's algorithm:** Starting from the virtual source and growing a tree through a heap also solves the augmented MST in `O(e log n)` time. Kruskal is natural when all choices are already an edge list.
- **Choose the cheapest well only:** Cheap pipes may not connect every house to that well, and building several wells can be better than expensive pipes. The MST evaluates all combinations.
- **Build a well at every house:** This is always feasible but can be unnecessarily expensive when cheap pipes share one well.
- **Ignore the virtual node:** Treating wells separately complicates the choice. Virtual edges unify both purchase types under one cut-property proof.
- **Parallel pipe offers:** Sorting considers them independently; a more expensive parallel edge will normally be skipped after the cheaper one connects the same components.
- **Disconnected original pipe graph:** Virtual well edges connect every component to zero, so a feasible augmented spanning tree always exists.
- **Zero-cost wells or pipes:** Kruskal processes them first, and the same correctness proof applies.
- **Cycle-forming edge:** It is skipped because it adds cost without connecting a new component.
- **Input mutation:** The exact method appends to and sorts `pipes`. Reusing that list after the call will expose the virtual edges and new order.
- **No union-by-rank array:** The source uses path compression only. Its behavior remains correct; rank would affect efficiency constants and tighter disjoint-set analysis, not MST validity.
