# Guided Example: All Divisions With the Highest Score of a Binary Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 0, 1, 0]}`
- **Required output:** `[2, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** binary array `nums` of length `n`. `nums` can be divided at index `i` (where $0 \le i \le n)$ into two arrays (possibly empty) $\text{nums}_{left}$ and $\text{nums}_{right}$:

The objective is to compute `[2, 4]` from `{"nums": [0, 0, 1, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Initialize the division before the array

At index zero, the left part is empty, so `l0 = 0`. The right part is the entire binary array, and `sum(nums)` counts its ones, so `r1 = sum(nums)`.

The score is `l0 + r1 = r1`. The source initializes `mx = r1` and `ans = [0]`, meaning division zero is the best and only division examined so far.

Including this initial state before entering the loop is essential because index zero can be the unique answer, as in an all-ones array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 0, 1, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Move one element across each boundary

The loop `for i, x in enumerate(nums, 1)` processes values in original order while making `i` range from one through $n$. After processing `x = nums[i-1]`, the maintained counts describe division index `i`.

When `x == 0`, moving it to the left increases the number of left zeros by one. When `x == 1`, it contributes no left zero. The expression `x ^ 1` flips a binary bit, producing one for zero and zero for one. Thus `l0 += x ^ 1` performs exactly the correct update.

The element leaves the right side. If it is one, right ones decrease by one; if it is zero, they stay unchanged. Because `x` itself is zero or one, `r1 -= x` handles both cases.

The new score is `t = l0 + r1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop `for i, x in enumerate(nums, 1)` processes values i... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep every index tied for the maximum

If `t == mx`, the current division ties the best score and `ans.append(i)` preserves it alongside earlier winners.

If `t > mx`, every previously stored division has a smaller score. The code sets `mx = t` and replaces the result with `ans = [i]`.

If `t < mx`, neither branch runs and the result remains unchanged.

This three-way behavior ensures that, after each iteration, `mx` is the greatest score among divisions zero through `i` and `ans` contains exactly all indexes in that processed prefix with score `mx`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 0, 1, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Prefix and suffix arrays:** Precompute left-ze:** - **Prefix and suffix arrays:** Precompute left-zero and right-one counts for every boundary, then compare scores. This is linear time but uses $O(n)$ extra arrays unnecessarily.
- **Recount each division:** Counting both sides independently at all $n+1$ indexes takes $O(n^2)$ time.
- **Track score alone:** Start with total ones, add one for each zero, and subtract one for each one. This is equivalent and uses slightly fewer named counts, but the exact source keeps `l0` and `r1`.
- **All zeros:** Every move raises the score, so only division $n$ is returned.
- **All ones:** Every move lowers the score, so only division zero is returned.
- **One zero:** Scores are zero at division zero and one at division one, so the result is `[1]`.
- **One one:** Scores are one at division zero and zero at division one, so the result is `[0]`.
- **Ties separated by lower scores:** The equality branch appends a later index even if intermediate divisions were worse.
- **New maximum:** Replacing `ans` discards all indexes tied only for the old, now inferior maximum.
- **Division zero:** It is initialized explicitly because the loop begins with division one.
- **Division n:** `enumerate(..., 1)` reaches `i = n` after the last element moves left.
- **Binary guarantee:** `x ^ 1` behaves as a zero indicator only because `x` is guaranteed to be zero or one.
- **Any output order:** The source returns ascending indexes because it scans left to right, which is accepted even though sorting is not required.
- **Output-size bound:** In some alternating arrays, many divisions may tie, so result storage can genuinely be linear.
- **Input preservation:** Counts are updated separately; `nums` retains all original bits.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. `sum(nums)` performs one $O(n)$ scan. The loop performs a second $O(n)$ scan with constant work per element. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
