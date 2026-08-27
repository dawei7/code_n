# Guided Example: Candy Crush

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}`
- **Required output:** `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

This question is about implementing a basic elimination algorithm for Candy Crush.

The objective is to compute `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` from `{"board": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simulate rounds until no crush is possible

One crush can cause candies above it to fall, and those moved candies may create new groups. Therefore a single scan is not sufficient. The exact solution repeats complete rounds:

1. Find and mark every horizontal group that must be crushed.
2. Find and mark every vertical group that must be crushed.
3. If anything was marked, apply gravity to every column.
4. Start another round on the changed board.

The loop ends only when a full marking pass finds no group. At that moment gravity is unnecessary and the board is stable by definition.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why crushing must be simultaneous within a round

All groups present at the beginning of a round must disappear together. If a horizontal group were immediately replaced with zero before checking vertical groups, an intersecting vertical group might be broken and missed.

The solution solves this by marking a candy for removal with the negative version of its type. A positive value is a live candy. A negative value is scheduled to be removed in the current round. Zero is empty.

The candy’s magnitude is preserved, so comparisons use `abs(board[i][j])`. A horizontally marked candy can still participate in a vertical match during the same marking phase. This is exactly what simultaneous detection requires.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | All groups present at the beginning of a round must disappea... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark every horizontal run

For each row, the scan considers every position `j` from `2` onward as the right endpoint of a length-three window. It checks that the current cell is nonzero and that the absolute values at `j`, `j - 1`, and `j - 2` are equal.

When they match, all three cells are assigned the negative absolute candy type and `run` becomes true.

Checking overlapping triples is sufficient for runs longer than three. A run of four equal candies contains triples ending at its third and fourth positions. The first triple marks the first three; the next comparison still recognizes their type through `abs` and marks the fourth as part of the overlapping triple. The same reasoning covers any longer run.

The nonzero check prevents three empty cells from being treated as a candy group. A negative marked value remains truthy, so it can still extend another same-type triple in the current phase.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Collect coordinates in a set:** Scan the board:** - **Collect coordinates in a set:** Scan the board and add every crushable position to a set, then clear those cells and apply gravity. This is conceptually direct but needs `O(mn)` extra space in the worst case. Negative marking stores the same information inside the board.
- **- **Crush immediately while scanning:** This is in:** - **Crush immediately while scanning:** This is incorrect because an erased cell may belong to another horizontal or vertical group that must be detected simultaneously. Mark first, then remove.
- **- **Copy the board for each round:** Comparing aga:** - **Copy the board for each round:** Comparing against an unchanged snapshot also preserves simultaneity, but it requires `O(mn)` additional memory per working copy. Absolute-value marking achieves the same effect in place.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((R + 1)$. Let `m` be the number of rows, `n` the number of columns, and `R` the number of successful crushing rounds.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
