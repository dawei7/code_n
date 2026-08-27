# Guided Example: Left and Right Sum Differences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [10, 4, 8, 3]}`
- **Required output:** `[15, 1, 11, 22]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` of size `n`.

The objective is to compute `[15, 1, 11, 22]` from `{"nums": [10, 4, 8, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain both sides instead of building two arrays

For each index $i$, the required values are the sum strictly before $i$ and the sum strictly after $i$. Recomputing both sums independently at every index would repeat work and cost $O(n^2)$ time.

The solution carries two running totals:

- `l` is the sum of elements already passed, so it represents the current left sum;
- `r` is the sum of elements not yet passed.

Initially no element lies to the left, so `l = 0`. The initial `r = sum(nums)` contains the entire array, including the first current element. The order of updates inside the loop removes that current element before using `r`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [10, 4, 8, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the update order matters

For each current value `x`, the statements occur in this exact order:

1. `r -= x`;
2. append `abs(l - r)`;
3. `l += x`.

Before step one, `r` includes the current value and everything to its right. Subtracting `x` makes it equal to the sum strictly to the right, which is `rightSum[i]`.

At that same moment, `l` contains only earlier values because the current value has not yet been added. It is exactly `leftSum[i]`. The appended absolute difference is therefore correct for the current index.

Only after recording the answer does the code add `x` to `l`, preparing it to be part of the left side at the next index.

If the last two updates were reversed, the current element would incorrectly appear on the left. If the subtraction from `r` occurred after appending, it would incorrectly appear on the right. The compact algorithm depends on this sequencing.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each current value `x`, the statements occur in this exa... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A loop invariant

At the beginning of the iteration for index $i$:

$$
\texttt{l}=\sum_{k=0}^{i-1}\texttt{nums[k]}
$$

and

$$
\texttt{r}=\sum_{k=i}^{n-1}\texttt{nums[k]}.
$$

Subtracting `nums[i]` changes `r` into the suffix strictly after $i$. The algorithm appends the exact absolute difference, then adding `nums[i]` changes `l` into the prefix through $i$. Those are precisely the invariant values required at the beginning of iteration $i+1$.

The invariant is true initially because the empty prefix sums to zero and `r` is the total array sum. By induction, every appended result is correct.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[15, 1, 11, 22]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [10, 4, 8, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[15, 1, 11, 22]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit left and right arrays:** Two prefix/s:** - **Explicit left and right arrays:** Two prefix/suffix passes are correct but allocate two additional $O(n)$ arrays when two running totals suffice.
- **Recompute sums for each index:** Slicing and summing both sides at every position costs $O(n^2)$ time.
- **One prefix array plus total sum:** This also answers each position in $O(1)$ after preprocessing, but still stores $O(n)$ auxiliary prefix values.
- **Single element:** Subtracting it makes `r=0` while `l=0`, so the sole answer is zero.
- **First position:** The initialized left sum is the required empty-side zero.
- **Last position:** Removing the current value from `r` leaves the required empty-side zero.
- **Equal side sums:** Absolute difference is zero, which the code appends normally.
- **Large total:** The maximum sum can exceed a 32-bit integer under broader constraints; Python integers expand automatically.
- **Update order:** Remove the current value from the right before measuring, and add it to the left only afterward.
- **Input preservation:** All updates affect scalar totals and the new answer list, never `nums`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Computing `sum(nums)` takes $O(n)$ time. The loop visits each element once and does constant work, adding another $O(n)$. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
