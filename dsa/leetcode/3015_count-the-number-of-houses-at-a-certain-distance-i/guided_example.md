# Guided Example: Count the Number of Houses at a Certain Distance I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "x": 1, "y": 3}`
- **Required output:** `[6, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given three **positive** integers `n`, `x`, and `y`.

The objective is to compute `[6, 0, 0]` from `{"n": 3, "x": 1, "y": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: There are only three relevant path shapes

Houses form a path graph: moving directly from house $i$ to $j$ along consecutive streets costs $|i-j|$. One extra undirected street connects `x` and `y`.

A shortest route between two houses either:

1. ignores the extra street;
2. travels from the first house to `x`, crosses to `y`, then reaches the second;
3. travels to `y`, crosses to `x`, then reaches the second.

Using the extra street more than once cannot improve a shortest path because all edges cost one; traversing it twice introduces a removable positive cycle.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "x": 1, "y": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Convert coordinates to zero-based indices

The code subtracts one from `x` and `y` so they match loop indices zero through $N-1$. Distances are unchanged by this uniform coordinate shift.

For each unordered pair `i < j`, it computes:

- `a = j - i`, the direct path distance;
- `b = abs(i - x) + 1 + abs(j - y)`, using shortcut $x\to y$;
- `c = abs(i - y) + 1 + abs(j - x)`, using shortcut $y\to x$.

The true graph distance is `min(a, b, c)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why these formulas cover every shortest path

Before and after crossing the extra edge, the graph is an ordinary line. The shortest way to reach an endpoint on a line is absolute index difference. The crossing itself costs one.

An optimal route that uses the extra edge chooses one of its two orientations, giving exactly `b` or `c`. An optimal route that does not use it gives `a`. No fourth structural possibility exists.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[6, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "x": 1, "y": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[6, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build the graph and run BFS from every house:** This costs $O(N^2)$ on the sparse graph too, but the three closed path formulas are simpler and avoid adjacency storage.
- **Count only unordered pairs:** The required result counts both directions, so every pair contributes two.
- **Consider one shortcut orientation:** The closer endpoint depends on the pair; both `b` and `c` are necessary.
- **Use the shortcut repeatedly:** Positive edge costs make repeated crossings nonoptimal.
- **`x == y`:** The self-loop never shortens a route, and direct distances win automatically.
- **Adjacent `x,y`:** The extra edge duplicates an existing street and does not change distances.
- **Shortcut endpoints at extremes:** It can substantially shorten many pairs; formulas remain unchanged.
- **Last result entry:** Distance $N$ is impossible between distinct houses, so it remains zero.
- **Conservation invariant:** Output counts always sum to $N(N-1)$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. The nested loops process $\binom N2=O(N^2)$ unordered pairs. Each pair performs constant arithmetic, so time is $O(N^2)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
