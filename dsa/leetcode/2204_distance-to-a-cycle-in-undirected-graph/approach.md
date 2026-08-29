## General

In a connected undirected graph with exactly one cycle, every non-cycle node belongs to a tree attached to some cycle node. Repeatedly removing degree-one leaves peels away those trees and leaves only the cycle.

The exact solution records the inward neighbor of each removed node. It then processes removed nodes in reverse order, giving each one distance one more than that neighbor.

The manifest mentions a multi-source BFS after peeling, but the stored source uses this reverse-peel dynamic calculation instead.

**Build mutable neighbor sets**

For every undirected edge `a, b`, the code adds `b` to `g[a]` and `a` to `g[b]`.

Sets make it possible to remove a peeled neighbor from another node's current adjacency in expected constant time. Their current lengths represent degrees in the graph that remains after prior peeling.

The initial queue contains every node whose degree is one.

**Peel leaves toward the unique cycle**

When leaf `i` is popped, it is appended to `seq`. At that moment, its current set contains its one surviving neighbor `j`.

The code removes `i` from `g[j]` and records `f[i] = j`. This neighbor lies one edge closer to the unpeeled core.

If `j`'s degree becomes one after removal, it is now a leaf and is enqueued. Finally `g[i].clear()` marks the removed node as absent from the remaining graph.

**Why cycle nodes are never peeled**

Every cycle node has two cycle neighbors. Tree branches attached to it may be removed, but those two cycle edges remain.

Its residual degree therefore never drops below two during leaf peeling, so it never enters the degree-one queue.

**Why every non-cycle node is peeled**

Contract the unique cycle conceptually into one root. All other nodes form ordinary trees attached to that root.

Every finite tree has a leaf. Removing leaves repeatedly eventually removes all of its nodes from the outside inward. Thus every non-cycle node enters `seq`, while exactly the cycle nodes remain unpeeled.

**Use zero as the cycle distance**

`ans` starts as an all-zero array. Unpeeled cycle nodes keep zero, which is their correct distance to the cycle.

Values for peeled nodes are filled afterward. No explicit cycle-node list is required; absence from `seq` identifies them implicitly.

**Reverse the peel order**

Leaves farthest from the cycle are generally removed before their inward parents. Therefore `seq` records dependencies in the wrong direction for distance calculation: `ans[i]` depends on `ans[f[i]]`, which may not yet be known in forward order.

Iterating `seq[::-1]` reverses those dependencies. The inward neighbor `f[i]` was either peeled later and has already been processed in reverse, or it is a cycle node whose zero value was initialized.

The recurrence

`ans[i] = ans[f[i]] + 1`

then assigns one edge plus the neighbor's shortest distance.

**Why the recorded neighbor lies on a shortest route**

In a tree attached to a unique cycle, a non-cycle node has exactly one path toward the cycle. When it is peeled, all outward descendants have already been removed, and its surviving neighbor is the next node on that unique inward path.

Following `f` repeatedly must eventually reach an unpeeled cycle node. The number of links followed is exactly the graph distance to the cycle, so the recurrence produces the minimum distance.

For a branch cycle–5–6, node six peels first with parent five, then five peels with its cycle neighbor. Reverse processing sets distance of five to one and six to two.

## Complexity detail

The graph has exactly $n$ edges. Building two adjacency entries per edge takes $O(n)$ expected time and space.

Each node is enqueued at most once, and each edge is removed or examined a constant number of times during peeling. Reverse processing visits each peeled node once. Total expected time is $O(n)$.

Neighbor sets, queue, parent array, sequence, and answer each use $O(n)$ space. The manifest's asymptotic bounds match, though its stated second phase differs from the exact reverse sequence.

## Alternatives and edge cases

- **Multi-source BFS from cycle nodes:** After peeling, enqueue every residual cycle node at distance zero and expand outward. This matches the manifest and also runs in linear time.
- **DFS cycle detection:** Find one back edge, mark the cycle path through parents, then traverse attached trees. It works but recursion depth may be large.
- **All nodes on the cycle:** No degree-one node enters the queue, `seq` stays empty, and every answer correctly remains zero.
- **Single long branch:** Peeling records nodes from farthest to nearest; reversal restores distances from nearest to farthest.
- **Several trees on cycle nodes:** Each branch peels independently and uses its own inward parent chain.
- **Degree changes:** A node is enqueued precisely when its residual degree becomes one.
- **Unique-cycle guarantee:** It ensures the residual two-core is exactly one cycle rather than a more complex core.
- **Connected guarantee:** Every peeled parent chain eventually reaches that cycle.
- **Set mutation:** The code removes only currently present leaf edges, so `remove` is valid.
- **Cycle nodes initialized implicitly:** Their zero values need no explicit assignment.
- **No second graph traversal:** Reverse peel order replaces multi-source BFS in the exact source.
- **Input preservation:** Edge descriptions are read into separate mutable sets.
- **Manifest discrepancy:** The solution peels plus reverse-propagates; it does not run the summarized BFS.
