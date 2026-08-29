# Guided Example: Bitwise AND of Numbers Range

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"left": 5, "right": 7}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integers `left` and `right` that represent the range `[left, right]`, return *the bitwise AND of all numbers in this range, inclusive*.

The objective is to compute `4` from `{"left": 5, "right": 7}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Find which bit positions can survive a whole range

Bitwise AND keeps a 1 at a position only when every number in the inclusive
range has a 1 there. If even one number has zero at that position, the final
bit is zero.

Binary representations of `left` and `right` share some high-order prefix. At
their highest differing position, `left` has 0 and `right` has 1. The range
crosses that binary boundary, so that position and every less significant
position vary somewhere across the interval. null of those suffix positions
can be guaranteed 1. Only the common high-order prefix can survive, followed by
zeros.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"left": 5, "right": 7}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Clear the right endpoint's least significant 1-bit

The update `right &= right - 1` is Brian Kernighan's bit-clearing identity.
Subtracting one changes the least significant 1-bit of `right` to zero and
changes lower trailing zeros to ones. AND with the original clears the chosen
1 and also clears those newly introduced lower ones, while preserving every
higher bit.

For example, `1101000 - 1` is `1100111`, and their AND is `1100000`. Exactly
the rightmost set bit of the original value disappears.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Continue while the candidate is above `left`

The current `right` is always the original upper endpoint with some low 1-bits
cleared. While it remains greater than `left`, it still contains a set bit in
the suffix where the range's binary values vary. Such a bit cannot survive the
AND of every range value, so clearing it is safe.

The loop stops once the transformed value is less than or equal to `left`. It
need not become exactly equal. For `[5,6]`, binary endpoints are `101` and
`110`; clearing 6's lowest 1 gives `100`, which is 4, below 5. That value is
also `5 & 6`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"left": 5, "right": 7}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Common-prefix shifts:** Shift both endpoints right until equal, count shifts, then restore the prefix with a left shift.
- **Brute-force range AND:** Correct but proportional to `right - left + 1`, which is infeasible for wide intervals.
- **Highest-difference mask:** Find the most significant differing endpoint bit and clear that bit and everything below in one calculation.
- **Equal endpoints:** Return the endpoint unchanged.
- **Range beginning at zero:** Return zero after all upper set bits are cleared.
- **Crossing a power of two:** The high prefix may become zero, making the whole result zero.
- **Narrow range:** Only a few suffix bits may need clearing.
- **Maximum endpoint:** Still at most 31 clearing iterations under the contract.
- **Nonnegative guarantee:** Ensures monotonic finite bit-clearing behavior.
- **Common-prefix bit:** The stopping condition prevents it from being cleared.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log right)$. Let $b$ be the bit width of `right`, so $b = O(\log(right+1))$. Each iteration
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
