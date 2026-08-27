# Guided Example: Minimum Sum of Mountain Triplets I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [8, 6, 1, 5, 3]}`
- **Required output:** `9`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `nums` of integers.

The objective is to compute `9` from `{"nums": [8, 6, 1, 5, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Precompute the minimum on every suffix

The array `right` has length $n+1$. Its meaning is:

$$
\texttt{right}[i] = \min(\texttt{nums}[i],\texttt{nums}[i+1],\ldots,\texttt{nums}[n-1]).
$$

The extra entry `right[n]` is initialized to positive infinity. It represents the empty suffix after the array. The reverse loop computes each real entry from the value at the current index and the already-known minimum of the suffix to its right:

`right[i] = min(right[i + 1], nums[i])`.

When index $j$ later acts as the middle, the solution reads `right[j + 1]`, not `right[j]`. That offset is crucial. It means the right candidate comes strictly after $j$, so the middle element can never accidentally be reused as the right member of the triplet.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [8, 6, 1, 5, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain the left minimum during the forward scan

The variable `left` starts at positive infinity. Immediately before processing index $j$, it equals the minimum value among indices $0$ through $j-1$. The update `left = min(left, nums[j])` happens only after the current index has been tested. This order ensures that `left` describes a strictly earlier position rather than a prefix that includes the middle itself.

Therefore, while examining `x = nums[j]`, the three relevant values are:

- `left`: the smallest value at any index before $j$;
- `x`: the proposed mountain peak;
- `right[j + 1]`: the smallest value at any index after $j$.

The peak is usable exactly when `left < x` and `right[j + 1] < x`. The comparisons are strict because the definition requires both sides to be smaller than the peak; equality does not form a mountain.

If both tests succeed, `left + x + right[j + 1]` is the minimum mountain-triplet sum having $j$ as its middle index. The solution compares this candidate with `ans` and keeps the smaller one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The variable `left` starts at positive infinity.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why taking the side minima cannot miss a valid answer

Suppose some valid triplet uses $j$ as its middle and has outside values `nums[i]` and `nums[k]`. Because `left` is the minimum of every value before $j$,

$$
\texttt{left} \le \texttt{nums}[i].
$$

The known triplet tells us `nums[i] < nums[j]`, so `left` must also be strictly smaller than `nums[j]`. Replacing `nums[i]` with the position that supplied `left` preserves validity and never increases the sum. The same reasoning applies to `right[j + 1]` on the other side. Thus, if any valid triplet exists for middle $j$, the two stored minima produce a valid triplet whose sum is no larger than that of any other triplet with the same middle.

The forward loop examines every index as a possible middle. Consequently, it evaluates the best triplet for every middle that can support one. Taking the smallest of those candidates gives the global minimum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `9` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [8, 6, 1, 5, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `9` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all triples:** Three nested loops ma:** - **Enumerate all triples:** Three nested loops match the definition directly and take $O(n^3)$ time. This can work for very small inputs, but it repeatedly rechecks the same left and right values.
- **Fix the middle and scan both sides:** For every $j$, scan the prefix for a valid minimum and the suffix for another. This improves the structure of the reasoning but still takes $O(n^2)$ time because the side scans are repeated.
- **Prefix and suffix arrays on both sides:** Storing a complete prefix-minimum array as well as `right` also gives $O(n)$ time, but it uses another $O(n)$ array. The running `left` variable supplies the needed prefix information with constant extra storage.
- **Equal values around the peak:** Conditions such as `left <= x` would be wrong. A side equal to the middle violates the strict mountain inequalities, so the implementation correctly uses `<` twice.
- **Middle at an endpoint:** Index $0$ has no earlier element and index $n-1$ has no later element. The infinity sentinels make their validity tests fail naturally without special branches.
- **Duplicate minima:** The algorithm stores values rather than indices, but this is safe. Any occurrence contributing to `left` is strictly before the middle, and any occurrence contributing to `right[j + 1]` is strictly after it.
- **No valid triplet:** Monotone arrays and arrays without a value having smaller elements on both sides leave `ans` unchanged, producing the required `-1`.
- **Negative infinity is unnecessary:** Array values are finite and the task minimizes sums, so positive infinity is the correct marker for “no value seen” and “no answer found.”
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
