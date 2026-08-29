# Guided Example: Equal Sum Grid Partition I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 4], [2, 3]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` matrix `grid` of positive integers. Your task is to determine if it is possible to make **either one horizontal or one vertical cut** on the grid such that:

The objective is to compute `true` from `{"grid": [[1, 4], [2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A straight cut is determined by complete row or column prefixes

A horizontal cut between rows `i` and `i+1` places rows zero through `i` in the top section and all later rows in the bottom.

A vertical cut between columns `j` and `j+1` places columns zero through `j` on the left and all later columns on the right.

No other submatrix shapes are permitted. Therefore, it is enough to compare cumulative sums of whole leading rows and whole leading columns with half of the total grid sum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 4], [2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reject an odd total immediately

Let total grid sum be `s`. Equal integer section sums would each be `s/2`. If `s` is odd, no such integer split exists, so the source returns false immediately.

This is a necessary condition, not a sufficient one; an even total still needs a cut boundary whose prefix sum is exactly half.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Check horizontal cuts

`pre` starts at zero. For each row, the source adds `sum(row)`. After processing row `i`:

`pre` equals the sum of every cell in rows zero through `i`.

The complementary bottom section has sum `s-pre`. They are equal exactly when:

`2*pre = s`.

The condition also requires `i != len(grid)-1`. A cut after the final row would leave the second section empty, which the problem forbids.

Although the loop computes the full-grid prefix at the final row, it explicitly refuses to treat that boundary as a cut.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 4], [2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **2D prefix sum:** Correct in `O(mn)` time but uses `O(mn)` space for more general rectangle queries than needed.
- **Store row and column sums:** Two arrays give `O(m+n)` space and a straightforward single cell pass.
- **Rotate the grid:** Lets one horizontal routine handle both orientations but allocates another matrix.
- **Check arbitrary submatrices:** The cut must span the whole grid, so arbitrary rectangle enumeration solves a different problem.
- **Odd total:** Immediate false is safe because integer halves cannot be equal.
- **One row:** No horizontal cut is legal, but vertical cuts may be.
- **One column:** No vertical cut is legal, but horizontal cuts may be.
- **Two cells total:** There is exactly one possible boundary along the non-singleton dimension.
- **Cut after the last row or column:** Explicit final-index checks reject the empty complementary section.
- **Positive entries:** Prefix sums strictly increase, but the source does not rely on early termination; equality logic is sufficient.
- **First possible boundary:** It is checked after the first row or column, so both sections are non-empty when another line remains.
- **zip space behavior:** The conceptual running-sum method is constant-state, but exact Python tuple/iterator materialization gives an `O(m)` caveat.
- **Even total without matching boundary:** The scans finish and correctly return false.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let the grid have `m` rows and `n` columns, with `mn <= 100,000`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
