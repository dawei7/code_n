# Guided Example: Single Number II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 2, 3, 2]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` where every element appears **three times** except for one, which appears **exactly once**. *Find the single element and return it*.

The objective is to compute `3` from `{"nums": [2, 2, 3, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count each bit modulo three

Ordinary XOR solves the version where every repeated value appears twice because XOR is addition modulo two at each bit. Here repeated values occur three times, so pairs do not cancel. The corresponding idea is to count ones at each bit position and keep the remainder modulo three.

Consider a fixed bit position `i`. Every tripled value contributes either:

- three zero bits, adding zero; or
- three one bits, adding three.

Both contributions are zero modulo three. The singleton contributes either zero or one at that position. Therefore:

$$
\left(\sum_{\texttt{num}\in\texttt{nums}}
\operatorname{bit}_i(\texttt{num})\right)\bmod 3
$$

is exactly bit `i` of the unique number.

The solution applies this reasoning independently to all 32 positions of the signed integer domain.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 2, 3, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extract one position from every number

For each `i` from zero through 31, the generator computes:

`num >> i & 1`

Right shift moves bit `i` into the least significant position. Bitwise AND with one clears every other position, leaving either zero or one. Parentheses are unnecessary because Python gives shifting higher precedence than bitwise AND in the intended grouping, but the expression means `(num >> i) & 1`.

`sum(...)` adds that bit over the whole array. If `cnt % 3` is zero, the singleton has zero at position `i`, so `ans` needs no change. If it is nonzero, the valid frequency guarantee means the remainder is exactly one and the singleton has that bit set.

For positions zero through 30, `ans |= 1 << i` places the bit into the answer. Left-shifting one creates a mask with only position `i` set, and OR preserves bits already reconstructed.

For `[2, 2, 3, 2]`, binary `2` contributes its bit pattern three times. At every position, those contributions vanish modulo three. The remaining remainders are the bits of `3`, so the result is three.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each `i` from zero through 31, the generator computes:

... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the sign bit needs different reconstruction

The constraints use signed 32-bit values from $-2^{31}$ through $2^{31}-1$. Position 31 is the sign bit in two’s-complement representation.

Python integers do not have a fixed 32-bit width. If the code handled position 31 with ordinary OR, it would construct the unsigned value having that high bit set, a positive integer at least $2^{31}$, rather than the required negative value.

Suppose the singleton’s lower 31 bits form the nonnegative value $L$ and its sign bit is one. Its unsigned 32-bit pattern has value:

$$
2^{31}+L.
$$

The signed value represented by the same pattern is:

$$
(2^{31}+L)-2^{32}=L-2^{31}.
$$

That is why the source uses `ans -= 1 << 31` for `i == 31`. At that moment, `ans` already equals $L$. Subtracting $2^{31}$ converts the reconstructed lower bits to the correct signed integer.

Python’s right shift of a negative number sign-extends with ones, which is consistent with two’s-complement bits at the 32 positions being examined. Applying `& 1` still extracts the desired position.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 2, 3, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two-mask finite-state machine:** Maintain mask:** - **Two-mask finite-state machine:** Maintain masks for bits seen once and twice modulo three. It processes all bit positions in parallel and also runs in $O(n)$ time and $O(1)$ space, but its Boolean transitions are less immediately intuitive.
- **Frequency dictionary:** Count complete integers and return the count-one key. It is linear expected time but requires $O(n)$ extra space.
- **Sort and scan triples:** Sorting makes equal values adjacent, but costs $O(n\log n)$ time and may mutate the input.
- **Set-and-sum formula:** `(3 * sum(set(nums)) - sum(nums)) // 2` derives the singleton algebraically, but the set violates constant space and fixed-width sums can overflow.
- **One element:** Its bits alone determine every remainder, so the same reconstruction returns it.
- **Singleton zero:** All position remainders are zero and `ans` remains zero.
- **Negative singleton:** The position-31 subtraction is necessary to return a negative Python integer instead of an unsigned 32-bit magnitude.
- **Negative repeated values:** Each sign-extended bit is still counted three times and vanishes modulo three.
- **Remainder two:** Valid input cannot leave remainder two at any bit because only the singleton survives and contributes at most one. The code treats any nonzero remainder as set, trusting the contract.
- **Runtime dependency:** The selected source uses `List` without importing it. A standalone module needs `from typing import List`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $n$ be the array length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
