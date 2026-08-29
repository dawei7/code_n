# Guided Example: Bus Routes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"routes": [[1, 2, 7], [3, 6, 7]], "source": 1, "target": 6}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `routes` representing bus routes where $\text{routes}[i]$ is a bus route that the $i^{\text{th}}$ bus repeats forever.

The objective is to compute `2` from `{"routes": [[1, 2, 7], [3, 6, 7]], "source": 1, "target": 6}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The number of buses, not the number of stops, is the distance

Traveling to any stop on one bus route costs exactly one boarded bus. Moving between two stops on the same route does not add another bus, because each route repeats forever. A transfer at a shared stop adds one when the next route is boarded.

This suggests breadth-first search, but the search level must represent buses taken rather than physical stop-to-stop movements. The exact solution stores queue entries as `(stop, bus_count)`. From a stop reached with `bus_count` buses, boarding one previously unused route generates all stops on that route with `bus_count + 1`.

Because each transition has the same cost of one newly boarded bus, breadth-first order guarantees that the first time the target stop is reached uses the fewest buses.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"routes": [[1, 2, 7], [3, 6, 7]], "source": 1, "target": 6}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Handle the zero-bus journey first

If `source == target`, the traveler is already at the destination and needs zero buses. The function returns 0 before building any graph.

This special case matters even if the shared stop does not appear in any route. Being at the destination requires no bus-service availability.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build the stop-to-routes index

The original input is organized from route to stops: `routes[i]` lists all stops served by bus route `i`. During search, however, we stand at a stop and need to know which routes can be boarded there.

The dictionary `g` reverses the relationship:

$$
\texttt{g[stop]}=\text{all route indices containing that stop}.
$$

The nested loops visit every route-stop occurrence once and append its route index to the stop's list. For routes `[1,2,7]` and `[3,6,7]`, for example, `g[7]` becomes `[0,1]`, revealing that stop 7 permits a transfer between the two buses.

If either `source` or `target` is absent from `g`, no bus can depart from the source or no bus can arrive at the target. Since the equal-stop case was already handled, the function safely returns `-1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"routes": [[1, 2, 7], [3, 6, 7]], "source": 1, "target": 6}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Route-node BFS:** Treat each route as a graph node and connect routes sharing a stop. A direct all-pairs route graph can be expensive to construct. The stop-to-routes index discovers exactly the needed transfers without materializing every route pair.
- **Stop-node graph with all pairwise edges:** Connecting every pair of stops on the same route may require quadratic edges for one long route. Expanding a route only once represents the same reachability in linear total input size.
- **Dijkstra's algorithm:** Every bus boarding costs one, so the graph is unweighted at the relevant level. BFS is sufficient and simpler.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
