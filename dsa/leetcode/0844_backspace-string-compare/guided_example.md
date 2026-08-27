# Guided Example: Backspace String Compare

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "ab#c", "t": "ad#c"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `s` and `t`, return `true` *if they are equal when both are typed into empty text editors*. `'#'` means a backspace character.

The objective is to compute `true` from `{"s": "ab#c", "t": "ad#c"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Read the final texts backward without constructing them

A backspace affects the nearest still-present character to its left. When scanning forward, we usually need a stack to know which earlier character to delete. Scanning backward reverses the dependency: when we encounter `#`, it tells us how many ordinary characters farther left should be skipped.

The solution keeps one pointer and one pending-skip count for each input string. It repeatedly finds the next character that would survive in each final editor text and compares those characters.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "ab#c", "t": "ad#c"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Pointer and skip meaning

`i` and `j` start at the final indices of `s` and `t`.

`skip1` is the number of ordinary characters in `s` that must still be erased by backspaces already encountered to their right. `skip2` has the same meaning for `t`.

These counts begin at zero because no characters have been examined yet.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `i` and `j` start at the final indices of `s` and `t`.

`ski... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the next surviving character in `s`

While `i >= 0`:

- if `s[i] == '#'`, increment `skip1` and move left;
- otherwise, if `skip1 > 0`, this ordinary character is erased, so decrement `skip1` and move left;
- otherwise, stop: `s[i]` survives and is the next character of the final text when read backward.

Several consecutive backspaces simply increase the count. If there are more backspaces than earlier characters, the pointer reaches `-1` with some skip count possibly remaining; this correctly represents backspacing an empty editor, which keeps it empty.

The same logic independently finds the next surviving character in `t`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "ab#c", "t": "ad#c"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Build each final string with a stack:** Push l:** - **Build each final string with a stack:** Push letters and pop on backspaces, then compare. It is straightforward and linear-time but uses linear extra space.
- **- **Repeatedly remove `letter#` patterns:** Immuta:** - **Repeatedly remove `letter#` patterns:** Immutable-string rebuilding can be quadratic and is harder to reason about with consecutive backspaces.
- **- **Strings already equal without backspaces:** Ev:** - **Strings already equal without backspaces:** Every character becomes a survivor and compares normally.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(|s|+|t|)$. Each pointer only moves left. Every character of `s` and `t` is examined at most once, so time is
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
