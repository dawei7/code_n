## General

The stability of a chosen spanning tree is its weakest final edge. Instead of trying to construct every possible tree and comparing those minima, the source asks a decision question:

> For a proposed stability `lim`, can the graph contain a valid spanning tree in which every selected edge has final strength at least `lim`?

Once that yes-or-no question can be answered, binary search finds the greatest feasible `lim`.

**Why threshold feasibility is monotone**

If stability `lim` is feasible, every selected edge also meets any smaller threshold. The same tree and the same upgrades remain valid. Conversely, if a threshold is impossible, increasing it cannot introduce a usable edge. Feasible values therefore form one continuous prefix such as `1, 2, ..., answer`, which is exactly the shape required by binary search.

**Rejecting impossible mandatory edges first**

The first Union-Find pass processes only edges whose `must` value is true. Every such edge has to appear in the final spanning tree. If one mandatory edge joins vertices that are already connected by earlier mandatory edges, the mandatory set contains a cycle. A spanning tree is acyclic and cannot omit any of those edges, so no valid answer exists; the source immediately returns `-1`.

At the same time, `mn` records the minimum original strength among all mandatory edges. Mandatory edges cannot be upgraded. Consequently, no valid tree can have stability greater than `mn`, and `mn` is a sound upper bound for binary search. When there are no mandatory edges, it stays at `10**6`. This is looser than necessary—the input strengths are at most `10^5` and one upgrade can only double them—but it is still a valid finite upper bound.

After checking the mandatory forest, the source unions every edge in the graph using the same Union-Find object. If more than one component remains, even the complete original graph is disconnected. Neither selecting edges nor doubling their strengths can create a missing connection, so the answer is `-1`.

**What `check(lim)` considers usable**

Each threshold check starts with a fresh Union-Find containing `n` separate components. It then makes two passes over the edges.

In the first pass, every edge with `s >= lim` is unioned. Such an edge already meets the target strength and costs no upgrade. Unioning all of them contracts every region that can be connected for free.

In the second pass, an edge is eligible when `2 * s >= lim` and an upgrade remains. A successful union means that this edge connects two currently separate components, so the source spends one upgrade by decrementing `rem`. If its endpoints are already connected, the edge is unnecessary for connectivity and no upgrade is spent.

The check succeeds exactly when the final number of components, `uf.cnt`, is one.

**Why the second pass may use the input order**

After all free edges are contracted, imagine a smaller graph whose vertices are the free components and whose edges are the optional edges that can reach `lim` after doubling. Connecting `c` such components requires exactly `c - 1` successful unions. Union-Find accepts an eligible edge only when it merges two components, so every accepted edge reduces the component count by one and never creates a cycle.

The order of eligible edges can change which particular forest is selected, but not the number of successful merges needed. If their component graph is connected, any complete scan will produce enough independent merges to connect it, provided `k >= c - 1`. If it is disconnected, no ordering can connect it. If `k < c - 1`, no solution can use fewer than `c - 1` connecting edges. Sorting is therefore unnecessary for this threshold decision.

**Why `check` does not explicitly inspect `must`**

At first this looks dangerous because mandatory edges cannot be upgraded, whereas both loops unpack their flag as `_`. The binary-search upper bound supplies the missing guarantee. Every tested `lim` is at most `mn`, and `mn` is the minimum mandatory strength. Thus every mandatory edge satisfies `s >= lim` and is included during the free first pass. A mandatory edge can never require an upgrade during a tested check.

Moreover, the preprocessing already proved that mandatory edges form a forest. If all threshold-usable edges connect the graph, there exists a spanning tree containing that mandatory forest: keep every mandatory edge, contract its components, and select cycle-free connecting edges between the components. The Union-Find check only needs to prove that those connections exist; it does not have to materialize the final tree.

Edges with `s >= lim` also satisfy `2 * s >= lim` and are seen again in the second pass. This does not waste upgrades because the first pass already connected each such edge's endpoints, making its second `union` return `False`.

**Binary-search mechanics**

The search starts with `l = 1` and `r = mn`. Because all strengths are positive and the full graph was proven connected, threshold `1` is feasible: every original edge meets it without an upgrade. The upper midpoint

`mid = (l + r + 1) >> 1`

prevents an infinite loop when two candidates remain. A feasible midpoint becomes the new lower bound; an infeasible midpoint reduces the upper bound to `mid - 1`. When the bounds meet, `l` is the greatest feasible stability.

**Union-Find's role**

`find` follows parent links and applies path compression. `union` attaches the smaller component under the larger one using the `size` array, decrements `cnt` only for a real merge, and returns whether a merge occurred. These properties simultaneously provide fast connectivity tests, prevent chosen connecting edges from creating cycles, and let `check` count upgrades only when an edge is actually useful.

**Difference from the manifest and local editorial**

The manifest describes contracting mandatory edges, constructing a maximum spanning tree with Kruskal, and upgrading weak selected optional edges in `O(m\log m)` time. The local editorial likewise describes sorting optional edges. The exact Optimal source does neither. It performs binary search plus repeated unsorted connectivity checks. The approach here intentionally explains the executable source rather than attributing the different one-pass strategy to it.

## Complexity detail

Let `n` be the number of vertices, `m` the number of edges, and `W` the inclusive numeric upper bound searched by the code. Here `W <= 10^6`.

The preprocessing scans the edges to validate the mandatory forest and then scans them again to test full connectivity. With union by size and path compression, this costs `O((n+m)\alpha(n))` time, including Union-Find initialization, where `\alpha` is the inverse Ackermann function.

One `check` creates fresh parent and size arrays in `O(n)` time and performs two complete edge scans, each with Union-Find operations. Its time is `O((n+m)\alpha(n))`. Binary search invokes it `O(\log W)` times, so the faithful total bound is

$$
O\bigl((n+m)\alpha(n)\log W\bigr).
$$

Because `W` is bounded by a constant in the given constraints, this behaves almost linearly in the input size, but `O(m\log m)` is not the operation count of this implementation.

Each live Union-Find stores parent and size arrays of length `n`. A check's Union-Find replaces the previous local one after that call; the code does not retain structures for all thresholds and does not copy or sort `edges`. Auxiliary space is `O(n)`, excluding the input edge list and Python call-stack depth inside `find`. Union by size keeps trees shallow, and path compression shortens them further.

## Alternatives and edge cases

- **Maximum-spanning-tree formulation:** Sort optional edges by descending strength, preserve the mandatory forest, and reason about which selected weak edges receive upgrades. This can match the manifest's `O(m\log m)` target, but it is not the algorithm in the exact source.
- **Binary search with sorted Kruskal:** Sorting can make a threshold construction intuitive, yet the two-phase free/upgrade connectivity test shows that ordering is unnecessary for a fixed threshold.
- **Rebuild candidate trees directly:** Enumerating spanning trees is exponential and ignores the monotone threshold structure.
- **Mandatory cycle:** Even very strong mandatory edges make the instance impossible because all must be included and a tree cannot contain their cycle.
- **Disconnected full graph:** Upgrades change strengths, not endpoints, so they cannot connect separate graph components.
- **No mandatory edges:** `mn` remains `10**6`. Checks above twice the maximum edge strength fail, and binary search still descends to the true answer.
- **No upgrades:** With `k = 0`, the second pass cannot add an edge; only edges already meeting `lim` may connect the graph.
- **More upgrades than needed:** The source spends upgrades only on successful component merges. Unused allowance is harmless because `k` is a maximum, not an exact count.
- **Mandatory edge at the bottleneck:** The search never exceeds the weakest mandatory strength because that edge cannot be doubled.
- **Optional edge already strong enough:** It is joined for free in the first pass and cannot consume an upgrade in the second pass.
- **Optional edge needs one upgrade:** It is useful only when `s < lim <= 2s` and it joins two remaining components.
- **Optional edge still too weak after doubling:** When `2s < lim`, neither pass can use it.
- **Parallel routes and cycles:** Redundant qualifying edges may fail `union`, but skipping them is safe because they do not reduce the component count.
- **Input order:** It may determine which eligible edges become the connecting forest, but not whether at most `k` successful merges can connect all free components.
- **Positive lower bound:** The constraints guarantee positive strengths, so the already-connected graph makes stability `1` feasible after the prechecks.
- **Input preservation:** The solution mutates only Union-Find arrays. It neither sorts nor rewrites the supplied `edges` list.
