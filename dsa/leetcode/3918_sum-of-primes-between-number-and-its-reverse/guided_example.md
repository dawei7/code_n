# Guided Example: Sum of Primes Between Number and Its Reverse

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000}`
- **Required output:** `76127`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`.

The objective is to compute `76127` from `{"n": 1000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reversing the decimal digits

The source converts `n` to a string, reverses that string with `[::-1]`, and converts it back to an integer.

Converting back naturally removes leading zeros created by reversal. For example:



Thus the reversed integer is 1, exactly as the mathematical decimal reversal requires.

A one-digit input reverses to itself.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the fixed sieve reaches every possible endpoint

The original number satisfies $1\le n\le1000$. Reversing any number in this range cannot produce a value above 1000:

- inputs below 1000 have at most three digits, so their reverse is at most 999;
- 1000 reverses to 1.

Therefore both interval endpoints lie within the precomputed `is_prime[0..1000]` table.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the sieve marks composites

The table begins by assuming every value is prime, then explicitly marks 0 and 1 false.

For each $i$ from 2 through $\lfloor\sqrt{1000}\rfloor$, the source acts only if `is_prime[i]` is still true. It marks

$$
i^2,\ i^2+i,\ i^2+2i,\ldots
$$

as composite.

Starting at $i^2$ is sufficient. Any smaller multiple $i\cdot q$ has $q<i$ and was already handled through a smaller prime factor. Every composite number at most 1000 has at least one prime factor no larger than its square root, so every composite is eventually marked.

Every number that remains true is prime.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `76127` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `76127` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Trial division per candidate:** Test each interval value up to its square root. This avoids a table but repeats factor work and is slower across many candidates.
- **Prime prefix sums:** Precompute cumulative prime totals and return `prefix[U] - prefix[L - 1]` in constant query time, using the same $O(B)$ storage.
- **Dynamic sieve to \(U\):** This matches the manifest description but repeats setup per independent call unless cached.
- **Trailing zeros in \(n\):** They become leading zeros in the reversed string and disappear during integer conversion.
- **One-digit input:** Its reverse is identical, so only that singleton interval is tested.
- **Prime singleton interval:** If $n=r$ and the value is prime, it is included once.
- **Composite singleton interval:** The result is zero.
- **Interval containing 0 or 1:** Neither is prime; the sieve explicitly marks both false.
- **Inclusive endpoints:** A prime equal to $n$ or its reverse contributes.
- **No primes in the interval:** Summing the filtered generator returns zero.
- **Fixed-ceiling dependency:** Raising the input constraint above 1000 without expanding the global table could cause missing entries or an index error.
- **Input preservation:** Integers are immutable, and the method does not modify external state beyond reading the shared sieve.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B)$. The checked-in source performs its sieve globally with fixed bound
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
