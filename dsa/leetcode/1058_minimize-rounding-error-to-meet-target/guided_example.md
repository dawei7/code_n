# Guided Example: Minimize Rounding Error to Meet Target

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"prices": ["0.700", "2.800", "4.900"], "target": 8}`
- **Required output:** `"1.000"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of `prices` `[p_1,p_2...,p_n]` and a `target`, round each price $p_{i}$ to $\text{Round}_{i}(p_{i})$ so that the rounded array `[Round_1(p_1),Round_2(p_2)...,Round_n(p_n)]` sums to the given `target`. Each operation $\text{Round}_{i}(p_{i})$ could be either $Floor(p_{i})$ or $Ceil(p_{i})$.

The objective is to compute `"1.000"` from `{"prices": ["0.700", "2.800", "4.900"], "target": 8}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Begin from the smallest possible rounded sum

Every non-negative price can be rounded either down to its floor or up to its ceiling. If all prices are rounded down, their sum is the smallest total that any permitted choices can produce.

The solution calls this floor sum `mi`:



Because every price is non-negative, Python's `int(p)` truncation is exactly the mathematical floor. That equivalence would not hold for negative non-integral values, but the input constraints exclude them.

The code parses each three-decimal string into a floating-point value. `mi` accumulates only the integer parts, so after the loop it is the sum obtained by flooring every price.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"prices": ["0.700", "2.800", "4.900"], "target": 8}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Only non-integral prices create a choice

Inside the same loop, the fractional part is computed and conditionally saved:



The walrus operator assigns the fractional part to `d` and then tests it. A zero fractional part is false, so an integral price is omitted. A positive fractional part is true and is appended to `arr`.

For an integral price such as `"4.000"`, floor and ceiling are both four. It contributes zero rounding error and cannot increase the rounded sum, so it creates no decision and does not belong in `arr`.

For a non-integral price with fractional part `f`:

- Rounding down contributes its floor to the sum and creates error `f`.
- Rounding up contributes one more than its floor and creates error `1 - f`.

Every non-integral price rounded up therefore adds exactly one to the all-floor sum. The actual integer part of that price no longer matters to the choice; only its fractional part determines the error.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Check whether the target is reachable

If `F = len(arr)`, the minimum possible rounded sum is `mi` and the maximum is `mi + F`. Every integer between them is reachable because each of the `F` independent non-integral prices can add either zero or one.

The code checks precisely that interval:



If `target < mi`, even rounding everything down is too large. If `target > mi + F`, even rounding every possible price up is too small. In either case, no selection can work.

If the target lies inside the interval, the required number of upward roundings is fixed:



This later assignment reuses the name `d`. From this point onward it no longer means one fractional part; it means the integer count of prices that must be rounded up.

Exactly `d` non-integral prices must use their ceilings. Fewer would make the total too small, and more would make it too large. The optimization question is therefore: which `d` fractional parts should be rounded upward?

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"1.000"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"prices": ["0.700", "2.800", "4.900"], "target": 8}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"1.000"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Thousandths frequency buckets for the manifest target:** Parse prices as exact scaled integers, count fractional values from zero through 999, and consume buckets from largest to smallest for upward rounding. This gives `O(N + K)` time and `O(K)` space.
- **Exact integer parsing with sorting:** Convert each price string to thousandths and sort the nonzero remainder values. This retains `O(N + F log F)` time but avoids all binary floating-point representation concerns.
- **Maximum heap:** Keep fractional parts in a heap and extract the `d` largest. This takes `O(N + d log F)` time and `O(F)` space, which can help when `d` is very small but is not as strong as bounded-domain counting.
- **Dynamic programming:** A DP over price count and rounded sum can find a minimum, but every non-integral choice changes the sum by exactly one. The required number of ceilings is already known, so DP is unnecessary.
- **Target below the floor sum:** No rounding choice can reduce a price below its floor, so the function returns `"-1"`.
- **Target above the ceiling sum:** No rounding choice can exceed the ceiling of a price, so the function returns `"-1"`.
- **All prices integral:** `arr` is empty and the only reachable target is `mi`. For that target, `d` is zero and the formatted error is `"0.000"`.
- **Round everything down:** When `target == mi`, `d` is zero and every fractional part contributes its floor error.
- **Round every non-integral price up:** When `target == mi + len(arr)`, the suffix is empty and every fractional part contributes its ceiling error.
- **Equal fractional parts:** Any choice among equal fractions has the same error. Their relative order after sorting is irrelevant.
- **Zero-valued price:** `"0.000"` adds nothing to the floor sum, creates no choice, and contributes zero error.
- **Floating-point accumulation:** The exact source relies on final three-decimal formatting to round small representation noise. Parsing scaled thousandths as integers is a more explicit exact-arithmetic alternative.
- **Walrus-name reuse:** `d` first denotes a fractional part inside the loop and later denotes the number of ceilings. The earlier value is no longer needed, so reuse is safe even though separate names would be clearer.
- **Input preservation:** The list of price strings is not modified. Parsed fractions are stored separately in `arr`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + F log F)$. Let `N` be the number of prices and `F` be the number of non-integral prices.
- **Auxiliary Space Complexity:** $O(F)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
