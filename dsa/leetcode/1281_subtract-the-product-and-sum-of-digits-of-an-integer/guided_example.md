# Guided Example: Subtract the Product and Sum of Digits of an Integer

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4421}`
- **Required output:** `21`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer number `n`, return the difference between the product of its digits and the sum of its digits.

The objective is to compute `21` from `{"n": 4421}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Process decimal digits with quotient and remainder

For a positive integer `n`, division by ten separates its final decimal digit from the remaining prefix. Python's `divmod(n, 10)` returns both results: the quotient is `n // 10` and the remainder is `n % 10`.

The assignment `n, v = divmod(n, 10)` replaces `n` with the unprocessed prefix and stores the removed digit in `v`. Repeating this until `n` becomes zero visits every decimal digit exactly once, from right to left.

Digit order does not matter for either addition or multiplication, so processing the least significant digit first gives the same final product and sum as reading left to right.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4421}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Choose the correct identities for both accumulators

Variable `x` stores the product of digits processed so far and begins at one, the multiplicative identity. If it began at zero, every product would remain zero regardless of the digits.

Variable `y` stores the sum and begins at zero, the additive identity. For every extracted digit `v`, the code performs `x *= v` and `y += v`.

After processing `234`, the extraction order is four, three, two. The product evolves from one to four, twelve, and twenty-four. The sum evolves from zero to four, seven, and nine. Returning `x - y` gives fifteen.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A loop invariant explains correctness

Before each iteration, `x` equals the product of all digits already removed from the original number, `y` equals their sum, and current `n` contains exactly the digits not yet processed. `divmod` removes one more digit. Multiplying and adding it preserve the invariant for the next iteration.

Because the input is positive, repeated quotient division by ten eventually makes `n` zero after all digits have been removed. At loop exit, `x` is the product of every original digit and `y` is their sum. Their difference is exactly the requested result.

The method modifies only its local parameter variable. Python integers are immutable values, so the caller's integer is not changed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `21` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4421}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `21` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Convert to a string:** Iterate through decimal characters and convert each with `int`. It is clear but allocates an $O(d)$ string representation.
- **Separate product and sum passes:** Extracting digits twice repeats work; both aggregates can be updated in one traversal.
- **Initialize product to zero:** This is incorrect because zero annihilates every multiplication; the identity must be one.
- **Single-digit input:** Product and sum equal that digit, so the answer is zero.
- **Contains a zero digit:** The product becomes zero while the sum continues accumulating all other digits.
- **Repeated digits:** Each occurrence is extracted and contributes independently.
- **Positive-input guarantee:** The exact loop assumes at least one digit is processed; zero is outside the contract.
- **Negative input:** Signs and remainder behavior would require separate handling and are not allowed.
- **Local mutation of `n`:** Replacing the parameter with successive quotients is safe because no later step needs the original whole value.
- **Result may be negative:** The task asks for product minus sum and does not require a nonnegative answer.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $d=\lfloor\log_{10}n\rfloor+1$ be the number of decimal digits. Every iteration removes one digit, so there are exactly $d$ iterations. Each performs constant-time arithmetic in the conventional bounded-integer model, giving $O(d)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
