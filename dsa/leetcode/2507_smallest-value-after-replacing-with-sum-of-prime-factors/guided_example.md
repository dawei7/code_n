# Guided Example: Smallest Value After Replacing With Sum of Prime Factors

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 100000}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n`.

The objective is to compute `7` from `{"n": 100000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simulate the required transformation until it stops changing

For the current value, factor it into primes with multiplicity and add those primes. That sum becomes the next value. The method repeats until the factor sum equals the value it started that iteration with.

At the top of each outer iteration:

- `t` stores the current value before factorization;
- `n` is used as a shrinking residual during factorization;
- `s` accumulates the prime-factor sum;
- `i` is the trial divisor, beginning at two.

Saving `t` is essential because `n` is divided down and no longer represents the iteration's original value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 100000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extract every copy of a factor

For a candidate divisor `i`, the inner `while n%i==0` repeatedly:

1. divides one copy of `i` out of `n`;
2. adds `i` to `s`.

Repeated division handles multiplicity exactly. For 8:

$$
8=2\cdot2\cdot2,
$$

so the loop adds $2+2+2=6$, not merely one copy of 2.

Once `i` no longer divides the residual, the candidate increments by one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a candidate divisor `i`, the inner `while n%i==0` repeat... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why testing only through the square root is enough

The condition `i <= n//i` is an overflow-safe form of $i^2\le n$ for positive integers.

If a composite residual had no factor at most its square root, both factors in any decomposition would be greater than the square root, making their product greater than the residual. That is impossible. Therefore, after trial division ends, any residual `n>1` must be prime.

The code adds that final residual once with `s += n`.

Notice that `n` shrinks as factors are removed. The square-root boundary shrinks with it, which safely avoids testing divisors that can no longer be needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 100000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Precomputed smallest prime factors:** A sieve :** - **Precomputed smallest prime factors:** A sieve supports fast repeated factorizations but uses $O(n)$ preprocessing and memory.
- **Store a factor list:** It is unnecessary because only the sum is needed.
- **Prime input:** Its only prime factor is itself, so it is returned immediately.
- **Repeated prime factor:** Add it once per division, preserving multiplicity.
- **Value 4:** It is a composite fixed point and must return 4.
- **Final residual:** If greater than one, it is prime and must be added.
- **Shrinking residual:** The square-root condition must use the current residual, as the exact code does.
- **Overflow-safe test:** `i<=n//i` avoids computing `i*i` in fixed-width languages.
- **No increase:** The prime-factor sum cannot exceed the original composite value.
- **Termination:** A decreasing positive-integer sequence must eventually reach a fixed point.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(sqrt(n) log n)$. For one current value $x$, trial division performs at most $O(\sqrt{x})$ candidate checks in the worst case, with additional successful divisions bounded by $O(\log x)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
