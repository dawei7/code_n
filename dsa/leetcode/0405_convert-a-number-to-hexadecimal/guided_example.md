# Guided Example: Convert a Number to Hexadecimal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 26}`
- **Required output:** `"1a"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a 32-bit integer `num`, return *a string representing its hexadecimal representation*. For negative integers, <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">two’s complement</a> method is used.

The objective is to compute `"1a"` from `{"num": 26}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Hexadecimal groups binary bits four at a time

One hexadecimal digit represents exactly four bits, called a nibble. A signed 32-bit integer therefore has exactly eight nibble positions:

$$
32/4=8.
$$

The exact solution examines those eight positions from most significant to least significant. For each position, it extracts a value from zero through fifteen and maps that value to the corresponding lowercase hexadecimal character.

This avoids any built-in integer-to-hexadecimal conversion.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 26}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Handle zero separately

The number zero has eight zero nibbles. The general loop suppresses leading zeroes, so it would append nothing for this input. The early branch returns `"0"`, the one case where a zero digit must be present.

For every nonzero number, at least one nibble is nonzero. Negative 32-bit values have nonzero high nibbles in two’s-complement form, so their result also cannot remain empty.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Extract one nibble with shifting and masking

The loop variable `i` runs through `7, 6, ..., 0`. Nibble `i` occupies bit positions `4*i` through `4*i + 3`.

The expression



performs two operations:

1. right shift by `4 * i`, moving the desired nibble into the lowest four bit positions;
2. bitwise AND with `0xF`, whose binary form is `1111`, discarding every bit except those lowest four.

The result `x` is always an integer from `0` through `15`.

For example, decimal `26` is binary `000...00011010`. At nibble position one, shifting right four gives binary `1`, so `x = 1`. At nibble position zero, masking the original low four bits gives binary `1010`, decimal ten.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"1a"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 26}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"1a"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeated division by 16:** For a nonnegative value, repeatedly take remainder 16 and divide, then reverse the collected digits. Negative inputs first require conversion to their unsigned 32-bit value. This is correct but needs separate sign handling.
- **Add `2**32` for negatives:** Converting `num` to `num + 2**32` makes the unsigned two’s-complement value explicit, after which repeated division works. The exact masking method achieves the same result directly.
- **Built-in `hex`:** It would violate the explicit restriction against a direct library conversion and formats negative numbers with a minus sign rather than the required 32-bit two’s-complement representation.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The loop always performs eight iterations because the input width is fixed at 32 bits. Every iteration does a bounded shift, mask, comparison, and optional append. Time complexity is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
