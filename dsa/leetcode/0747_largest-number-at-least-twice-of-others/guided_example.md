# Guided Example: Largest Number At Least Twice of Others

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 6, 1, 0]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` where the largest integer is **unique**.

The objective is to compute `1` from `{"nums": [3, 6, 1, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only the largest competitor matters

Let `x` be the unique largest value and `y` be the second-largest value. Every other array value is at most `y`.

Therefore:

- If `x >= 2 * y`, then `x` is at least twice every other value.
- If `x < 2 * y`, the condition already fails for `y`.

Checking the largest against the second largest is both necessary and sufficient. There is no need to compare `x` separately with all remaining smaller values after those two have been identified.

This argument uses the nonnegative-value constraint. Multiplying preserves the ordering among competitors.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 6, 1, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extract the two largest values

The exact solution calls

`x, y = nlargest(2, nums)`.

`heapq.nlargest` returns the requested number of elements in descending order, so `x` is the largest and `y` the second largest. It internally maintains only a fixed-size selection structure for two values rather than sorting the entire input.

The array length is at least two, so unpacking exactly two results is always safe.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Test the dominance condition

The comparison `x >= 2 * y` directly represents “at least twice.” Equality qualifies. For example, largest six and second largest three pass.

If the test fails, `y` is a concrete other element for which the largest is less than twice its value, so the method returns `-1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 6, 1, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One-pass largest and second-largest tracking:** Maintain both values and the largest index while scanning. This achieves the same `O(n)` time and `O(1)` space without a second index scan.
- **Find maximum, then scan all others:** Obtain the maximum and index, then verify `max >= 2 * value` for every other position. This is also linear but performs explicit repeated checks instead of using the second-largest reduction.
- **Sort value-index pairs:** The last two pairs reveal the needed values and preserve the index, but sorting costs `O(n log n)`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. Selecting the two largest values with a heap of fixed size two costs `O(n log 2) = O(n)` time. Finding `x`’s index performs another linear scan, so total time remains `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
