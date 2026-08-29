# Guided Example: Longest Uncommon Subsequence I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"a": "aba", "b": "cdc"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `a` and `b`, return *the length of the **longest uncommon subsequence** between *`a` *and* `b`. *If no such uncommon subsequence exists, return* `-1`*.*

The objective is to compute `3` from `{"a": "aba", "b": "cdc"}` while avoiding redundant calculations and unnecessary overhead.

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

The word “subsequence” can make this problem look as though it requires generating many strings, but with exactly two input strings the whole-string candidates settle the answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"a": "aba", "b": "cdc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

A string is always a subsequence of itself: delete zero characters. Therefore `a` is a subsequence of `a`, and `b` is a subsequence of `b`. The only remaining question is whether one entire input string is also a subsequence of the other.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Case one: the strings are equal.** If `a == b`, they have exactly the same characters in the same order. Every subsequence obtainable from `a` is also obtainable from `b` by making the same deletions. The reverse is equally true.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"a": "aba", "b": "cdc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate all subsequences:** Each length-$n$ string has up to $2^n$ deletion choices, which is exponential and unnecessary because a whole input string is always the optimal witness when the inputs differ.
- **Two-pointer subsequence check:** It would correctly test whether one input is a subsequence of the other, but length and equality already imply the needed result for whole-string candidates.
- **Longest common subsequence DP:** Computing an LCS solves a much harder question and costs quadratic time and space without changing this answer.
- **Equal strings:** Every subsequence occurs in both, so the required sentinel is `-1`.
- **Different lengths:** The longer entire string is automatically uncommon because it cannot fit as a subsequence of the shorter one.
- **Equal lengths but different characters:** Neither full string can be a subsequence of the other; a same-length subsequence would have to use every character unchanged.
- **One-character equal strings:** They have no uncommon subsequence and return `-1`.
- **One-character unequal strings:** Either whole character is uncommon, so the answer is one.
- **Repeated characters:** Repetition does not affect the equality-and-length proof.
- **One string is a subsequence of the other:** If lengths differ, the longer whole string still supplies the optimum even when the shorter is common to both.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(A)$. Let $A=\lvert a\rvert$ and $B=\lvert b\rvert$. Computing lengths is constant time in Python because strings store their lengths. The equality comparison can inspect characters until it finds a mismatch and takes $O(\min(A,B))$ time in the worst relevant equal-length case; when the strings are identical it takes $O(A)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
