# Guided Example: GCD of Odd and Even Sums

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000}`
- **Required output:** `1000`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`. Your task is to compute the **GCD** (greatest common divisor) of two values:

The objective is to compute `1000` from `{"n": 1000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace both sequences with closed forms

The smallest `n` positive odd numbers are

`1, 3, 5, ..., 2n - 1`.

Their sum is `n^2`. One way to derive this is with the arithmetic-series formula: there are `n` terms, the first is one, and the last is `2n - 1`, so

`sumOdd = n(1 + 2n - 1) / 2 = n * 2n / 2 = n^2`.

There is also a geometric identity: adding the next odd number grows one square into the next square,

`1 = 1^2`,

`1 + 3 = 2^2`,

`1 + 3 + 5 = 3^2`,

and so on.

The smallest `n` positive even numbers are

`2, 4, 6, ..., 2n`.

Factoring out two gives

`sumEven = 2(1 + 2 + ... + n)`.

Since `1 + 2 + ... + n = n(n + 1)/2`,

`sumEven = n(n + 1)`.

The requested value is therefore

`gcd(n^2, n(n + 1))`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Factor out the common `n`

Both numbers contain a factor of `n`:

`n^2 = n * n`

and

`n(n + 1) = n * (n + 1)`.

For positive `n`,

`gcd(n * a, n * b) = n * gcd(a, b)`.

Applying this identity gives

`gcd(n^2, n(n + 1)) = n * gcd(n, n + 1)`.

The problem is now reduced to the GCD of two consecutive integers.

The common-factor identity is exact because every common divisor of `a` and `b` becomes `n` times as large after both numbers are multiplied by `n`. Conversely, after removing the shared factor `n` from any greatest common divisor of `na` and `nb`, the remaining factor must divide both `a` and `b`. Thus factoring does not merely find one common divisor; it preserves the greatest one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why consecutive integers are coprime

Suppose a positive integer `d` divides both `n` and `n + 1`. A divisor of two numbers also divides their difference, so `d` must divide

`(n + 1) - n = 1`.

The only positive divisor of one is one. Therefore

`gcd(n, n + 1) = 1`.

Substituting this result gives

`gcd(n^2, n(n + 1)) = n * 1 = n`.

That is why the exact Optimal source can immediately return `n`. It is not skipping a computation that still depends on the input’s digits; the algebra proves that the requested GCD equals the input for every allowed positive `n`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1000` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1000` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Euclidean algorithm on the closed forms:** Compute `gcd(n^2, n(n + 1))` in `O(log n)` time. It is correct but slower and less specialized than returning the proven result.
- **Sum both sequences explicitly:** This takes `O(n)` time and adds unnecessary loop state.
- **Use arithmetic-series formulas only:** Computing both sums in `O(1)` and passing them to a library GCD is acceptable, but the remaining GCD also has a closed form.
- **Forget the common factor:** The factorization by `n` is what exposes consecutive integers and makes the final simplification possible.
- **Assume consecutive integers are coprime without explanation:** Their only common divisor must divide their difference one, which supplies the needed reason.
- **`n = 1`:** The first odd and even sums are one and two; the answer remains `n`.
- **Largest allowed `n`:** Returning `n` avoids constructing squared intermediate values and remains constant-time.
- **Positive-input guarantee:** Factoring the GCD as `n * gcd(n, n+1)` uses positive `n`. The constraints exclude zero and negative inputs.
- **Different sequence definitions:** The result `n` is specific to these exact first-`n` odd and even sums and should not be generalized blindly.
- **Input preservation:** The integer argument is immutable and no external state is changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The source performs one return operation and no arithmetic loop, recursion, allocation, or GCD computation. Its time complexity is `O(1)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
