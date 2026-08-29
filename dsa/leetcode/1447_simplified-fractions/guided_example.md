# Guided Example: Simplified Fractions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2}`
- **Required output:** `["1/2"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return *a list of all **simplified** fractions between *`0`* and *`1`* (exclusive) such that the denominator is less-than-or-equal-to *`n`. You can return the answer in **any order**.

The objective is to compute `["1/2"]` from `{"n": 2}` while avoiding redundant calculations and unnecessary overhead.

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

**Translate the interval into numerator and denominator bounds.** A positive fraction `i / j` lies strictly between zero and one exactly when `0 < i < j`. The denominator must also satisfy `j <= n`. The list comprehension directly enumerates those inequalities:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- `i` ranges from `1` through `n - 1`.
- For each `i`, `j` ranges from `i + 1` through `n`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Starting `i` at one excludes zero, so the fraction cannot equal zero. Starting `j` at `i + 1` guarantees that the denominator is larger than the numerator, so the fraction cannot equal or exceed one. Ending the denominator range at `n` enforces the required maximum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["1/2"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["1/2"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Denominator-first enumeration:** Loop `j` from two through `n` and `i` from one through `j - 1`, accepting coprime pairs. This is equally correct and naturally groups results by denominator rather than numerator.
- **Explicit nested loops:** Replace the comprehension with loops and `ans.append(...)`. It may be easier for beginners to debug, but it performs the same candidate tests and has the same bounds.
- **Generate a Farey sequence:** Farey-sequence methods enumerate reduced fractions in sorted numerical order and can avoid a `gcd` call for every possible pair. They are valuable when ordering or larger bounds matter, but are more complex than required here.
- **Store floating-point values in a set:** This risks rounding collisions, loses exact fraction formatting, and does unnecessary deduplication work. Coprimality gives an exact integer criterion.
- **Reduce every candidate and insert into a set:** Dividing by the greatest common divisor and deduplicating would eventually find the same rational values, but it creates many repeated forms. Rejecting non-coprime pairs directly is simpler.
- **Sort by numeric value:** The problem allows any order, so sorting adds cost without improving correctness. Lexicographic string sorting would also differ from true rational order.
- **n equals one:** No positive numerator can be smaller than a denominator at most one. Both ranges produce no accepted pair, so the returned list is empty.
- **n equals two:** The only legal pair is `1, 2`, whose greatest common divisor is one, producing `"1/2"`.
- **Numerator equals denominator:** Such a fraction equals one and is excluded structurally because `j` always begins at `i + 1`.
- **Zero numerator:** Such a fraction equals zero and is excluded because `i` begins at one.
- **Denominator above n:** The inner range ends at `n` inclusively through Python's exclusive stop `n + 1`, so no oversized denominator appears.
- **Non-reduced fraction:** Any pair such as `2, 4` has greatest common divisor above one and is omitted, even if its reduced value would otherwise be valid.
- **Prime denominator:** Every numerator from one through one less than that prime is coprime to it, so all of those fractions are included.
- **Composite denominator:** Numerators sharing any factor with it are excluded, while the remaining coprime numerators are included.
- **Any-order contract:** The numerator-major order produced by the comprehension is valid. Tests should not require the denominator-major or numerically sorted order of a different implementation.
- **Exact string form:** Each output uses decimal integers separated by one slash, with no spaces and no reduction step left for the caller.
- **Imported gcd:** The solution environment must provide `gcd` from the standard math utilities. Replacing it with division or a floating-point check would not test simplification correctly.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2 log n)$. The number of candidate numerator-denominator pairs is
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
