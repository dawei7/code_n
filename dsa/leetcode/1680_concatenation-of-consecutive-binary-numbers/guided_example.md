# Guided Example: Concatenation of Consecutive Binary Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000}`
- **Required output:** `499361981`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return *the **decimal value** of the binary string formed by concatenating the binary representations of *`1`* to *`n`* in order, **modulo ***$10^{9} + 7$.

The objective is to compute `499361981` from `{"n": 1000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Append a binary block with arithmetic instead of strings

Suppose `ans` is the numeric value of the binary concatenation for integers one through `i - 1`. To append the binary representation of `i`, the existing bits must move left by exactly the number of bits in `i`. If that length is `b`, the new value is

$$
\texttt{ans}\cdot 2^b + i.
$$

The source implements multiplication by $2^b$ as `ans << b`. It combines `i` with bitwise OR:

`(ans << i.bit_length()) | i`.

This OR is equivalent to addition here. Shifting left by `b` places `b` zero bits at the bottom of `ans`. Since `i` fits in exactly `b` bits, its set bits occupy only those zero positions, so OR introduces no carry or overlap.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Get the correct block length

`i.bit_length()` is the number of bits required to represent positive integer `i` without leading zeros. For example:

- one has binary `1` and bit length one;
- two has binary `10` and bit length two;
- three has binary `11` and bit length two;
- four has binary `100` and bit length three.

Those are precisely the block widths used by ordinary binary representation. No explicit conversion to a string is needed, and no special power-of-two counter is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain the concatenation invariant

Before the first iteration, `ans = 0` represents an empty bit string. At iteration `i`, assume `ans` is congruent modulo `mod` to the full concatenation through `i - 1`. Shifting by `i.bit_length()` and placing `i` in the new low bits constructs the concatenation through `i`.

The source then takes the result modulo

$$
10^9+7.
$$

Reducing after every append is valid because modular congruence is preserved by multiplication and addition:

$$
(a\bmod M)\cdot 2^b+i
\equiv a\cdot 2^b+i\pmod M.
$$

Thus the algorithm never needs to hold the astronomically large full concatenated integer. The reduced `ans` still contains all information needed for the final remainder.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `499361981` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `499361981` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build one binary string:** Convert every integer with `bin(i)[2:]`, concatenate, parse, and reduce. It is direct but uses $O(n\log n)$ characters and constructs a huge integer.
- **Track bit length at powers of two:** Increase a counter when `i & (i-1) == 0`. This avoids calling `bit_length` and yields the same $O(n)$ time and $O(1)$ space.
- **Use multiplication and addition:** `ans = (ans * (1 << b) + i) % mod` is mathematically identical to shift and OR.
- **`n == 1`:** One iteration appends binary `1` and returns one.
- **Power-of-two boundary:** `bit_length` increases exactly at values such as two, four, and eight, ensuring the prior result shifts by the newly required width.
- **Modulo during every step:** This does not alter the final remainder and prevents the accumulator from growing with the total concatenated length.
- **OR versus addition:** They are interchangeable only because the shift clears all low `b` bits and `i` fits within them.
- **Positive-input guarantee:** `bit_length` for zero is zero, but the sequence begins at one, so every appended block has at least one bit.
- **No leading zeros:** Minimal bit length matches the problem’s conventional binary representation.
- **Large `n`:** The loop remains linear through $10^5$ and avoids any object proportional to the combined binary-string length.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop runs `n` times. Under the standard word-RAM model for values within the constraints, `bit_length`, a bounded-width shift, OR, and modulo are constant-time operations. `ans` remains below `mod` after every iteration, and the shift amount is at most the bit length of `n`, so intermediate values stay bounded. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
