# Guided Example: Minimum Bit Flips to Convert Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"start": 10, "goal": 7}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **bit flip** of a number `x` is choosing a bit in the binary representation of `x` and **flipping** it from either `0` to `1` or `1` to `0`.

The objective is to compute `3` from `{"start": 10, "goal": 7}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each bit position is an independent requirement

To turn `start` into `goal`, every binary position must eventually contain the bit that `goal` has at that position. If the two numbers already have the same bit at a position, that position requires no flip. If their bits differ, at least one flip at that position is unavoidable.

Flipping one position has no effect on any other position. Consequently, there is no scheduling or greedy-choice interaction to solve: the minimum number of operations is exactly the number of positions where the two binary representations differ. This quantity is also called their Hamming distance.

Leading zeros fit the same rule. Binary notation normally omits them, but both nonnegative integers can be imagined as having infinitely many leading zero bits. Beyond the most significant `1` of either number, both have zeros, so those positions agree and contribute nothing. Only finitely many positions can differ.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"start": 10, "goal": 7}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: XOR creates a mask of exactly the differing positions

The exclusive-or operation compares corresponding bits according to this table:

| start bit | goal bit | XOR bit |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Thus, `start ^ goal` has a `1` exactly where the inputs disagree and a `0` exactly where they agree. Rather than compare two numbers bit by bit, the XOR operation produces one integer whose set bits are the complete to-do list.

For `start = 10` and `goal = 7`, align their binary forms as `1010` and `0111`. Their XOR is `1101`. It contains three `1` bits, corresponding to the least significant, third, and fourth positions. Those are precisely the three positions described in the example.

For `start = 3` and `goal = 4`, the aligned forms are `011` and `100`. XOR produces `111`, so all three positions must change.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count that mask with Python's integer operation

The exact solution returns

`(start ^ goal).bit_count()`.

Python's `int.bit_count()` reports the number of `1` bits in the absolute binary representation of an integer. Here both inputs are nonnegative, so their XOR is also nonnegative and its bit count directly equals the number of differing positions.

No explicit loop appears in the Python source because the language runtime performs the population count. Conceptually, it is doing the same job as repeatedly examining bits or clearing set bits, but the built-in operation states the intent directly and can use an efficient low-level implementation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"start": 10, "goal": 7}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Compare least significant bits in a loop:** Repeatedly test `start & 1` against `goal & 1` and right-shift both values. This is correct and explicit, but XOR consolidates the comparison into one mask and `bit_count()` expresses the final operation directly.
- **Count XOR bits by shifting:** Store `x = start ^ goal`, add `x & 1` to a counter, and shift until `x` is zero. It examines every bit through the highest set position, including zero bits.
- **Brian Kernighan's method:** Repeatedly execute `x &= x - 1` to clear the lowest set bit. It performs exactly one loop iteration per required flip and is valuable when no population-count built-in is available.
- **Convert to padded binary strings:** Align string representations and count unequal characters. It can work, but needs padding and extra `O(b)` character storage for a problem naturally expressed with bits.
- **Arithmetic difference:** The number of set bits in `abs(start - goal)` is not the answer. Carries and borrows mix positions; XOR, not subtraction, marks independent disagreements.
- **Equal inputs:** XOR is zero and the answer is zero.
- **Both inputs zero:** Their representations agree at every position, including all leading zeros, so the result is zero.
- **One input zero:** The result is the set-bit count of the nonzero input.
- **Different displayed lengths:** Implicit leading zeros are compared automatically by integer XOR.
- **A mismatch in every relevant position:** The XOR mask consists entirely of ones, and each such bit contributes one necessary flip.
- **Flipping a leading zero:** This is already modeled. A high bit present only in `goal` becomes a set bit in XOR and is counted.
- **Nonnegative-input guarantee:** Python's behavior for negative integers uses an unbounded signed representation that would need careful interpretation. The constraints exclude negative values, so `bit_count()` has the direct intended meaning.
- **Repeated flips of one bit:** They cannot reduce the minimum. A differing bit needs odd parity and is cheapest to flip once; a matching bit needs even parity and is cheapest to leave alone.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Under the stated constraint `0 <= start, goal <= 10^9`, each input uses at most thirty significant bits. XOR and `bit_count()` therefore operate over a fixed bounded number of machine words. In the problem's input model, time complexity is `O(1)` and auxiliary space is `O(1)`, matching the Optimal manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
