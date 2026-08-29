# Guided Example: Count Prime-Gap Balanced Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3], "k": 1}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`.

The objective is to compute `2` from `{"nums": [1, 2, 3], "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Prime preprocessing

A Sieve of Eratosthenes marks primality through `max(nums)`. Zero and one are nonprime. For each prime factor through its square root, multiples beginning at its square are cleared.

The required variable `zelmoricad` stores `(nums,k)` midway in the function. It does not participate in the algorithm afterward.

The source then records parallel arrays:

- `prime_positions[t]`: original index of the t-th prime occurrence;
- `prime_values[t]`: its numeric prime value.

Repeated equal primes remain separate occurrences because their positions create different subarrays.

If fewer than two prime occurrences exist, no qualifying subarray is possible and zero is returned.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3], "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Valid windows in prime-occurrence order

A subarray’s prime occurrences are consecutive in the compressed arrays. For a fixed rightmost prime occurrence `right`, the source maintains the smallest `left` such that:

`max(prime_values[left:right+1]) - min(...) <= k`.

The minimum deque stores indices in increasing value order; the maximum deque stores decreasing value order. Their fronts reveal current extrema.

When a new prime enters, worse candidates are removed from each back. While the value gap exceeds `k`, `left` advances and a deque front is removed if it is exactly the departing index.

Each compressed index enters and leaves each deque at most once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every later first prime is also valid

Once prime window `[left,right]` satisfies the gap, dropping primes from its left cannot increase max-minus-min. Therefore every first-prime choice `t` from `left` through `right-1` forms a valid prime set ending at `right`.

Any `t<left` is invalid by minimality of the sliding boundary. This makes valid first-prime indices one continuous range.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3], "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all subarrays:** Maintaining prime extrema incrementally still gives `O(n^2)` time.
- **Balanced multiset over primes:** It can maintain extrema in `O(\log n)` per move, but monotonic deques exploit one-way sliding for linear work.
- **Prefix prime counts only:** Counts can enforce at least two primes but cannot maintain prime-value minimum and maximum alone.
- **No primes or one prime:** Immediate zero is correct.
- **Exactly two primes:** The window contributes when their numeric difference is at most `k`, multiplied by surrounding nonprime boundary choices.
- **Repeated equal primes:** Their gap is zero, so they are compatible even when `k=0`.
- **k equals zero:** All primes in a counted subarray must have the same numeric value.
- **Leading nonprimes:** The first left gap includes starts from index zero.
- **Trailing nonprimes:** The final right gap includes ends through index `n-1`.
- **Nonprime between primes:** It changes boundary distances but not prime extrema.
- **Future invalid prime:** Shrinking may discard several earlier prime occurrences until the extrema gap is restored.
- **Required variable:** `zelmoricad` is deliberately inert; it satisfies the explicit storage instruction without altering state.
- **Large count:** Python integers hold the result; the problem does not request a modulus.
- **Prime occurrence versus distinct prime:** The “at least two” condition counts occurrences, so two equal prime elements qualify.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V)$. Let `V=max(nums)`. The sieve costs `O(V\log\log V)` time and `O(V)` space.
- **Auxiliary Space Complexity:** $O(V + n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
