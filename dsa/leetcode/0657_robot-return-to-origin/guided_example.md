# Guided Example: Robot Return to Origin

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"moves": "UD"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a robot starting at the position `(0, 0)`, the origin, on a 2D plane. Given a sequence of its moves, judge if this robot **ends up at **`(0, 0)` after it completes its moves.

The objective is to compute `true` from `{"moves": "UD"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track net displacement

The robot begins at coordinate `(0, 0)`. Every command changes exactly one coordinate by one unit:

- `U` adds one to the vertical coordinate `y`;
- `D` subtracts one from `y`;
- `L` subtracts one from the horizontal coordinate `x`;
- `R` adds one to `x`.

The final position is obtained by accumulating all these changes. The robot returns to the origin exactly when both final coordinates are zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"moves": "UD"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why two counters contain all necessary state

The plane position after any prefix of moves is fully described by its horizontal and vertical displacement from the start. We do not need to remember the entire path, visited points, the direction the robot faces, or the order in which canceling moves occurred.

For example, `U` followed by `D` changes `y` by plus one and then minus one, for net zero. Those commands cancel even if many horizontal moves occur between them. Similarly, every `L` can be canceled by some `R` regardless of their positions in the string.

The task asks only where the robot ends, not whether it revisits the origin earlier or what route it draws.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Simulate each command

The exact implementation initializes `x = y = 0` and scans `moves` once. Python's `match` statement selects the update corresponding to the current character.

Only one branch executes for each command. Because the contract guarantees that every character is one of `U`, `D`, `L`, or `R`, no default branch is required.

After the scan, the condition `x == 0 and y == 0` checks both independent axes. Testing only one coordinate would be insufficient: `LRU` has horizontal displacement zero but ends one unit above the origin.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"moves": "UD"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Compare character counts:** Return whether `moves.count("U") == moves.count("D")` and `moves.count("L") == moves.count("R")`. It is correct but may scan the string four times; the coordinate simulation is one pass.
- **Use a frequency map:** Count all four commands, then compare opposites. This takes `O(N)` time but introduces a data structure when two counters suffice.
- **Store every visited coordinate:** This uses `O(N)` space and is necessary only for questions about intersections or revisits, not the final position.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the number of move characters.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
