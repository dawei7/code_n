# Guided Example: Number of Spaces Cleaning Robot Cleaned

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"room": [[0, 0, 0], [1, 1, 0], [0, 0, 0]]}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A room is represented by a **0-indexed** 2D binary matrix `room` where a `0` represents an **empty** space and a `1` represents a space with an **object**. The top left corner of the room will be empty in all test cases.

The objective is to compute `7` from `{"room": [[0, 0, 0], [1, 1, 0], [0, 0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The robot's full state includes direction

Knowing only the robot's cell is insufficient. From the same cell, facing right and facing down lead to different next actions.

The source represents a state as `(i,j,k)`, where `i,j` is the position and `k` is one of four direction indices. `dirs = (0,1,0,-1,0)` encodes right, down, left, and up as adjacent coordinate pairs.

A repeated full state means every future action will repeat forever, so simulation can stop.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"room": [[0, 0, 0], [1, 1, 0], [0, 0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Mark directional states to detect the eventual cycle

At the beginning of `dfs`, the source checks whether `(i,j,k)` is already in `vis`. If so, it returns without further recursion.

The room and direction choices are deterministic. Once the same position and facing direction recur, the robot will follow the identical infinite suffix of movements and turns. No new cell can be cleaned after that point.

There are at most four states per cell, so indefinite physical running becomes a finite state traversal.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At the beginning of `dfs`, the source checks whether `(i,j,k... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count a cell only on its first visit

The source adds `room[i][j] == 0` to `ans`. Python treats the Boolean as one for an uncleaned empty cell and zero otherwise.

It then writes `room[i][j] = -1`. Later visits to that cell do not increment the answer because negative one differs from zero.

Objects remain value one and are never entered. Thus the matrix itself doubles as the cleaned-cell marker.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"room": [[0, 0, 0], [1, 1, 0], [0, 0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative simulation:** Use a loop until a sta:** - **Iterative simulation:** Use a loop until a state repeats, avoiding recursion-limit failure with the same $O(MN)$ bounds.
- **Separate cleaned set:** Preserves `room` but adds another $O(MN)$ structure.
- **Visited cell only:** Insufficient because direction changes future behavior.
- **Starting cell:** Always empty and is counted immediately.
- **Previously cleaned cell:** Remains traversable but contributes zero on revisit.
- **Object cell:** Never entered and remains value one.
- **Boundary:** Treated exactly like a blocked forward cell and causes a clockwise turn.
- **Four consecutive blocks:** Return to the same directional state and terminate.
- **Open rectangular room:** The robot may cycle around a boundary without cleaning every interior cell.
- **Repeated full state:** Proves the future is periodic.
- **Input mutation:** Cleaned spaces are changed from zero to negative one.
- **Recursion risk:** A long state path can raise `RecursionError` under default Python limits.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(MN)$. Let $M$ and $N$ be room dimensions. At most $4MN$ position-direction states are entered, and each performs constant work. Time is $O(MN)$.
- **Auxiliary Space Complexity:** $O(MN)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
