## General

**Translate a length-three cycle into a triangle**

Corridors work in both directions, so the maze is an undirected graph. A cycle of length three consists of three distinct rooms where every pair is connected by a corridor. In graph terminology, the task is to count triangles.

The solution builds an adjacency structure `g` whose entry `g[a]` is the set of rooms directly connected to room `a`. For each corridor `[a, b]`, it inserts `b` into `g[a]` and `a` into `g[b]`. Adding both directions is essential: later logic may choose any of the triangle's rooms as its center.

Sets serve two different needs:

- they store all neighbors of a room;
- they support the expected constant-time membership test `j in g[k]`.

The input guarantees no duplicate corridors, but sets also naturally prevent duplicate neighbor entries.

**Choose one room and test pairs of its neighbors**

Fix a room `i`. If rooms `j` and `k` are both in `g[i]`, then corridors `i-j` and `i-k` already exist. These three rooms form a triangle if and only if the third corridor `j-k` also exists.

The call `combinations(g[i], 2)` enumerates every unordered pair of distinct neighbors of `i` exactly once. For each pair `j, k`, the condition `j in g[k]` tests for that closing corridor. If it exists, the code increments `ans`.

Using unordered combinations matters. Enumerating ordered neighbor pairs would examine both `(j, k)` and `(k, j)` around the same center and create another layer of duplicate counting.

Consider triangle rooms 1, 3, and 4. When `i = 1`, the pair `(3, 4)` occurs among neighbors of 1 and passes the membership test. When `i = 3`, pair `(1, 4)` passes. When `i = 4`, pair `(1, 3)` passes. Other rooms do not count that triangle because they are not one of its vertices.

**Why divide by exactly three**

Every real triangle is detected once at each of its three rooms:

- centered at its first room, the other two are a neighbor pair;
- centered at its second room, the other two are a neighbor pair;
- centered at its third room, the other two are a neighbor pair.

At a fixed center, `combinations` emits the other two rooms only once, so there is no additional directional duplication. Therefore, each triangle contributes exactly 3 to `ans`. Returning `ans // 3` converts the centered detections into the number of distinct room sets.

The division is exact. `ans` cannot contain an unmatched successful detection: any successful test proves all three corridors exist, so the same triangle will also be detected at the other two vertices when their turns arrive.

This matches the definition that cycles are considered the same when they visit the same rooms. Different starting points and traversal directions do not create new answers.

**Why the membership test proves a cycle**

For a selected `i` and neighbor pair `j, k`, adjacency construction proves corridors `i-j` and `i-k` exist. If `j in g[k]`, corridor `k-j` exists too. The input forbids self-corridors, and the combination chooses two distinct neighbors, so `i`, `j`, and `k` are three distinct rooms. Those three undirected edges form a valid length-three cycle.

Conversely, take any valid length-three cycle with rooms `a`, `b`, and `c`. When the outer loop reaches `a`, both `b` and `c` are in `g[a]`. Their unordered pair is enumerated, and `b in g[c]` is true because the third cycle corridor exists. Thus no triangle is missed.

Combining both directions shows that the successful tests are exactly three centered representations of every required cycle, so the final quotient is correct.

**Be precise about what the executable source actually enumerates**

The loops do not orient edges by degree and do not restrict work to a smaller-neighbor subset. For room `i` with degree $d_i$, they generate

$$
\binom{d_i}{2}
$$

neighbor pairs whether or not any pair closes a triangle.

This distinction matters for complexity. A star graph with one center connected to $E$ leaves has no triangles, yet the center alone generates $\binom{E}{2}$ pairs. Therefore, the exact implementation can perform quadratic work in the number of corridors. The branch manifest's $O(n+E^{3/2})$ bound describes a stronger triangle-counting target, but it is not a valid worst-case bound for these exact nested loops. A beginner-friendly explanation should follow the code that runs rather than hide this gap.

## Complexity detail

Let $n$ be the number of rooms, $E$ the number of corridors, and $d_i$ the degree of room $i$.

Building the undirected adjacency sets takes $O(n+E)$ expected time when including traversal of room labels and expected constant-time set insertion. The triangle scan creates $\binom{d_i}{2}$ pairs at room $i$, and each closing-edge lookup is expected $O(1)$. Its exact expected running time is

$$
O\left(n+E+\sum_{i=1}^{n}\binom{d_i}{2}\right).
$$

Since degrees sum to $2E$, the pair sum can be $O(E^2)$ in the worst case, as the star example demonstrates. Thus a safe worst-case statement for the exact source is $O(n+E^2)$ expected time with hash-set operations.

The adjacency sets store each undirected corridor twice, once at each endpoint, using $O(n+E)$ space. The temporary pair values and counters use constant extra space beyond the iterator machinery. The graph representation dominates storage, so auxiliary space is $O(n+E)$.

An $O(n+E^{3/2})$ triangle-counting method is possible by orienting edges according to degree and checking only forward neighbor intersections, but that is not what this solution file executes.

## Alternatives and edge cases

- **Degree-oriented triangle counting:** Direct every edge from the lower-degree endpoint toward the higher-degree endpoint, breaking ties consistently, and intersect forward neighborhoods. This can achieve the advertised $O(E^{3/2})$ style bound, but it requires orientation logic absent from the exact source.
- **Adjacency matrix:** A matrix makes the closing-edge test constant time without hashing, but it consumes $O(n^2)$ space even for a sparse maze. Sets use storage proportional to the actual corridors.
- **Triple enumeration of rooms:** Trying every room triple costs $O(n^3)$ and wastes work on triples with few or no corridors. Neighbor-pair enumeration narrows candidates to triples already known to contain two edges.
- **Ordered neighbor pairs:** Iterating both `j, k` and `k, j` would count every triangle six times rather than three. `combinations(..., 2)` avoids that local duplication.
- **Forgetting the final division:** Each triangle is centered once at each of its three vertices. Returning raw `ans` would always triple the required score.
- **Dividing by six:** Six is the duplication factor when directions and starting points are both enumerated. This source uses unordered neighbor pairs, so its factor is only three.
- **Rooms with degree zero or one:** They have no pair of distinct neighbors, so `combinations` yields nothing and they correctly contribute zero.
- **Disconnected maze:** Each triangle lies entirely inside one connected component. The outer loop examines every room, so disconnected components require no special handling.
- **No triangles:** Every closing-edge test fails, `ans` stays zero, and integer division returns zero.
- **Set iteration order:** The order of neighbors in a set is irrelevant because every unordered pair is generated and only the final count matters.
- **No duplicate corridors:** The input guarantee and set storage ensure a physical corridor cannot create duplicate adjacency entries or duplicate detections at one center.
- **High-degree star:** It has no triangles but triggers many failed neighbor-pair checks. This is the concrete edge shape that exposes the exact implementation's $O(E^2)$ worst case.
