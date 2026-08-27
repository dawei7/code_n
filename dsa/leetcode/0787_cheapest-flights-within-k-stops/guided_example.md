# Guided Example: Cheapest Flights Within K Stops

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]], "src": 0, "dst": 2, "k": 1}`
- **Required output:** `200`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` cities connected by some number of flights. You are given an array `flights` where $\text{flights}[i] = [\text{from}_{i}, \text{to}_{i}, \text{price}_{i}]$ indicates that there is a flight from city $\text{from}_{i}$ to city $\text{to}_{i}$ with cost $\text{price}_{i}$.

The objective is to compute `200` from `{"n": 3, "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]], "src": 0, "dst": 2, "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert the stop limit into an edge limit

A route with zero intermediate stops is one direct flight, so it uses one edge. In general, a route with at most `k` stops uses at most `k + 1` flight edges.

The task is therefore to find the cheapest source-to-destination path using no more than `k + 1` edges. Ordinary single-distance shortest-path reasoning is not enough by itself because reaching a city cheaply with many edges may leave no edge budget, while a slightly more expensive arrival with fewer edges may still lead to the best legal destination route.

The solution uses the edge-bounded form of Bellman–Ford dynamic programming.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]], "src": 0, "dst": 2, "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Define what the distance array means after each round

Before any relaxation round, `dist[src] = 0` and every other entry is a large sentinel `INF`. This represents cheapest costs using at most zero edges: only the source is reachable.

After one complete round, `dist[v]` should mean the cheapest cost from `src` to `v` using at most one edge. After two rounds it should mean at most two edges, and so on.

Running exactly `k + 1` rounds therefore produces the cheapest costs among all routes allowed by the stop constraint.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Before any relaxation round, `dist[src] = 0` and every other... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Freeze the previous round with a snapshot

At the beginning of each round, the method creates `backup = dist.copy()`. Every flight relaxation reads its starting-city cost from `backup`:

`dist[t] = min(dist[t], backup[f] + p)`.

This separation is essential. `backup[f]` represents a path using at most the previous round's edge count. Adding flight `f -> t` creates a candidate using at most one more edge.

The destination update is written to `dist`, but no later flight in the same round is allowed to use that fresh update because all reads still come from `backup`. Thus one round can add at most one flight edge, regardless of the order in which flights appear.

Without the copy, a chain of several flights could propagate through `dist` during one scan. That would silently exceed the intended edge budget and make results depend on input edge order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `200` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]], "src": 0, "dst": 2, "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `200` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two-row dynamic programming:** Explicitly comp:** - **Two-row dynamic programming:** Explicitly compute costs for each exact or bounded edge count. It expresses the same recurrence and also uses $O(V)$ rolling space.
- **- **State-expanded Dijkstra:** Treat `(city, edges:** - **State-expanded Dijkstra:** Treat `(city, edges_used)` as a state and use a heap. It can return early but requires more elaborate dominance handling.
- **- **Ordinary Dijkstra with one distance per city:*:** - **Ordinary Dijkstra with one distance per city:** It can discard a more expensive but lower-edge state that is necessary under the stop constraint.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E)$. Let $V$ be the number of cities and $E$ the number of flights. There are `k + 1` rounds. Each round copies a $V$-entry distance array in $O(V)$ time and scans all $E$ flights in $O(E)$ time.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
