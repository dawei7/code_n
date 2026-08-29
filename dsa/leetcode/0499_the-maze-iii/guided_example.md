# Guided Example: The Maze III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "ball": [0, 0], "hole": [2, 2]}`
- **Required output:** `"dr"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a ball in a `maze` with empty spaces (represented as `0`) and walls (represented as `1`). The ball can go through the empty spaces by rolling **up, down, left or right**, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction (must be different from last chosen direction). There is also a hole in this maze. The ball will drop into the hole if it rolls onto the hole.

The objective is to compute `"dr"` from `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "ball": [0, 0], "hole": [2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

This problem combines three details that an ordinary maze BFS does not handle:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "ball": [0, 0], "hole": [2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

1. one instruction rolls through multiple cells, so graph edges have different distances;
2. the ball falls into the hole immediately, even before reaching a wall;
3. equal-distance routes must be compared by their complete instruction strings.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The source models each cell where the ball can stop—or the hole where it disappears—as a graph node. It maintains the best known pair for each node:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"dr"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "ball": [0, 0], "hole": [2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"dr"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Priority-queue Dijkstra:** Order entries by `(distance, path)` and finalize the first optimal hole entry. This matches the editorial and manifest more directly and gives predictable logarithmic queue operations.
- **Precompute roll endpoints:** Directional sweeps can avoid rescanning corridors, but hole interception must still stop a roll early.
- **Plain BFS:** It is incorrect because roll edges have unequal traveled distances; few instructions do not necessarily mean short distance.
- **Hole before a wall:** The loop must stop as soon as the ball enters the hole, not at the corridor endpoint.
- **Equal distance:** Replace a stored path only when the new complete string is lexicographically smaller.
- **Blocked direction:** It creates a zero-distance self-edge with a longer path and cannot improve the current pair.
- **Unreachable hole:** Its path remains `null` and the method returns `"impossible"`.
- **Queue duplicates:** They may repeat work, but each pop reads the newest table values rather than stale values embedded in the entry.
- **Direction order:** Correctness does not rely on iteration order because tie-breaking is explicit.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(rows \cdot cols \cdot p \log(rows \cdot cols))$. Let $V = RC$ be the number of grid cells, $E <= 4V$ the implicit roll edges, $L = \max(R,C)$ the maximum cells scanned by one roll, and $p$ a bound on stored instruction-string length. A heap-based Dijkstra implementation would have the manifest's logarithmic priority-queue factor. This source has no heap.
- **Auxiliary Space Complexity:** $O(rows \cdot cols \cdot p)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
