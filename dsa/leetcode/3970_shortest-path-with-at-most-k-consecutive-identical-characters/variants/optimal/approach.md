## General

Ordinary shortest-path algorithms usually store one best distance per graph node. That is insufficient here because future legality depends on how the path arrived.

Suppose two paths reach the same node with the same label:

- one path's current run of that label has length one;
- another path's current run has length `k`.

The second path cannot move next to another node with the same label, while the first may be able to. Even if the second path is currently cheaper, it does not dominate the first. The current run length must therefore be part of the shortest-path state.

The source treats each pair

$$
(\texttt{node},\texttt{runLength})
$$

as a distinct state, where `1\le\texttt{runLength}\le k`. This turns the label restriction into an ordinary transition rule on an expanded graph.

**Building the directed weighted graph**

For every edge `[u,v,w]`, the source appends `(v,w)` to `graph[u]` only. It does not add a reverse edge because the original graph is directed.

The expanded state graph is not built explicitly. When a state is removed from the priority queue, the source scans the original outgoing edges and calculates the next run length on demand.

**Meaning of the distance table**

`distance[u][r]` is the smallest cost discovered so far for a path that:

- starts at node zero;
- ends at node `u`;
- satisfies the run constraint everywhere;
- has a final same-label run of length exactly `r`.

Column zero is allocated for convenient indexing but is never a valid state. The table has `k+1` entries per node so that real run lengths can be used directly as indices.

The starting route already contains node zero's label, so its run length is one:

```python
distance[0][1] = 0
heap = [(0, 0, 1)]
```

No edge has been taken, so the cost is zero. Initializing the run length to zero would be wrong: moving to a node with the same label must create a run of length two, not one.

**How one directed edge changes the state**

From state `(u,r)`, consider an edge to `v`.

- If `labels[u] == labels[v]`, the current identical-character run continues, so the new length is `r+1`.
- Otherwise a different character starts a new run, so the new length is one.

The source computes:

```python
next_run = (
    run_length + 1
    if labels[node] == labels[neighbor]
    else 1
)
```

If `next_run>k`, traversing this edge would create an invalid path and the transition is discarded. Otherwise, the state `(neighbor,next_run)` is legal.

Only the final run length must be remembered. Every earlier run is already complete and was checked while it was formed; later moves cannot change it.

**Dijkstra's relaxation**

All edge weights are positive. Therefore the expanded state graph also has positive edge weights, and Dijkstra's algorithm applies.

When the current state has finalized candidate cost `cost` and the original edge weight is `weight`, the new path costs

$$
\texttt{nextCost}=\texttt{cost}+\texttt{weight}.
$$

If this is smaller than the recorded distance for the destination state, the source updates the table and pushes a heap tuple:

```python
(next_cost, neighbor, next_run)
```

Python compares tuples from left to right, so the minimum heap orders entries primarily by cost. Node and run length only break ties and do not affect optimality.

**Why stale heap entries are skipped**

The source uses the common “push a new entry” form of Dijkstra rather than trying to modify an existing heap item. A state can therefore have an older, more expensive entry still in the heap after a cheaper route is found.

After popping, it checks:

```python
if cost != distance[node][run_length]:
    continue
```

If the values differ, this tuple no longer represents the best known route to its state. Skipping it avoids scanning outgoing edges unnecessarily and prevents obsolete work from affecting the reasoning.

**Why returning at the first destination pop is safe**

The target node may have several valid states, one for each possible final run length. The answer is the minimum of their distances.

Dijkstra's heap always removes the globally smallest unsettled cost. Once a non-stale state whose node is `n-1` is popped, no other target state still in the heap or not yet discovered can have smaller distance. With positive weights, extending another unsettled path cannot lower its cost.

Therefore:

```python
if node == n - 1:
    return cost
```

returns the minimum across all target run lengths without waiting to fill the entire distance table.

If the heap becomes empty without reaching a target state, every legal state reachable from node zero has been exhausted. No valid path exists, so the source returns `-1`.

**A short illustration of why the expanded state matters**

Assume `k=2` and a node labeled `a` can be reached either with ending labels `"ba"` or `"aa"`. Both routes are at the same physical node, but their run lengths are one and two.

An outgoing edge to another `a` node is legal from the first state, producing run length two. It is illegal from the second, which would produce length three. Keeping only the cheaper distance for the physical node could discard the only state capable of reaching the destination.

**The one-node case**

When `n=1`, the start is already the destination. Since `k\ge1`, the one-character route is valid. The initial state is popped first, the destination check succeeds, and the source returns zero.

## Complexity detail

Let `n` be the number of original nodes, `m` the number of directed edges, and `k` the allowed maximum run length.

There are at most `nk` valid expanded states. Each original edge can be considered from each possible run length of its source, so the expanded graph has at most `mk` transitions. The source generates these transitions lazily but can still examine that many in the worst case.

Under the standard binary-heap Dijkstra analysis, time is

$$
O\bigl((nk+mk)\log(nk)\bigr)
=O\bigl(k(n+m)\log(nk)\bigr),
$$

matching the manifest's stated bound under the usual simple-graph or polynomial-edge assumption.

Because the implementation pushes duplicates instead of performing a true decrease-key, up to `O(mk)` successful relaxation entries can be created. A fully heap-size-explicit bound uses

$$
O\bigl(k(n+m)\log(nk+mk)\bigr).
$$

For ordinary simple graphs, `m` is polynomial in `n`, so the two logarithmic forms differ only by a constant factor in big-O terms. The second form also remains literal if many parallel edges are allowed.

The adjacency lists require `O(n+m)` space. The distance table requires `O(nk)`. The heap can retain stale entries and in a conservative worst case use `O(mk)` space. Total auxiliary space is therefore

$$
O(n+m+nk+mk)=O(k(n+m)).
$$

The source does not modify `edges` or `labels`.

## Alternatives and edge cases

- **One distance per node:** This merges arrivals with different run lengths even though they permit different future edges. It can discard the only valid continuation and is not sufficient.

- **Store the full label string of each route:** Future validity depends only on the label and length of the final run. The current node supplies the label, so only the run length needs extra state.

- **Breadth-first search:** BFS minimizes edge count, not total weight. The positive weights may differ, so a binary-heap Dijkstra traversal is required.

- **Bellman–Ford on expanded states:** It would handle arbitrary edge weights but cost much more than necessary. All given weights are positive.

- **Explicitly build every expanded edge:** This is conceptually valid but allocates `O(mk)` transition objects. The source generates transitions from the original adjacency list as needed.

- **Start with run length zero:** The starting node's character is already part of the route. The correct initial length is one.

- **Label change:** Moving to a different label resets the run to one, not zero.

- **Exactly `k` equal labels:** This is valid because the restriction is “at most” `k`. Only `next_run>k` is rejected.

- **`k=1`:** Every traversed edge must lead to a differently labeled node. The transition rule enforces this naturally.

- **Cycles:** A route may revisit nodes, but there are only `nk` distinct states. Positive weights and distance relaxation prevent beneficial infinite cycling.

- **Parallel edges:** Each directed edge is stored and considered. The cheaper one may improve a state; stale entries from worse discoveries are ignored.

- **Unreachable target:** Emptying the heap proves that no legal expanded state at the destination is reachable, and `-1` is returned.

- **One node:** The empty-edge route costs zero and contains one-character runs only, so the initial heap pop returns zero.

- **Early destination return:** Returning when a target is first discovered would be unsafe because another heap state might later be cheaper. The source returns only when a non-stale target state is popped.

- **Stale-entry equality test:** A tuple with cost different from the current table value must not be expanded. Exact integer edge weights make direct equality appropriate.

- **Space bound and stale entries:** The distance table alone is `O(nk)`, but the exact push-without-decrease-key heap can contain additional obsolete tuples. The manifest's broader `O(k(n+m))` bound accounts for them.
