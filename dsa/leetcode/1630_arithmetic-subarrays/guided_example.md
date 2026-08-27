# Guided Example: Arithmetic Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 6, 5, 9, 3, 7], "l": [0, 0, 2], "r": [2, 3, 5]}`
- **Required output:** `[true, false, true]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A sequence of numbers is called **arithmetic** if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence `s` is arithmetic if and only if $s[i+1] - s[i] = s[1] - s[0]$for all valid `i`.

The objective is to compute `[true, false, true]` from `{"nums": [4, 6, 5, 9, 3, 7], "l": [0, 0, 2], "r": [2, 3, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the minimum and maximum to determine the only possible spacing

For one query, let the inclusive subarray length be

$$
k=r-l+1.
$$

If its values can be rearranged into an arithmetic sequence, sorting that sequence would place its minimum value first and its maximum value last. A length-$k$ arithmetic sequence has $k-1$ equal gaps. Therefore its common difference is forced to be

$$
d=\frac{\textit{maximum}-\textit{minimum}}{k-1}.
$$

There is no need to try several possible differences. The two extremes and the number of elements leave exactly one candidate.

The helper `check(nums, l, r)` computes `n = r - l + 1` for this query. Here `n` is the query length, not necessarily the length of the original array.

It builds `s` as a set of the values in `nums[l:l+n]`. Since `l + n = r + 1`, this Python slice contains exactly indices $l$ through $r$. The helper separately obtains `a1` and `an` as the minimum and maximum of the same inclusive range.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 6, 5, 9, 3, 7], "l": [0, 0, 2], "r": [2, 3, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reject a fractional common difference

All input values are integers, so every member of any rearranged arithmetic sequence must remain an integer. `divmod(an - a1, n - 1)` returns both the integer quotient `d` and remainder `mod`.

If `mod != 0`, the distance between the extremes cannot be split evenly among the $n-1$ gaps. No rearrangement can repair this numerical impossibility, and the helper returns false through the leading condition `mod == 0`.

Using `divmod` avoids floating-point arithmetic. A division such as $2/3$ must be rejected, not approximated and rounded. Integer quotient and remainder express the divisibility test exactly, including when input values are negative, because `an - a1` is always non-negative.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | All input values are integers, so every member of any rearra... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Check that every required value is present

When the difference is integral, the only possible sorted sequence is

$$
a_1,\ a_1+d,\ a_1+2d,\ \ldots,\ a_1+(n-1)d=a_n.
$$

The generator tests

`(a1 + (i - 1) * d) in s for i in range(1, n)`.

Because `i` runs from 1 through $n-1$, `i-1` runs from 0 through $n-2$. Thus it checks the minimum and every expected interior value. It does not explicitly test the final maximum, because `an` was obtained from the subarray and is necessarily present in its set.

`all` returns true only if every generated membership test is true. It also short-circuits: as soon as one required value is absent, later expected values are not checked.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[true, false, true]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 6, 5, 9, 3, 7], "l": [0, 0, 2], "r": [2, 3, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[true, false, true]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort every queried subarray:** After sorting, :** - **Sort every queried subarray:** After sorting, compare adjacent differences. This is straightforward but costs $O(k_i\log k_i)$ per query instead of expected linear time.
- **Boolean placement array:** Map each value to its expected progression index and mark occupied slots. This avoids hashing but still needs $O(k_i)$ storage and careful range and duplicate checks.
- **Reuse one query slice:** Store `arr = nums[l:r+1]` once, then pass it to `set`, `min`, and `max`. It has the same asymptotic bounds with fewer slice copies than the exact source.
- **Length two:** Any two numbers form an arithmetic sequence. The computed gap has denominator one, the remainder is zero, and the membership test succeeds.
- **All values equal:** `d = 0`. Minimum equals maximum, and the repeated expected value is present, so the query correctly returns true.
- **Negative values:** Only differences from the minimum are used. `an - a1` is non-negative, and set membership works identically for negative integers.
- **Fractional required gap:** A nonzero remainder rejects the query before membership checks.
- **Duplicate with positive gap:** A duplicate consumes one of the $n$ positions and forces some distinct expected value to be absent; the set checks expose that absence.
- **The maximum is not generated by `range(1, n)`:** It need not be checked because `an` came directly from the subarray. The generator covers the other $n-1$ required values.
- **Inclusive right endpoint:** Python slicing excludes its stop, so the slice ends at `l + n = r + 1` to include index `r`.
- **Parallel query arrays:** `zip` is safe because the contract guarantees equal lengths. Without that guarantee, it would silently stop at the shorter input.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. For query $i$, let
- **Auxiliary Space Complexity:** $O(K)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
