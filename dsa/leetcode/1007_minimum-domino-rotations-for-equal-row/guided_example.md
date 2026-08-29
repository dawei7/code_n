# Guided Example: Minimum Domino Rotations For Equal Row

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tops": [2, 1, 2, 4, 2, 2], "bottoms": [5, 2, 6, 2, 3, 2]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In a row of dominoes, $\text{tops}[i]$ and $\text{bottoms}[i]$ represent the top and bottom halves of the $i^{\text{th}}$ domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

The objective is to compute `2` from `{"tops": [2, 1, 2, 4, 2, 2], "bottoms": [5, 2, 6, 2, 3, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only two target values can possibly work

Suppose one row can be made uniform with value `x`. At domino zero, the final chosen row must show `x`. Rotation can expose only `tops[0]` or `bottoms[0]` at that position.

Therefore, `x` must be one of those two values. No other domino number needs to be tried as a global target.

The solution evaluates both candidates with helper `f` and takes the smaller valid rotation count.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tops": [2, 1, 2, 4, 2, 2], "bottoms": [5, 2, 6, 2, 3, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A candidate must appear on every domino

For target `x`, each domino pair `(a, b)` must contain `x` on at least one side. If

`x not in (a, b)`,

neither leaving that domino nor rotating it can place `x` into either uniform row at this position. The candidate is impossible, so `f` returns `inf` immediately.

This condition checks feasibility for making either the top row or the bottom row uniform at the same time. If every domino contains `x` somewhere, at least one side can expose it after an appropriate rotation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count how many positions already match each row

For every feasible domino:

- `cnt1 += a == x` counts positions whose top already equals `x`;
- `cnt2 += b == x` counts positions whose bottom already equals `x`.

In Python, a Boolean used in arithmetic contributes one for true and zero for false.

To make the entire top row equal `x`, every position whose top is not `x` must be rotated. Since feasibility proved the bottom contains `x` at those positions, each such rotation works. The required count is:

`len(tops) - cnt1`.

Similarly, making the bottom row uniform requires:

`len(tops) - cnt2`

rotations.

The cheaper orientation is

`len(tops) - max(cnt1, cnt2)`,

which is algebraically the minimum of those two rotation counts.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tops": [2, 1, 2, 4, 2, 2], "bottoms": [5, 2, 6, 2, 3, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try all six domino values:** Check feasibility and rotations for values one through six. This remains linear because six is fixed, but the first-domino observation reduces unnecessary scans.
- **Count frequencies separately without pair feasibility:** Large top or bottom counts are insufficient if some domino lacks the target entirely. Each pair must be checked.
- **Physically simulate rotations:** Once a target row is chosen, simulation can construct it, but the problem asks only for the count and every required position is directly identifiable.
- **Both first faces equal:** The same candidate is checked twice; the result remains correct.
- **Target appears on both sides of a domino:** That position contributes to both already-correct counts and needs no rotation.
- **Candidate missing from one pair:** It is impossible for both row orientations, so the helper returns immediately.
- **Top already uniform:** For its target, `cnt1 = N` and the result is zero.
- **Bottom already uniform:** Symmetrically, `cnt2 = N` gives zero.
- **Both candidates feasible:** The algorithm compares their best top/bottom rotation counts and returns the smaller.
- **Unique minimum not required:** Different rotation plans may use the same minimum number; only the numeric count is returned.
- **Input preservation:** The paired arrays are read-only and retain their original orientation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the number of dominoes.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
