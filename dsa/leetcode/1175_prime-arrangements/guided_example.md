# Guided Example: Prime Arrangements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5}`
- **Required output:** `12`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Return the number of permutations of 1 to `n` so that prime numbers are at prime indices (1-indexed.)

The objective is to compute `12` from `{"n": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count prime values and prime positions

The values being permuted are the integers one through `n`. The valid indices are also one through `n`. Therefore, the number of prime values is exactly the same as the number of prime-indexed positions.

Let that count be `p`. Every valid permutation must place the `p` prime values into the `p` prime positions, and every nonprime value into one of the remaining `n - p` nonprime positions.

The exact identities of the primes matter only when arranging them within their allowed positions; first the algorithm needs their count.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count primes with a sieve

The helper creates `primes = [true] * (n + 1)`. Indices represent integers. Although entries zero and one remain true, the loop begins at two, so neither is ever counted as prime.

For each `i` from two through `n`:

- if `primes[i]` is still true, no smaller prime marked it as a multiple, so `i` is prime and `cnt` increases;
- every multiple `2i, 3i, ...` through `n` is marked false.

Any composite number has a prime divisor smaller than itself. When that divisor is processed, the composite is marked before its own iteration. Conversely, no prime is a multiple of a smaller integer greater than one, so it remains true and is counted.

The sieve starts marking at `i + i` rather than `i * i`. Starting at the square would avoid revisiting multiples already handled by smaller primes, but both versions are correct and have the conventional sieve bound.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Arrange primes only among prime indices

There are `p!` bijections from the `p` distinct prime values to the `p` prime positions.

After those choices, the `n - p` distinct nonprime values, including one, can be arranged among the remaining positions in `(n - p)!` ways.

The two choices are independent. For every prime placement, every nonprime placement completes one unique valid permutation. The product is therefore

`p! * (n - p)!`.

There is no binomial factor for choosing which positions are prime positions because those indices are fixed by the numbers one through `n`. Likewise, prime values cannot be assigned to nonprime positions in a valid arrangement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `12` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `12` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Trial division for every integer:** Testing divisors up to each square root is simple but slower than a sieve when counting all primes through `n`.
- **Start sieve marking at `i * i`:** Smaller multiples were already marked by smaller prime factors, so this standard optimization reduces repeated work without changing the result.
- **Hard-code the prime count up to 100:** The domain is small enough, but a sieve derives the answer transparently and generalizes naturally.
- **Choose prime positions with a binomial coefficient:** Prime-index positions are predetermined; there is no choice of position subset, so such a factor would overcount.
- **Treat one as prime:** This changes both factorial group sizes and produces incorrect arrangements. The loop correctly starts at two.
- **`n = 1`:** There are zero primes and one nonprime. `0! * 1! = 1`, representing the sole permutation.
- **No primes in the range:** The zero factorial is one, so all values arrange within the nonprime positions as expected.
- **Modulo timing:** Python safely computes the exact product first for `n <= 100`. Fixed-width implementations should reduce during multiplication.
- **Distinct values:** The integers one through `n` are all distinct, which is why ordinary factorials count placements.
- **Prime count equals prime-position count:** Both are defined over the identical range one through `n`, enabling the direct partition.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log\log n)$. The sieve marks multiples of each discovered prime. The total conventional work is `O(n log log n)`. Counting and factorial computation add `O(n)` arithmetic steps, so the sieve term gives the stated time bound.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
