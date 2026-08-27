# Guided Example: Longest Well-Performing Interval

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"hours": [9, 9, 6, 0, 6, 6, 9]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We are given `hours`, a list of the number of hours worked per day for a given employee.

The objective is to compute `3` from `{"hours": [9, 9, 6, 0, 6, 6, 9]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert the condition into a positive-sum interval

A tiring day should contribute one and a non-tiring day should contribute negative one. Then an interval’s sum equals:

`number of tiring days - number of non-tiring days`.

The interval is well-performing exactly when this sum is strictly positive.

The loop maintains prefix sum `s` through the current day. Each hour value greater than eight adds one; every value at most eight subtracts one. The original scheduling story is now a standard longest positive-sum subarray problem.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"hours": [9, 9, 6, 0, 6, 6, 9]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use prefix-sum differences

Let the prefix sum through index `i` be $S_i$. An interval starting after earlier index `j` and ending at `i` has sum:

$S_i-S_j$.

It is positive when $S_j<S_i$. To maximize interval length for a fixed end, the algorithm wants the earliest earlier position whose prefix sum is smaller than the current sum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let the prefix sum through index `i` be $S_i$.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle a positive whole prefix

If current `s > 0`, the interval from day zero through `i` is already well-performing. Its length is `i + 1`.

No interval ending at `i` can be longer because this one begins at the first array position. Therefore, the code directly assigns `ans = i + 1`.

The conceptual prefix before the array has sum zero at index negative one. This branch is equivalent to using that sentinel when current sum exceeds zero, without storing it in the dictionary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"hours": [9, 9, 6, 0, 6, 6, 9]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Quadratic enumeration:** Compute every interva:** - **Quadratic enumeration:** Compute every interval sum, taking $O(n^2)$ time even with prefix sums.
- **Monotonic-stack prefix method:** Build all prefixes, keep decreasing candidate indices, and scan from the right. It also achieves $O(n)$ but uses a more global proof.
- **Store every prefix occurrence:** Correct but unnecessary; only the earliest can maximize length.
- **All tiring days:** Every prefix is positive, so the answer grows to $n$.
- **No tiring days:** Prefix sums only decrease and no `s - 1` was seen earlier, so the answer remains zero.
- **Exactly balanced interval:** Sum zero is not sufficient because tiring days must be strictly more numerous.
- **Eight hours:** It is non-tiring because the threshold is strictly greater than eight.
- **Repeated prefix sum:** Later occurrences are ignored to preserve the longest future span.
- **Positive prefix after earlier negatives:** The whole prefix branch still dominates every shorter candidate ending there.
- **Single tiring day:** The answer is one.
- **Single non-tiring day:** The answer is zero.
- **Implicit prefix zero:** The `s > 0` branch replaces the need to store sum zero at index negative one.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of days. The loop processes every day once. Dictionary membership, lookup, and insertion take expected $O(1)$ time, so total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
