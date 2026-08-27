# Guided Example: Contiguous Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a binary array `nums`, return *the maximum length of a contiguous subarray with an equal number of *`0`* and *`1`.

The objective is to compute `2` from `{"nums": [0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

The condition “equal numbers of zeroes and ones” becomes easier to track after assigning opposite contributions to the two values:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- treat each `1` as `+1`;
- treat each `0` as `-1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - treat each `1` as `+1`;
- treat each `0` as `-1`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Under this transformation, a subarray has equal counts exactly when its transformed sum is zero. Every one contributes one positive unit and every zero contributes one negative unit, so the units cancel precisely when the two counts match.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all subarrays:** Maintaining counts :** - **Enumerate all subarrays:** Maintaining counts while extending each start avoids a third loop but still takes $O(n^2)$ time.
- **Build an explicit transformed array:** It makes the plus-one/minus-one model visible but costs an unnecessary additional $O(n)$ array; the implementation transforms values during the scan.
- **Overwrite a repeated balance:** This loses the farthest-left boundary and can produce a shorter answer.
- **Subarray starting at index zero:** The `0: -1` sentinel gives its full length without special handling.
- **All zeroes:** The balance strictly decreases, never repeats, and the answer remains zero.
- **All ones:** The balance strictly increases with the same result.
- **Two opposite values:** Either `[0, 1]` or `[1, 0]` returns two.
- **Odd-length interval:** It cannot contain equal integer counts of two symbols, and the balance method never reports one.
- **Several maximum intervals:** Only their common maximum length is requested.
- **Boolean conditional:** It is safe here because the input domain contains only zero and one.
- **Negative balances:** Dictionary keys may be negative; they carry the same prefix-state meaning as positive balances.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The solution visits every element once. Each iteration performs constant arithmetic and an expected-$O(1)$ dictionary operation, so expected running time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
