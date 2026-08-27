# Guided Example: Number Complement

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 10}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **complement** of an integer is the integer you get when you flip all the `0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

The objective is to compute `5` from `{"num": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Find the meaningful width

`num.bit_length()` returns the number of bits required to represent positive `num` without leading zeros. For example:

- `1` is binary `1`, so its bit length is one.
- `5` is binary `101`, so its bit length is three.
- `8` is binary `1000`, so its bit length is four.

Let this width be `b`. The highest meaningful position is `b - 1`, and positions at `b` or above are implicit leading zeros that must remain outside the operation.

The contract guarantees `num >= 1`, so `b` is always positive. Python defines `0.bit_length()` as zero, but the exact source does not need a separate zero policy for this problem.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Construct `b` one-bits

The expression `1 << b` shifts a single one left by `b` positions, creating the binary pattern `1` followed by `b` zeros. Subtracting one borrows through those zeros and produces exactly `b` trailing ones:

$$
(1\ll b)-1=\underbrace{11\ldots1}_{b\text{ bits}}.
$$

For `b = 3`, `1 << 3` is binary `1000`, and subtracting one gives `111`.

This is the exact width mask needed for `num`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The expression `1 << b` shifts a single one left by `b` posi... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why XOR performs the complement

For one bit `x`, XOR has these relevant identities:

$$
x\oplus1=1-x,
\qquad
x\oplus0=x.
$$

Every meaningful bit is aligned with a mask bit of one, so it flips. Every higher position is aligned with mask zero, so it stays zero and creates no unwanted leading ones.

The returned expression is therefore

`num ^ ((1 << num.bit_length()) - 1)`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Flip one bit at a time:** Walk through `num`'s:** - **Flip one bit at a time:** Walk through `num`'s bits with a shifting one-bit mask. It is correct but uses a loop instead of one same-width XOR.
- **Propagate the highest bit downward:** Repeated OR-with-shift operations turn every lower position into one, then XOR. This avoids `bit_length` but is more verbose.
- **Use `~num` directly:** Incorrect in Python because it flips unbounded leading sign bits and returns a negative value.
- **Subtract from the mask:** `(1 << b) - 1 - num` is algebraically equivalent to XOR for this all-ones width.
- **`num = 1`:** The one meaningful bit flips to zero.
- **Power of two:** The leading one becomes zero and every lower zero becomes one, yielding one less than the original number.
- **All bits already one:** A value such as `7 = 111` complements to zero.
- **Leading zeros:** They are intentionally excluded by `bit_length`; complementing a fixed 32-bit width would solve a different problem.
- **Zero outside the contract:** A separate definition would be needed because its ordinary representation policy varies by problem; this source guarantees positive input.
- **Why XOR stays within the intended width:** The mask contains zeros above the highest meaningful bit, so XOR leaves every higher position zero while toggling precisely the represented binary digits.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $b=\lfloor\log_2(\texttt{num})\rfloor+1$ be the bit length. At the arbitrary-precision bit-operation level, determining bit length, constructing the mask, and applying XOR require $O(b)=O(\log\texttt{num})$ bit work. This matches the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
