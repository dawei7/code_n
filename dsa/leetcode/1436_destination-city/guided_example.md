# Guided Example: Destination City

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"paths": [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]}`
- **Required output:** `"Sao Paulo"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given the array `paths`, where $\text{paths}[i] = [\text{cityA}_{i}, \text{cityB}_{i}]$ means there exists a direct path going from $\text{cityA}_{i}$ to $\text{cityB}_{i}$. *Return the destination city, that is, the city without any path outgoing to another city.*

The objective is to compute `"Sao Paulo"` from `{"paths": [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The destination is characterized by having no outgoing edge

Each path `[a,b]` says that travel leaves city `a` and arrives at city `b`. The destination city is not merely a city that appears on the right; intermediate cities also appear there. It is the right-side city that never appears as a left-side departure.

Because the paths form one loop-free line, exactly one such city exists.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"paths": [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Collect every city with an outgoing path

The set comprehension:



unpacks every pair, keeps the departure `a`, and ignores the arrival with underscore. The resulting set contains exactly the cities that have an outgoing path.

A set is appropriate because only presence matters. If a more general input repeated a departure city, storing it once would still answer whether it has any outgoing edge.

Expected set membership is constant time, replacing a repeated scan through all paths.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Search among arrival cities

The return expression is:



Every destination candidate must appear as `b` in some path because it is reached from the previous city on the line. The generator visits arrivals in input order and yields only those absent from the outgoing-city set.

`next` returns the first yielded city. The problem guarantee ensures exactly one destination exists, so the generator cannot be exhausted without a result.

The city does not have to appear in the final input row. Paths may be listed in arbitrary order. Membership in `s`, not row position, determines whether an arrival is terminal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"Sao Paulo"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"paths": [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"Sao Paulo"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Nested scan:** For each arrival, scan all departures to see whether it leaves again. It uses constant space but takes $O(n^2)$ time.
- **Set difference:** Build both arrival and departure sets, then return the sole member of `arrivals - departures`. It is concise but stores a second set that the generator avoids.
- **Degree counting:** Record incoming and outgoing degrees for every city, then select outdegree zero. This generalizes to richer graphs but stores more information than needed.
- **Follow the chain:** Build a map from departure to arrival, find the start, and walk until no next city exists. It works but requires identifying and traversing the entire line.
- **One path:** Its right city is absent from the one-element departure set and is returned.
- **Input edges out of order:** Set membership makes order irrelevant.
- **City names with spaces:** Strings are used as opaque hash keys; their contents require no parsing.
- **Intermediate arrival:** It is rejected because it also occurs as a departure.
- **Uniqueness guarantee:** `next` safely returns the first match because exactly one destination exists.
- **No fallback return:** Malformed input without a destination would raise generator exhaustion, but the contract rules that case out.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of paths. Building the outgoing set scans $n$ pairs in expected $O(n)$ time. Searching arrivals scans at most $n$ pairs with expected $O(1)$ membership tests, so total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
