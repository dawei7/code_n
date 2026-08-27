# Guided Example: Pour Water

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heights": [3, 3, 2, 2, 2, 2, 2], "volume": 4, "k": 3}`
- **Required output:** `[2, 2, 2, 3, 2, 2, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an elevation map represents as an integer array `heights` where $\text{heights}[i]$ representing the height of the terrain at index `i`. The width at each index is `1`. You are also given two integers `volume` and `k`. `volume` units of water will fall at index `k`.

The objective is to compute `[2, 2, 2, 3, 2, 2, 2]` from `{"heights": [3, 3, 2, 2, 2, 2, 2], "volume": 4, "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simulate droplets sequentially

Each unit of water changes one column level, which can change where the next unit settles. The exact solution processes `volume` droplets one at a time and mutates `heights` to represent terrain plus accumulated water.

For each droplet, it searches left first, then right, and finally settles at `k` if neither direction offers an eventual fall. This ordering exactly matches the problem’s preference rule.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heights": [3, 3, 2, 2, 2, 2, 2], "volume": 4, "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Search one direction across non-increasing levels

For direction `d`, where `-1` means left and `1` means right, both `i` and candidate `j` begin at `k`.

The scan may continue while the next index is in bounds and

`heights[i + d] <= heights[i]`.

A higher adjacent column is a ridge that water cannot cross. An equal or lower column can be traversed while checking whether movement eventually reaches a lower level.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For direction `d`, where `-1` means left and `1` means right... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Record only actual downward progress

Whenever the next level is strictly lower, the code sets `j = i + d`. This records a location where the droplet would genuinely fall.

The scan still moves across following equal-height cells, but `j` is not changed by equality. After first falling onto a flat low plateau, moving farther along that plateau does not create another eventual fall, so the recorded settle point remains where the strict decrease was reached.

If the scan later finds another strict decrease, `j` updates again because that farther position is at an even lower reachable level.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 2, 2, 3, 2, 2, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heights": [3, 3, 2, 2, 2, 2, 2], "volume": 4, "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 2, 2, 3, 2, 2, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Precompute fixed basins once:** This fails bec:** - **Precompute fixed basins once:** This fails because every droplet changes levels and therefore future basins.
- **- **Choose the globally lowest reachable column:**:** - **Choose the globally lowest reachable column:** The rule is directional and left-preferring, not a global minimum search.
- **- **Update candidate on equal height:** That would:** - **Update candidate on equal height:** That would move water across a flat plateau even though it does not eventually fall there. Update only on strict decreases.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(vn)$. Let `n` be the number of columns and `v` the volume. A directional scan can traverse `O(n)` columns, and at most two directions are scanned for each droplet. Total time is `O(vn)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
