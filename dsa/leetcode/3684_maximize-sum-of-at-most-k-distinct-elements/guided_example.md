# Guided Example: Maximize Sum of At Most K Distinct Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [84, 93, 100, 77, 90], "k": 3}`
- **Required output:** `[100, 93, 90]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **positive** integer array `nums` and an integer `k`.

The objective is to compute `[100, 93, 90]` from `{"nums": [84, 93, 100, 77, 90], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why positivity determines how many values to choose

Suppose fewer than $r$ distinct values have been selected. Because $r \le U$, another unused distinct value exists. It is positive, so adding it increases the total sum. The smaller selection cannot be optimal.

This argument would fail if zero or negative values were allowed: under an “at most” limit, adding such a value might not help. The problem's positive-integer guarantee is therefore essential, not incidental.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [84, 93, 100, 77, 90], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sorting places useful values at the end

The source calls

`nums.sort()`

which mutates `nums` into nondecreasing order. Equal values become adjacent, and the largest values occupy the highest indices.

It then scans indices from `n - 1` down through zero. This direction immediately encounters values in descending order, which serves both goals:

- the first distinct values encountered are the largest ones, so they maximize the sum; and
- appending them in encounter order automatically produces the required strictly descending result.

No separate reversal of `ans` is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source calls

`nums.sort()`

which mutates `nums` into n... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Skipping duplicate occurrences

At index `i`, the code checks:

`if i + 1 < n and nums[i] == nums[i + 1]:`

`    continue`

Because the scan moves right to left, index `i+1` has already been examined. If the two values are equal, a copy of this value was already encountered farther to the right, so the current occurrence must not be appended again.

The rightmost copy in each equal-value run is selected, and every remaining copy in that run is skipped. The identity of the occurrence does not matter because the output contains values, not original indices.

For example, after sorting `[84, 93, 100, 77, 93]`, the array is `[77, 84, 93, 93, 100]`. The reverse scan proceeds as follows:

- append $100$;
- append the rightmost $93$;
- skip the other $93$ because its right neighbor is equal;
- append $84$ and stop if $k=3$.

The result is `[100, 93, 84]`, already strictly descending.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[100, 93, 90]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [84, 93, 100, 77, 90], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[100, 93, 90]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Deduplicate with a set, then sort:** `sorted(s:** - **Deduplicate with a set, then sort:** `sorted(set(nums), reverse=true)[:k]` implements the manifest summary in expected $O(n + U \log U)$ time and $O(U)$ explicit space. It avoids sorting duplicate positions but creates a hash set.
- **Keep a size-$k$ min-heap:** After deduplication, retain only the largest $k$ values in $O(n + U \log k)$ expected time. This can help when $k \ll U$, but the final heap still must be sorted descending for the required output.
- **Repeatedly search for the next maximum:** Performing a fresh scan for every chosen value can cost $O(nk)$ time and needs additional logic to exclude duplicates.
- **All values distinct:** No duplicate check succeeds. The algorithm returns the last $k$ sorted values in reverse order.
- **All values equal:** The rightmost copy is appended and every earlier copy is skipped, so the result contains one value even when $k$ is larger.
- **`k > U`:** The scan exhausts the array before the countdown reaches zero and correctly returns all $U$ distinct positive values.
- **`k = 1`:** The first reverse-scan value is the array maximum, and the method stops immediately after appending it.
- **Duplicate boundary:** Comparing with `nums[i+1]` is safe only because of the `i + 1 < n` guard. At the rightmost index there is no already-scanned neighbor.
- **Input mutation:** Callers that need the original array order would have to pass a copy or use a nonmutating sorted expression. The exact method sorts `nums` in place.
- **Hypothetical nonpositive values:** Choosing all available slots would no longer be automatically optimal. The current reasoning is valid because the contract guarantees every element is positive.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums` and $U$ its number of distinct values.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
