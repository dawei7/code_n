# Guided Example: Double Modular Exponentiation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"variables": [[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], "target": 2}`
- **Required output:** `[0, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** 2D array `variables` where $\text{variables}[i] = [a_{i}, b_{i}, c_{i}, m_{i}]$, and an integer `target`.

The objective is to compute `[0, 2]` from `{"variables": [[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], "target": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Respect the two separate modular powers

For each row `[a, b, c, m]`, the required value has a nested definition: first compute $a^b$ modulo $10$, then raise that remainder to the power $c$ and take the result modulo $m$. The modulus $10$ belongs only to the inner exponentiation. It is not valid to combine the exponents into $a^{bc}$ and apply both moduli afterward, because modular reduction changes the base used by the outer power.

The implementation mirrors the mathematical order exactly:

`pow(pow(a, b, 10), c, m)`

Python’s three-argument `pow(base, exponent, modulus)` calculates modular exponentiation without first constructing the enormous ordinary power. The inner call returns a value from zero through nine. The outer call uses that small remainder as its base and returns a value from zero through `m - 1`.

The list comprehension uses `enumerate(variables)` so that each row is processed together with its original zero-based index `i`. If the nested result equals `target`, that index is included in the returned list. Because `enumerate` scans in input order, the qualifying indices automatically appear in increasing order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"variables": [[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], "target": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why modular exponentiation avoids huge integers

A direct evaluation of `a ** b` can have a number of digits proportional to $b$, even though only its last decimal digit is needed. Repeated-squaring modular exponentiation instead maintains a running result and a current base, reducing both modulo the requested modulus after every multiplication.

At a conceptual level, write the exponent in binary. While exponent bits remain, if the current low bit is one, multiply the running result by the current base modulo the modulus. Square the base modulo the modulus and move to the next exponent bit. Each step halves the remaining exponent, so only logarithmically many steps are necessary. Python performs this internally in `pow`.

The same reasoning applies to the outer power. Even though its base is already below ten, `base ** c` may still be astronomically large. The three-argument outer `pow` keeps only residues modulo `m` throughout.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A direct evaluation of `a ** b` can have a number of digits ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the nested calculation is exact

Modular arithmetic guarantees that replacing a base by its residue preserves the result under further multiplication with the same modulus: if $x \equiv y \pmod q$, then $x^e \equiv y^e \pmod q$. This is why the inner call can reduce after every multiplication and still produce exactly $a^b \bmod 10$. Applying the analogous argument to the outer call produces exactly

$$
\left(a^b \bmod 10\right)^c \bmod m.
$$

Notice that the outer modulus is generally different from ten. The inner result is an actual integer in $[0,9]$, and the outer exponentiation starts from that integer. One must not replace the inner calculation with `pow(a, b, m)`, because that asks a different modular question.

For example, for `[3, 4, 2, 5]`, the inner value is `pow(3, 4, 10) = 1` because $3^4 = 81$. The outer value is then `pow(1, 2, 5) = 1`. Computing $3^{4\cdot2} \bmod 5$ happens to give one here, but that coincidence is not an identity and cannot justify exponent multiplication.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"variables": [[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], "target": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Ordinary exponentiation first:** Computing `(a:** - **Ordinary exponentiation first:** Computing `(a ** b % 10) ** c % m` is mathematically correct but may allocate integers with an enormous number of digits before reducing them.
- **Multiplying exponents:** Replacing the expression with `pow(a, b * c, m)` is generally wrong because the required inner reduction modulo ten occurs before the outer exponentiation.
- **Cycle tables for last digits:** Powers modulo ten are periodic, so the inner stage can be implemented with cases. Built-in modular exponentiation is clearer and already logarithmic.
- **Manual repeated squaring:** It gives the same asymptotic behavior and can be educational, but Python’s three-argument `pow` is optimized and expresses the intent directly.
- **Inner result zero:** The outer power is still handled exactly by `pow`, including the exponent rules defined for the valid input domain.
- **Modulus one:** Every outer result is zero because all integers are congruent to zero modulo one; only a zero target can match.
- **Repeated qualifying rows:** Each row contributes its own index. Equal data does not cause deduplication.
- **No qualifying rows:** The comprehension naturally returns an empty list.
- **Index order:** Sorting variables or results by value would break the required original indices; `enumerate` preserves input order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V(\log B+\log C)$. Let $V$ be the number of rows. For a row `[a, b, c, m]`, repeated-squaring modular exponentiation uses $O(\log b)$ multiplication stages for the inner call and $O(\log c)$ stages for the outer call. Under the usual word-arithmetic model for bounded problem integers, the total time is
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
