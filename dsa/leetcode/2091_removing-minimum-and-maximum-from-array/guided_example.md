# Guided Example: Removing Minimum and Maximum From Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 10, 7, 5, 4, 1, 8, 6]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array of **distinct** integers `nums`.

The objective is to compute `5` from `{"nums": [2, 10, 7, 5, 4, 1, 8, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Find the two important positions in one scan

Only the positions of the minimum and maximum matter. Their actual values are used to locate them, but the deletion count depends on how far their indices are from the two ends.

The variables `mi` and `mx` start at index 0. While enumerating `nums`:

- if `num < nums[mi]`, `mi` becomes the current index;
- if `num > nums[mx]`, `mx` becomes the current index.

The values are distinct, so for arrays longer than one there is one unique minimum index and one unique maximum index. For a one-element array, index 0 is both.

The two comparisons are independent `if` statements. That is appropriate because each current value is considered separately against the known extremes, and initialization handles the first element.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 10, 7, 5, 4, 1, 8, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Normalize the positions into left-to-right order

After the scan, the code swaps the indices when `mi > mx`. From that point onward, `mi` is the leftmost of the two extreme-element positions and `mx` is the rightmost.

The variable names still originated as minimum and maximum indices, but after a swap their left/right ordering is what the formulas use. Whether the smaller value lies left or right is irrelevant; both elements must be deleted.

Normalizing once avoids writing symmetric formulas for both possible arrangements.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After the scan, the code swaps the indices when `mi > mx`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: There are only three useful deletion strategies

Every deletion removes from the front or the back. With left important index `mi` and right important index `mx`, an optimal plan has one of three forms.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 10, 7, 5, 4, 1, 8, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort value-index pairs:** Sorting can locate t:** - **Sort value-index pairs:** Sorting can locate the minimum and maximum but costs $O(n\log n)$ and adds storage or mutation. One scan finds both positions optimally.
- **Simulate deletions:** Trying front and back operations step by step obscures that only prefix and suffix lengths matter. The three formulas evaluate every meaningful plan directly.
- **Four directional combinations:** After ordering the indices, the supposed combination that takes the right position from the front and left position from the back is dominated and unnecessary.
- **Minimum lies after maximum:** The swap normalizes the positions, so the same formulas apply without caring which value is on which side.
- **One-element array:** `mi == mx == 0`. Front-only and back-only candidates both equal one, so the answer is correctly one.
- **Two-element array:** Both elements are the extremes, and two deletions are required; the formulas return two.
- **Extremes at opposite endpoints:** The split formula gives one deletion from each side, totaling two.
- **Both extremes near the front:** The front-only candidate usually wins because reaching the farther one removes both.
- **Both extremes near the back:** The back-only candidate symmetrically wins.
- **Distinctness guarantee:** It makes the minimum and maximum positions unique. The one-element case legitimately uses the same position for both roles.
- **No physical mutation:** Returning a count does not require constructing the remaining array or changing the input.
- **Off-by-one boundaries:** Deleting through index `mx` from the front costs `mx + 1`, while deleting from index `mi` through the back costs `n - mi`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
