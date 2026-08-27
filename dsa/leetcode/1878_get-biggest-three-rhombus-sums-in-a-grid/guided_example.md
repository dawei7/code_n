# Guided Example: Get Biggest Three Rhombus Sums in a Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}`
- **Required output:** `[20, 9, 8]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` integer matrix `grid`​​​.

The objective is to compute `[20, 9, 8]` from `{"grid": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Describe every rhombus by a center and radius.** The source uses one-based coordinates `(i, j)` for a rhombus's center and a radius `k`. For `k > 0`, its four corners are top `(i - k, j)`, right `(i, j + k)`, bottom `(i + k, j)`, and left `(i, j - k)`. Radius zero is the area-zero rhombus consisting only of the center cell. This representation enumerates every valid rotated square exactly once because the four corners uniquely determine their center and equal vertical and horizontal radius.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Bound the radius before enumeration.** For a center `(i, j)`, the distance to the four grid boundaries is `i - 1` upward, `m - i` downward, `j - 1` leftward, and `n - j` rightward. The largest valid radius is their minimum:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Bound the radius before enumeration.** For a center `(i, j... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Every `k` from `1` through `l` keeps all four corners in the grid. Any larger radius crosses at least one boundary. The code separately inserts the center value `x` for radius zero, then loops through all positive radii, so narrow grids and single rows need no exceptional geometry branch.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[20, 9, 8]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[20, 9, 8]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Fixed top-three structure:** Track at most thr:** - **Fixed top-three structure:** Track at most three distinct values with direct comparisons after every candidate. This restores constant-time answer maintenance and gives the manifest's clean $O(mn\min(m,n))$ time without relying on a balanced sorted container.
- **Enumerating every border cell:** Walking all four edges for every center and radius avoids prefix tables but adds another factor proportional to the radius, producing a substantially slower worst case.
- **Horizontal and vertical prefix sums:** They do not align with a 45-degree rhombus border. Two diagonal prefix directions are the natural structures that make each edge a difference of two stored values.
- **Area-zero rhombi:** Every individual cell is a valid candidate. The explicit `ss.add(x)` is essential because the positive-radius loop starts at one and cannot discover them.
- **Single row or single column:** Every boundary minimum is zero, so only cell values are inserted. Distinctness and top-three selection still work normally.
- **Repeated sums from different rhombi:** `SortedSet` stores a numeric sum once, as required. The task asks for distinct values, not distinct shapes.
- **Fewer than three distinct sums:** The set is never padded. Reversing it returns exactly one or two values when that is all the grid provides.
- **Corner double counting:** Simply adding four inclusive diagonal segments counts every corner twice. The exact endpoint conventions here instead omit top and duplicate bottom, so the specific subtract-bottom/add-top correction must be understood rather than replaced mechanically.
- **Dependency on `SortedSet`:** This is not Python's built-in `set`; it relies on an ordered-set implementation supplied by the execution environment. A portable solution can use an ordinary set plus fixed top-three comparisons because only three final values are needed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ and $n$ be the grid dimensions, and let $q=\min(m,n)$. Building `s1` and `s2` takes $O(mn)$ time and $O(mn)$ space. Across all centers, the number of enumerated radii is $O(mnq)$; each geometric sum uses a constant number of prefix lookups and arithmetic operations.
- **Auxiliary Space Complexity:** $O(MN)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
