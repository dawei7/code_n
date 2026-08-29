## General

**A query asks about connectivity at one weight threshold**

For limit $L$, keep exactly the edges whose weights are strictly less than $L$. The query is true if its two vertices are connected in that thresholded graph.

Many online queries can have limits in any order, so an ordinary union-find that only accumulates edges cannot answer them directly: after adding a heavy edge for one query, it cannot remove that edge for a later smaller limit.

The exact source builds a timestamped union-find forest once. Every parent link records the edge weight at which that link became active. A query follows only links activated before its limit.

**Process edges from lightest to heaviest**

The constructor sorts `edgeList` in ascending order by weight and then calls `union(u,v,dis)` for each edge. This mutates the input edge order.

When an edge of weight `dis` is processed, all earlier union links came from edges with weight no greater than `dis`. Joining its endpoints therefore records the moment at which two previously separate components first become connected during the increasing-weight sweep.

Parallel edges and redundant edges are harmless. If the endpoints already share a current root, `union` returns false and adds no link.

**Store when each parent link becomes valid**

`p[x]` is the parent of node `x` in the final union forest. `version[x]` is the edge weight at which `x` stopped being a root and was attached to that parent.

Roots begin with parent equal to themselves and version infinity. When root `pa` becomes a child of `pb` at weight `t`, the source sets

`version[pa] = t` and `p[pa] = pb`.

The opposite orientation uses the same assignments for `pb`. Every nonroot acquires one permanent parent link and one activation timestamp.

**Balance the permanent forest by rank**

`rank` approximates tree height. The smaller-rank root is attached below the larger-rank root. On equal ranks, the source attaches `pa` under `pb` and increments `rank[pb]`.

There is intentionally no path compression. Rewriting parent links would erase the historical sequence of activation times needed by earlier-threshold queries. Union by rank alone keeps forest height $O(\log n)$.

**Find a representative at a requested time**

`find(x, t)` stops and returns `x` in either of two cases:

- `p[x] == x`: there is no parent.
- `version[x] >= t`: the link from `x` to its parent was created at weight at least `t` and is not allowed under the strict limit.

Otherwise `version[x] < t`, so that parent link corresponds to an eligible edge connection, and the function recursively follows `p[x]`.

The returned node is the representative of `x` in the graph formed by edges with weight strictly below `t`.

**Why equality must stop traversal**

An edge with weight equal to the query limit is forbidden. A parent link created at weight `t = limit` must therefore remain inactive. The condition `version[x] >= t` stops on equality.

For a slightly larger query limit, the same finite version is less than the limit and becomes traversable. This precisely models the strict inequality without subtracting one from large integer limits.

**Use infinity for ordinary current unions**

Inside `union`, calls `find(a)` and `find(b)` omit the time argument, so `t` defaults to infinity. Every finite activation version is less than infinity, and the search reaches the final current root.

A final root also has version infinity, but the parent-equals-self condition returns it. Thus unions operate on the fully accumulated structure built so far, while queries can view an earlier threshold.

**Answer each query independently**

`query(p,q,limit)` compares `find(p,limit)` and `find(q,limit)`. Equal threshold representatives mean the eligible union links connect both vertices. Different representatives mean no path consisting solely of edges below the limit exists.

The data structure is read-only during queries, so query order does not matter.

**Why the timestamp forest is sufficient**

During the sorted sweep, union-find components exactly match graph connectivity after each processed weight. A successful union link records the weight at which two components merge. Following links with timestamps below $L$ reconstructs precisely the merges that would have occurred after processing all edges of weight below $L$.

Therefore two nodes reach the same threshold representative if and only if they are connected by an allowed path. The forest stores connectivity history compactly without storing a complete copy for every weight.

## Complexity detail

Let $m$ be the number of edges and $q$ the number of queries. Sorting costs $O(m\log m)$. Union by rank keeps height $O(\log n)$, so each union performs $O(\log n)$ work and construction costs $O(m\log n)$ after sorting. Initialization is $O(n)$.

Each query performs two historical finds, costing $O(\log n)$. Total time is

$$
O(m\log m+m\log n+n+q\log n),
$$

consistent with the manifest's broad construction-and-query bound.

The three arrays `rank`, `p`, and `version` each have length $n$, so the persistent structure itself uses $O(n)$ space. Recursive find uses $O(\log n)$ stack. The manifest's $O(n\log n)$ space is a loose upper bound; this exact timestamp-per-parent implementation does not allocate logarithmic versions per node.

## Alternatives and edge cases

- **Offline query sorting:** Sort all queries by limit and use ordinary DSU while adding eligible edges. It is excellent when queries are known together, but this class must answer calls after construction.
- **Minimum spanning forest plus binary lifting:** Two vertices are eligible when the maximum edge on their forest path is below the limit. It gives $O(\log n)$ queries with $O(n\log n)$ tables.
- **Search per query:** DFS or BFS using only light edges can cost $O(n+m)$ for each call.
- **Weight equal to limit:** The timestamp link is not followed because the condition is strict.
- **No edges:** Every distinct-node query is false.
- **Disconnected graph:** Separate final union roots remain separate for every limit.
- **Parallel edges:** The lighter edge may connect components; later redundant edges add no historical link.
- **Equal-weight unions:** All links receive that weight and remain inactive for a query with the same limit.
- **Query order:** It has no effect because historical find does not mutate the forest.
- **Input mutation:** Constructor sorting permanently reorders `edgeList`.
- **No path compression:** This is deliberate to preserve timestamp semantics; rank bounds depth.
- **Infinity defaults:** They expose the fully built component structure during construction, while finite limits expose history.
