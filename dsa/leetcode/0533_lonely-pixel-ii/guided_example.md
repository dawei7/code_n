# Guided Example: Lonely Pixel II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"picture": [["W", "W", "B"], ["W", "W", "B"], ["W", "W", "B"]], "target": 1}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` `picture` consisting of black `'B'` and white `'W'` pixels and an integer target, return *the number of **black** lonely pixels*.

The objective is to compute `0` from `{"picture": [["W", "W", "B"], ["W", "W", "B"], ["W", "W", "B"]], "target": 1}` while avoiding redundant calculations and unnecessary overhead.

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

A qualifying black pixel at `(r, c)` must satisfy two coupled rules:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"picture": [["W", "W", "B"], ["W", "W", "B"], ["W", "W", "B"]], "target": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- its row and column each contain exactly `target` black pixels;
- every row containing a black pixel in column `c` must be identical to row `r`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - its row and column each contain exactly `target` black pix... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The solution groups black pixels by column, counts black pixels per row, and then validates one whole column group at a time.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"picture": [["W", "W", "B"], ["W", "W", "B"], ["W", "W", "B"]], "target": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Count identical row patterns with tuples:** Ha:** - **Count identical row patterns with tuples:** Hash each qualifying row pattern and combine its frequency with column counts. It can make the intended $O(RC)$ time bound explicit while using $O(RC)$ space for patterns.
- **Check every black pixel independently:** Recounting its row, column, and peer rows repeats substantial work.
- **Columns with no black pixels:** They are absent from `g` and cannot contribute.
- **Representative row has wrong count:** The column is skipped immediately.
- **Column has wrong black count:** `len(g[j]) == rows[i1]` fails after the representative count is known to equal `target`.
- **Rows have equal counts but different patterns:** Full list equality rejects them.
- **One qualifying column:** It contributes exactly `target` pixels, not one.
- **One row or one column:** The same count and equality rules apply without special branches.
- **Repeated identical rows:** They are permitted and are exactly what the second rule may require.
- **Several qualifying columns in the same rows:** Each column contributes its distinct set of coordinates.
- **Rectangular guarantee:** Direct whole-row equality compares patterns of the same length.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R+B)$. Let $R$ and $C$ be the matrix dimensions, and let $B$ be the number of black pixels. Building `rows` and `g` takes $O(RC)$ time and stores $B$ row indices, using $O(R+B)=O(RC)$ space.
- **Auxiliary Space Complexity:** $O(RC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
