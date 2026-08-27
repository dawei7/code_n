# Guided Example: Sort Array By Absolute Value

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, -1, -4, 1, 5]}`
- **Required output:** `[-1, 1, 3, -4, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `[-1, 1, 3, -4, 5]` from `{"nums": [3, -1, -4, 1, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort by the required key rather than by the original value

The requested order compares `|nums[i]|`. Python’s `sorted` accepts a `key` function that transforms each element only for comparison while retaining the original element in the result.

The source uses

`sorted(nums, key=lambda x: abs(x))`.

For each integer `x`, `abs(x)` is its non-negative magnitude. The sorting algorithm orders elements by these magnitudes in non-decreasing order.

The key does not replace `-4` with `4` in the output. It uses four as comparison metadata and still returns the original `-4` value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, -1, -4, 1, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why one key comparison establishes the required result

After key-based sorting, for every adjacent output pair `a, b`,

`abs(a) <= abs(b)`.

By transitivity, every earlier element’s magnitude is no greater than every later element’s magnitude. That is exactly the required non-decreasing absolute-value condition.

No additional rule is specified for values with equal magnitudes. Either `-1, 1` or `1, -1` is valid because both keys are one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After key-based sorting, for every adjacent output pair `a, ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Python’s stability gives a deterministic tie behavior

Python sorting is stable: when two elements have equal keys, their relative input order is preserved.

For `[3, -1, -4, 1, 5]`, the two magnitude-one values appear as `-1` then `1` in the input, so they retain that order in the result. If their input order were reversed, the source would return `1` before `-1`.

Stability is not required by the problem, which permits any valid rearrangement, but it explains the exact output behavior of the source.

Duplicates and opposite-signed pairs need no special handling. They are ordinary elements with equal or different absolute-value keys.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[-1, 1, 3, -4, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, -1, -4, 1, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[-1, 1, 3, -4, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Fixed-domain counting:** Count each value from:** - **Fixed-domain counting:** Count each value from `-100` through `100`, then emit values by magnitude. This realizes the manifest’s `O(n)` time and constant-domain storage.
- **In-place key sort:** `nums.sort(key=abs)` avoids a separate returned copy but mutates the caller’s array and still has `O(n log n)` time.
- **Sort ordinary numeric values:** This orders negatives before positives rather than ordering by magnitude and solves a different task.
- **Replace values with their absolute values:** The output must contain the original signed elements, not only their magnitudes.
- **Add a sign tie-break:** It is permitted but unnecessary; any order among equal magnitudes is valid.
- **Zero:** Its absolute value is zero, so all zeros appear before nonzero values.
- **Opposite values:** `x` and `-x` tie. Stable sorting retains whichever appeared first.
- **Duplicate values:** Every occurrence remains in the result.
- **Already absolute-value sorted:** Stable TimSort preserves the valid order.
- **Single element:** Sorting returns a new one-element list with the same value.
- **Most negative allowed value:** `abs(-100) = 100` is valid and poses no overflow issue in Python.
- **Input preservation:** `sorted` leaves `nums` unchanged.
- **Missing import:** The stored source uses `List` without importing it. Standalone Python needs `from typing import List` unless the harness provides the name.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. Python’s key-based TimSort has worst-case `O(n log n)` time, with `O(n)` key extraction work included in that bound. It can run closer to `O(n)` on already structured data, but the worst-case source complexity is `O(n log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
