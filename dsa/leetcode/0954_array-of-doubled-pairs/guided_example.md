# Guided Example: Array of Doubled Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [3, 1, 3, 6]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array of even length `arr`, return `true`* if it is possible to reorder *`arr`* such that *$arr[2 * i + 1] = 2 * arr[2 * i]$* for every *$0 \le i < len(arr) / 2$*, or *`false`* otherwise*.

The objective is to compute `false` from `{"arr": [3, 1, 3, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each smaller absolute value must claim its double

Every pair must have the form `(x, 2x)`. The difficult part is deciding which occurrence plays the role of `x` and which plays the role of its double, especially for negative numbers.

The solution counts occurrences with `Counter` and processes distinct values in increasing order of absolute value:

`sorted(freq, key=abs)`.

For each `x`, all remaining occurrences of `x` must be paired with the same number of occurrences of `2x`. If fewer doubles remain, pairing is impossible. Otherwise, those doubles are consumed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [3, 1, 3, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why ordinary numeric sorting is wrong for negatives

For positive values, the base `x` is smaller than `2x`. For negative values, numeric order reverses that appearance: `-4 < -2`, but the valid pair is `(-2, -4)`.

Absolute-value order solves both cases. A nonzero value always has smaller absolute value than its double:

`abs(x) < abs(2x)`.

Therefore, when `x` is processed, it is the natural base whose required double has not been used as a base earlier.

For example, `-2` is processed before `-4`, so the algorithm consumes `-4` as its double rather than incorrectly demanding `-8` for `-4` first.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Frequency accounting

Suppose `freq[x] = c` at the moment value `x` is processed. Every one of those `c` copies must be the first element of a pair, so at least `c` copies of `2x` are required.

The check `freq[x << 1] < freq[x]` detects a shortage. Left shift by one multiplies an integer by two, including negative integers in Python.

If enough copies exist, the code performs:

`freq[x << 1] -= freq[x]`.

This reserves those double values and prevents them from being reused by another base.

Counter returns zero for a missing key, so absent doubles naturally fail the comparison.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [3, 1, 3, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort every array occurrence by absolute value:** Pair each occurrence greedily with its double using counts. This has the same asymptotic bounds but may sort more items than distinct-key sorting.
- **Ordinary ascending sort:** It mishandles negative bases because a more negative double appears before its half.
- **Backtracking:** Trying pair assignments is exponential and unnecessary once absolute-value order reveals forced choices.
- **Odd number of zeros:** Always false because zeros pair only with zeros.
- **Even zeros:** They can all be paired and do not interact with nonzero values.
- **Duplicate bases:** The double frequency must cover the complete remaining multiplicity.
- **Values already consumed as doubles:** Their frequency becomes zero, so later processing does nothing.
- **Negative left shift:** In Python, `x << 1` equals `2x` for negative and positive integers.
- **Even input length:** It is necessary but not sufficient; factor relationships must also match.
- **Missing Counter key:** It behaves as count zero, allowing a direct shortage check.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N log N)$. Let `N` be the array length.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
