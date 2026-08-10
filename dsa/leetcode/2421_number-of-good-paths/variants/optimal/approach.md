## General

**View a good path at the moment its maximum value becomes available**

In a tree, exactly one simple path connects any two nodes. Two equal-valued endpoints with value $v$ form a good path precisely when every node on their unique connecting path has value at most $v$. Imagine activating nodes from smallest value to largest value. After all nodes with value at most $v$ are active, two nodes of value $v$ are connected if and only if their path contains no value greater than $v$. That is exactly the good-path condition.

This observation turns path enumeration into dynamic connectivity. A disjoint-set union structure, also called union-find, maintains which activated nodes are connected as edges become usable.

**Prepare adjacency and component state**

The adjacency list `g` stores both directions of every undirected edge. The parent list `p` initially makes each node its own component. The nested `find` function follows parent links to a representative and applies path compression on the way back, shortening later searches.

The structure named `size` is a dictionary of counters. Initially, `size[i][vals[i]] = 1` because the singleton component rooted at node `i` contains one endpoint of that node's value. During processing of a particular value `v`, `size[root][v]` records how many nodes of value `v` are currently in that component. Counts for lower values no longer need to generate paths at a later value, which is why the union step only updates the count for the current `v`.

Every single node is already a good path, so `ans` starts at `n`. The union logic then counts only paths with distinct endpoints.

**Activate nodes in non-decreasing value order**

The loop iterates over `sorted(zip(vals, range(n)))`. Each pair is `(value, node)`, so sorting processes smaller values first and uses the node index only to order ties. When node `a` of current value `v` is processed, the algorithm examines each neighbor `b`.

If `vals[b] > v`, that neighbor is not yet allowed in a path whose maximum is $v$, so the edge is skipped for now. It will be reconsidered from the higher-valued endpoint when that endpoint's turn arrives.

If `vals[b] <= v`, every node already joined through prior processing has value at most `v`, and this edge is safe to activate. The representatives `pa` and `pb` identify the two endpoint components. If they are already equal, the edge connects nodes already known to be connected and no union or new path count is needed. Otherwise the edge merges two components.

**Why multiplying component counts gives exactly the new paths**

Immediately before merging distinct components, let `size[pa][v]` be the number of current-value nodes on one side and `size[pb][v]` the number on the other. Choosing one value-$v$ endpoint from the first component and one from the second creates

$$
\texttt{size[pa][v]} \cdot \texttt{size[pb][v]}
$$

new unordered endpoint pairs. Their unique tree paths become connected by this merge, and all nodes on those paths have values at most $v$. Each pair is therefore a new good path.

No other new good path with maximum $v$ appears at this merge. Endpoints already in the same old component were counted when they first became connected, while endpoints with lower values do not both equal $v$. The product is added to `ans`, `pa` is attached beneath `pb`, and the count of value-$v$ nodes is combined with `size[pb][v] += size[pa][v]`.

Attaching roots without rank is valid for correctness. Path compression keeps later representative searches efficient enough for the stated $O(n \log n)$ overall bound, whose sorting step already dominates.

**Ties and repeated edge visits**

Nodes with equal value are processed one at a time. That is safe: edges between equal-valued nodes become eligible as soon as either endpoint is processed, and the counters merge progressively. If three value-$v$ groups of sizes $x$, $y$, and $z$ become connected, the successive additions might be $xy$ and $(x+y)z$. Their sum is $xy+xz+yz$, exactly one count for every pair drawn from different original groups.

Every undirected edge appears twice in `g`. A second visit usually finds the same representative on both sides and does nothing, so paths are not double-counted. The fact that a path and its reverse are the same is also respected: the multiplication chooses one endpoint from each of two distinct components without assigning a directional order.

**Why every and only good path is counted**

Consider any non-singleton good path with endpoint value $v$. Just before all relevant value-$v$ unions finish, every node on its path is eligible because its value is at most $v$. As edges along that unique tree path are activated, there is a first union that connects the two endpoint components. At that moment, the endpoints contribute exactly once to the product added by that union.

Conversely, every pair counted by a union has equal endpoint value $v$, and the union-find components and joining edge contain only nodes of value at most $v$. Their unique connecting path is therefore good. Singleton paths were counted once in the initial `n`. These categories are disjoint and exhaustive, so the final answer is correct.

## Complexity detail

Let $n$ be the number of nodes; the tree has $n-1$ edges. Building the adjacency list takes $O(n)$ time and space. Sorting the $n$ `(value, index)` pairs takes $O(n \log n)$ time and $O(n)$ working space in Python.

The adjacency loops inspect two entries per edge, so there are $O(n)$ union-find operations. With path compression, these operations are efficient; even using a conservative logarithmic amortized bound because the implementation does not use rank or size for parent selection, they contribute at most $O(n \log n)$. Thus the manifest's overall $O(n \log n)$ time bound holds, with sorting as the clear principal term.

The adjacency list, parent list, sorted pairs, and per-component counters together use $O(n)$ space. Although `size` is a dictionary of `Counter` objects, the algorithm creates one initial value entry per node and combines only current-value counts needed by roots; total live bookkeeping remains linear for this tree-processing pattern. Recursive `find` can use stack frames along a parent chain before compression. The stated auxiliary bound remains $O(n)$, while an iterative `find` could avoid recursion-stack risk.

## Alternatives and edge cases

- **Group nodes by value before unioning:** Process all nodes sharing $v$ as a batch, union every edge to an already active neighbor, then count how many value-$v$ nodes lie in each component and add $\binom{c}{2}$. This is a common equivalent formulation and can make tie handling more explicit.
- **Depth-first search from every endpoint:** Searching paths separately repeats large parts of the tree and can degrade to $O(n^2)$, which is too slow for $3 \cdot 10^4$ nodes.
- **Lowest common ancestor machinery:** LCA can identify paths, but determining the maximum node value on every equal-valued endpoint pair still leaves potentially quadratic many pairs. Incremental connectivity counts them in aggregate.
- **Union by rank or component size:** Adding a balancing array gives the classic near-constant amortized union-find guarantee and prevents deep parent chains. The exact source uses path compression alone.
- **One node:** `ans` starts at 1, there are no edges or unions, and 1 is returned.
- **All values distinct:** No two distinct endpoints can have the same value, so only the $n$ singleton paths are good. Every multiplication has a zero on at least one side for the current value.
- **All values equal:** Every pair of nodes has a path containing only that value. The result becomes $n + \binom{n}{2} = n(n+1)/2$.
- **Higher-valued bridge:** Two equal low-valued endpoints separated by a higher node are never connected during the low value's processing, so their invalid path is not counted.
- **Reverse paths:** Endpoint pairs are created only when two components merge, not once in each direction, so a path and its reverse contribute one.
- **Repeated adjacency visits:** The representative equality check prevents an already activated edge from producing a second union or duplicate count.
