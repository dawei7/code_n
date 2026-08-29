# Guided Example: Number of 1 Bits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4294967295}`
- **Required output:** `32`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).

The objective is to compute `32` from `{"n": 4294967295}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count set bits without visiting zero positions

The straightforward method examines every one of the 32 bit positions. The
stored optimal method uses Brian Kernighan's observation to perform one loop
iteration per set bit instead. It repeatedly changes the least significant
remaining 1-bit to 0 and increments the answer.

This works especially well for sparse numbers. A power of two such as 128 has
only one set bit, so the loop executes once even though that bit may be far from
the least significant position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4294967295}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand what subtracting one does in binary

Consider a positive integer `n` and locate its least significant 1-bit. All
positions to its right must be zeros. Subtracting one changes that chosen 1 to
0 and changes every trailing zero on its right to 1. Bits to its left remain
unchanged.

For example:

`n     = 1011000`

`n - 1 = 1010111`

The rightmost 1 in `n` is the fourth bit from the right. Subtraction clears it
and fills the three lower zero positions with ones.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use AND to remove exactly that bit

The update `n &= n - 1` compares those two patterns position by position. Bits
to the left of the rightmost 1 are unchanged in `n - 1`, so any set bits there
remain set after AND. At the rightmost 1 position, `n - 1` contains zero, so
AND clears it. In every lower position, original `n` contains zero, so the new
ones introduced by subtraction are cleared by AND.

Consequently, the result is the original number with exactly its least
significant set bit removed and every other set bit preserved. One update can
never remove two set bits and can never create a set bit.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `32` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4294967295}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `32` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check every bit:** AND with a moving mask for 32 iterations; simpler fixed work but ignores sparsity.
- **Parallel mask-and-add:** Sum neighboring bit counts in five fixed stages, as the competitive variant does.
- **Byte lookup table:** Four fixed lookups per call make a useful repeated-call optimization with a 256-entry cache.
- **Built-in population count:** `n.bit_count()` is concise and usually highly optimized, though it hides the interview technique.
- **Binary-string count:** Correct for positive inputs but allocates a textual representation.
- **Power of two:** Exactly one iteration because `n & (n - 1)` becomes zero immediately.
- **All low 31 bits set:** Executes 31 iterations, still constant under the fixed-width contract.
- **Zero:** Returns zero naturally even though the Reference says positive.
- **Negative Python integer:** Mask to the intended width first; otherwise the finite-word reasoning does not apply.
- **Variable-width integers:** Report complexity in the word length or popcount instead of calling it unconditional $O(1)$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(p)$. Let $p$ be the number of set bits. The loop executes exactly $p$ times, so a
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
