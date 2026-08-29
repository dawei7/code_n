# Guided Example: Find All Duplicates in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 3, 2, 7, 8, 2, 3, 1]}`
- **Required output:** `[2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears **at most** **twice**, return *an array of all the integers that appears **twice***.

The objective is to compute `[2, 3]` from `{"nums": [4, 3, 2, 7, 8, 2, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use each value's natural destination index

The length is $n$, and every value lies in `[1,n]`. Therefore value `v` has a valid canonical array position `v - 1`. If every distinct value is moved to its canonical position, a second occurrence cannot occupy that same position. It must remain somewhere whose index does not match its value, revealing the duplicate.

The solution performs an in-place cycle-placement process. For each index `i`, it repeatedly examines the current value `nums[i]` and its canonical destination `nums[i] - 1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 3, 2, 7, 8, 2, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: When to swap

The condition is

`nums[i] != nums[nums[i] - 1]`.

If the destination contains a different value, the current value is not yet represented there. The simultaneous assignment

`nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]`

moves the current value into its canonical slot and brings the displaced value back to index `i` for examination.

Python evaluates all right-hand expressions before performing left-hand assignments. In particular, both destination calculations use the pre-swap `nums[i]`, so the exchange is well-defined even though the array changes.

After a swap, the `while` loop repeats because `nums[i]` is now a different displaced value that may also belong elsewhere.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the destination test stops safely

If `nums[i] == nums[nums[i] - 1]`, the canonical slot for this value already contains an equal copy.

There are two possibilities. If `i == nums[i]-1`, the current occurrence itself is correctly placed. Otherwise, the canonical position contains the first occurrence and `nums[i]` is the second copy. Swapping equal values would make no progress and loop forever, so equality is exactly the correct stopping condition.

The “at most twice” guarantee means there is only one extra copy to account for per duplicate value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 3, 2, 7, 8, 2, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sign marking:** For value `v`, use the sign of `nums[v-1]` as a seen bit; an already negative location reveals a duplicate. It also achieves $O(n)$ time and $O(1)$ auxiliary space but changes signs rather than positions.
- **Hash set:** Track seen values and append repeats. It is linear average time but uses $O(n)$ extra memory.
- **Sort then compare adjacent values:** This costs $O(n\log n)$ time with comparison sorting and also mutates order.
- **Brute-force later occurrences:** It needs $O(n^2)$ time.
- **Single element:** It moves nowhere and produces an empty output.
- **No duplicates:** Every present value reaches its canonical index, leaving no mismatches.
- **One duplicate:** Exactly one extra occurrence remains at the index of a missing value.
- **Already canonical values:** The equality condition stops without a useless self-swap.
- **Duplicate at a noncanonical index:** Equality with the canonical copy stops the loop and preserves it for final reporting.
- **Values outside `[1,n]`:** Destination indexing would be invalid, which is why the range guarantee is essential.
- **More than two occurrences:** The comprehension could return the same value multiple times; the contract excludes this case.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The outer loop visits $n$ indices. Across all indices, at most $O(n)$ swaps occur because each swap establishes a previously absent canonical placement. The final comprehension performs one more linear scan. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
