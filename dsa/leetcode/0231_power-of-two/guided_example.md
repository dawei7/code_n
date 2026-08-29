# Guided Example: Power of Two

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

The objective is to compute `true` from `{"n": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A positive power of two has exactly one set bit

The binary representation of $2^x$ contains one `1` followed by $x$ zeros.
For example, 1 is `0001`, 2 is `0010`, 4 is `0100`, and 8 is `1000`.
Conversely, every positive integer with exactly one `1` bit has value $2^x$,
where $x$ is that bit's zero-based position.

The problem can therefore be reduced from repeated arithmetic division to a
constant-number bit test: determine whether positive `n` has exactly one set
bit.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Subtracting one changes the least significant set bit and everything below it

Consider a positive binary number and locate its rightmost `1`. All bits to its
right are zero by definition. Subtracting one changes that rightmost `1` to
zero and changes all lower zeros to ones. Bits to the left remain unchanged.

For example:

`n     = 1011000`

`n - 1 = 1010111`

The rightmost set bit of `n` is cleared in `n - 1`. Lower positions are one in
`n - 1` but zero in `n`. When the two numbers are combined with bitwise AND,
all those positions become zero. Higher set bits, if any, are one in both
numbers and remain set. Thus `n & (n - 1)` clears exactly the rightmost set bit
of `n`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Clearing the only set bit distinguishes powers of two

If `n` is a positive power of two, it has one set bit. Clearing that bit leaves
zero, so `(n & (n - 1)) == 0` is true.

If positive `n` is not a power of two, it has at least two set bits. The AND
operation clears the rightmost one but leaves at least one higher set bit, so
the result is nonzero. This makes the zero comparison both necessary and
sufficient for positive integers.

For `n = 16`, binary `10000` is ANDed with `01111`, producing zero. For
`n = 12`, binary `1100` is ANDed with `1011`, producing `1000`, so the method
returns false.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Isolate the lowest set bit:** For positive `n`, `n & -n` equals `n` exactly when `n` has one set bit. It is another constant-operation identity based on two's-complement negation.
- **Repeated division by two:** Reject nonpositive input, repeatedly divide even values by 2, and test whether the result reaches 1. It is intuitive but takes $O(\log n)$ time and does not satisfy the no-loop follow-up.
- **Count set bits:** Count ones in the binary representation and test for exactly one. Built-in or iterative counting expresses the criterion but does more work than clearing one bit.
- **Floating-point logarithm:** Test whether $\log_2 n$ is integral. Floating-point rounding near representational boundaries can cause errors, so an exact bit identity is preferable.
- **`n = 0`:** The positivity guard is essential because the bit expression by itself equals zero.
- **`n = 1`:** This is $2^0$ and is accepted even though no trailing zero bits are present.
- **Negative values:** They fail `n > 0` immediately; powers of two in this problem are positive.
- **Largest positive 32-bit power:** $2^{30}$ has one set bit and passes. $2^{31}$ lies outside the signed upper bound.
- **One more or less than a power:** Adding or subtracting one generally creates several set bits, and the AND result remains nonzero.
- **No mutation:** `n` is an immutable integer, and the expression creates only temporary numeric results.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Under the problem's fixed signed 32-bit input domain, subtraction, bitwise AND,
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
