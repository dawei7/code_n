## General

**Turning maximum removals into minimum necessary connectivity**

Alice can traverse type 1 and type 3 edges, while Bob can traverse type 2 and type 3 edges. An edge is removable exactly when discarding it does not prevent either person from reaching every node. Equivalently, the method retains only edges that merge previously disconnected components in at least one required traversal graph. Every edge that merely closes a cycle is unnecessary and can be counted as removable.

The implementation maintains two disjoint-set union structures, `ufa` for Alice and `ufb` for Bob. Each structure records the connected components currently formed by edges available to that person. A successful `union` merges two different components and returns `True`, meaning the edge contributes new connectivity. If both endpoints already have the same representative, `union` returns `False`, meaning the edge is redundant for that structure.

**Why shared edges are processed first**

Type 3 edges are more valuable than private edges because one retained physical edge can connect components for both Alice and Bob. The first pass processes every type 3 edge before either type 1 or type 2 edge. Whenever such an edge connects two previously separate components, it is added to both union-find structures. Whenever it connects nodes already joined through earlier shared edges, it helps neither person and `ans` is incremented.

This ordering is essential to maximizing removals. If Alice and Bob first used separate private edges to make the same connection, a later shared edge might appear redundant even though retaining the one shared edge and removing two private edges would use fewer total edges. Giving shared edges priority captures their two-for-one value before private choices can obscure it.

There is a precise reason the code checks only `ufa.union(u, v)` in the condition for a type 3 edge. Before the second pass starts, both structures have received exactly the same successful type 3 unions and no private union. Therefore, they represent identical partitions throughout the first pass. If the edge connects different Alice components, it also connects different Bob components, so `ufb.union(u, v)` must succeed. If it is redundant for Alice, it is redundant for Bob as well. The unchecked Bob return value is safe because of this synchronization invariant.

**How the disjoint-set structure works**

For `n` nodes, `p` initially stores `[0, 1, ..., n - 1]`, so every node is its own representative. `size` begins with one for every component, and `cnt = n` records how many components remain.

Input edges name nodes from one through `n`, but the arrays are zero-indexed. The `union` method converts endpoints with `a - 1` and `b - 1` before calling `find`. This conversion happens in one place, which keeps the internal representation consistent.

The `find` operation follows parent links to a representative. On the recursive return path, it assigns every visited node directly to that representative. This path compression makes future searches through the same area very short.

When two representatives differ, `union` attaches the smaller component below the larger one according to `size`. If `size[pa] > size[pb]`, `pb` becomes a child of `pa`; otherwise, `pa` becomes a child of `pb`. The equality case may choose either root, so attaching `pa` below `pb` is valid. The surviving root’s size increases by the absorbed size, `cnt` decreases by one, and the method returns `True`.

If the representatives are already equal, the edge cannot reduce the component count. The method immediately returns `False` without changing parents, sizes, or `cnt`.

**Processing private edges**

After all shared edges have been considered, the second pass scans the full edge list again:

- a type 1 edge is offered only to Alice’s structure;
- a type 2 edge is offered only to Bob’s structure;
- type 3 edges do nothing in this pass because they were handled already.

For a private edge, the expression `ans += not ufa.union(u, v)` or its Bob equivalent uses Python’s Boolean arithmetic. `False` behaves like zero and `True` behaves like one. A successful union returns `True`, so `not True` adds zero because the edge must be retained. A failed union returns `False`, so `not False` adds one because the edge is redundant and removable.

Private edges cannot substitute for one another across users. A type 1 edge that helps Alice says nothing about Bob’s components, and a type 2 edge that helps Bob says nothing about Alice’s. Maintaining two structures keeps those connectivity requirements separate after the common shared foundation has been built.

**Why the removable count is maximal**

Within any union-find structure, an edge whose endpoints are already connected can be deleted without changing that structure’s connected components. Conversely, an edge that merges two currently separate components is necessary for the particular forest selected so far.

The first pass builds a maximal forest from shared edges. Every retained shared edge reduces both users’ component counts with one physical edge. Any discarded shared edge lies within a component already created by other shared edges and therefore cannot improve either traversal graph. This gives the greatest possible shared connectivity before private edges are used.

The second pass extends Alice’s shared forest with only the type 1 edges needed to connect her remaining components, and independently extends Bob’s with only necessary type 2 edges. Each retained private edge reduces exactly the corresponding component count. Every rejected private edge is a cycle edge for its user and can be removed safely.

No solution can use fewer private connections after obtaining less shared connectivity: replacing a useful shared merge would require restoring its effect separately for Alice, Bob, or both. Thus prioritizing every useful shared merge and then retaining only component-merging private edges minimizes the number of retained physical edges. Since the input edge count is fixed, minimizing retained edges maximizes removable edges.

**Detecting impossibility**

After both passes, `ufa.cnt == 1` means all nodes belong to one Alice component, and `ufb.cnt == 1` means the same for Bob. Only when both conditions hold does the method return `ans`. If either count exceeds one, some nodes remain disconnected for that user even after every usable edge was considered. Removing fewer edges cannot invent a missing connection, so the required state is impossible and the correct return value is `-1`.

## Complexity detail

Let $N$ be the number of nodes and $E$ the number of edges. The code scans the edge list twice, which is $2E$ iterations and therefore $O(E)$ iterations asymptotically. Each relevant iteration performs one or two disjoint-set operations.

Path compression together with union by size gives amortized $O(\alpha(N))$ time per `find` or `union`, where $\alpha$ is the inverse Ackermann function and grows so slowly that it is effectively constant for practical input sizes. The total time complexity is $O(E\alpha(N))$. Initializing the two parent and size arrays costs $O(N)$; the complete bound can be written $O(N+E\alpha(N))$, and connectivity inputs ordinarily summarize the edge-processing term as $O(E\alpha(N))$.

Each union-find structure stores a parent array and a size array of length $N$. There are two such structures, plus constant-size counters and loop variables. Constants do not affect asymptotic notation, so the auxiliary space complexity is $O(N)$. The algorithm does not copy the edge list.

## Alternatives and edge cases

- **Processing edges in input order:** This can retain private edges before discovering shared replacements, losing the opportunity for one type 3 edge to serve both users. Shared edges must receive priority for the greedy maximum-removal argument.
- **One union-find for both users:** After shared edges, Alice and Bob can gain different connections from types 1 and 2. A single partition cannot represent both states, so two structures are necessary.
- **Graph traversal after every proposed removal:** Removing an edge and running DFS or BFS for both users can test validity, but repeated connectivity checks are far more expensive and complicate restoration. Union-find identifies cycle edges incrementally.
- **Building two graphs and taking arbitrary spanning trees:** Separate spanning trees may choose two private edges where one shared edge could serve both. Any such approach still needs a rule that maximizes shared participation; the shared-first DSU does this directly.
- **Redundant type 3 edge:** During the first pass, the Alice and Bob partitions are identical. If its endpoints are already connected in one, they are connected in both, so the edge contributes one to `ans`.
- **Why Bob’s shared union result is ignored:** It cannot disagree with Alice’s result during the shared-only pass. That fact would stop being true if private edges were interleaved, which is another reason the two-pass order matters.
- **Boolean addition in Python:** `not union(...)` is one only for a failed union. A port to a language without Boolean-to-integer conversion should use an explicit conditional increment.
- **One node:** Both structures start with `cnt == 1`, so connectivity is already satisfied. Every supplied self-contained redundant edge would be removable under the contract’s edge rules.
- **Already connected by shared edges:** All later private edges join endpoints within an existing component for their respective user and are counted as removable.
- **Only private edges:** The method can still connect each user independently if their respective edge sets span all nodes. Otherwise, the final component-count check returns `-1`.
- **One user disconnected:** Even if the other structure has one component, both people must traverse the whole graph. The conjunction in the final return correctly rejects the instance.
- **Parallel edges:** After one copy connects the endpoints, later copies of the same usable type are redundant. Union-find naturally counts them as removable.
- **Self-loops:** A self-loop never joins different components, so `union` returns false and the edge is removable; it cannot help global connectivity.
- **One-based endpoints:** The subtraction inside `union` is required. Omitting it would leave node `n` outside a length-$N$ array and would misalign every other node.
- **Recursive `find` depth:** Union by size prevents tall adversarial trees, and path compression flattens them further. The combination supports the stated amortized bound and keeps recursion shallow in practice.
- **Disconnected final graph:** Returning the number of cycle edges would be misleading when full traversal was never achievable. The final `-1` check takes precedence over `ans`.
