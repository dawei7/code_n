# Guided Example: Next Greater Element III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 230241}`
- **Required output:** `230412`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a positive integer `n`, find *the smallest integer which has exactly the same digits existing in the integer* `n` *and is greater in value than* `n`. If no such positive integer exists, return `-1`.

The objective is to compute `230412` from `{"n": 230241}` while avoiding redundant calculations and unnecessary overhead.

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

The task is the standard next lexicographic permutation of the decimal digits. Among all rearrangements greater than the current digit string, the next permutation changes the rightmost possible position by the smallest possible amount, then makes the remaining suffix minimal.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 230241}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The code converts the integer to mutable character list `cs`. Digit characters compare in the same order as their numeric values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Find the rightmost pivot that can increase.** Starting at the second-last index, the loop moves left while:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `230412` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 230241}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `230412` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate all digit permutations:** It is factorial and produces many duplicates when digits repeat.
- **Sort all digits and search:** It discards the useful near-sorted suffix structure and still needs permutation logic.
- **Choose any greater suffix digit:** Picking one larger than necessary skips closer valid numbers.
- **Leave the suffix descending:** The result would be greater but not the smallest greater permutation.
- **Already descending digits:** No greater permutation exists.
- **Repeated digits:** The strict pivot and successor comparisons handle duplicates correctly.
- **One digit:** No pivot exists, so return `-1`.
- **Zeroes in the suffix:** Reversal places them as early as possible after the pivot, minimizing the result.
- **Overflow:** A valid permutation above the signed 32-bit maximum returns `-1`.
- **Input unchanged:** Only the character list is mutated.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $d$ be the number of decimal digits. Pivot search, successor search, suffix reversal, join, and parsing each take $O(d)$ time, so total time is $O(d)$.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
