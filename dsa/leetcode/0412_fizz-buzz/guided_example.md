# Guided Example: Fizz Buzz

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3}`
- **Required output:** `["1", "2", "Fizz"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return *a string array *`answer`* (**1-indexed**) where*:

The objective is to compute `["1", "2", "Fizz"]` from `{"n": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Produce exactly one answer for every integer

The output must describe the integers from `1` through `n` in increasing order. The solution therefore loops over `range(1, n + 1)`. Python includes the starting value and excludes the stopping value, so `n + 1` is necessary to process `n`. Each iteration appends exactly one string to `ans`; after the loop, the list has exactly `n` elements, and list index `i - 1` represents integer `i`.

For each integer, the required categories overlap. A multiple of `15` is also a multiple of `3` and a multiple of `5`. The order of the conditional chain is what resolves that overlap correctly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Test the most specific condition first

An integer is divisible by both `3` and `5` exactly when it is divisible by their least common multiple. Because `3` and `5` are coprime, their least common multiple is `15`. Thus `i % 15 == 0` is an exact test for the combined `"FizzBuzz"` case.

The first branch checks this combined condition. Only if it is false does the `elif` chain test divisibility by `3`, then divisibility by `5`. If none of those conditions is true, the integer is converted to its decimal string with `str(i)`.

The ordering is essential. If `i % 3 == 0` were tested first, `i = 15` would enter that branch and append only `"Fizz"`; Python would skip the remaining `elif` branches. Testing the intersection first ensures every multiple of both divisors receives the combined label.

The four actions are:

- append `"FizzBuzz"` when `i % 15 == 0`;
- otherwise append `"Fizz"` when `i % 3 == 0`;
- otherwise append `"Buzz"` when `i % 5 == 0`; and
- otherwise append `str(i)`.

Because this is one `if`/`elif`/`elif`/`else` chain, exactly one action runs. No integer can add two separate list items, and no integer can add none.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why remainder zero means divisible

For integers $i$ and $d>0$, division gives a quotient and a remainder. The divisor $d$ divides $i$ precisely when that remainder is zero. Python's `%` operator computes the remainder, so `i % d == 0` directly expresses divisibility by `d`. The input values are positive, so there are no sign subtleties.

For a short trace with `n = 5`:

- `1` has nonzero remainder modulo `3`, `5`, and `15`, so append `"1"`.
- `2` also reaches the fallback, so append `"2"`.
- `3 % 3 == 0`, so append `"Fizz"`.
- `4` reaches the fallback, so append `"4"`.
- `5 % 5 == 0`, so append `"Buzz"`.

At `i = 15`, the first condition succeeds, so the list receives one `"FizzBuzz"` entry.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["1", "2", "Fizz"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["1", "2", "Fizz"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two independent divisibility checks with concatenation:** Start an empty string, append `"Fizz"` if divisible by `3`, append `"Buzz"` if divisible by `5`, and use the number if the string remains empty. This naturally builds `"FizzBuzz"` and is easy to extend, with the same asymptotic bounds. The chosen chain is equally efficient and explicit for the fixed rules.
- **Divisor-to-label mapping:** Iterate through pairs such as `(3, "Fizz")` and `(5, "Buzz")`. This is preferable when mappings are configurable, but introduces a nested loop and requires preserving mapping order so combined labels are spelled correctly.
- **Precompute the 15-value cycle:** Divisibility categories repeat every 15 integers, but ordinary numeric entries do not repeat because their text changes. Cycle precomputation adds complexity without improving the required $O(n)$ output time.
- **Check `3` before `15`:** This is incorrect in an `if`/`elif` chain because multiples of 15 would stop at `"Fizz"`. The combined condition must come first.
- **Use `i % 3 == 0 and i % 5 == 0`:** This is logically equivalent to `i % 15 == 0`. It performs two explicit checks and may be clearer when the divisors are not coprime; for `3` and `5`, the single least-common-multiple test is exact.
- **`n == 1`:** The loop executes once and returns `["1"]`; no special case is needed.
- **Upper endpoint:** `range(1, n + 1)` includes `n`. Using `range(1, n)` would silently omit the final required entry.
- **Multiples such as 3 and 5:** They enter exactly one single-label branch because the earlier combined test failed.
- **Multiples of 15:** They enter the first branch and never fall through to a shorter label.
- **Nonmultiples:** `str(i)` is necessary because every output element must be a string, not an integer.
- **Positive-input guarantee:** The contract starts at `n = 1`; behavior for zero or negative upper bounds is outside the problem and need not be added to the algorithm.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the input upper bound. The loop executes exactly $n$ iterations. Each iteration performs at most three modulo comparisons, one possible integer-to-string conversion, and one list append. Under the usual fixed-width integer model for the stated constraint, each is constant work, so the total time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
