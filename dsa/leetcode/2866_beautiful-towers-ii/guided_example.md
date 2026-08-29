# Guided Example: Beautiful Towers II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"maxHeights": [5, 3, 4, 1, 1]}`
- **Required output:** `13`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `maxHeights` of `n` integers.

The objective is to compute `13` from `{"maxHeights": [5, 3, 4, 1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

**What is fixed once a peak is chosen.** If index `i` is the peak, its best height is `maxHeights[i]`. Moving left, every tower must be no higher than both its own cap and the tower to its right. Moving right, every tower must be no higher than both its cap and the tower to its left. Thus the best mountain for a fixed peak can be found with running minima. Repeating that scan for every peak would cost $O(n^2)$, which is too slow for $n=10^5$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"maxHeights": [5, 3, 4, 1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution accelerates the repeated running-minimum sums. Array `f` stores the maximum total height of positions `0..i` when position `i` is the rightmost peak. Array `g` stores the symmetric maximum total over `i..n-1` when position `i` is the leftmost peak. Once these are known, peak `i` has total

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

where the subtraction removes the peak counted by both sides.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `13` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"maxHeights": [5, 3, 4, 1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `13` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every peak directly:** Running minima outward from every index is easy to derive and works for Beautiful Towers I, but costs $O(n^2)$ and is too slow here.
- **Single-pass contribution variants:** It is possible to combine stack events more compactly, but separate `f` and `g` arrays make the two constrained sides easier to verify.
- **Equal caps:** Non-strict mountain slopes allow plateaus. The left and right stacks deliberately use different equality popping rules so equal boundaries are owned consistently.
- **Peak counted twice:** Always subtract `maxHeights[i]` when combining `f[i]` and `g[i]`.
- **Peak at an endpoint:** One side consists only of that peak; sentinel boundaries make the same formulas work.
- **Single tower:** Both side sums equal its cap, and subtracting one copy returns that cap.
- **Large values:** Use a wide sum type; the answer greatly exceeds 32-bit range even though indices do not.
- **Input preservation:** The algorithm reads `maxHeights` without changing it and stores all derived state separately.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each of the two boundary passes pushes and pops every index at most once, taking $O(n)$ time. Computing `f`, computing `g`, and taking the maximum each take another $O(n)$. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
