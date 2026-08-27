# Guided Example: Number of Centered Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-1, 1, 0]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `5` from `{"nums": [-1, 1, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerate each contiguous interval by its endpoints

The outer loop fixes left endpoint `i`. The inner loop advances right endpoint `j` from `i` through the final index.

For this fixed left endpoint, `s` is the running sum of `nums[i..j]` and `st` contains all values appearing in that same interval.

After adding `nums[j]` to both structures, `s in st` is exactly the centered-subarray condition.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-1, 1, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reuse state while extending right

Moving `j` one step adds one element. The new sum is the previous sum plus that value, and the new contained-value set is the previous set plus that value.

This makes each interval check expected constant time after its extension. Recomputing `sum(nums[i:j+1])` and rebuilding a set for every pair would introduce another linear factor.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Moving `j` one step adds one element.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reset for each new left endpoint

When `i` increases, earlier elements must no longer belong to the candidate intervals. The source creates a fresh empty set and zero sum inside the outer loop.

It does not attempt a sliding-window optimization because values may be negative and the centered property is not monotone when boundaries move.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-1, 1, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recompute sum and set per interval:** This rai:** - **Recompute sum and set per interval:** This raises time toward $O(N^3)$.
- **Prefix sums only:** They give interval sums quickly but do not answer whether that sum appears inside the interval.
- **Sliding window:** Negative values and nonmonotone membership provide no safe one-direction shrink rule.
- **Count each matching occurrence:** A centered interval counts once even if its sum appears several times.
- **Singleton:** Always centered.
- **All zeros:** Every interval has sum zero and contains zero, so all intervals count.
- **Negative sums:** Set membership handles them normally.
- **Duplicate values:** The set preserves existence semantics.
- **No qualifying longer intervals:** Singletons still contribute $N$.
- **Input preservation:** Only local sums and sets are changed.
- **Several matching occurrences:** The interval still counts once.
- **Nonmonotone validity:** Extension may destroy or restore the property.
- **Fresh outer state:** Each left endpoint resets sum and membership.
- **Right endpoint witness:** Add it to the set before testing the extended interval.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. There are $N(N+1)/2=O(N^2)$ intervals. Each extension performs constant arithmetic and expected $O(1)$ set operations, so expected total time is $O(N^2)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
