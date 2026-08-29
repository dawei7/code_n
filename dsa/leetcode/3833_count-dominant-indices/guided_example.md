# Guided Example: Count Dominant Indices

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 4, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`.

The objective is to compute `2` from `{"nums": [5, 4, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A right-to-left scan makes the needed suffix available

For index `i`, dominance depends on every element to its right. Recomputing that suffix sum from scratch at each index would repeat work.

The source instead scans from right to left while maintaining `suf`. Before checking index `i`, the invariant is

$$
\texttt{suf}
=
\sum_{j=i+1}^{N-1}\texttt{nums}[j].
$$

The number of terms in this suffix is

$$
N-i-1.
$$

Therefore its average is exactly

$$
\frac{\texttt{suf}}{N-i-1}.
$$

The source compares `nums[i]` with that value and increments `ans` only for a strict greater-than result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 4, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize with the rightmost suffix

The scan begins at `i = N - 2`, the second-to-last index. Its right suffix contains only `nums[N - 1]`, so `suf = nums[-1]` is the correct initial sum.

After checking an index, the source performs

`suf += nums[i]`.

When the loop moves from `i` to `i - 1`, the needed suffix has gained exactly `nums[i]`. The update restores the invariant for the next iteration.

This ordering is essential. Adding `nums[i]` before the comparison would incorrectly include the candidate itself in its right-side average.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The final element is excluded naturally

The rightmost index has no elements after it, so its suffix average is undefined and the statement declares it non-dominant. The loop begins at `N - 2` and never checks `N - 1`.

For a one-element array, `range(n - 2, -1, -1)` is empty. The answer stays zero, correctly excluding the only, rightmost element.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 4, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Exact cross multiplication:** Test `nums[i] * (n - i - 1) > suf`. It preserves strictness and avoids floating-point division while retaining $O(N)$ time.
- **Suffix-sum array:** Precompute every suffix sum and query each average in constant time. This is also $O(N)$ time but uses unnecessary $O(N)$ space.
- **Recompute every average:** Summing `nums[i + 1:]` for every index costs $O(N^2)$ time and creates repeated slice work in Python.
- **One element:** It is the rightmost element and is explicitly not dominant, so the answer is zero.
- **Two elements:** The first is dominant exactly when it is greater than the second.
- **Equality with the suffix average:** The requirement is strict, so equality does not increment the count.
- **Fractional average:** The source compares directly against the fraction; it does not round it up or down.
- **All equal values:** Every eligible value equals its suffix average, so none is dominant.
- **Strictly decreasing values:** Every value except the rightmost exceeds every value to its right and therefore exceeds their average.
- **Positive suffix count:** Every checked index has at least one right-side value, so the division denominator is never zero.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{nums}\rvert$. The loop visits exactly $N-1$ eligible indices and performs constant arithmetic at each one. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
