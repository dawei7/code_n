# Guided Example: Brick Wall

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"wall": [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a rectangular brick wall in front of you with `n` rows of bricks. The $i^{\text{th}}$ row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

The objective is to compute `2` from `{"wall": [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

A vertical line crosses a brick in a row unless it lands on an internal boundary between two bricks. Therefore the best line is the internal horizontal position shared by the largest number of rows.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"wall": [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution counts internal boundary positions using prefix sums of brick widths.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

For one row, variable `s` begins at zero. As each brick width `x` is processed, adding it gives the horizontal coordinate of that brick's right edge.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"wall": [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Test every possible coordinate against every row:** This repeats row scans and can become quadratic in the number of bricks.
- **Use physical-width buckets:** Wall width may be enormous, so allocating one slot per coordinate is unsafe.
- **Count the final edge:** It would always appear in every row and incorrectly return zero, despite the forbidden outside boundary.
- **Count the left edge:** Coordinate zero is also forbidden and intentionally absent.
- **One brick per row:** No internal edge exists, so every row is crossed.
- **All rows share an internal edge:** The answer is zero because that position is legal.
- **Different brick counts:** Only accumulated widths determine alignment.
- **Large widths:** Hashing prefix coordinates avoids dependence on total wall width.
- **Several equally common edges:** Any gives the same minimum; only the count is returned.
- **Positive widths:** They ensure strictly increasing boundaries within each row.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B)$. Let $B$ be the total number of bricks across all rows. Every brick except the final brick of each row is processed once. Time is $O(B)$.
- **Auxiliary Space Complexity:** $O(B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
