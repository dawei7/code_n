# Guided Example: Length of the Longest Alphabetical Continuous Substring

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abacaba"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An **alphabetical continuous string** is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string `"abcdefghijklmnopqrstuvwxyz"`.

The objective is to compute `2` from `{"s": "abacaba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A valid substring is an exact successor run

Within an alphabetical continuous substring, every next character must be exactly one alphabet position after the previous:



It is not enough for characters merely to increase. `'a'` followed by `'c'` skips a letter and breaks continuity. `'z'` followed by `'a'` is also invalid because the alphabet does not wrap.

The algorithm tracks the length `cnt` of the current exact-successor suffix and `ans` as the longest such run seen.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abacaba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compare numeric character codes

`map(ord, s)` lazily converts letters to code points. For consecutive values `x` and `y`, the condition:



is true precisely when the second lowercase English letter is the immediate alphabet successor of the first.

ASCII/Unicode lowercase code points are consecutive, so no lookup table is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `map(ord, s)` lazily converts letters to code points.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Initialize the first character

The input is nonempty. Any one-character substring appears in the alphabet string and is continuous, so both `ans` and `cnt` begin at one.

`pairwise(...)` then yields every adjacent code-point pair. If the successor condition holds, the current run extends and `cnt` increments. The code updates `ans` with the larger run length.

If the condition fails, `cnt` resets to one because the current character begins a new valid one-character run.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abacaba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare characters directly:** Test `ord(y) ==:** - **Compare characters directly:** Test `ord(y) == ord(x) + 1` without mapping the entire iterator. It has the same complexity.
- **Split at failures:** Record maximal runs and take their lengths. This is equivalent but needs more bookkeeping.
- **Enumerate substrings:** Testing every substring takes quadratic or worse time.
- **One character:** Initialization returns one.
- **Entire string continuous:** The answer is `len(s)`.
- **Repeated character:** Difference zero breaks the run.
- **Skipped alphabet letter:** Difference greater than one breaks the run.
- **Decreasing pair:** Negative difference breaks the run.
- **`"za"`:** There is no wraparound, so it forms only singleton runs.
- **Substring requirement:** Characters cannot be skipped to repair a broken adjacency.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. The lazy map and `pairwise` iterator process $n-1$ adjacent pairs. Each performs constant-time arithmetic and assignments, giving $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
