# Guided Example: Reaching Points

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sx": 1, "sy": 1, "tx": 3, "ty": 5}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given four integers `sx`, `sy`, `tx`, and `ty`, return `true`* if it is possible to convert the point *`(sx, sy)`* to the point *`(tx, ty)` *through some operations**, or *`false`* otherwise*.

The objective is to compute `true` from `{"sx": 1, "sy": 1, "tx": 3, "ty": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Forward search branches, but backward search is almost forced

From `(x, y)`, one move produces either `(x, x + y)` or `(x + y, y)`. A forward search has two choices at every point, and coordinates can grow toward $10^9$, so enumerating descendants is impractical.

Work backward from `(tx, ty)` instead. All coordinates are positive. If `tx > ty`, the last forward move could only have added `ty` to the first coordinate, so the preceding point must be `(tx - ty, ty)`. The other operation would have made the second coordinate larger, contrary to `tx > ty`.

Similarly, if `ty > tx`, the unique possible parent is `(tx, ty - tx)`. This turns a branching forward process into a deterministic reverse process.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sx": 1, "sy": 1, "tx": 3, "ty": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Bundle repeated subtractions with modulo

Repeatedly subtracting the smaller coordinate is correct but can be too slow. If `tx` is much larger than `ty`, several reverse steps will keep `ty` fixed:

`tx, tx - ty, tx - 2 * ty, ...`.

Modulo performs all those subtractions at once. Therefore:

- When `tx > ty`, replace `tx` with `tx % ty`.
- When `ty > tx`, replace `ty` with `ty % tx`.

This is the same acceleration used by the Euclidean algorithm.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Repeatedly subtracting the smaller coordinate is correct but... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the main loop keeps both coordinates strictly above the start

The loop continues only while `tx > sx` and `ty > sy` and the target coordinates differ. While both are still above their respective starting values, bundling all possible same-direction reverse steps cannot skip the only remaining form of a solution that must be checked separately.

Once one target coordinate equals its starting coordinate, that coordinate must remain fixed for the rest of the forward journey. Applying modulo again could jump below the boundary or to zero and lose the information needed to test how many repeated additions remain.

The loop also stops if `tx == ty`. For equal positive coordinates, subtracting one from the other would make a coordinate zero. Positive starting coordinates cannot reach such a parent. Equality is useful only if the complete target already equals the start, which is tested afterward.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sx": 1, "sy": 1, "tx": 3, "ty": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Repeated reverse subtraction:** It follows the:** - **Repeated reverse subtraction:** It follows the same unique-parent proof, but cases such as a huge `tx` with small `ty` can require nearly $10^9$ iterations.
- **- **Forward breadth-first or depth-first search:**:** - **Forward breadth-first or depth-first search:** Each point has two children and the reachable tree grows too quickly for the coordinate limits.
- **- **Memoized forward search:** Avoiding duplicate :** - **Memoized forward search:** Avoiding duplicate states does not solve the enormous two-dimensional search-space problem.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log(\max(tx, ty)))$. Each loop iteration performs the larger coordinate modulo the smaller coordinate, matching Euclid's algorithm. The coordinate scale decreases geometrically over successive iterations in the standard amortized analysis, giving $O(\log(\max(tx, ty)))$ time under constant-time integer arithmetic.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
