# Guided Example: Add Digits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 38}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

The objective is to compute `2` from `{"num": 38}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why digit sums preserve modulo 9

Write a nonnegative decimal integer using digits $d_0,d_1,\ldots,d_k$:

$$
n=d_0+d_1\cdot10+d_2\cdot10^2+\cdots+d_k\cdot10^k.
$$

Because $10\equiv1\pmod9$, every power of ten also satisfies

$$
10^i\equiv1^i\equiv1\pmod9.
$$

Taking the decimal expansion modulo 9 therefore gives

$$
n\equiv d_0+d_1+d_2+\cdots+d_k\pmod9.
$$

So replacing a number by the sum of its digits does not change its remainder modulo 9. Applying the operation repeatedly preserves that same remainder at every stage, including the final one-digit result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 38}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Which one-digit value represents each remainder

For a positive input, the final digital root must be one of `1` through `9`. These nine values represent the nine remainder classes modulo 9:

| Remainder modulo 9 | Positive digital root |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |
| 7 | 7 |
| 8 | 8 |
| 0 | 9 |

The last row is the subtle one. A positive multiple of 9 has remainder zero, but its repeated digit sum cannot end at `0`: sums of the digits of a positive integer remain positive. Its correct digital root is `9`. The number zero itself is different; it begins and ends at `0`.

That gives the piecewise rule

$$
\operatorname{dr}(n)=
\begin{cases}
0,&n=0,\\
9,&n>0\text{ and }n\equiv0\pmod9,\\
n\bmod9,&\text{otherwise}.
\end{cases}
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the compact formula merges the positive cases

For a positive number, the source computes



Subtracting one shifts the positive range `1..9` to the zero-based range `0..8`. Modulo 9 then cycles every positive integer into that range, and adding one shifts the result back to `1..9`.

If `num` is not divisible by 9, this expression returns its ordinary remainder. For example, `38 - 1 = 37`, `37 % 9 = 1`, and adding one yields `2`.

If `num` is a positive multiple of 9, then `num - 1` has remainder `8`; adding one produces `9`, exactly handling the otherwise awkward zero-remainder case. For `18`, the calculation is `(18 - 1) % 9 + 1 = 17 % 9 + 1 = 8 + 1 = 9`.

Zero must remain a separate branch. Applying the positive formula to zero in Python would evaluate `(-1) % 9 + 1` as `8 + 1 = 9`, which is incorrect. The conditional `0 if num == 0 else ...` returns the required `0` before using the formula.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 38}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Direct digit-sum simulation:** Repeatedly extract digits with `% 10` and `// 10` until one digit remains. It is easy to discover but uses loops and takes time proportional to the digits processed, missing the constant-time follow-up.
- **String conversion:** Convert the number to text and sum converted characters repeatedly. This is more allocation-heavy and still iterative.
- **Three-branch modulo formula:** Return `0` for zero, `9` for positive multiples of 9, and `num % 9` otherwise. It is equivalent to the exact compact expression but uses an additional explicit case.
- **`num = 0`:** This is the only input whose digital root is zero. It must be handled before the positive formula.
- **Positive multiple of 9:** The result is `9`, not `0`; subtracting one before modulo encodes this distinction.
- **Already one digit:** Values `1` through `9` map to themselves, while zero is handled separately.
- **Largest permitted input:** The formula uses only bounded integer arithmetic and does not depend on how many decimal digits the value contains.
- **Nonnegative-input assumption:** The mathematical digital root can be extended to negatives with a chosen convention, but the source and contract define only `num >= 0`.
- **Decimal-base dependency:** Modulo 9 appears because $10\equiv1\pmod9$. In base $b$, the analogous positive digital-root formula uses modulo $b-1$.
- **Divisibility intuition:** The familiar rule “a number is divisible by 9 exactly when its digit sum is divisible by 9” is a consequence of the same congruence used here.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The implementation performs one equality check and, for a positive input, one subtraction, one modulo operation, and one addition. The number of operations does not depend on the number of decimal digits, so under the fixed-width integer model and the stated 32-bit input bound, time complexity is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
