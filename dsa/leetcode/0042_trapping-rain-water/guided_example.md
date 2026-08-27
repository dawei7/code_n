# Guided Example: Trapping Rain Water

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

The objective is to compute `6` from `{"height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Water above one position is controlled by two walls

Water cannot remain above bar `i` unless some bar at or to its left and some bar at or to its right contain it. Let the tallest height on the left side, including `i`, be $L_i$, and let the tallest height on the right side, also including `i`, be $R_i$. The water surface at that position can rise only to the shorter of those two boundaries:

$$
W_i = \min(L_i, R_i) - \texttt{height}[i].
$$

Including the current bar in both maxima guarantees $L_i$ and $R_i$ are each at least `height[i]`, so $W_i$ is never negative. A taller wall on only one side is insufficient: water spills over the shorter side, which is why the formula uses `min` rather than `max`.

Because every bar has width 1, a vertical depth of $W_i$ at one index contributes exactly $W_i$ unit squares of water. The total answer is the sum over all indices.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Precompute the left boundary at every index

The list `left` has length `n`. It starts filled with `height[0]`, and the forward recurrence is

$$
L_i = \max(L_{i-1}, \texttt{height}[i]).
$$

This recurrence is correct because the prefix ending at `i` consists of the preceding prefix plus the current bar. Its maximum must be either the old prefix maximum or the new height. After the forward assignments, `left[i]` equals the tallest bar among indices 0 through `i`.

For example, heights `[4, 2, 0, 3, 2, 5]` produce left maxima `[4, 4, 4, 4, 4, 5]`. A shorter bar never lowers the known boundary; a taller bar replaces it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The list `left` has length `n`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build right boundaries in the same loop

The list `right` begins filled with `height[-1]`. During forward loop counter `i`, the code updates position `n - i - 1`, thereby moving from right to left. Its recurrence is

$$
R_j = \max(R_{j+1}, \texttt{height}[j]).
$$

where `j = n - i - 1`. The position `j + 1` has already been computed, so this records the maximum height from `j` through the final index.

Combining both recurrences in one `for` loop is only a compact scheduling choice. The left update depends on the previously completed position to its left, while the right update depends on the previously completed position to its right. They write different arrays and do not interfere.

For the same example, right maxima are `[5, 5, 5, 5, 5, 5]` because the final height 5 dominates every suffix. The per-index depths are then `[0, 2, 4, 1, 2, 0]`, which sum to 9.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two pointers with running maxima:** Move inwar:** - **Two pointers with running maxima:** Move inward from both ends and process the side with the smaller boundary. It computes the same per-column depths in $O(n)$ time and genuinely $O(1)$ auxiliary space, but its correctness invariant is subtler than explicit boundary arrays.
- **Monotonic decreasing stack:** When a taller bar arrives, pop basin bottoms and calculate horizontally bounded layers. It runs in $O(n)$ time and uses $O(n)$ stack space, with more involved width and bounded-height calculations.
- **Split at a global maximum:** Scan toward the tallest bar from each side, maintaining the best wall seen. The global maximum guarantees closure for both directional scans and uses constant extra space.
- **Brute-force boundaries:** For each index, rescan left and right for maxima. It implements the formula directly but costs $O(n^2)$ time.
- **Strictly increasing or decreasing heights:** One side never supplies a higher closing wall, so every computed depth is zero.
- **Flat terrain:** Left and right maxima equal every bar height, producing zero water.
- **Repeated peaks:** Equal-height walls contain water normally; the use of `max` and `min` does not require a unique maximum.
- **Valleys of height zero:** Zero is a valid bar height and simply increases possible depth when bounded by taller bars.
- **Single bar:** Both arrays contain that height and the only contribution is zero.
- **Empty list outside the contract:** Accessing `height[0]` would fail. The documented constraint starts at one element, so the selected source intentionally relies on that precondition.
- **Input preservation:** The method reads `height` and creates separate maximum arrays; it does not modify the elevation map.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Creating each length-$n$ list takes $O(n)$ time. The combined precomputation loop performs $n - 1$ constant-time updates, and the zipped generator scans $n$ aligned elements for the sum. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
