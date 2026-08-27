# Guided Example: Complement of Base 10 Integer

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 999999999}`
- **Required output:** `73741824`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **complement** of an integer is the integer you get when you flip all the `0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

The objective is to compute `73741824` from `{"n": 999999999}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Flip only the bits that belong to the ordinary binary representation

Positive integers conceptually have infinitely many leading zero bits, but those leading zeros are not written in the standard binary representation and must not be complemented. For example, five is `101`, not `000...0101`, so only its three significant positions are flipped.

The algorithm processes bits from least significant to most significant and stops once all original significant bits have been consumed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 999999999}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Handle zero separately

Zero's ordinary binary representation is `"0"`, whose complement is `"1"`, or decimal one.

The main loop uses `while n`. If `n` were initially zero, it would run zero times and leave `ans = 0`, which would be wrong. The explicit base case returns one before the loop.

This is the only input whose significant representation contains a bit even though right-shifting the numeric value offers no loop iteration.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Zero's ordinary binary representation is `"0"`, whose comple... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Extract and flip the current bit

At each iteration:

`n & 1`

extracts the least significant bit. AND with one clears every higher position and leaves either zero or one.

XOR with one flips that bit:

- `0 ^ 1 = 1`;
- `1 ^ 1 = 0`.

Conceptually, the subexpression is `(n & 1) ^ 1`. It produces the complement bit for the current position.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `73741824` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 999999999}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `73741824` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Same-length all-ones mask:** Compute `mask = (:** - **Same-length all-ones mask:** Compute `mask = (1 << n.bit_length()) - 1` and return `mask ^ n`. It flips all significant positions at once.
- **Subtract from the mask:** For an all-ones mask of the same bit length, `mask - n` also equals the complement.
- **Propagate the highest one bit:** Repeated OR-with-shift operations can turn every bit below the highest one into a mask, then XOR with `n`.
- **Binary-string conversion:** Map each `0` to `1` and each `1` to `0`, then parse. It is clear but allocates text and extra storage.
- **Bitwise NOT:** Produces a negative two's-complement value unless explicitly masked, so using it alone is incorrect.
- **`n = 0`:** Requires the explicit result one because the loop would otherwise process no bits.
- **All one bits:** Values such as seven complement to zero.
- **Power of two:** A representation such as `1000` becomes `0111`, one less than the original power.
- **Leading zeros:** They are not part of the representation and are deliberately never visited.
- **Maximum input:** Fewer than thirty-one loop iterations are needed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B)$. Let `B` be the number of bits in the binary representation of the original positive input.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
