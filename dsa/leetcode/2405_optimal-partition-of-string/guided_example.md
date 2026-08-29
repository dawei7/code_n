# Guided Example: Optimal Partition of String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abacaba"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, partition the string into one or more **substrings** such that the characters in each substring are **unique**. That is, no letter appears in a single substring more than **once**.

The objective is to compute `4` from `{"s": "abacaba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Extend the current part as far as validity allows

Each substring in the partition must contain unique characters. The greedy rule is:

- keep appending while the next character has not appeared in the current substring;
- when it repeats, end the current substring immediately before that character and start a new substring with it.

The exact code represents letters already in the current part with a 26-bit mask.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abacaba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Map lowercase letters to mask bits

`ord(c) - ord("a")` maps each lowercase character to an index `0` through `25`. Bit `x` is one when that letter has already appeared in the current substring.

The membership test:



extracts that bit. Adding the letter uses `mask |= 1 << x`.

The fixed lowercase alphabet means this state is one integer rather than a growing set.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Start with one substring

The input is guaranteed nonempty, so at least one substring is required. `ans` begins at one and `mask` begins empty.

For each character, if its bit is already set, the current substring cannot legally include it. The code increments `ans` and resets `mask = 0`. It then executes the common insertion line, adding the current character as the first member of the new substring.

Forgetting that final insertion would allow an immediate duplicate to slip into the new part.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abacaba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Set for the current part:** A set provides clearer membership semantics and remains $O(1)$ space for 26 letters, but the bitmask has lower overhead.
- **Dynamic programming over cut positions:** It can find a minimum but is unnecessary because the latest-valid-cut greedy choice is provably optimal.
- **One character:** Initialization returns one part.
- **All characters unique:** No reset occurs, so the entire string is one substring.
- **All characters equal:** Every character after the first forces a new part.
- **Repeated character after a cut:** The reset removes prior-part bits, so characters may repeat across different substrings.
- **Current character insertion:** It must be added after reset as the first letter of its new part.
- **Lowercase-only contract:** It makes a 26-bit integer sufficient.
- **Nonempty input:** It justifies initializing `ans` to one rather than zero.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. The lazy `map` and loop process each character exactly once. Every iteration performs constant-time code-point arithmetic and bit operations. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
