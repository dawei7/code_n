# Guided Example: Wiggle Sort

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 5, 2, 1, 6, 4]}`
- **Required output:** `[3, 5, 1, 6, 2, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, reorder it such that $\text{nums}[0] \le \text{nums}[1] \ge \text{nums}[2] \le \text{nums}[3]...$.

The objective is to compute `[3, 5, 1, 6, 2, 4]` from `{"nums": [3, 5, 2, 1, 6, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Repair one adjacent inequality at a time

The required pattern is

$$
\texttt{nums}[0]
\le \texttt{nums}[1]
\ge \texttt{nums}[2]
\le \texttt{nums}[3]
\ge \cdots.
$$

Odd indices are peaks: an odd-indexed value must be at least the value immediately before it. Even positive indices are valleys: an even-indexed value must be at most the value immediately before it.

The exact solution scans from left to right. At index `i`, it inspects only `nums[i - 1]` and `nums[i]`. If their required inequality is reversed, it swaps those two adjacent values. The central insight is that this local repair also preserves every inequality already established to the left, so no sorting or backward repair is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 5, 2, 1, 6, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: State the parity rule exactly

When `i` is odd, the pair occupies an even index followed by an odd index, so it must satisfy

$$
\texttt{nums}[i-1]\le\texttt{nums}[i].
$$

The source swaps precisely when `nums[i] < nums[i - 1]`.

When `i` is even, the pair occupies an odd index followed by an even index, so it must satisfy

$$
\texttt{nums}[i-1]\ge\texttt{nums}[i].
$$

The source swaps precisely when `nums[i] > nums[i - 1]`.

These two violations are joined by `or` in the condition. If the pair already satisfies the required non-strict inequality, it is left unchanged. Equal adjacent values are valid in either orientation because the pattern uses `<=` and `>=`, not strict comparisons.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When `i` is odd, the pair occupies an even index followed by... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why swapping fixes the current pair

For odd `i`, a swap occurs only when the left value is larger than the right value. Exchanging them puts the smaller value on the even-indexed left side and the larger value on the odd-indexed right side, establishing `nums[i - 1] <= nums[i]`.

For even `i`, a swap occurs only when the new right value is larger than the left value. Exchanging them places the larger value at the odd-indexed left position and the smaller value at the even-indexed right position, establishing `nums[i - 1] >= nums[i]`.

Thus one adjacent swap is always sufficient to repair the newly considered inequality.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 5, 1, 6, 2, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 5, 2, 1, 6, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 5, 1, 6, 2, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort then swap neighboring positions:** Sortin:** - **Sort then swap neighboring positions:** Sorting first and exchanging selected adjacent values can create the wiggle pattern, but costs $O(n\log n)$ time and is unnecessary for non-strict inequalities.
- **Build a separate result:** Selecting alternating low and high values into another list is possible but uses $O(n)$ extra space and often still requires sorting.
- **Check only odd peaks:** Ensuring each odd index dominates both neighbors is equivalent, but the one-pass adjacent formulation repairs the right relationship as it arrives and proves preservation locally.
- **Length one:** The loop is empty, and the one-element array vacuously satisfies every adjacent inequality.
- **Length two:** One comparison and at most one swap establish `nums[0] <= nums[1]`.
- **All values equal:** Every non-strict inequality holds, so no swaps occur and the array is valid.
- **Already wiggled input:** Every violation test is false; the method preserves the existing order.
- **Strict wiggle variant:** This solution targets `<=` and `>=`. A requirement for strict `<` and `>` with duplicates is a different problem and may need median partitioning; the local equality-friendly proof would not suffice.
- **Negative values outside the stated range:** The logic uses only comparisons, so it would still work unchanged even though legal values are non-negative.
- **Input mutation:** Swapping changes the caller's list. That is required by the function contract; callers needing the original order must copy it before calling.
- **Existence guarantee:** For this non-strict version, the greedy proof itself constructs a valid arrangement for any array. The stated guarantee is therefore consistent but not additionally needed by the implementation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The loop visits each index from 1 through $n-1$ once. Each visit performs constant-time parity checks, comparisons, and at most one swap, giving $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
