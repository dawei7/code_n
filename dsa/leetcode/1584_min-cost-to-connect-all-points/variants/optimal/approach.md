## General

**Recognizing a minimum spanning tree**

Treat every point as a graph vertex. Any pair of points can be connected, so the graph is complete. The undirected edge between points `i` and `j` has weight equal to their Manhattan distance:

$$
\lvert x_i-x_j\rvert+\lvert y_i-y_j\rvert.
$$

The required connections must make all vertices reachable while leaving exactly one simple path between every pair. A connected undirected graph with exactly one simple path between each pair is a tree. Among all such spanning trees, the task asks for the one with minimum total edge weight: a minimum spanning tree, or MST.

The checked-in implementation uses Prim’s greedy algorithm. It grows one tree from vertex zero. At each step, it selects the unvisited vertex that can be attached to the current tree by the cheapest available edge.

**Materializing the complete weighted graph**

The solution first creates `g` as an $N\times N$ matrix of zeros. For every pair with `i < j`, it computes the Manhattan distance `t` and assigns both:

`g[i][j] = g[j][i] = t`.

Writing both entries reflects that connections are undirected: the cost from `i` to `j` equals the cost from `j` to `i`. Restricting the computation to `j > i` prevents calculating every distance twice. The diagonal remains zero because connecting a point to itself is never a candidate MST edge.

This matrix makes all later edge-weight lookups constant time. It is important to describe this exact allocation because it differs from a matrix-free Prim implementation, which could calculate Manhattan distances during relaxation and use only linear auxiliary space.

**The meaning of `dist` and `vis`**

`vis[j]` records whether point `j` has already been added to the growing tree.

For an unvisited point `j`, `dist[j]` stores the cheapest edge found so far from any visited point to `j`. In other words, it is the least cost currently known for attaching `j` to the tree.

Initially, no actual point is in the tree, and every distance is infinity. The assignment `dist[0] = 0` creates an imaginary zero-cost connection to point zero. This lets the ordinary selection loop choose point zero first without a special-case insertion. Adding its zero distance to `ans` does not affect the final MST cost.

**Selecting the next point**

The outer loop runs exactly $N$ times, once for every point. During each iteration, the code scans all indices to choose an unvisited point with minimum `dist`:

`if not vis[j] and (i == -1 or dist[j] < dist[i])`.

The candidate index `i` begins at `-1`, meaning no candidate has been chosen yet. The `i == -1` part makes the first unvisited point become the current candidate without reading `dist[-1]` as the comparison basis. Later unvisited points replace it only when their attachment cost is strictly smaller.

Ties do not require special handling. If several points have the same minimum attachment cost, choosing any of them is safe for Prim’s algorithm. The strict comparison simply retains the first minimum encountered.

Because the graph is complete, every unvisited point has an edge to every visited point. After point zero has been selected, every remaining `dist` becomes finite. Therefore, each later outer iteration always finds an unvisited index.

Once `i` is selected, `vis[i] = True` permanently adds that point to the tree, and `ans += dist[i]` pays for its cheapest connecting edge. The parent endpoint is not stored because the problem asks only for total cost, not the list of selected connections.

**Relaxing all remaining attachment costs**

After adding point `i`, the solution scans every unvisited point `j` and performs:

`dist[j] = min(dist[j], g[i][j])`.

Before this update, `dist[j]` is the cheapest edge from any previously visited point to `j`. The newly visited `i` adds exactly one new possible crossing edge, with weight `g[i][j]`. Taking the minimum therefore restores the invariant that `dist[j]` is cheapest across all currently visited vertices.

After the first iteration, this fills `dist[j]` with the direct distance from point zero. On later iterations, some entries decrease when a newly added point offers a cheaper connection. Entries never need to increase because expanding the visited set can only introduce more choices.

**Why the greedy edge is safe**

At any iteration, divide the graph into the visited points and unvisited points. Any final spanning tree must contain at least one edge crossing this cut; otherwise, the two sides would remain disconnected.

The selected point `i` has the minimum `dist` among all unvisited points, and each `dist` is the cheapest crossing edge ending at that point. Therefore, `dist[i]` is the minimum-weight edge crossing the entire visited/unvisited cut.

The MST cut property says a lightest edge crossing a cut can be included in some minimum spanning tree. An exchange argument explains why. Take an MST that does not use the chosen edge and add the edge to it. This creates one cycle. That cycle must contain another edge crossing the same cut. Removing that other crossing edge restores a spanning tree, and because the chosen edge is no heavier, the total cost does not increase. Thus the greedy choice is compatible with an MST.

Repeating this safe choice until every point is visited constructs a spanning tree of minimum possible total weight. `ans` is the sum of the imaginary zero edge for point zero and the $N-1$ real chosen attachment costs, so it equals the MST cost.

**A small execution picture**

For points `[[0,0],[2,2],[3,10]]`, the matrix contains distances four, thirteen, and nine between the three pairs. Point zero enters for cost zero. The initial attachments become four for point one and thirteen for point two, so point one is selected next and contributes four. Relaxing from point one lowers point two’s attachment from thirteen to nine. Point two then contributes nine, for a total of thirteen. Connecting point two directly to point zero would have cost more, and the relaxation is what discovers the better intermediate attachment.

## Complexity detail

Let $N$ be the number of points.

The nested distance-building loops calculate $\binom{N}{2}$ pair distances, taking $O(N^2)$ time. Prim’s outer loop runs $N$ times. Each iteration scans $N$ points to find the minimum unvisited `dist` and scans up to $N$ points again to relax distances. This is another $O(N^2)$ time. The total time complexity is $O(N^2)$.

The exact checked-in implementation allocates `g` with $N^2$ numeric entries. Its `dist` and `vis` arrays each add $O(N)$ storage. Consequently, the actual auxiliary space complexity of this source is $O(N^2)$, not $O(N)$.

The package manifest’s $O(N)$ space bound corresponds to optimized Prim when Manhattan distances are computed directly from `points` during relaxation instead of stored in `g`. That is not what this source does. The documentation preserves the exact implementation’s matrix allocation and reports its real memory bound.

## Alternatives and edge cases

- **Matrix-free optimized Prim:** Compute the Manhattan distance from the newly selected point to each unvisited point during relaxation. It keeps the same $O(N^2)$ time and reduces explicit auxiliary space to $O(N)$; this is the variant matching the manifest’s stated space bound.
- **Heap-based Prim:** A priority queue can select candidate edges, but a complete graph may place $O(N^2)$ edges in the heap and cost $O(N^2\log N)$ time and $O(N^2)$ space.
- **Kruskal’s algorithm:** Generate all $\binom{N}{2}$ edges, sort them, and use union-find to avoid cycles. It is correct but takes $O(N^2\log N)$ time and $O(N^2)$ edge storage.
- **Connecting each point to its nearest neighbor:** Independent nearest choices can form disconnected clusters or cycles. MST construction must reason about connectivity of the whole growing component.
- **One point:** `g` is a one-cell matrix, point zero is selected with distance zero, and the answer is zero because no real edge is needed.
- **Two points:** The second point’s `dist` becomes their Manhattan distance, so that sole required edge is returned.
- **Equal edge weights:** The selection scan keeps one tied minimum. Any lightest crossing edge is safe, and the minimum total cost is unchanged.
- **Negative coordinates:** Manhattan distance uses absolute coordinate differences, so negative coordinates require no special branch.
- **Distinct point guarantee:** Separate vertices never have identical coordinate pairs, although different edges may still have zero only on the diagonal. The algorithm would remain structurally valid with duplicates, but the source contract excludes them.
- **Complete-graph connectivity:** An index is always found after initialization because every point connects to every other point. On a general disconnected graph, the `i == -1` state would need explicit impossibility handling.
- **No parent array:** The source returns only total cost. It does not retain which particular edge produced `dist[i]`, so it cannot reconstruct the MST without an additional parent structure.
- **Input preservation:** The points list is read-only. The distance matrix, visited flags, and best distances are separate allocations.
