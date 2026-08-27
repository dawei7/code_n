# Guided Example: Minimum Cost to Buy Apples II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "prices": [8, 3], "roads": [[0, 1, 1, 2]]}`
- **Required output:** `[6, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` and an integer array `prices` of length `n`, where $\text{prices}[i]$ is the price of apples at shop `i`.

The objective is to compute `[6, 3]` from `{"n": 2, "prices": [8, 3], "roads": [[0, 1, 1, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One graph, two edge-weight systems

Each road row contains endpoints `left` and `right`, an empty-travel `cost`, and a multiplier `tax`. The source stores the road in both adjacency lists because roads are bidirectional. Its edge record is

`(neighbor, cost, cost * tax)`.

The second and third fields are respectively the empty weight and loaded weight. Storing both once avoids recomputing multiplication during every relaxation and makes it possible for one shortest-path helper to support both travel modes.

All edge costs are positive. Dijkstra's algorithm is therefore valid under either weighting:

- with `carrying == false`, each road contributes `empty_cost`;
- with `carrying == true`, it contributes `loaded_cost`.

The paths found by these two runs need not use the same roads. That is exactly what the statement permits.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "prices": [8, 3], "roads": [[0, 1, 1, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the shortest-path helper returns

For one `start` and one carrying mode, `shortest` creates a distance array initialized to infinity and sets the start distance to zero. The heap begins with `(0, start)`.

Whenever the smallest heap entry is removed, the check

`distance != distances[node]`

discards a stale entry. A vertex can receive a better distance after an older, larger distance has already been pushed. Python's heap does not remove the obsolete pair automatically, so this comparison prevents the algorithm from scanning outgoing roads using an outdated cost.

For each neighboring road, the helper chooses the weight matching the mode and forms

`candidate = distance + edge_cost`.

Only a strict improvement replaces `distances[neighbor]` and enters the heap. Since weights are positive, when a non-stale distance is processed, it is the shortest possible distance for that vertex. Repeating the relaxation eventually returns the shortest distance from `start` to every reachable shop under that mode.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For one `start` and one carrying mode, `shortest` creates a ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a loaded run from the start also gives the return cost

The formula needs the loaded distance from purchase shop `j` back to starting shop `i`. The source instead runs loaded Dijkstra from `i` and later reads `loaded_distances[j]`, which is the distance from `i` to `j`.

This reversal is safe because every road is bidirectional and has the same loaded cost in both directions. Reversing any path from `j` to `i` produces a path from `i` to `j` with exactly the same road costs, and vice versa. Hence

$$
D_{\mathrm{loaded}}(j,i)=D_{\mathrm{loaded}}(i,j).
$$

This symmetry would not be valid for directed roads or direction-dependent taxes, but it is valid for the contract used here.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[6, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "prices": [8, 3], "roads": [[0, 1, 1, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[6, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Use one shared weight per road:** This loses t:** - **Use one shared weight per road:** This loses the distinction between empty travel and loaded travel. The two shortest paths must be computed under their respective edge costs.
- **Force the return to reverse the forward path:** That can be more expensive than choosing separate routes because taxes change the relative desirability of roads. The source minimizes the two directions independently.
- **Run Floyd-Warshall twice:** Two all-pairs dynamic programs would take $O(n^3)$ time and $O(n^2)$ space. Repeated Dijkstra benefits from the limit of at most $2000$ roads and keeps memory linear in the graph size.
- **Use breadth-first search:** BFS minimizes the number of roads only when all relevant edge weights are equal. Here both base costs and loaded costs vary.
- **Combine the two Dijkstra runs into a single ordinary run:** Empty and loaded distances obey different metrics. A single scalar distance per vertex cannot represent both at once.
- **Buy locally:** Selecting `shop == start` contributes zero travel in both modes, so the local price is always a valid candidate.
- **Disconnected graph:** Remote shops may retain infinite distance, but the local candidate guarantees a finite answer.
- **Tax equal to one:** Empty and loaded weights match on that road, yet the general two-metric algorithm remains correct without a special branch.
- **Different optimal routes:** The best empty route and best loaded route may have different intermediate shops. Separate shortest-path runs preserve that freedom.
- **Stale heap entries:** A vertex can appear in the heap more than once. The equality check skips older distances and is necessary for the usual efficient Dijkstra behavior.
- **Large monetary totals:** Python integers do not overflow when edge costs, multipliers, path costs, and prices are added.
- **Single shop and no roads:** Both shortest-path calls return distance zero to the only shop, so the answer is its local price.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n$ be the number of shops and $m$ the number of roads. The adjacency list takes $O(n+m)$ time to build and $O(n+m)$ space because each undirected road is stored twice.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
