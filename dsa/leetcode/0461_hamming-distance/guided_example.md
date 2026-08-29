# Guided Example: Hamming Distance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"x": 1, "y": 4}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.

The objective is to compute `2` from `{"x": 1, "y": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why XOR isolates differences

Write both nonnegative integers in binary and align them at the least significant bit. Leading positions omitted from the shorter representation are zeros. XOR applies the truth table independently at every position, so equal pairs become zero and unequal pairs become one.

For `x = 1` and `y = 4`, use four displayed bits:



The XOR result is decimal `5`, whose binary representation contains two ones. The Hamming distance is therefore two.

For `x = 3` (`11`) and `y = 1` (`01`), XOR gives `10`, which has one set bit, so the answer is one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"x": 1, "y": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What `bit_count` returns

Python's integer method `bit_count()` returns the number of ones in the integer's binary representation, also called the population count. Because both inputs are nonnegative, their XOR is nonnegative. Each counted one corresponds to one differing bit position, and no equal position contributes.

This is not the same as counting the number of binary digits. For example, XOR result `8` is binary `1000`: it spans four positions but contains only one set bit, so the Hamming distance is one.

Leading zeros need no explicit padding. Above the highest set bit of both inputs, both conceptual bits are zero and therefore equal. Between their bit lengths, the shorter number contributes conceptual zero bits, and ordinary integer XOR already handles those positions correctly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the one-line result is exact

Take any bit position `p`. If `x` and `y` have different bits there, XOR places one at `p`, and `bit_count` adds exactly one for it. If their bits are equal, XOR places zero there, and it adds nothing. Since bit positions are independent, summing the set bits counts every disagreement once and no agreement. That is exactly the definition of Hamming distance.

The method also handles equality naturally. If `x == y`, XOR returns zero. Zero has no set bits, so the result is zero.

If one input is zero, XOR returns the other input. The distance is then the number of ones already present in that number, which is correct because those are precisely the positions where it differs from zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"x": 1, "y": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Brian Kernighan's method:** Repeatedly replace `z` with `z & (z - 1)`. Each iteration clears the lowest set bit, so the iteration count equals the answer. It is useful when a built-in population count is unavailable.
- **Shift and inspect:** Repeatedly add `z & 1` and shift `z` right. It is straightforward but examines zero bits between set bits as well.
- **Convert to a binary string:** `bin(x ^ y).count('1')` is concise but allocates a textual representation and performs more conversion work than `bit_count`.
- **Compare decimal digits:** Hamming distance concerns binary positions, not decimal notation; decimal comparison gives unrelated results.
- **Equal inputs:** XOR is zero and the answer is zero.
- **One input zero:** The answer is the population count of the other input.
- **Different bit lengths:** Conceptual leading zeros are handled automatically by integer XOR.
- **Maximum allowed value:** At most 31 relevant bits are processed, so no loop or recursion depth concern exists.
- **Negative values outside the contract:** Python defines bitwise operations using an infinite two's-complement model, which changes how leading sign bits should be interpreted. The nonnegative-input guarantee avoids that ambiguity.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log\max(x,y)$. Let $w$ be the number of relevant bits, which is $O(\log(\max(x,y)+1))$. At the bit-operation level, forming the XOR and counting its set bits process $O(w)$ machine-word information, giving the manifest-style time bound $O(\log\max(x,y))$ for positive inputs.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
