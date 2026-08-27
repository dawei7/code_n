# Guided Example: Wiggle Sort II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 5, 1, 1, 6, 4]}`
- **Required output:** `[1, 6, 1, 5, 1, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, reorder it such that $\text{nums}[0] < \text{nums}[1] > \text{nums}[2] < \text{nums}[3]...$.

The objective is to compute `[1, 6, 1, 5, 1, 4]` from `{"nums": [1, 5, 1, 1, 6, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the inequalities into alternating roles.

The required pattern is

$$
\text{nums}[0] < \text{nums}[1] > \text{nums}[2] < \text{nums}[3] > \cdots.
$$

Even indices are valleys and odd indices are peaks. It is therefore natural to reserve the smaller half of the values for even positions and the larger half for odd positions. Sorting first makes those two groups explicit.

The exact optimal source creates `arr = sorted(nums)`. This is a new ascending copy; all later reads come from `arr`, while assignments overwrite the original `nums`. Keeping a separate copy prevents early writes from destroying values that have not yet been placed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 5, 1, 1, 6, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Split the sorted values into lower and upper halves.

Let $n$ be the array length. The index

$$
i = \left\lfloor\frac{n-1}{2}\right\rfloor
$$

is the final index of the lower half, and `j = n - 1` is the final index of the upper half.

For an even length $n=2q$, the lower and upper halves each contain $q$ values:

$$
\text{lower} = \text{arr}[0:q],
\qquad
\text{upper} = \text{arr}[q:2q].
$$

For an odd length $n=2q+1$, there are $q+1$ even positions but only $q$ odd positions. Accordingly, the lower half contains $q+1$ values and the upper half contains $q$:

$$
\text{lower} = \text{arr}[0:q+1],
\qquad
\text{upper} = \text{arr}[q+1:2q+1].
$$

This size difference is why the formula uses `(n - 1) >> 1`, which is integer division of $n-1$ by two. The extra value for an odd-length array belongs in a valley position, including the unpaired final even index.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let $n$ be the array length.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Read both halves backward.

The loop visits destination index `k` from left to right. At an even `k`, it writes `arr[i]` and decrements `i`; at an odd `k`, it writes `arr[j]` and decrements `j`. The resulting arrangement has the form

$$
L_0, U_0, L_1, U_1, L_2, U_2, \ldots,
$$

where $L_0,L_1,\ldots$ are the lower-half values in descending order and $U_0,U_1,\ldots$ are the upper-half values in descending order.

Using descending order inside each half is essential when duplicates exist. If both halves were read from left to right, equal values near the split could land next to each other. For the sorted array `[1,2,2,2,3,3]`, ascending interleaving would begin `[1,2,2,3,...]`, which already fails at `2 > 2`. Reversing the halves separates the equal values: lower descending is `[2,2,1]`, upper descending is `[3,3,2]`, and their interleaving is `[2,3,2,3,1,2]`.

The reversal places the largest lower value first, but it also pairs it with the largest upper value. As the lower choices decrease, the upper choices decrease in step. Duplicate values around the median are pushed apart instead of being aligned across an early peak boundary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 6, 1, 5, 1, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 5, 1, 1, 6, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 6, 1, 5, 1, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Quickselect plus virtual indexing:** Select th:** - **Quickselect plus virtual indexing:** Select the median in expected $O(n)$ time, then three-way partition values through the index mapping that visits odd positions before even positions. This can meet the expected $O(n)$-time and $O(1)$-space follow-up, but it is considerably more intricate and is not the exact source shown here.
- **- **Sort and interleave halves in ascending order::** - **Sort and interleave halves in ascending order:** This looks similar but fails with duplicates around the median, because equal boundary values can become adjacent. Reversing both halves is the detail that spreads duplicates safely.
- **- **Sort without a separate copy:** Rearranging `n:** - **Sort without a separate copy:** Rearranging `nums` while also using it as the unread sorted source risks overwriting values before they are consumed. The copied `arr` cleanly separates reads from writes.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of elements. Creating `arr = sorted(nums)` takes $O(n\log n)$ time. The placement loop visits every destination once and takes $O(n)$ time, so the exact implementation's total time complexity is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
