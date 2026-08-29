## General

**View each query as a thresholded graph**

A query `[a, b, limit]` allows precisely those edges whose weights are strictly less than `limit`. If those eligible edges were placed into a temporary graph, the answer would be true exactly when `a` and `b` belonged to the same connected component.

Building that graph and searching it independently for every query would repeat almost all work. The key observation is monotonicity: as the limit increases, edges only become eligible; none becomes ineligible. Processing queries from smallest limit to largest therefore lets one evolving connectivity structure serve every query.

**Sort edges and queries by their thresholds**

The source sorts `edgeList` in place by each edge's third value, its weight. It also evaluates `sorted(enumerate(queries), key=lambda x: x[1][2])`. Each enumerated item carries the original query index together with the query, and sorting orders these items by limit without changing the original `queries` list.

The original index matters because the required answer order is the input order, not threshold order. The result array `ans` begins with one false entry per query. After a sorted query is answered, its Boolean is stored at `ans[i]` using that preserved index.

An edge pointer `j` begins at zero. For the current query, the loop consumes every still-unprocessed edge satisfying

`edgeList[j][2] < limit`.

The strict comparison is essential. An edge whose weight equals the limit is forbidden by the contract and must wait for a later query with a larger limit. Since both sequences are sorted, all eligible edges form one prefix of `edgeList`, and `j` never needs to move backward.

**Represent connectivity with disjoint-set union**

The parent array `p` initially contains `p[x] = x` for every node. Each node is therefore the representative of its own one-vertex component.

The nested `find(x)` function follows parent links until it reaches a representative whose parent is itself. On the way back from recursion, `p[x] = find(p[x])` rewrites every visited node's parent directly to the representative. This path compression makes later searches through the same area much shorter.

When an eligible edge `[u, v, weight]` is processed, the assignment

`p[find(u)] = find(v)`

joins the two components by making `u`'s root point to `v`'s root. If they are already connected, both calls return the same root and the assignment changes nothing. Multiple edges between the same endpoints are consequently harmless.

After all edges lighter than the current limit have been joined, `find(a) == find(b)` tests whether the query endpoints share a component. The Boolean is written into the original query position.

**The invariant before every query answer**

Immediately before answering a query with threshold $L$, the disjoint-set structure represents exactly the connected components of the graph containing all and only edges of weight less than $L$.

For the first query, the while loop adds the complete eligible prefix because `j` starts at zero. Assume the invariant held for the preceding, no-larger threshold. Those already added edges remain eligible. The while loop adds exactly the newly eligible edges before stopping at the first weight greater than or equal to $L$. Sorted order proves that no eligible edge remains later in the list and no forbidden edge was added.

Connectivity in an undirected graph is exactly the equivalence relation created by unioning every edge's endpoints. Thus, under this invariant, equal roots mean there is a path made entirely of permitted edges, while different roots mean no such path exists.

**Why later queries can reuse all previous unions**

If the next limit is at least the current one, every edge already admitted still has weight below the new threshold. DSU need not support deletion or rollback. Equal-limit queries add no new edges between them and correctly see the same thresholded graph.

For example, with edges of weights two, four, and eight, a query with limit two admits none of them because equality is not enough. A later query with limit five admits the weight-two and weight-four edges. If those edges chain its endpoints together, the query is true even if no direct edge exists.

**Implementation-specific union behavior**

This exact source uses path compression but does not use rank or component size when selecting which root becomes the parent. That keeps the union statement short, and sorting still dominates the broad bound stated in the manifest. It also means the parent trees can temporarily be more unbalanced than in the textbook rank-plus-compression version. The recursive `find` and this tradeoff are part of the actual implementation and should not be mistaken for union by rank.

## Complexity detail

Let $n$ be the number of vertices, $E$ the number of edges, and $Q$ the number of queries. Initializing `p` and `ans` costs $O(n+Q)$. Sorting edges costs $O(E\log E)$, and sorting the enumerated queries costs $O(Q\log Q)$. The edge pointer processes each edge once; every query is answered once.

With path compression but no rank heuristic, a conservative amortized allowance for the disjoint-set operations is logarithmic per operation, so they fit within $O((E+Q)\log n)$. Combined with sorting, the total is

$$
O\!\left(E\log E+Q\log Q+(E+Q)\log n+n\right),
$$

The sorting and edge/query processing terms fit the manifest's broad $O((E+Q)\log(E+Q))$ form. Strictly, however, the exact source also has the separate $O(n)$ initialization term. Because the constraints allow many isolated vertices, $n$ need not be bounded by $E+Q$; the manifest omits that term. A rank-plus-path-compression DSU would give the familiar near-constant inverse-Ackermann amortized operation term, but that rank heuristic is not present in this file.

The parent array uses $O(n)$ space and `ans` uses $O(Q)$. The sorted enumerated query list uses $O(Q)$ additional storage. Python's in-place sorting can require linear temporary storage, including $O(E)$ for the edge sort. The total is therefore $O(n+E+Q)$, matching the manifest. Recursive `find` also uses stack space proportional to the current parent-chain depth.

## Alternatives and edge cases

- **Breadth-first or depth-first search per query:** Build or filter adjacency and search for each threshold. It is straightforward but can revisit $E$ edges for each of $Q$ queries.
- **Union by rank or size:** Add a balancing array while retaining path compression. This gives stronger standard DSU guarantees and protects recursive depth, at the cost of a little extra code and $O(n)$ space.
- **Minimum spanning forest:** The maximum edge on the forest path determines threshold connectivity, after which binary lifting can answer queries. This is useful for online queries but is more complex than the offline sweep.
- **Queries in original order:** Processing them unsorted would require adding and then removing edges as limits move up and down; ordinary DSU cannot perform those deletions.
- **Weight equal to limit:** It must not be unioned for that query. Replacing `<` with `<=` changes the problem's strict boundary and is incorrect.
- **Equal query limits:** They observe exactly the same set of eligible edges, regardless of their relative order in the sorted list.
- **Parallel edges:** Each is processed at its own weight. Re-unioning an already connected pair is harmless, and a lighter parallel edge may make the connection available earlier.
- **Disconnected graph:** Components that no eligible edge joins keep different roots, producing false without any special case.
- **Indirect path:** Endpoints need not have a direct edge; equality of roots captures any chain of eligible undirected edges.
- **Input mutation:** `edgeList.sort` changes the caller-provided edge order, whereas `queries` itself is not reordered.
- **Deep parent chains:** Because the source does not union by rank and uses recursive `find`, adversarial union orientation can create a deep call before compression; an iterative find or rank heuristic would make the implementation more robust.
