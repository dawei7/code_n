## General

The input began as a tree on `n` nodes and then received one additional undirected edge. A tree is connected and contains no cycle. Adding one edge to a tree preserves connectivity but creates exactly one cycle. Any edge on that cycle can be removed to restore a tree, and when more than one answer is possible, the problem asks for the edge that appears last in the input order.

The solution processes the edges from first to last while maintaining the connected components formed by the edges accepted so far. For each new edge `[a, b]`, it asks one decisive question:

> Are `a` and `b` already connected by the earlier edges?

If they are not connected, the edge joins two previously separate components and cannot create a cycle. If they are already connected, an earlier path from `a` to `b` exists. Adding the new edge completes a cycle, so this edge is redundant.

The data structure used to answer that question is disjoint set union, also called union-find.

**Representing connected components**

The array `p` stores parent links for a collection of rooted trees. Every node in the same disjoint-set tree belongs to the same graph component. The root of such a tree is its component representative and is characterized by `p[root] == root`.

There are `n` graph nodes, and there are also `n` edges because the input is a tree's `n-1` edges plus one added edge. The implementation therefore obtains `n` as `len(edges)` and creates

`p = list(range(len(edges)))`.

This initializes parent entries `0` through `n-1` so that every node starts in its own component.

The source labels graph nodes from `1` through `n`, whereas Python lists use indices `0` through `n-1`. Accordingly, an input endpoint `a` is passed to union-find as `a - 1`, and `b` is passed as `b - 1`. This conversion changes only the storage index; the returned answer preserves the original labels `[a, b]`.

**Finding a component representative**

The nested `find(x)` function follows parent links until it reaches a root. If `p[x] != x`, then `x` is not a representative, and `find(p[x])` continues toward the root.

The assignment

`p[x] = find(p[x])`

performs path compression. It does more than return the representative: it rewrites `x`'s parent to point directly to that representative. Nodes visited during later recursive returns receive the same shortcut. Future `find` calls involving those nodes traverse fewer links.

Path compression never changes component membership. Every rewritten parent is the root of the same tree that `x` already belonged to. It changes only the internal shape used to reach the representative.

**Processing an edge**

For an edge `[a, b]`, the code computes

`pa = find(a - 1)` and `pb = find(b - 1)`.

There are two cases.

If `pa != pb`, the endpoints belong to different components among all edges processed so far. There is no earlier path between `a` and `b`. The current edge safely joins those components, and `p[pa] = pb` performs that union by making one root a child of the other root.

It is important that the code links roots, not the raw endpoint indices. Assigning `p[a - 1] = b - 1` without first finding representatives could break the component forest or fail to merge the complete components correctly.

If `pa == pb`, both endpoints already have the same representative. Earlier accepted edges already provide a path between them. The new edge and that path form a cycle. The code immediately returns the original edge `[a, b]` and does not union it.

**The component invariant**

Immediately before an input edge is considered, two nodes have the same union-find representative exactly when they are connected by the previously accepted input edges.

Initially no edge has been accepted. Every node is its own union-find component, matching a graph with no connections.

When an edge connects different representatives, the graph joins two connected components into one. The assignment `p[pa] = pb` does exactly the same in union-find, so the invariant remains true.

When an edge's representatives are already equal, the graph already contains a path between its endpoints. The edge would not change which nodes are connected; it would only introduce a cycle. Returning at that point is therefore justified.

This invariant connects the data structure's root comparison to the actual graph property the problem asks about.

**Why the returned edge obeys the last-in-input rule**

Because the original graph contains exactly one cycle, the possible removable edges are precisely the edges on that cycle. Consider those cycle edges in input order, and let `e` be the last one.

Before `e` is processed, every other edge of the cycle has already appeared. Those other cycle edges form a path between `e`'s endpoints, even without `e` itself. Therefore both endpoints have the same representative when `e` is reached, and the algorithm returns `e`.

No earlier cycle edge can be returned. When an earlier cycle edge is processed, at least one of the remaining cycle edges—including `e`—has not appeared yet, so the full alternative path connecting its endpoints is not yet present among processed edges. Its endpoints are still in different components, and it is accepted.

Thus the first edge in input order that union-find identifies as cycle-closing is exactly the last-listed edge of the unique cycle. This is why returning immediately satisfies the tie-breaking rule instead of conflicting with it.

**A concrete trace**

For `edges = [[1, 2], [1, 3], [2, 3]]`, the parent structure begins with three separate components.

- Edge `[1, 2]` has different roots, so their components are joined.
- Edge `[1, 3]` also has different roots, so node `3`'s component joins the component containing `1` and `2`.
- For edge `[2, 3]`, both endpoints now resolve to the same representative. Earlier edges give the path `2 -> 1 -> 3`.
- Adding `[2, 3]` would close the cycle, so the method returns `[2, 3]`.

The order matters. The same undirected cycle presented in a different edge order can have a different required answer because the last cycle edge would then be different.

**Why a return after the loop is unnecessary under the contract**

The function has no explicit fallback return. Ordinarily, a Python function that reaches the end would return `None`. Here, however, the source guarantees that the input was formed by adding an edge to a tree. That guarantee ensures one cycle-closing edge exists, so execution must enter the `pa == pb` branch before the loop finishes.

## Complexity detail

Let `n` be the number of nodes. The input contains `n` edges.

The parent array initialization takes `O(n)` time. Each edge performs two `find` operations and, unless it is the redundant edge, one constant-time parent assignment.

The exact implementation uses path compression, but it does not use union by rank or union by size. With both path compression and a balancing rule, the standard amortized bound is `O(n\alpha(n))` for all operations, where `\alpha` is the inverse Ackermann function. That especially strong bound should not automatically be assigned to this literal code because `p[pa] = pb` can attach a large or deep tree beneath another root without considering either tree's rank.

A conservative worst-case bound for the full sequence implemented here is

$$
O(n\log n)
$$

time with path compression alone. In ordinary inputs it behaves very close to linear because repeated finds flatten visited paths. Adding a rank or size array to control unions would justify the familiar `O(n\alpha(n))` amortized bound without changing the algorithm's decisions.

The parent array contains one integer for each node, so auxiliary data-structure space is

$$
O(n).
$$

The recursive `find` also uses call-stack space proportional to the parent-chain depth reached by that call. Because unions are not balanced, a chain can in principle have `O(n)` depth before it is compressed. Thus the strict auxiliary-space bound including recursion is `O(n)`. Path compression reduces later depths but does not provide a constant worst-case stack guarantee.

## Alternatives and edge cases

- **Union-find with rank or size:** Keep a second array recording each root's rank or component size, attach the smaller or shallower tree beneath the larger one, and retain path compression. This preserves the same correctness reasoning and gives the conventional `O(n\alpha(n))` amortized time bound at the cost of another `O(n)` array.

- **Depth-first search before every insertion:** Maintain an adjacency list and, before adding `[a, b]`, search whether `b` is already reachable from `a`. This mirrors the same cycle-closing idea but can take `O(n)` per edge and `O(n^2)` overall.

- **Build the full graph and identify the cycle:** A traversal can find the unique cycle and then scan the input backward to select its last-listed edge. This can be linear, but it needs more graph bookkeeping than the streaming union-find solution.

- **One-based labels versus zero-based storage:** Forgetting `-1` when calling `find` would access the wrong parent entries and could access index `n`, which is outside the array. The output itself must not be decremented because the problem expects original labels.

- **Returning the original edge orientation:** The graph is undirected, but the requested result uses the input pair. Returning `[a, b]` exactly as read preserves that representation.

- **Linking representatives only:** The union statement must use `p[pa] = pb`. Linking arbitrary endpoint nodes can detach or misrepresent existing component trees.

- **Path compression recursion depth:** Without rank or size, adversarial edge order can build a deep parent chain. The problem's bound is small, but an iterative `find` or balanced union would be safer in an environment with a strict recursion limit.

- **The redundant edge appears early among non-cycle edges:** Its absolute input position is irrelevant. It is returned when its endpoints are already connected; the proof shows this is the last edge among the unique cycle's edges, even if unrelated tree edges occur later.

- **Several removable cycle edges:** Removing any cycle edge would mathematically restore a tree, but the required answer is not arbitrary. Forward processing deliberately selects the first edge that closes the cycle, which equals the last such edge in the input.

- **No fallback result:** Returning `None` would be possible for a general acyclic graph, but it is unreachable for a valid input because the extra edge guarantees a cycle.

- **Duplicate undirected edge as the extra edge:** If the source constraints allowed two identical undirected connections, the second one would find its endpoints already connected and would be returned. The union-find reasoning still applies to the resulting two-edge cycle interpretation.

- **Self-loops:** A self-loop would have equal endpoint representatives immediately. The stated input uses two different nodes for each edge, so this behavior is not needed for the canonical contract.

- **Disconnected arbitrary input:** The proof relies on the source guarantee that the graph is a tree plus one edge. Union-find would still detect the first cycle-closing edge in a more general graph, but the unique-cycle and last-answer proof would need to be reconsidered.
