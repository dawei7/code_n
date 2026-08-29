# Guided Example: Prime Pairs With Target Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 10}`
- **Required output:** `[[3, 7], [5, 5]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`. We say that two integers `x` and `y` form a prime number pair if:

The objective is to compute `[[3, 7], [5, 5]]` from `{"n": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate prime discovery from pair discovery

The desired pairs must satisfy two independent facts: both numbers are prime, and their sum is `n`. Testing primality from scratch for every possible pair would repeat the same divisibility work many times. The exact solution first builds a table that answers “is this number prime?” in constant time, then performs a simple complement scan.

The table is the list `primes` of length `n`. An index represents the number with the same value. It is initially true everywhere, and the sieve marks composite indices false. Although indices zero and one are never explicitly corrected, this does not affect the result because the later pair scan only examines `x >= 2` and its complement `y = n - x >= x >= 2`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the sieve eliminates composites

The outer loop considers every `i` from 2 through `n - 1`. If `primes[i]` is still true, no smaller prime has marked `i`, so `i` is prime. The inner loop visits `2i, 3i, 4i, ...` below `n` and marks each multiple false.

Every marked value is composite because it is a product of `i` and an integer of at least two. In the opposite direction, take any composite `c < n`. It has some prime divisor `p` smaller than `c`. When the outer loop reaches `p`, `p` is still true and its multiples include `c`, so `c` becomes false. Thus, for every queried index from two onward, the table is true exactly for primes.

The exact code starts marking at `i + i` rather than `i * i`. Multiples below `i * i` may already have been marked by smaller factors, so starting at the square would avoid redundant writes. Starting at `2i` is nevertheless correct and retains the standard sieve asymptotic bound.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Only scan through half of the target

After the sieve, the solution loops over

`x = 2, 3, ..., n // 2`

and defines `y = n - x`. The sum condition is then automatic: `x + y = n`. The upper limit gives `x <= y`, which is exactly the ordering required inside each pair. It also prevents producing both `[x, y]` and `[y, x]`.

The test `primes[x] and primes[y]` is now constant-time. If both entries are true, the pair satisfies all requirements and is appended.

There is no need to search for `y`, factor it, or use a second nested loop. Every possible partner for a chosen `x` is uniquely determined by subtraction.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[3, 7], [5, 5]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[3, 7], [5, 5]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Trial division for every complement:** Checking each `x` and `n - x` up to their square roots avoids the sieve array but repeats work and can take about `O(n sqrt n)` time in the straightforward form.
- **Sieve from `i * i`:** This is a safe constant-factor optimization because smaller multiples already have smaller prime factors. The exact solution starts at `2i` and remains correct.
- **Generate a prime list and use two pointers:** Two pointers can find sums in the sorted prime list, but constructing that list still needs primality preprocessing and the direct complement scan is simpler here.
- **Scan all `x < n`:** Doing so produces reversed duplicates unless extra deduplication is added. Stopping at `n // 2` enforces `x <= y` directly.
- **`n < 4`:** Two primes cannot sum to these targets under the minimum prime value two, so the scan is empty and the answer is empty.
- **Odd `n`:** Since every prime except two is odd, an odd target can only use two as one member. The general scan handles that fact without a special branch.
- **Equal prime pair:** When `n` is twice a prime, the midpoint pair is legal and included once.
- **Indices zero and one remain true:** They are never queried by the pair scan, so this unconventional initialization does not create a false result.
- **Largest allowed target:** The linear table for `n <= 10^6` is practical, while checking every pair by repeated factorization would be considerably slower.
- **Output ordering:** Appending during the increasing `x` scan already satisfies the sort requirement; sorting again would be redundant.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log log n)$. Let `n` be the target. Initializing the Boolean list takes `O(n)` time and space. For each prime `p < n`, the inner loop marks about `n / p` multiples. The sum over primes is `O(n log log n)`, which dominates the initialization and the final `O(n)` half-range scan. The total time is therefore `O(n log log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
