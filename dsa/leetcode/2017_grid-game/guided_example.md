# Guided Example: Grid Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[2, 5, 4], [1, 5, 1]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** 2D array `grid` of size `2 x n`, where $\text{grid}[r][c]$ represents the number of points at position `(r, c)` on the matrix. Two robots are playing a game on this matrix.

The objective is to compute `4` from `{"grid": [[2, 5, 4], [1, 5, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A first-robot path is determined by one column

In a grid with only two rows, a path begins on the top row, moves right some number of times, moves down exactly once, and then continues right on the bottom row. Choose the column `j` where the first robot moves down.

That path clears top-row columns zero through `j` and bottom-row columns `j` through the end.

The two cells in column `j` are both on the first robot's path: it arrives at the top cell and moves down into the bottom cell. This shared cleared column separates the surviving top-right and bottom-left regions, which is why neither remaining sum includes column `j`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[2, 5, 4], [1, 5, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Identify what remains for the second robot

Only two positive regions can remain:

- the top-row suffix strictly after `j`;
- the bottom-row prefix strictly before `j`.

The second robot cannot collect both regions. To collect the bottom-left prefix it must move down early and can never move back up to the top-right suffix. To collect the top-right suffix it stays on top past the cut and misses the bottom-left prefix.

It can choose whichever region has the larger sum, so for a fixed first-robot turn column its optimal score is

$$
\max(\text{top suffix after }j,\text{bottom prefix before }j).
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain both sums with exact update order

`s1` begins as the sum of the entire top row. `s2` begins at zero.

At column `j`, the source first executes `s1 -= grid[0][j]`. Now `s1` is the top suffix strictly after the turn column, excluding the cell cleared by the first robot.

It computes `max(s1,s2)` while `s2` still contains only bottom columns strictly before `j`. This is exactly the second robot's best response.

Only afterward does `s2 += grid[1][j]` prepare the bottom prefix for the next turn column.

Changing this order would incorrectly leave a turn-column cell available even though the first robot traverses both row cells at the downward move.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[2, 5, 4], [1, 5, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate both paths:** Enumerating first and second turn columns takes $O(N^2)$ and is unnecessary after deriving the two regions.
- **Prefix-sum arrays:** Permit constant-time region queries for every cut but use $O(N)$ space; rolling sums are simpler.
- **Maximize first robot's points greedily:** Solves the wrong objective and can leave a larger score for the opponent.
- **One column:** The first robot clears both cells and the second receives zero.
- **Turn at first column:** Bottom prefix is empty and only top suffix can score.
- **Turn at last column:** Top suffix is empty and only bottom prefix can score.
- **Balanced regions:** The second may choose either; their equal value is still the fixed-cut outcome.
- **Positive cell values:** Ensure collecting an entire available region is never worse than skipping part of it.
- **Update order:** Remove current top, evaluate, then add current bottom.
- **Large sums:** Python integers avoid overflow across $5\cdot10^4$ columns.
- **No grid mutation:** Running sums model the cleared path without writing zeroes.
- **Minimax:** First chooses the smallest possible value of the second's best response.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of columns. Computing the initial top sum takes $O(N)$ and the loop takes $O(N)$, for total time $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
