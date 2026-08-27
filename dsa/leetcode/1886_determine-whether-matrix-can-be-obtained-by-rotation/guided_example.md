# Guided Example: Determine Whether Matrix Can Be Obtained By Rotation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mat": [[0, 1], [1, 0]], "target": [[1, 0], [0, 1]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two `n x n` binary matrices `mat` and `target`, return `true`* if it is possible to make *`mat`* equal to *`target`* by **rotating** *`mat`* in **90-degree increments**, or *`false`* otherwise.*

The objective is to compute `true` from `{"mat": [[0, 1], [1, 0]], "target": [[1, 0], [0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

**There are only four possible orientations.** Rotating a square matrix by 90 degrees four times returns to the original arrangement. Therefore, every allowed result is one of the 0-degree, 90-degree, 180-degree, or 270-degree orientations. The source checks all four possibilities simultaneously while scanning the target rather than physically rotating `mat` four times.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mat": [[0, 1], [1, 0]], "target": [[1, 0], [0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Store surviving orientations as bits.** Variable `ok` starts as binary `0b1111`. Each of its four low bits means that one orientation is still compatible with every cell examined so far. When a comparison for an orientation fails, the code clears only that orientation's bit with `ok &= ~bit`. A cleared bit can never become viable later because one mismatching cell is enough to disprove whole-matrix equality.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Store surviving orientations as bits.** Variable `ok` star... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Although Python's `~` produces a negative integer with conceptually unbounded leading one bits, AND with the current four-bit `ok` clears the intended low bit and leaves the other candidate bits unchanged. For example, `ok &= ~0b0010` removes the second orientation but preserves the first, third, and fourth.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mat": [[0, 1], [1, 0]], "target": [[1, 0], [0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Rotate in place up to four times:** Compare af:** - **Rotate in place up to four times:** Compare after each rotation and mutate layers of `mat`. This also uses $O(1)$ extra space and $O(n^2)$ time, but changes the input and has more error-prone swap logic.
- **Build a new rotated matrix:** A comprehension such as transposed reversed rows makes each orientation easy to see, but allocates $O(n^2)$ additional space for every rotation.
- **Compare only counts of zeros and ones:** Equal counts are necessary but not sufficient because rotation must preserve exact relative positions. Coordinate comparisons are required.
- **One-by-one matrix:** All four coordinate formulas refer to the sole cell. The result is simply whether the two cells are equal.
- **Rotational symmetry:** More than one bit may survive when `mat` is symmetric. The result only needs existence, so retaining multiple candidates is harmless.
- **Target equal without rotation:** The identity bit remains set and true is returned even if all rotated orientations fail.
- **No orientation works:** Bits may fail at different cells. Early false occurs as soon as the last remaining orientation receives its first mismatch.
- **Direction terminology:** The source checks both quarter-turn directions plus 180 degrees and identity. Since repeated 90-degree rotations generate all four, the result does not depend on naming one direction as the primary rotation.
- **Bitwise complement in Python:** `~bit` is negative, but AND with the nonnegative four-bit candidate mask has the intended low-bit clearing behavior. Using `ok ^= bit` would be unsafe because it could turn an already-cleared candidate back on.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. The nested loops visit all $n^2$ cells in the worst case. At each cell, four comparisons, four possible bit clears, and one mask test take constant time. Four is a fixed number of orientations, so total time is $O(n^2)$. Early exit can reduce work on incompatible matrices but does not change the worst-case bound.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
