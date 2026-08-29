# Guided Example: Faulty Keyboard

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "string"}`
- **Required output:** `"rtsng"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Your laptop keyboard is faulty, and whenever you type a character `'i'` on it, it reverses the string that you have written. Typing other characters works as expected.

The objective is to compute `"rtsng"` from `{"s": "string"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Simulate the faulty key literally.** The input is processed from left to right. For an ordinary character, that character appears at the end of the text currently displayed. When the character is `"i"`, it is not typed into the display; instead, the entire displayed text is reversed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "string"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution stores the current displayed characters in a Python list named `t`. Lists support efficient appending and can be joined into one string at the end.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Maintain the exact displayed text after every input character.** Initially, no keys have been processed and `t` is empty, matching the empty display. For each character `c`:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"rtsng"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "string"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"rtsng"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Deque plus direction flag:** Toggle a Boolean instead of reversing stored characters. Append new characters to the logical back, which is one physical end or the other depending on the flag, and materialize in the correct direction once. This gives $O(n)$ time and $O(n)$ space and matches the manifest.
- **List plus two buffers:** Accumulate runs between faulty keys and combine them with direction awareness. This can also avoid repeated full reversals but is more complex than a deque.
- **In-place `list.reverse`:** It avoids allocating a new list for every reversal but still scans the current output each time, so worst-case time remains $O(n^2)$.
- **No faulty key:** Every character appends, and the result equals the input.
- **Faulty key at the beginning:** The stated contract says the first character is not `i`, but reversing an empty list would still be harmless.
- **Consecutive faulty keys:** Every pair cancels in effect, although the exact source still pays for both reversals.
- **Faulty key after one character:** Reversing a one-element display changes nothing, but the key is still omitted.
- **All later characters ordinary:** They append after whatever orientation the most recent physical reversal produced.
- **Repeated ordinary letters:** Each occurrence is a separate keystroke and is preserved; no set or deduplication is involved.
- **Empty output outside the constraints:** An input consisting only of faulty keys would leave the list empty and return an empty string, though the first-character guarantee prevents that exact valid case.
- **Do not use reversal parity alone:** The positions of ordinary characters relative to reversal events affect the answer, so total count parity lacks enough information without direction-aware insertion.
- **Input preservation:** The immutable input string is only read, while all simulation state lives in the new list.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the input length. Appending an ordinary character is amortized $O(1)$. When a faulty key occurs after $r$ ordinary characters have been retained, `t[::-1]` takes $O(r)$ time and allocates a list of length $r$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
