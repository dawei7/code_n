# Guided Example: Ugly Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 6}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An **ugly number** is a *positive* integer which does not have a prime factor other than 2, 3, and 5.

The objective is to compute `true` from `{"n": 6}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reject nonpositive values before division

The first condition is `if n < 1: return false`. Negative integers and zero are not positive, so they cannot be ugly.

This guard is also operationally essential for zero. Since `0 % 2 == 0` and `0 // 2 == 0`, entering the repeated-division loop with zero would never make progress. Rejecting it first prevents an infinite loop while matching the mathematical definition.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 6}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Remove the complete exponent of each permitted prime

For each `x` in `[2, 3, 5]`, the loop



keeps dividing until `x` is no longer a factor. One division would not be enough: a number such as `8 = 2 * 2 * 2` contains three copies of the factor `2`, and all three must be removed.

If the original positive number has prime factorization

$$
n=2^a3^b5^cR,
$$

where $R$ contains no factor `2`, `3`, or `5`, the three loops reduce it to exactly $R$. The exponents $a$, $b$, and $c$ may be zero, in which case the corresponding inner loop performs no division.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the final comparison is sufficient

By the fundamental theorem of arithmetic, every positive integer has a unique prime factorization. After every permitted prime factor has been divided away, two cases remain:

- If the residual value is `1`, there is no unpermitted prime factor. The original number consisted only of powers of `2`, `3`, and `5`, so it is ugly.
- If the residual value is greater than `1`, its prime factorization contains at least one prime other than `2`, `3`, or `5`. The original number is not ugly.

The return statement `n == 1` expresses exactly this distinction.

The order `2`, then `3`, then `5` is convenient but not required for correctness. Prime factors commute under multiplication, and dividing by one permitted prime does not create a new copy of another that was previously absent. Any order that exhausts all three would leave the same residual factor.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 6}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prime-factorize by testing every divisor:** General trial division can discover all prime factors but may take $O(\sqrt n)$ time. Only three allowed primes matter here, so testing anything else is unnecessary.
- **Recursive division:** Recursively divide by an allowed factor until reaching one or failure. It can be correct but uses $O(\log n)$ call-stack space instead of the loop's constant space.
- **Repeated greatest common divisor:** Divide by `gcd(n, 30)` until no progress. Since `30 = 2 * 3 * 5`, this removes allowed factors in batches, but it is less direct than the three simple loops.
- **`n = 1`:** It is positive and has no forbidden prime factor, so it is correctly accepted.
- **`n = 0`:** It must be rejected before division; otherwise repeated divisibility by every factor would never change it.
- **Negative input:** Ugly numbers are defined as positive, so sign handling is not a factorization question and the method rejects immediately.
- **A pure allowed prime power:** Values such as `2^k`, `3^k`, or `5^k` reduce fully to one and are accepted.
- **A permitted product with repeated factors:** The `while` loops, rather than single `if` statements, remove every copy.
- **A forbidden prime alone:** No allowed loop changes it, so the final residual exposes it directly.
- **Mixed allowed and forbidden factors:** Allowed factors are removed, leaving the forbidden portion greater than one and producing `false`.
- **Largest 32-bit values:** The loops never multiply, so there is no overflow risk; division only reduces magnitude.
- **Order of allowed factors:** Changing `[2, 3, 5]` to another ordering leaves the same residual because prime factorization is unique.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$. Let $N$ be the original positive input. Every successful inner-loop iteration divides the current value by at least two. If there are $k$ successful divisions in total, then $2^k\le N$, so $k\le\log_2N$. The three outer iterations add only a constant number of failed divisibility checks. Total time is $O(\log N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
