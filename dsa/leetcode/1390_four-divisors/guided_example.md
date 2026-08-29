# Guided Example: Four Divisors

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [21, 4, 7]}`
- **Required output:** `32`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return *the sum of divisors of the integers in that array that have exactly four divisors*. If there is no such integer in the array, return `0`.

The objective is to compute `32` from `{"nums": [21, 4, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Divisors arrive in pairs

If positive integer $i$ divides $x$, then $x/i$ also divides $x$. One of the two values is at most $\sqrt{x}$ and the other is at least $\sqrt{x}$. Therefore checking candidate divisors only through the square root discovers every pair.

The helper `f(x)` begins by assuming the universal divisors 1 and $x$:

- `cnt = 2` records two divisors.
- `s = x + 1` records their sum.

It then tests possible smaller divisors starting at two. For normal $x>1$, this avoids rediscovering 1 and $x$.

For $x=1$, the initialization conceptually counts the same divisor twice. The loop does not run and `cnt` is not four, so the helper still correctly returns zero. A more general divisor routine might special-case one, but the exact four-divisor decision is unaffected.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [21, 4, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the loop condition reaches exactly the square root

`while i <= x // i` is an integer-safe form of $i^2\le x$. In languages with fixed-width integers it avoids overflow from multiplying large `i` values. In Python overflow is not a concern, but the condition remains exact and avoids floating-point square roots.

For each `i` that divides `x`, the code adds `i` as one divisor. If `i * i != x`, the paired quotient `x // i` is different and is added as a second divisor. If $i^2=x$, the pair is the same middle divisor and must be counted only once.

For $x=21$, initialization records 1 and 21. Candidate 3 divides it and pairs with 7, bringing the count to four and the sum to 32. No other candidate divides it, so `f(21)` returns 32.

For $x=4$, candidate 2 is the square root. It is counted once, producing three divisors 1, 2, and 4. The helper returns zero because the number does not have exactly four.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the helper does not stop at four

Finding four divisors partway through is not enough; later factor pairs may raise the count beyond four. The code continues through the full square-root range and returns the sum only if final `cnt == 4`. This prevents numbers with six or more divisors from contributing an early partial sum.

It could stop early once `cnt > 4` because the count can never decrease, but the exact implementation favors simple complete enumeration. The asymptotic bound is unchanged.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `32` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [21, 4, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `32` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prime-factor classification:** Factor $x$ and test whether its exponent pattern is either three or one-plus-one. It reaches a similar square-root bound but requires careful prime bookkeeping.
- **Sieve preprocessing:** Precompute divisor counts and sums for every value through $V$, then answer each array element in constant time. It can help for many inputs but uses $O(V)$ space.
- **Precompute $p^3$ and $pq$ forms:** Generate primes and map all four-divisor values to their sums. It leverages the classification but is more elaborate for a single array.
- **Early exit after count exceeds four:** Safe because divisor count only grows, though the exact code scans the full range.
- **`x = 1`:** It has one divisor and contributes zero despite the helper's harmless doubled initialization.
- **Prime number:** Only 1 and itself are found, so it contributes zero.
- **Prime cube:** Exactly one nonsquare or square-pair structure yields four total divisors and is accepted.
- **Product of two distinct primes:** Its one inner factor pair plus 1 and itself yields four.
- **Perfect square:** The square-root divisor is counted once, preventing a duplicate.
- **More than four divisors:** Full enumeration raises `cnt` beyond four, and the entire sum is discarded.
- **Duplicate array values:** Each occurrence contributes separately.
- **Integer loop bound:** `i <= x // i` avoids floating-point rounding and fixed-width multiplication overflow.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m\sqrt{V})$. Let $m$ be the number of input elements and $V$ the maximum value. For one $x$, the helper tests $O(\sqrt{x})$ candidates. Across the array this is
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
