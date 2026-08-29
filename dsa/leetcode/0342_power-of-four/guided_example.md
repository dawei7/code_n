# Guided Example: Power of Four

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1073741824}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return *`true` if it is a power of four. Otherwise, return `false`*.

The objective is to compute `true` from `{"n": 1073741824}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A power of four has one set bit in an even bit position.

Every nonnegative power of four can be rewritten as a power of two:

$$
4^x=(2^2)^x=2^{2x}.
$$

A positive power of two has a binary representation containing exactly one `1` bit. The exponent tells us the zero-based position of that bit. Because a power of four has exponent $2x$, its lone set bit is always at an even position: `0`, `2`, `4`, and so on.

For example:

$$
1=4^0=(1)_2
$$

has its set bit at position zero,

$$
4=4^1=(100)_2
$$

has it at position two, and

$$
16=4^2=(10000)_2
$$

has it at position four.

The exact source checks these two properties separately: first it proves `n` is a positive power of two, then it rejects the powers of two whose set bit is at an odd position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1073741824}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: First require positivity.

The expression begins with `n > 0`. Every $4^x$ relevant to an integer input is positive. A negative exponent would produce a non-integer fraction, and zero or a negative number cannot equal a power of the positive base four.

This check is also required for the one-set-bit trick. The value zero has no set bits, yet `0 & (0 - 1)` evaluates to zero in Python. Without the positivity condition, zero would be incorrectly treated as a power of two.

Python's `and` short-circuits from left to right. If `n` is nonpositive, later bit-mask expressions do not need to establish anything; the full result is immediately false.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use `n & (n - 1)` to demand exactly one set bit.

Subtracting one from a positive integer changes its rightmost `1` bit to `0` and changes all lower `0` bits to `1`. Taking a bitwise AND with the original number therefore clears the original number's rightmost set bit.

If `n` had exactly one set bit, clearing it leaves zero:

$$
n\mathbin{\&}(n-1)=0.
$$

For `n = 16`, the relevant binary values are

$$
10000_2
\quad\text{and}\quad
01111_2,
$$

whose AND is zero.

If `n` has two or more set bits, clearing only the rightmost one leaves at least one other `1`, so the AND is nonzero. For `n = 5`, binary `101`, subtracting one gives `100`, and their AND is `100`, not zero.

After the positivity and zero-AND checks, `n` is known to be $2^p$ for some nonnegative integer bit position $p$. It may still be a power of two that is not a power of four, such as `2`, `8`, or `32`. The mask performs that final distinction.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1073741824}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeated division by four:** While the positive value is divisible by four, divide it by four; accept only if the result reaches one. This is exact and easy to understand, but takes $O(\log_4 n)$ time and does not meet the constant-work follow-up.
- **Power-of-two test plus modulo three:** Even powers of two satisfy $2^{2x}\bmod3=1$, while odd powers satisfy $2^{2x+1}\bmod3=2$. Thus a positive power of two is a power of four exactly when `n % 3 == 1`. It is also constant time under fixed-width arithmetic.
- **Precomputed valid set:** Only sixteen powers from $4^0$ through $4^{15}$ fit in the signed 32-bit positive range. Membership in a constant set works but hides the bit-position structure.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The input is a fixed-width signed 32-bit integer. The source performs a constant number of comparisons, subtractions, and bitwise AND operations, each fixed-size. Its time complexity is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
