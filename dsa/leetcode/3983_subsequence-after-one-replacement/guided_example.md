# Guided Example: Subsequence After One Replacement

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "cat", "t": "chat"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `t` consisting of lowercase English letters.

The objective is to compute `true` from `{"s": "cat", "t": "chat"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the longest prefix is enough

Suppose two exact states have matched prefix lengths `a<b` after consuming the same portion of `t`. State `b` dominates `a`: it has matched every character that `a` has and more, while using the same zero replacements. Any future characters capable of finishing from `a` can be considered from the more advanced position `b` without needing to recover skipped target characters.

The same reasoning applies among states that may already have used the one replacement. Thus one maximum length per replacement budget is sufficient.

However, `i0` cannot be discarded in favor of `i1`. The longer `i1` route may have spent its replacement, while the exact route still has the replacement available for a future mismatch. The two budgets must remain separate.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "cat", "t": "chat"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extending the at-most-one-replacement state exactly

For current target character `t[j]`, if it matches the next character needed by `i1`, that state can advance without spending any additional replacement:



If the path represented by `i1` already used a replacement, this is an ordinary exact continuation. If it has not, it still remains legal under “at most one.”

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Spending the replacement now

Before processing `t[j]`, the exact state has matched `i0` characters of `s`. The current `t[j]` can always match the next `s[i0]` by replacing that source character with `t[j]`.

That creates a one-replacement prefix of length `i0+1`. The best one-replacement progress after considering both possibilities is:



This transition is allowed regardless of whether `s[i0]` originally equals `t[j]`. If they are equal, no replacement is actually needed and the state is still valid under an at-most-one allowance. If they differ, one replacement makes them equal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "cat", "t": "chat"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every replacement:** For each source index and each of 26 letters, running a full subsequence check costs `O(26ST)` in the straightforward form. The two-progress scan considers all replacement moments together.
- **Dynamic programming over both strings and replacement count:** A table can solve the problem in `O(ST)` time and space, but subsequence matching needs only the farthest prefix for each budget.
- **Keep only `i1`:** This loses the less-advanced exact route that still has its replacement available for a later mismatch.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T)$. Let
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
