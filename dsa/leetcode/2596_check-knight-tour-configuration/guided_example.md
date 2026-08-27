# Guided Example: Check Knight Tour Configuration

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 3, 6], [5, 8, 1], [2, 7, 4]]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a knight on an `n x n` chessboard. In a valid configuration, the knight starts **at the top-left cell** of the board and visits every cell on the board **exactly once**.

The objective is to compute `false` from `{"grid": [[0, 3, 6], [5, 8, 1], [2, 7, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The grid gives visit times, not a path directly

Each cell stores when the knight visited it. To validate the tour, the useful order is the reverse mapping:

`visit number -> cell coordinates`.

The solution builds array `pos` of length $n^2$. When it sees `grid[i][j] = t`, it stores `pos[t] = (i,j)`. Because the matrix contains every distinct integer from zero through $n^2-1$, every position in `pos` is filled exactly once.

After inversion, `pos[0]` is the starting cell, `pos[1]` is the next cell, and so on. The tour can be validated by checking consecutive coordinate pairs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 3, 6], [5, 8, 1], [2, 7, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Check the required starting cell first

A valid tour must begin at the top-left cell. Since visit numbers are zero-indexed, `grid[0][0]` must equal zero.

The condition `if grid[0][0]: return false` uses Python truthiness: zero is false, while every positive visit number is true. Thus any nonzero top-left label is rejected immediately.

The distinct complete-label guarantee then ensures visit zero appears nowhere else when this check passes.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A valid tour must begin at the top-left cell.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recognize one legal knight move

A knight changes one coordinate by two cells and the other by one. Direction signs do not matter, so the code computes absolute differences:

`dx = abs(x1 - x2)` and `dy = abs(y1 - y2)`.

The move is legal exactly when

$$
(dx,dy)=(1,2)
\quad\text{or}\quad
(dx,dy)=(2,1).
$$

These two cases cover all eight directional moves: each coordinate change can be positive or negative, and the one-step and two-step roles may be exchanged.

A move such as $(2,2)$ is diagonal but not a knight move. A move such as $(0,1)$ is adjacent but also invalid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 3, 6], [5, 8, 1], [2, 7, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Search for each next label:** Repeatedly scann:** - **Search for each next label:** Repeatedly scanning the grid for visit $t+1$ would take $O(n^4)$ time; inversion makes every lookup direct.
- **Sort coordinate-label triples:** Sorting all cells by label also works in $O(n^2\log n)$ time but ignores the dense complete label range.
- **Wrong starting label:** Any nonzero `grid[0][0]` fails before other work.
- **Illegal final move:** `pairwise` includes the transition to label $n^2-1$, so it is checked.
- **All labels unique:** The contract makes a separate duplicate-cell or missing-label check unnecessary.
- **Reversed knight displacement:** Both $(1,2)$ and $(2,1)$ are accepted.
- **Direction signs:** Absolute differences cover left, right, up, and down variants.
- **Nonconsecutive cells:** They need not be a knight move and are intentionally not compared.
- **Input preservation:** Only the new `pos` array is written.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. There are $n^2$ cells. Building `pos` visits each once in $O(n^2)$ time. `pairwise` produces $n^2-1$ transitions, each checked in constant time, so total time is $O(n^2)$.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
