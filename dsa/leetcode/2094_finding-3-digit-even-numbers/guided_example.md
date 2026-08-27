# Guided Example: Finding 3-Digit Even Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"digits": [2, 2, 8, 8, 2]}`
- **Required output:** `[222, 228, 282, 288, 822, 828, 882]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `digits`, where each element is a digit. The array may contain duplicates.

The objective is to compute `[222, 228, 282, 288, 822, 828, 882]` from `{"digits": [2, 2, 8, 8, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerate the small answer domain instead of index triples

Every valid result is a three-digit even integer. There are only 450 such candidates: 100, 102, ..., 998. This fixed numeric domain does not grow with the input length.

The source first counts available digits with `cnt = Counter(digits)`. It then visits every candidate using `range(100, 1000, 2)`.

Starting at 100 guarantees three digits and automatically excludes leading zero. Stepping by two guarantees the last digit is even. Candidate order is increasing, so accepted values are already sorted. Each numeric candidate appears once, so uniqueness is automatic.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"digits": [2, 2, 8, 8, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extract a candidate's required digit multiset

For one candidate `x`, the code copies it to `y` and repeatedly applies `divmod(y, 10)`. The quotient becomes the remaining prefix, and the remainder `v` is the final digit just removed. `cnt1[v]` is incremented.

Because `x` is between 100 and 999, the loop executes exactly three times. The digits are extracted from right to left, but frequency counts do not depend on order.

For candidate 282, `cnt1` records two copies of digit 2 and one copy of digit 8. This distinguishes it from simply checking whether digits 2 and 8 are present.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For one candidate `x`, the code copies it to `y` and repeate... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Test availability for every digit

The condition

`all(cnt[i] >= cnt1[i] for i in range(10))`

requires the input to provide at least as many copies of every digit as the candidate uses. A `Counter` returns zero for missing keys, so absent digits fail naturally.

This condition is necessary: forming the candidate uses one separate array element per digit position, so no digit may be used more often than it occurs.

It is also sufficient: if the input frequency covers every required frequency, one can select the required number of indices for each digit and arrange them in the candidate's hundreds, tens, and units positions.

The same digit may therefore be reused only through distinct occurrences in `digits`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[222, 228, 282, 288, 822, 828, 882]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"digits": [2, 2, 8, 8, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[222, 228, 282, 288, 822, 828, 882]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate three array indices:** This directly:** - **Enumerate three array indices:** This directly constructs arrangements but costs $O(n^3)$ before deduplication. Candidate enumeration exploits the fixed result domain.
- **Backtracking over digit counts:** It can generate hundreds, tens, and even units positions without reusing unavailable digits, but needs a set or careful ordering to avoid duplicates.
- **Store generated numbers in a set:** A set removes duplicates from index enumeration, followed by sorting. The exact method produces each numeric candidate only once and needs neither.
- **No even digit:** Every candidate frequency test fails because its units digit is even, so the result is empty.
- **Zeros in the input:** Zero may be used in the tens or units place. The candidate range prevents it from becoming a leading digit.
- **Repeated digits required:** The frequency comparison checks multiplicity, so 222 requires three copies of 2.
- **Extra input digits:** They do not hurt; the comparison requires at least the candidate counts, not exact equality.
- **Candidate order:** `range` is increasing, so appending preserves the required sorted order.
- **Uniqueness:** Each integer from 100 to 998 is tested once even when many index selections could form it.
- **Missing counter keys:** Both counters treat missing digit counts as zero, making the ten-way comparison safe.
- **Exactly three input elements:** The same logic applies; a candidate passes only if its multiset matches available elements.
- **Fixed-domain assumption:** The $O(n)$ analysis relies on exactly three decimal digits and ten possible digit values.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `digits`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
