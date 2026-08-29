## General

Treat every board coordinate as a graph vertex. A legal knight move creates an unweighted edge to one of eight neighboring coordinates. The task is then an unweighted shortest-path problem from the origin to `(x, y)`, and breadth-first search is the direct tool because it explores vertices in increasing number of edges from the start.

**Represent the eight legal moves**

The tuple `dirs` contains every combination where one coordinate changes by two and the other by one, with all required signs and orientations. From `(i, j)`, adding `(a, b)` produces neighbor `(i + a, j + b)`.

The board is infinite, so there is no boundary check. Negative and positive coordinates are equally valid.

**Queue and visited set start at the origin**

The deque `q` initially contains `(0, 0)`. The set `vis` also contains the origin. Recording a position when it is enqueued, rather than later when it is removed, prevents several parents from inserting the same coordinate into the queue.

Without `vis`, the graph’s cycles would cause endless repeated exploration. A knight can revisit previously reached squares through many different paths.

**Process one distance layer at a time**

`ans` is the move count of every coordinate currently in the queue at the start of an outer iteration. The loop captures `len(q)` and removes exactly that many positions in the inner loop. Any neighbors appended during this processing are one move farther and remain for the next outer iteration.

For each removed coordinate, the code first tests whether it equals the target. If so, it immediately returns `ans`. Otherwise, it generates all eight legal neighbors, inserts each unseen one into `vis`, and appends it to the queue.

After the entire current layer is processed, `ans += 1` advances the distance associated with the next queue layer.

Starting with `ans = 0` is important. The origin is reachable in zero moves. If the target is `(0, 0)`, it is detected in the first layer and zero is returned.

**Why the first target visit is minimal**

Initially, the queue’s only vertex is exactly distance zero from the origin. Assume a layer contains precisely the not-yet-processed vertices whose shortest distance is `ans`. Every unseen neighbor reached from that layer has a path of length `ans + 1`, so it belongs no later than the next layer. It cannot have a shorter unseen path, because every vertex at a smaller distance was processed in an earlier layer and would already have discovered it.

Thus the layer property holds inductively. When the target is removed, all positions at smaller distance have already been examined and no shorter route exists. The returned `ans` is the minimum number of moves.

The visited set does not discard a better path. The first time a coordinate is generated is from the earliest possible BFS layer. Any later generation would have equal or greater length.

For target `(2, 1)`, one of the eight neighbors generated from the origin is that coordinate. It enters the distance-one layer and is returned with answer one.

For `(5, 5)`, the wave expands through successive move counts until the target enters the distance-four layer. BFS need not know the example’s particular route in advance; the layer ordering guarantees that the first discovered distance is optimal.

**Why the search eventually terminates on an infinite board**

The graph is locally finite because every coordinate has only eight neighbors. Every target is reachable by some finite knight path, as guaranteed by the problem. BFS processes all vertices at distances below that finite target distance and then reaches the target layer. There are finitely many coordinates within any fixed knight-move distance, so the algorithm completes.

The final `return -1` is defensive. Under the reachability guarantee and the knight graph’s connectivity, the queue will not empty before finding the target.

The exact code does not use coordinate symmetry, bidirectional search, or pruning. It explores the full BFS wave around the origin, which affects its true resource bounds.

## Complexity detail

Let $R=\max(\lvert x\rvert,\lvert y\rvert)$, with a constant additive margin for the knight’s possible overshoot near the target.

Before reaching the target, an unpruned BFS explores a two-dimensional region whose width and height are proportional to $R$. The number of visited coordinates is therefore $O(R^2)$, and each generates eight constant-count neighbors. Time complexity is $O(R^2)$.

The visited set stores $O(R^2)$ coordinates in the same worst-case region. The queue holds frontier layers, which are smaller than the full visited area, so total auxiliary-space complexity is $O(R^2)$.

Because the contract bounds coordinates by 300, one may call the legal input domain fixed and describe the maximum work as a large constant. That does not make the exact search structurally $O(1)$ as coordinates scale; its natural coordinate-sensitive behavior is quadratic. This differs from the manifest’s simplified constant bound.

## Alternatives and edge cases

- **Symmetry-reduced memoized recursion:** Reflect the target into the first quadrant and recursively approach the origin with two move patterns plus small base cases. Memoization reduces repeated work.
- **Bidirectional BFS:** Expand from both origin and target until the visited regions meet. It can reduce explored constants, though its asymptotic two-dimensional bound remains similar.
- **Closed-form knight-distance formula:** A mathematical solution can run in $O(1)$ time but requires careful exceptions near the origin and is harder to derive safely.
- **Target is the origin:** The first queue removal matches and returns zero.
- **Negative coordinates:** All eight signed moves are present, so the BFS handles them without normalization.
- **Coordinate symmetry:** Targets related by sign changes or swapping coordinates have equal answers, but this exact implementation does not exploit that fact.
- **No board boundary:** Generating negative or overshooting coordinates is legal and sometimes necessary for shortest paths near the origin.
- **Visited-on-enqueue:** Marking before append prevents duplicate queue entries from different parents in the same layer.
- **Layer length capture:** `range(len(q))` evaluates the current size once, so newly appended neighbors wait for the next distance layer.
- **Unreachable fallback:** `-1` should never occur under the guarantee; it exists only as a defensive final return.
