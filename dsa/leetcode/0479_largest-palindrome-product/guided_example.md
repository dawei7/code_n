# Guided Example: Largest Palindrome Product

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1}`
- **Required output:** `9`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer n, return *the **largest palindromic integer** that can be represented as the product of two `n`-digits integers*. Since the answer can be very large, return it **modulo** `1337`.

The objective is to compute `9` from `{"n": 1}` while avoiding redundant calculations and unnecessary overhead.

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

The task has two distinct stages: first identify the largest palindrome that is the product of two `n`-digit integers, and only then reduce that palindrome modulo `1337`. That order matters. Comparing remainders would not reveal which original product is largest, because taking a modulus does not preserve numeric order. The solution therefore searches with the full palindrome in `x` and returns `x % 1337` only after it has proved that `x` has suitable factors.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Turn one descending number into descending palindrome candidates.** Let `mx = 10**n - 1`, the largest `n`-digit integer. The outer loop lets `a` run from `mx` down through `10**(n - 1)`. The actual stop value in `range(mx, mx // 10, -1)` is excluded; because `mx // 10 = 10**(n - 1) - 1`, every possible `n`-digit value is included.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Turn one descending number into descending palindrome cand... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

For each `a`, the code forms an even-length palindrome whose left half is `a`. It starts with `b = x = a`. On every iteration, `b % 10` extracts the last digit still present in `b`, `x = x * 10 + b % 10` appends that digit to `x`, and `b //= 10` removes the extracted digit. The digits of `a` are consequently appended in reverse order. For example, if `a = 91`, the updates are `91 -> 919 -> 9191`, producing the palindrome `9191`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `9` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `9` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Precomputed eight-answer table:** Because `n` :** - **Precomputed eight-answer table:** Because `n` is restricted to `1` through `8`, a reviewed table gives literal constant-time lookup and is a natural bounded-domain alternative. The present solution instead derives the answer by search, which exposes why a candidate is valid but performs more work.
- **Enumerate every pair of factors:** Multiplying all pairs and testing each product for palindromicity is straightforward, but it repeats work because many pairs share products and most products are not palindromes. Generating only palindromes directs the search toward viable answers.
- **Generate all decimal palindromes:** Constructing and storing a full candidate collection is unnecessary. Mirroring descending left halves already produces the needed order, so candidates can be checked one at a time with constant auxiliary storage.
- **Reduce modulo too early:** Searching or comparing `x % 1337` values is incorrect. Different original palindromes can have unrelated remainder order, so reduction must happen only after the largest valid original palindrome is known.
- **Stop factor testing below the square root:** That adds duplicate factor checks. Every factor pair has a member at least as large as the square root, and testing that member is sufficient to detect the pair.
- **Perfect-square candidate:** The condition `t * t >= x` includes equality. If the legal factorization is `t * t = x`, the square-root factor is tested rather than skipped.
- **Single-digit input:** The even-length mirroring search is not the mechanism used for `n = 1`; the explicit fallback returns `9`, the correct largest palindromic product of one-digit factors.
- **Return value versus witness factors:** The contract asks only for the palindrome modulo `1337`, so the quotient `x // t` does not need to be retained or returned after divisibility proves that the factor pair exists.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Under the problem's fixed legal domain, `n` can take only eight values, so both the largest candidate and the maximum number of loop iterations are bounded by a problem constant. This is why the manifest records time as $O(1)$ and auxiliary space as $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
