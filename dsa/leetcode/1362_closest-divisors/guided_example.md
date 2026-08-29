# Guided Example: Closest Divisors

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 123}`
- **Required output:** `[5, 25]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `num`, find the closest two integers in absolute difference whose product equals $num + 1$ or $num + 2$.

The objective is to compute `[5, 25]` from `{"num": 123}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the square root is the right starting point

For positive `x`, any factor pair can be written as `(a, x // a)` with `a <= x // a`. The smaller factor then satisfies `a <= sqrt(x)`.

As `a` grows toward `sqrt(x)`, its paired factor `x / a` decreases toward the same value, reducing their difference. Therefore, among divisors no greater than the square root, the largest divisor produces the closest factor pair.

More explicitly, for real `a` in the interval from one through `sqrt(x)`, the difference is `x / a - a`. Increasing `a` makes the first term smaller and the second subtracted term larger, so the difference strictly decreases. Restricting `a` to actual integer divisors does not change that monotonic direction. The largest eligible divisor is therefore optimal.

The helper initializes its loop at `int(sqrt(x))` and checks values downward. The first `i` satisfying `x % i == 0` is the largest divisor at or below the square root. It returns `[i, x // i]`.

The loop always succeeds because one divides every positive integer. Prime values simply fall all the way to `i = 1` and return one with the number itself.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 123}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Evaluate both permitted products

`a = f(num + 1)` finds the closest pair for the first candidate product. `b = f(num + 2)` does the same for the second.

The final conditional compares `abs(a[0] - a[1])` with the corresponding difference for `b`. It returns `a` only when its difference is strictly smaller; otherwise it returns `b`.

If the two best differences tie, either pair is globally optimal because the problem only minimizes the absolute difference and allows the factors in any order. Choosing `b` on a tie is therefore valid.

For `num = 8`, the first product is nine. Starting at three immediately finds `3 * 3` with difference zero. The second product is ten; its closest pair is two and five with difference three. The method selects three and three.

For `num = 123`, the candidates are 124 and 125. The downward search for 124 finds four and thirty-one. The search for 125 finds five and twenty-five. Their differences are twenty-seven and twenty, so the method returns five and twenty-five.

The helper performs a fresh square-root search for each candidate. It cannot reuse the first factorization directly because consecutive integers may have completely different divisor structures.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why separate local optima give the global optimum

Every valid answer belongs to exactly one of the two product choices. For each product, `f` returns the minimum-difference pair by choosing its largest divisor no greater than the square root. Comparing those two local minimum differences therefore selects the minimum across the entire allowed answer set.

The returned pair’s product is exact because the helper checks divisibility before using integer quotient. No floating approximate factor is returned.

The final strict comparison does not attempt another tie-break such as smaller factors or preferring `num + 1`. null is required by the contract. Returning the second pair on equality remains globally optimal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[5, 25]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 123}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[5, 25]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Exact integer square root:** Start from `isqrt(x)`. It preserves the same search and complexity while avoiding floating rounding.
- **Scan upward from one:** It eventually finds all divisors but does not know the closest pair until reaching the square-root region.
- **Enumerate every factor pair:** Correct but unnecessary; the first divisor found in the downward search is already optimal for that product.
- **Prime candidate product:** The helper returns one and the prime.
- **Perfect square:** The square root divides exactly, producing equal factors and difference zero, the best possible.
- **Tie between products:** The source returns the `num + 2` pair because the comparison is strict; either tied pair satisfies the problem.
- **Return order:** The helper returns the smaller factor first, although the contract accepts either order.
- **Large `num`:** Only about the square root number of modulus tests are needed, not a scan through the product itself.
- **Guaranteed positive products:** Since `num >= 1`, both candidates are positive and divisor one always exists.
- **Floating start point:** The current constraints make it safe in practice, while `isqrt` is the robust general choice.
- **Candidate values differ by one:** Being numerically close does not imply their best factor gaps are close; both must be searched independently.
- **First successful divisor:** Continuing farther downward would only decrease the smaller factor and increase its partner, producing a larger gap.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\sqrt{\texttt{num}})$. For an input `x`, the helper examines at most $\lfloor\sqrt{x}\rfloor$ candidate divisors. It is called for `num + 1` and `num + 2`, so total time is $O(\sqrt{\texttt{num}})$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
