# Guided Example: Robot Collisions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"positions": [5, 4, 3, 2, 1], "healths": [2, 17, 9, 15, 10], "directions": "RRRRR"}`
- **Required output:** `[2, 17, 9, 15, 10]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` **1-indexed** robots, each having a position on a line, health, and movement direction.

The objective is to compute `[2, 17, 9, 15, 10]` from `{"positions": [5, 4, 3, 2, 1], "healths": [2, 17, 9, 15, 10], "directions": "RRRRR"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Process robots in physical left-to-right order

Input order is unrelated to position, but collisions depend on spatial order. The code sorts original indices by `positions[i]` and processes robots from leftmost to rightmost.

Keeping indices rather than rearranging robot records preserves access to directions and mutable health values at their original indices. It also makes final input-order output easy.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"positions": [5, 4, 3, 2, 1], "healths": [2, 17, 9, 15, 10], "directions": "RRRRR"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Which direction pattern can collide

Two robots with equal speed can approach only when the left robot moves right and the right robot moves left. Same-direction robots maintain their separation. A left-moving robot followed spatially by a right-moving robot moves away from it.

Therefore, when scanning left to right, only previously seen unmatched right movers can collide with a current left mover.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Two robots with equal speed can approach only when the left ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Stack stores pending right movers

Whenever direction is `R`, append its index to `stk`. These robots are ordered by position, and the top is the nearest pending right mover to the current scan position.

A current left mover must collide with that nearest right mover before it could reach any earlier one. This last-in-first-out collision order is exactly what a stack represents.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 17, 9, 15, 10]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"positions": [5, 4, 3, 2, 1], "healths": [2, 17, 9, 15, 10], "directions": "RRRRR"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 17, 9, 15, 10]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate positions over time:** Inefficient an:** - **Simulate positions over time:** Inefficient and difficult because collision times may be fractional.
- **Queue of right movers:** Incorrect because the nearest, most recently seen right mover collides first.
- **All move right:** Every index stays on the stack and all healths survive unchanged.
- **All move left:** The stack stays empty and all survive unchanged.
- **Equal-health collision:** Both become zero and disappear.
- **One strong left mover:** May pop several weaker right movers, losing one health for each.
- **Right mover survives:** It stays on the stack with health decreased by one.
- **Unsorted input:** Sorted indices establish correct physical order without losing original identity.
- **No survivors:** Final filtering returns an empty list.
- **Input mutation:** The original `healths` list contains zeros and reduced survivor healths after execution.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Sorting the $n$ original indices by position costs $O(n\log n)$. After sorting, every index is pushed at most once and popped at most once, and every collision destroys at least one robot. The simulation is $O(n)$, so total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
