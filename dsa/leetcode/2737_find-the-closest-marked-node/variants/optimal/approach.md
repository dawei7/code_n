## General

**Use Dijkstra because every edge weight is positive**

The graph is directed, so only the listed direction `u -> v` is usable. Every weight is at least one, which makes Dijkstra's greedy shortest-path rule valid.

The exact implementation uses the dense, array-based form of Dijkstra rather than a heap. It computes shortest distances from source `s` to every node and only afterward takes the minimum over marked nodes.

**Build a dense adjacency matrix**

`g` is an `n by n` matrix initially filled with infinity. Entry `g[u][v]` represents the cheapest direct edge from `u` to `v`.

Repeated edges are allowed. The assignment:

`g[u][v] = min(g[u][v], w)`

keeps only the lightest parallel edge. A heavier direct edge can never improve a shortest path between the same endpoints, so discarding it is safe.

Missing directed edges remain infinity. The code does not mirror entries, correctly preserving direction.

**Distance and finalized arrays**

`dist[v]` is the best source-to-`v` distance discovered so far. It starts at infinity for every node except `dist[s] = 0`.

`vis[v]` records whether Dijkstra has finalized node `v`. Once finalized, its distance will never improve because all edge weights are nonnegative and it was the smallest unvisited tentative distance.

**Select the closest unvisited node by scanning**

For each of `n` rounds, the inner scan chooses unvisited index `t` with minimum `dist[t]`. Starting `t=-1` allows the first unvisited node to become the candidate.

Unlike heap Dijkstra, this selection costs $O(n)$ per round. It is appropriate for the exact dense-matrix representation and the constraint $n\le500$.

Even when all remaining nodes are unreachable, the scan still selects one of them with infinite distance. Infinity arithmetic then leaves every relaxation unchanged. Repeating until all nodes are visited is safe, though it does extra work.

**Relax every possible outgoing destination**

After marking `t` visited, the algorithm considers every node `j` and applies:

`dist[j] = min(dist[j], dist[t] + g[t][j])`.

If a direct edge exists, the second expression is the length of a path reaching `t` optimally and then taking that edge. If no edge exists, `g[t][j]` is infinity and cannot improve anything.

The matrix scan makes relaxation $O(n)$ for each selected node, regardless of its actual out-degree.

**Why finalizing the minimum is correct**

Assume `t` is the unvisited node with smallest tentative distance. Any alternative path to `t` through another unvisited node must first reach that node with distance at least `dist[t]` and then add a positive edge weight. Such a path cannot be shorter.

Paths through already visited nodes were considered when those nodes were relaxed. Therefore `dist[t]` is final at selection time. Repeating this argument establishes correct shortest distances for every reachable node.

**Choose the closest marked result**

After all rounds, the code computes:

`min(dist[i] for i in marked)`.

If at least one marked node is reachable, this is the minimum shortest-path distance to any marked node. If all are unreachable, the minimum remains infinity and the function returns `-1`.

The source is guaranteed not to be marked, so a zero answer does not arise from selecting `s` itself.

**Trace the first example**

From node zero, direct tentative distances include one to node one and four to node three. Node one is finalized next and relaxes node two to distance four. Both marked nodes two and three then have shortest distance four, so the final minimum is four.

The path of weight six to node three through nodes one and two never replaces its better direct distance four.

**Exact source versus manifest description**

The manifest describes heap-based Dijkstra with early return at the first finalized marked node and complexity $O((n+e)\log n)$. The protected source does neither.

It stores an $n^2$ matrix, performs $n$ linear selections and $n$ full relaxation scans, and evaluates marked nodes only at the end. This document follows that exact behavior.


The matrix preserves the cheapest direct edge for every ordered pair. Dense Dijkstra repeatedly finalizes the unvisited node with minimum tentative distance, which is safe for positive weights, and relaxes every outgoing matrix entry. Hence `dist` contains the true shortest distance from `s` to every reachable node and infinity otherwise. Taking the minimum at marked indices returns the closest marked distance, with `-1` exactly when none is reachable.

## Complexity detail

Let $n$ be the node count and $e$ the input edge count. Initializing the matrix costs $O(n^2)$ time and space. Reading edges costs $O(e)$. The algorithm performs $n$ rounds, each with an $O(n)$ selection and $O(n)$ relaxation scan, for $O(n^2)$ shortest-path time.

Total time is $O(n^2+e)$ and auxiliary space is $O(n^2)$ for `g` plus $O(n)$ for `dist` and `vis`. These are the exact implementation bounds and supersede the heap-oriented manifest summary.

## Alternatives and edge cases

- **Adjacency-list heap Dijkstra:** Achieves $O((n+e)\log n)$ time and $O(n+e)$ space and can return when the first marked node is popped without stale distance.
- **Bellman-Ford:** Handles negative weights but costs $O(ne)$ and is unnecessary because weights are positive.
- **Reverse multi-source search:** Reversing edges and starting from all marked nodes is another valid formulation for the distance to `s`.
- **Repeated directed edges:** Only the minimum weight is retained.
- **Unreachable nodes:** They remain at infinity; dense rounds over them do not alter distances.
- **All marked nodes unreachable:** The final answer is `-1`.
- **Several closest marked nodes:** Only their common minimum distance matters.
- **Directedness:** An edge `u -> v` does not permit travel from `v` to `u`.
- **No self-loops:** Guaranteed, though positive self-loops would not improve a shortest path anyway.
- **Manifest mismatch:** The exact code is dense $O(n^2)$ Dijkstra and does not stop early.
