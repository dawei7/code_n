# Guided Example: Count Primes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 10}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return *the number of prime numbers that are strictly less than* `n`.

The objective is to compute `4` from `{"n": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat every index as a candidate number

The solution allocates `primes = [true] * n`. Index `x` represents integer
`x`, and a true value means no smaller processed prime has yet proved `x`
composite.

Indices 0 and 1 also begin true, even though neither is prime. This causes no
incorrect count because the outer loop starts at 2 and never examines those
indices. A more explicit sieve might initialize them false, but the exact code
does not need to.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan candidates in increasing order

For every `i` from 2 through `n - 1`, the algorithm checks `primes[i]`. If the
entry is false, some earlier prime marked `i` as a multiple, so it is composite
and is skipped.

If the entry is still true, `i` is prime. The proof comes from the smallest
prime factor: if `i` were composite, it would have a factor smaller than `i`,
and that factor's marking pass would already have set this entry false. The
algorithm therefore increments `ans` exactly at prime indices.

Scanning only through `n - 1` enforces the exclusive upper bound. Even if `n`
itself is prime, it has no array index in this length-$n$ list and is not
counted.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark all later multiples of a discovered prime

For a prime `i`, the inner range begins at `i + i`, advances by `i`, and stops
before `n`. These values are `2i, 3i, 4i, ...`, each divisible by `i` with a
second factor at least two, so every marked value is composite.

The prime `i` itself is not marked because marking begins at twice its value.
Some composite entries are written false many times; for example, 30 is a
multiple of 2, 3, and 5. Repeatedly assigning false does not change correctness,
though it adds work.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Square-start sieve:** Begin marking at `p*p` and stop outer candidate processing near $\sqrt n$; avoids redundant writes.
- **Bytearray slicing:** Compact storage and C-level bulk marking can be substantially faster in Python.
- **Odd-only sieve:** Store only odd candidates and treat 2 separately, as the competitive variant effectively does.
- **Linear sieve:** Record smallest prime factors so each composite is generated once; $O(n)$ time but more bookkeeping.
- **Trial division per number:** Uses less sieve storage but is too slow near five million.
- **`n <= 2`:** No primes are strictly below the bound.
- **Prime `n`:** Excluded because the range is `[0,n)`.
- **Repeated marking:** Safe because false assignment is idempotent.
- **Indices 0 and 1:** Remain true internally but are never scanned or counted.
- **Manifest mismatch:** Exact source is a boolean-list, `2p`-start sieve, not a bytearray square-start implementation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log \log n)$. The outer scan is $O(n)$. For each prime $p<n$, the inner loop performs roughly
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
