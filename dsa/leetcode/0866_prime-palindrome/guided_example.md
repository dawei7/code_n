# Guided Example: Prime Palindrome

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 9989900}`
- **Required output:** `100030001`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer n, return *the smallest **prime palindrome** greater than or equal to *`n`.

The objective is to compute `100030001` from `{"n": 9989900}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Test candidates in increasing order

The function starts at `n` and returns the first number that is both:

- equal to its digit reversal;
- prime.

Because candidates are considered in increasing numeric order, the first successful one is automatically the smallest prime palindrome at least the original input.

A crucial skip avoids examining almost all eight-digit values, where no prime palindrome can exist.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 9989900}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reverse digits numerically

Helper `reverse(x)` constructs the decimal reversal without converting to a string:

1. take last digit `x % 10`;
2. append it to `res` through `res*10 + digit`;
3. remove the last digit using `x //= 10`.

When the loop ends, `res` is the reversed digit order.

`reverse(n) == n` is exactly the palindrome condition. Leading zeroes in a reversal disappear numerically, which correctly prevents a number ending in zero from appearing palindromic unless it is zero itself.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Helper `reverse(x)` constructs the decimal reversal without ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Primality test

`is_prime(x)` rejects values below two, correctly excluding 0 and 1.

It tries divisors `v` from two while `v*v <= x`. If any divides `x` exactly, `x` is composite.

If a composite number has factors `a*b=x`, at least one factor is at most $\sqrt{x}$. Therefore, finding no divisor through the square root proves primality.

The direct test uses every integer divisor rather than only primes; this is simpler and remains within the stated complexity.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `100030001` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 9989900}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `100030001` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Generate palindromes rather than scan integers:** - **Generate palindromes rather than scan integers:** Mirror a digit prefix to enumerate only palindromes, then test primality. This can reduce `P` substantially but requires careful length transitions.
- **- **Sieve primes:** The upper range is too large f:** - **Sieve primes:** The upper range is too large for a simple full boolean sieve to be attractive for one query.
- **- **Test primality before palindrome:** Correct bu:** - **Test primality before palindrome:** Correct but wastes expensive divisor checks on most candidates.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P\sqrt{A})$. Let `P` be the number of candidates tested after accounting for the eight-digit skip, and let `A` be the returned answer.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
