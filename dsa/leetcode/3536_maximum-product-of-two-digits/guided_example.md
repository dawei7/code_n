# Guided Example: Maximum Product of Two Digits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 98368}`
- **Required output:** `72`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n`.

The objective is to compute `72` from `{"n": 98368}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The best pair consists of the two largest digit occurrences

All decimal digits are nonnegative integers from zero through nine. If two chosen digits are `p <= q` and an unchosen digit `r > p` exists, replacing `p` by `r` cannot decrease the product:

`r*q >= p*q`.

Applying this exchange repeatedly shows that a maximum-product pair must use the largest and second-largest digit occurrences.

“Occurrences” matters. If the largest digit appears twice, both copies may be selected. The problem permits using the same digit value twice only when it occurs more than once, and tracking two slots naturally enforces that multiplicity.

The source therefore scans digits once while maintaining:

- `a`: largest processed digit occurrence;
- `b`: second-largest processed digit occurrence;

with invariant `a >= b`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 98368}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extract digits from right to left

`divmod(n,10)` returns quotient and remainder:

`n = 10 * quotient + remainder`.

The remainder `x` is the last decimal digit, and the quotient removes it. The assignment:

`n, x = divmod(n,10)`

therefore visits every digit exactly once from least significant to most significant.

Digit order is irrelevant because the task chooses any two digits, so right-to-left scanning loses nothing.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `divmod(n,10)` returns quotient and remainder:

`n = 10 * qu... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Update the two best slots

If `x > a`, the new digit becomes the largest. The old largest is still the best remaining occurrence, so:

`a,b = x,a`.

If `x` is not larger than `a` but `x > b`, it belongs in the second slot:

`b = x`.

Otherwise, at least two processed occurrences are already no smaller than `x`, so it can be discarded.

The source writes these comparisons as `a < x` and `b < x`, which are equivalent forms.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `72` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 98368}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `72` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Convert to a string and sort digits:** Correct:** - **Convert to a string and sort digits:** Correct, but sorting costs `O(D log D)` and allocates digit storage where two running maxima suffice.
- **Count frequencies for digits zero through nine:** Also correct in `O(D)` time and constant space; scanning down from nine can select the top two occurrences.
- **Check every digit pair:** Costs `O(D^2)`, unnecessary when nonnegative ordering determines the best pair.
- **Use the two largest distinct values:** Wrong for repeated maximum digits such as `22` or `991`.
- **Largest digit appears once:** `b` correctly stores the next-largest occurrence.
- **Largest digit appears multiple times:** One copy occupies each slot, maximizing the product.
- **Zeros:** If every pair must include zero, the maximum product is zero and the initialized slots handle it.
- **Number ending in zero:** `divmod` extracts the zero as a real digit before removing it.
- **Exactly two digits:** The invariant ends with those two occurrences, so their product is returned.
- **Repeated second-largest digit:** Only one second slot is needed once the largest occurrence count is accounted for.
- **Positive n guarantee:** The loop would skip for zero, but zero is outside the documented `n >= 10` domain.
- **At least two digits:** This guarantee is what makes both result slots correspond to real selectable occurrences.
- **Strict comparisons:** They preserve ordering while still allowing an equal-to-`a` digit to enter `b` through the second branch.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. If `D` is the number of decimal digits, the loop executes `D` times. Each iteration performs one `divmod` and a constant number of comparisons/assignments, so time is `O(D)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
