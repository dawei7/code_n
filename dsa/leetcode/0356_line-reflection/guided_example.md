# Guided Example: Line Reflection

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[1, 1], [-1, 1]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given `n` points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.

The objective is to compute `true` from `{"points": [[1, 1], [-1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the extreme horizontal coordinates determine the axis.

Let `min_x` be the smallest horizontal coordinate in the point set and `max_x` the largest. If a vertical reflection preserves the set, the leftmost point or points must reflect to the rightmost horizontal position. Reflection reverses horizontal order: smaller $x$ values become larger reflected values. Therefore the reflection axis must lie halfway between the two extremes:

$$
c=\frac{\texttt{min\_x}+\texttt{max\_x}}{2}.
$$

There is no need to try multiple candidate lines. Any other axis would send the minimum horizontal coordinate somewhere other than the maximum, so the extreme coordinates could not be preserved.

The exact solution stores `s = min_x + max_x`, which equals $2c$. This avoids floating-point arithmetic. The axis may lie at a half-integer, such as $x=1.5$, but `s` remains an exact integer. A point's reflected horizontal coordinate is simply `s - x`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[1, 1], [-1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Collecting the facts in one pass.

The first loop begins with `min_x = inf` and `max_x = -inf`. Every point updates both extremes. At the same time, `(x, y)` is inserted into `point_set`, a hash set used for expected constant-time membership checks.

Tuples are used because Python lists are mutable and cannot be hash-set keys. Converting `[x, y]` to `(x, y)` preserves both coordinate values in an immutable, hashable form.

Repeated input points collapse into one set entry. That is consistent with the problem's set-preservation meaning: repeating the same coordinate does not introduce a new geometric location that needs a different mirror. The second pass still visits repeated entries from the original list, but it asks the same membership question each time.

If the intended object were a multiset whose exact multiplicities had to match across the axis, a plain set would be insufficient. One would need frequencies. The accepted set-based interpretation treats the input as geometric points with duplicates allowed but not multiplicity-significant.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first loop begins with `min_x = inf` and `max_x = -inf`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Verifying every mirror.

After computing `s`, the generator examines every original point `(x, y)`. Its uniquely required mirror is `(s - x, y)`. The expression



checks whether that reflected location exists. `all(...)` returns true only if every point passes. It can stop early at the first missing partner.

For `[[1, 1], [-1, 1]]`, the extremes are `-1` and `1`, so `s = 0` and the axis is $x=0$. Point `(1, 1)` requires `(-1, 1)`, and point `(-1, 1)` requires `(1, 1)`. Both exist.

For `[[1, 1], [-1, -1]]`, the same candidate axis is derived. The mirror of `(1, 1)` would be `(-1, 1)`, not `(-1, -1)`. The missing same-height partner makes the answer false. This demonstrates why comparing only horizontal coordinate counts is not enough; pairing must preserve $y$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[1, 1], [-1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Group and sort x-coordinates by height:** For :** - **Group and sort x-coordinates by height:** For every $y$, sort that row's horizontal coordinates and compare pairs from the outside inward against a common sum. This can verify symmetry but costs $O(n\log n)$ time overall.
- **- **Try every possible partner or axis:** Comparin:** - **Try every possible partner or axis:** Comparing point pairs can reach $O(n^2)$ time and ignores the fact that the global extremes uniquely determine the candidate axis.
- **- **Frequency map for multiset symmetry:** Store c:** - **Frequency map for multiset symmetry:** Store counts of every coordinate and require equal counts for `(x, y)` and `(s - x, y)`. This is necessary only if duplicate multiplicity is semantically meaningful; the exact source follows set semantics.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $n$ be the number of entries in `points` and let $u$ be the number of distinct coordinate pairs, where $u\le n$.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
