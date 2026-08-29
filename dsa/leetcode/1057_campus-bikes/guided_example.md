# Guided Example: Campus Bikes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"workers": [[0, 0], [2, 1]], "bikes": [[1, 2], [3, 3]]}`
- **Required output:** `[1, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

On a campus represented on the X-Y plane, there are `n` workers and `m` bikes, with $n \le m$.

The objective is to compute `[1, 0]` from `{"workers": [[0, 0], [2, 1]], "bikes": [[1, 2], [3, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the repeated rule into one sortable key

At every assignment step, the problem chooses among all currently available worker–bike pairs using three priorities:

1. Smaller Manhattan distance.
2. Smaller worker index when distances tie.
3. Smaller bike index when both distance and worker index tie.

Those priorities are exactly the lexicographic order of a tuple `(distance, worker_index, bike_index)`. Python compares tuples from left to right, moving to the next component only when the earlier components are equal.

The exact solution generates one such tuple for every possible worker–bike combination, sorts all tuples once, and scans them from smallest to largest. Availability arrays decide whether a pair is still usable.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"workers": [[0, 0], [2, 1]], "bikes": [[1, 2], [3, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate every candidate pair

Let `n` be the worker count and `m` be the bike count. The loop:



enumerates the Cartesian product of worker indices and bike indices. For every worker `i`, it visits every bike `j` exactly once. There are therefore `n * m` iterations.

For each pair, Manhattan distance is:



The first absolute difference is horizontal distance and the second is vertical distance. Their sum is the required shortest grid-walking distance between the two coordinates.

The code appends:



Including both indices is not merely bookkeeping. Their order in the tuple encodes the two specified tie-breakers after distance.

All positions are unique, but distances need not be. Two different pairs can easily have the same Manhattan distance, so relying on distance alone would not reproduce the required deterministic assignment process.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort once in the exact global priority order

The statement:



sorts tuples in ascending lexicographic order. The resulting sequence is ordered first by distance, then by worker index, then by bike index. It is therefore the same order in which pairs would be considered by repeatedly searching for the smallest currently available key.

A subtle point is that some early tuples will later be unusable because their worker or bike was already assigned. They remain in `arr`, but the scan simply ignores them.

This works because availability changes only from true to false. Once a pair is unusable, it can never become usable later: assigned workers are never released, and assigned bikes are never returned. Consequently, a skipped tuple never needs to be reconsidered.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"workers": [[0, 0], [2, 1]], "bikes": [[1, 2], [3, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Distance buckets for the manifest target:** Group each `(worker, bike)` pair by its integer Manhattan distance and scan buckets from zero through `D`. Generate pairs in worker-major and bike-minor order so no per-bucket sort is needed. This achieves `O(WB + D)` time.
- **Global minimum heap of all pairs:** Heapifying every tuple and popping by priority reproduces the rule but uses `O(WB log(WB))` total pop time in the worst case and does not improve space.
- **One sorted bike list per worker plus a heap:** Keep each worker's bikes ordered by distance and maintain only that worker's current closest candidate in a global heap. This reduces heap size but still requires substantial preprocessing and careful replacement when a bike is taken.
- **Repeated full search:** Recompute the best available pair by scanning every worker and bike before each assignment. It directly mirrors the statement but can take `O(W^2B)` time.
- **One worker:** The first available tuple for that worker gives the globally closest bike, with bike index resolving distance ties.
- **Equal numbers of workers and bikes:** Every bike is eventually used, though assignment order still follows the global pair priority rather than independent nearest choices.
- **More bikes than workers:** Some bikes remain unused. Their tuples are harmless after all workers are marked assigned.
- **Distance ties across workers:** Tuple ordering gives the smaller worker index priority, even if the other tied worker has fewer good alternatives. The contract requires this local greedy choice.
- **Distance ties for one worker:** The smaller bike index appears first and is selected if still free.
- **Already-taken closest bike:** The tuple is skipped, and the worker remains unassigned until the scan reaches its next legal bike.
- **Parallel coordinate values are absent:** Locations are unique, but workers and bikes can still be at Manhattan distance zero only if a worker position equals a bike position. Cross-category equality is not prohibited by uniqueness wording, and the formula handles it.
- **No early break:** The exact loop scans all tuples after assignments are complete. Adding an assigned-worker counter could stop early but would not improve the asymptotic sorting bound.
- **Placeholder zeros:** Bike zero is a valid assignment, so `ans` alone cannot indicate whether a worker is assigned. `vis1` provides that separate status.
- **Input preservation:** Coordinates are only read. Sorting affects the newly built tuple list, not `workers` or `bikes`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(WB + D)$. Let `W` be the number of workers, `B` the number of bikes, and `P = WB` the number of possible pairs.
- **Auxiliary Space Complexity:** $O(W)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
