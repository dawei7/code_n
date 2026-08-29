# Guided Example: Execution of All Suffix Instructions Staying in a Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "startPos": [0, 1], "s": "RRDDLU"}`
- **Required output:** `[1, 5, 4, 3, 1, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an `n x n` grid, with the top-left cell at `(0, 0)` and the bottom-right cell at $(n - 1, n - 1)$. You are given the integer `n` and an integer array `startPos` where $startPos = [\text{start}_{row}, \text{start}_{col}]$ indicates that a robot is initially at cell $(\text{start}_{row}, \text{start}_{col})$.

The objective is to compute `[1, 5, 4, 3, 1, 0]` from `{"n": 3, "startPos": [0, 1], "s": "RRDDLU"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat every suffix as an independent simulation

For answer index `i`, the robot always starts from the original `startPos` and executes `s[i]`, `s[i + 1]`, and so on.

Movement from an earlier answer must not carry into the next one. The source therefore resets

`x, y = startPos`

and `t = 0` for every outer-loop index.

`t` counts only instructions actually executed while remaining inside the grid.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "startPos": [0, 1], "s": "RRDDLU"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Translate each instruction into a coordinate delta

The fixed map `mp` assigns:

- `L -> [0, -1]`;
- `R -> [0, 1]`;
- `U -> [-1, 0]`;
- `D -> [1, 0]`.

For current position $(x,y)$ and delta $(a,b)$, the proposed next position is $(x+a,y+b)$.

The move is legal exactly when both coordinates remain within 0 through `n - 1`:

`0 <= x + a < n and 0 <= y + b < n`.

Only after this test succeeds does the source update the position and increment `t`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Stop before executing an illegal instruction

The contract says the robot stops when the next instruction would leave the grid. That instruction is not counted.

The source checks the proposed position first. On failure it executes `break` without changing `x`, `y`, or `t`. This avoids the common off-by-one error of moving outside and then subtracting one from the count.

If all instructions through the end are legal, the inner loop ends naturally and `t` equals the suffix length `m - i`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 5, 4, 3, 1, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "startPos": [0, 1], "s": "RRDDLU"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 5, 4, 3, 1, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Coordinate prefix sums with range queries:** One can analyze when a suffix's relative row or column displacement first exceeds grid margins, but the implementation is substantially more complex.
- **Carry position between suffixes:** Incorrect because every suffix restarts at `startPos`.
- **Count the failing instruction:** Incorrect; the robot stops before executing it.
- **One-cell grid:** Every possible move leaves immediately, so all answers are zero.
- **Start on an edge:** Instructions pointing outward can fail at the first step.
- **All suffix moves legal:** Answer `i` equals `m - i`.
- **Failure followed by safe characters:** Later characters are irrelevant because execution stops permanently at the first failure.
- **Last instruction:** Its answer is either one or zero.
- **Direction mapping:** Row changes implement up/down, while column changes implement left/right.
- **Bounds are inclusive-exclusive:** Legal coordinates satisfy `0 <= coordinate < n`.
- **Output order:** One count is appended for each suffix in increasing `i`.
- **Input preservation:** `startPos` is unpacked but never changed.
- **Fresh counter per suffix:** `t` must reset to zero together with coordinates.
- **Valid instruction alphabet:** Guarantees every character has a delta in `mp`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m^2)$. Let $m$ be the instruction-string length.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
