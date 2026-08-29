# Guided Example: Count the Digits That Divide a Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 121}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `num`, return *the number of digits in `num` that divide *`num`.

The objective is to compute `2` from `{"num": 121}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Inspect every decimal digit as a separate occurrence

The answer counts digit positions, not distinct digit values. If digit 1 appears twice and divides the number, both occurrences contribute.

The method repeatedly removes the last decimal digit from a working copy while testing that digit against the unchanged original number.

Two variables keep these roles separate:

- `num` remains the original value used in every divisibility test;
- `x` is progressively shortened to expose its digits.

If the code divided `num` itself while extracting digits, later tests would use the wrong dividend.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 121}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use `divmod` to split quotient and last digit

For a positive integer `x`:

`divmod(x,10)`

returns:

- quotient $\lfloor x/10\rfloor$, which removes the final decimal digit;
- remainder `x%10`, which is that final digit.

The assignment

`x,val = divmod(x,10)`

updates the working number and names the extracted digit in one step.

For `x=1248`, successive iterations extract 8, 4, 2, and 1, while `x` becomes 124, 12, 1, and finally 0.

Digits are processed right to left, but their order does not affect a count.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Test the exact definition of divisibility

A nonzero digit `val` divides `num` exactly when the remainder is zero:

`num%val==0`.

Python represents this comparison as a Boolean. `true` behaves numerically as one and `false` as zero, so

`ans += num%val==0`

increments the count exactly for a dividing digit.

The constraint guarantees that no digit is zero. This matters because `num%0` would be undefined and raise an error. No zero guard is needed for valid inputs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 121}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **String iteration:** Convert `num` to text, convert each character back to an integer, and test divisibility; it is also $O(d)$ but allocates the string.
- **Repeated digit:** Count every occurrence separately.
- **Digit one:** It always divides the number.
- **Digit equal to `num`:** This occurs for one-digit input and always contributes.
- **Zero digit:** The contract excludes it; otherwise a guard would be mandatory before modulo.
- **Right-to-left processing:** Order is irrelevant because only the count is returned.
- **Preserve original `num`:** Divisibility must not be tested against the shrinking quotient.
- **Boolean arithmetic:** true adds one and false adds zero.
- **Largest input:** Ten extraction iterations suffice for $10^9$.
- **No floating point:** Decimal digits are obtained exactly with integer arithmetic.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $d$ be the number of decimal digits in `num`, so
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
