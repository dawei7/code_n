# Guided Example: Rotating the Box

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"boxGrid": [["#", ".", "#"]]}`
- **Required output:** `[["."], ["#"], ["#"]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` matrix of characters `boxGrid` representing a side-view of a box. Each cell of the box is one of the following:

The objective is to compute `[["."], ["#"], ["#"]]` from `{"boxGrid": [["#", ".", "#"]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate rotation from gravity.** The method first constructs the box’s exact 90-degree clockwise orientation, including stones, obstacles, and empty cells. It then lets stones fall downward within each output column. Keeping these phases separate makes both coordinate mapping and obstacle behavior explicit.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"boxGrid": [["#", ".", "#"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

If the input has `m` rows and `n` columns, the rotated result has `n` rows and `m` columns. `ans = [[null] * m for _ in range(n)]` allocates that shape.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Map every input cell to its rotated coordinate.** Input cell `(i, j)` moves to output row `j` and output column `m - i - 1`. The assignment

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[["."], ["#"], ["#"]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"boxGrid": [["#", ".", "#"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[["."], ["#"], ["#"]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Apply gravity before rotating:** In the original orientation, post-rotation downward corresponds to moving stones right. This can work but requires careful equivalence reasoning.
- **Write directly into the final matrix:** Rotation and falling can be combined segment by segment, reducing phases but increasing index complexity.
- **No stones:** Rotation copies obstacles and empties, and gravity makes no changes.
- **No empty cells:** Every deque remains empty and all stones stay after rotation.
- **Obstacle-separated regions:** Clearing the deque prevents stones from crossing boundaries.
- **Several stones above empties:** Bottom-up processing packs them at the bottom with no gaps.
- **Single row input:** It becomes one output column, and stones fall to its bottom.
- **Single column input:** Rotation produces one output row, so there is no vertical space for additional falling.
- **Input preservation:** All changes occur in `ans`; `boxGrid` is only read.
- **Output placeholders:** Every `null` is overwritten during complete rotation before gravity begins.
- **Deque order:** `popleft` selects the lowest reachable empty, while appending a moved stone’s origin preserves ordering.
- **Guaranteed initial rest:** The algorithm does not rely critically on it; the gravity phase still settles any represented stones correctly after rotation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N = m * n` be the number of cells. Rotation visits all `N` cells, and the gravity scan visits all `N` cells. Each row index enters and leaves a deque at most a constant number of times, so total time is `O(N)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
