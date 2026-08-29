# Guided Example: Find the Difference

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abcd", "t": "abcde"}`
- **Required output:** `"e"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `t`.

The objective is to compute `"e"` from `{"s": "abcd", "t": "abcde"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Shuffling removes positional information

String `t` contains every occurrence from `s`, plus exactly one new occurrence, but those characters may appear in any order. Comparing `s[i]` with `t[i]` is therefore meaningless: an ordinary character from `s` can move to a different position and look like a mismatch even though it is not the addition.

What shuffling preserves is frequency. For every character except the added one, `s` and `t` contain the same number of occurrences. For the added character, `t` contains exactly one more occurrence.

The exact solution turns this observation into inventory accounting. It creates `cnt = Counter(s)`, then scans `t`. Every `t` character consumes one matching occurrence from the inventory by executing `cnt[c] -= 1`. The first count that becomes negative identifies the extra occurrence and is returned.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abcd", "t": "abcde"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why an added character may already exist in `s`

The answer is not necessarily a character absent from `s`. For example, `s = "aab"` and `t = "abaa"` are valid: the extra letter is another `a`. A membership set would know only that `a` appears in both strings and would miss the difference.

Frequencies solve this correctly. The counter begins with `a: 2`. The first two `a` occurrences encountered in `t` reduce that supply to zero. The third reduces it to `-1`, revealing that this occurrence cannot be matched with any copy from `s`.

Thus, the method finds an extra occurrence, not merely a new distinct character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The inventory invariant

After processing any prefix of `t`, for each character `c`, the counter value is

$$
\texttt{cnt}[c]
=
\operatorname{freq}_{s}(c)
-
\operatorname{freq}_{\text{processed prefix of }t}(c).
$$

Initially the processed prefix is empty, so `Counter(s)` establishes the equation. Processing one character subtracts one from exactly its entry, maintaining the equation.

A nonnegative count means the processed copies of that character can still be matched one-for-one with copies from `s`. A negative count means the prefix of `t` has used more copies than all of `s` contains. Under the contract, exactly one total occurrence in `t` is unmatched, so the character that first crosses below zero is precisely the added letter.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"e"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abcd", "t": "abcde"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"e"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Bitwise XOR:** XOR the character codes from both strings. Equal occurrences cancel because $x \mathbin{\oplus} x = 0$, leaving the extra code. This also achieves $O(n)$ time and $O(1)$ space and is elegant for this exact one-extra-item contract, but frequency counting is often easier for beginners to generalize and audit.
- **Sum character codes:** Subtract the code-point sum of `s` from that of `t`. The difference is the added character code. Python avoids overflow, but fixed-width languages may need a wider type; XOR avoids arithmetic overflow.
- **Sort both strings:** Sorting aligns matching characters so the first mismatch reveals the extra one, but costs $O(n\log n)$ time and $O(n)$ storage in Python.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`; then `t` has length $n+1$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
