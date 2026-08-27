# Guided Example: Paths in Maze That Lead to Same Room

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "corridors": [[1, 2], [5, 2], [4, 1], [2, 4], [3, 1], [3, 4]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A maze consists of `n` rooms numbered from `1` to `n`, and some rooms are connected by corridors. You are given a 2D integer array `corridors` where $\text{corridors}[i] = [\text{room1}_{i}, \text{room2}_{i}]$ indicates that there is a corridor connecting $\text{room1}_{i}$ and $\text{room2}_{i}$, allowing a person in the maze to go from $\text{room1}_{i}$ to $\text{room2}_{i}$ **and vice versa**.

The objective is to compute `2` from `{"n": 5, "corridors": [[1, 2], [5, 2], [4, 1], [2, 4], [3, 1], [3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Translate a length-three cycle into a triangle

Corridors work in both directions, so the maze is an undirected graph. A cycle of length three consists of three distinct rooms where every pair is connected by a corridor. In graph terminology, the task is to count triangles.

The solution builds an adjacency structure `g` whose entry `g[a]` is the set of rooms directly connected to room `a`. For each corridor `[a, b]`, it inserts `b` into `g[a]` and `a` into `g[b]`. Adding both directions is essential: later logic may choose any of the triangle's rooms as its center.

Sets serve two different needs:

- they store all neighbors of a room;
- they support the expected constant-time membership test `j in g[k]`.

The input guarantees no duplicate corridors, but sets also naturally prevent duplicate neighbor entries.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "corridors": [[1, 2], [5, 2], [4, 1], [2, 4], [3, 1], [3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Choose one room and test pairs of its neighbors

Fix a room `i`. If rooms `j` and `k` are both in `g[i]`, then corridors `i-j` and `i-k` already exist. These three rooms form a triangle if and only if the third corridor `j-k` also exists.

The call `combinations(g[i], 2)` enumerates every unordered pair of distinct neighbors of `i` exactly once. For each pair `j, k`, the condition `j in g[k]` tests for that closing corridor. If it exists, the code increments `ans`.

Using unordered combinations matters. Enumerating ordered neighbor pairs would examine both `(j, k)` and `(k, j)` around the same center and create another layer of duplicate counting.

Consider triangle rooms 1, 3, and 4. When `i = 1`, the pair `(3, 4)` occurs among neighbors of 1 and passes the membership test. When `i = 3`, pair `(1, 4)` passes. When `i = 4`, pair `(1, 3)` passes. Other rooms do not count that triangle because they are not one of its vertices.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Fix a room `i`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why divide by exactly three

Every real triangle is detected once at each of its three rooms:

- centered at its first room, the other two are a neighbor pair;
- centered at its second room, the other two are a neighbor pair;
- centered at its third room, the other two are a neighbor pair.

At a fixed center, `combinations` emits the other two rooms only once, so there is no additional directional duplication. Therefore, each triangle contributes exactly 3 to `ans`. Returning `ans // 3` converts the centered detections into the number of distinct room sets.

The division is exact. `ans` cannot contain an unmatched successful detection: any successful test proves all three corridors exist, so the same triangle will also be detected at the other two vertices when their turns arrive.

This matches the definition that cycles are considered the same when they visit the same rooms. Different starting points and traversal directions do not create new answers.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "corridors": [[1, 2], [5, 2], [4, 1], [2, 4], [3, 1], [3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Degree-oriented triangle counting:** Direct ev:** - **Degree-oriented triangle counting:** Direct every edge from the lower-degree endpoint toward the higher-degree endpoint, breaking ties consistently, and intersect forward neighborhoods. This can achieve the advertised $O(E^{3/2})$ style bound, but it requires orientation logic absent from the exact source.
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
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O\left(n+E+\sum_{i=1}^{n}\binom{d_i}{2}\right)$. Let $n$ be the number of rooms, $E$ the number of corridors, and $d_i$ the degree of room $i$.
- **Auxiliary Space Complexity:** $O(n+E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
