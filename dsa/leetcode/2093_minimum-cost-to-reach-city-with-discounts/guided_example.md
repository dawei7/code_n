# Guided Example: Minimum Cost to Reach City With Discounts

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "highways": [[0, 1, 3], [2, 3, 2]], "discounts": 0}`
- **Required output:** `-1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A series of highways connect `n` cities numbered from `0` to $n - 1$. You are given a 2D integer array `highways` where $\text{highways}[i] = [\text{city1}_{i}, \text{city2}_{i}, \text{toll}_{i}]$ indicates that there is a highway that connects $\text{city1}_{i}$ and $\text{city2}_{i}$, allowing a car to go from $\text{city1}_{i}$ to $\text{city2}_{i}$ **and vice versa** for a cost of $\text{toll}_{i}$.

The objective is to compute `-1` from `{"n": 4, "highways": [[0, 1, 3], [2, 3, 2]], "discounts": 0}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A city alone is not enough to describe progress

Reaching the same city after using different numbers of discounts creates different future possibilities. A route that costs slightly more but preserves discounts may become better later.

The algorithm therefore treats `(city, k)` as a state, where `k` is the number of discounts already used. There are `n * (discounts + 1)` valid states.

Each undirected highway `[a, b, c]` is stored in both adjacency lists. From state `(i, k)` across a highway of toll `v`, there are two transitions:

- pay the full toll and reach `(j, k)` with added cost `v`;
- use a discount and reach `(j, k + 1)` with added cost `v // 2`.

Integer floor division is exactly the required discounted toll calculation for nonnegative tolls.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "highways": [[0, 1, 3], [2, 3, 2]], "discounts": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Run Dijkstra on the expanded state graph

The heap `q` starts with `(0, 0, 0)`: zero cost, city 0, zero discounts used. Heap tuples are ordered first by cost, so `heappop` always selects the currently smallest path cost.

`dist[i][k]` records the best cost at which state `(i, k)` has already been expanded. It begins at infinity.

When a valid state is popped, the source expands it only if `cost` is strictly smaller than the stored value. It then records the cost and pushes both transition choices for every neighboring highway.

The implementation does not perform decrease-key operations. It may push multiple entries for the same state; later, expensive duplicates fail `dist[i][k] > cost` and are ignored. This lazy pattern is standard for heap-based Dijkstra.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle the discount limit through an extra rejected layer

The source always pushes the discounted transition with `k + 1`, even when `k == discounts`. Such an entry has too many discounts. It is safe because the first pop-time check is `if k > discounts: continue`, before indexing `dist`.

This creates some useless heap entries but never treats an invalid path as an answer. A more selective implementation could push the discounted transition only when `k < discounts`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `-1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "highways": [[0, 1, 3], [2, 3, 2]], "discounts": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `-1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Ordinary Dijkstra by city only:** This discards how many discounts remain and can prune a route that is more valuable later. The discount count must be part of the state.
- **Bellman-Ford:** All costs are nonnegative, so repeated global relaxation is unnecessary. Dijkstra is the natural shortest-path method.
- **Dynamic programming by discount layers:** Repeated shortest-path passes can work but are less direct than one expanded-state Dijkstra.
- **Push discounted edges conditionally:** Checking `k < discounts` before pushing avoids invalid layer `K + 1` entries while preserving the algorithm.
- **No discounts:** Only layer zero is valid. Discounted pushes enter layer one and are skipped; full-cost Dijkstra still works.
- **More discounts than route edges:** Discounts are optional, so the answer may use fewer than the allowance.
- **Odd toll:** `v // 2` correctly drops the fractional half.
- **Zero toll:** Nonnegative zero edges remain compatible with Dijkstra; strict distance improvement prevents endless expansion of equal-cost states.
- **Disconnected destination:** The heap eventually empties and `-1` is returned.
- **Multiple routes to one state:** The heap may contain duplicates, but only a strictly improving pop expands neighbors.
- **Undirected highways:** Both adjacency directions are required because travel is allowed either way.
- **Early destination return:** It occurs only after rejecting `k > discounts`, so an illegally over-discounted path can never be returned.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E(K+1)\log(n(K+1)))$. Let $E$ be the number of highways and $K$ the discount limit.
- **Auxiliary Space Complexity:** $O(n(K+1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
