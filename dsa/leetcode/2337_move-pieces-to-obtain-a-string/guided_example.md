# Guided Example: Move Pieces to Obtain a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"start": "_L__R__R_", "target": "L______RR"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `start` and `target`, both of length `n`. Each string consists **only** of the characters `'L'`, `'R'`, and `'_'` where:

The objective is to compute `true` from `{"start": "_L__R__R_", "target": "L______RR"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Blanks move around pieces, but pieces never cross

An `L` piece may swap only with a blank immediately to its left, and an `R` piece may swap only with a blank immediately to its right. Neither move lets one piece jump over another piece.

Therefore, if all underscores are deleted, the remaining sequence of `L` and `R` characters must be identical in `start` and `target`. The first nonblank piece in the start must correspond to the first nonblank piece in the target, the second to the second, and so on.

The exact solution records these ordered pieces with their positions:

`a = [(piece, index) ... from start]`

and the analogous list `b` for `target`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"start": "_L__R__R_", "target": "L______RR"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: First ensure both strings contain the same number of pieces

Moves exchange a piece with a blank. They never create or destroy pieces. If `len(a) != len(b)`, one string contains more nonblank pieces than the other and transformation is impossible.

Equal counts are necessary but not sufficient. The corresponding types and movement directions must also be checked.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Pair pieces by their invariant order

`zip(a, b)` pairs the first start piece with the first target piece, then the second with the second, and so on. If paired characters `c` and `d` differ, achieving the target would require an `L` and an `R` to exchange relative order or change type. Neither operation is legal, so the method returns `false`.

This catches examples such as a nonblank sequence `RL` in the start and `LR` in the target. Even if individual directions appear favorable, the pieces cannot pass through each other.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"start": "_L__R__R_", "target": "L______RR"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two pointers skipping blanks:** Walk through both strings, compare the next pieces and their indices immediately. This preserves `O(n)` time while achieving true `O(1)` auxiliary space.
- **Breadth-first search over configurations:** It explores an enormous state graph and is unnecessary because reachability has a simple invariant characterization.
- **Compare only strings with underscores removed:** Matching piece order is necessary, but direction constraints are also required; `"_R"` cannot become `"R_"`.
- **Check only each character count:** Equal numbers of L and R do not preserve their relative order. Pieces cannot cross.
- **Allow pieces to jump over one another:** The rules permit only adjacent piece-blank swaps, so jumps would solve a different problem.
- **No pieces:** Both strings consist only of blanks, both lists are empty, and the transformation is already complete.
- **Different piece counts:** Immediate false because moves conserve pieces.
- **Same counts but different order:** Paired characters differ, proving a crossing would be necessary.
- **L stays in place:** `i == j` satisfies the left-only constraint.
- **R stays in place:** `i == j` satisfies the right-only constraint.
- **L target to the left:** It may traverse the intervening blanks without crossing matched earlier pieces.
- **R target to the right:** It may traverse blanks toward that position.
- **Adjacent opposing pieces:** Their order cannot reverse because neither can move through the other.
- **Input preservation:** The method builds separate pair lists and never modifies either string.
- **Exact-source space:** Storing nonblank tuples is linear even though the underlying reachability test can be streamed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the common string length. Each list comprehension scans its string once, and the paired loop visits at most `n` pieces. Total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
