# Guided Example: Find Beautiful Indices in the Given Array I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "isawsquirrelnearmysquirrelhouseohmy", "a": "my", "b": "squirrel", "k": 15}`
- **Required output:** `[16, 33]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** string `s`, a string `a`, a string `b`, and an integer `k`.

The objective is to compute `[16, 33]` from `{"s": "isawsquirrelnearmysquirrelhouseohmy", "a": "my", "b": "squirrel", "k": 15}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate pattern matching from proximity matching

An index can be beautiful only if pattern `a` starts there. It then needs at least one occurrence of `b` whose start lies within distance `k`. The exact solution first creates two sorted occurrence lists and then matches their positions.

It uses Knuth–Morris–Pratt search rather than repeatedly slicing the text. Although this version limits pattern lengths to ten, `s` can have length $10^5$, and KMP provides a clean linear bound.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "isawsquirrelnearmysquirrelhouseohmy", "a": "my", "b": "squirrel", "k": 15}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build each prefix function

For a pattern, `prefix_function[i]` is the length of the longest proper prefix that is also a suffix of `pattern[:i + 1]`.

Variable `j` is the current matched prefix length. On a mismatch, `j = prefix_function[j - 1]` falls back to the next possible border instead of restarting at zero and rechecking known characters. On a match, `j` advances. Each pattern index moves forward once, while fallback movement is amortized linear.

Separate tables are built for `a` and `b` because their border structures differ.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Search while preserving overlapping occurrences

`kmp_search` scans `s` left to right. `j` records how many pattern characters match the suffix ending just before the current text character. Mismatch fallback and match advancement mirror prefix construction.

When `j == len(pattern)`, a full occurrence ends at text index `i`, so its start is `i - j + 1`. The code appends that start, then sets `j = prefix_function[j - 1]`.

That fallback after a match is essential for overlaps. Searching `"aaa"` in `"aaaa"` finds starts zero and one. Resetting `j` to zero would miss the second occurrence.

Since text scanning is left to right, both `resa` and `resb` are sorted ascending.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[16, 33]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "isawsquirrelnearmysquirrelhouseohmy", "a": "my", "b": "squirrel", "k": 15}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[16, 33]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeated slicing with `find`:** Pattern lengths are small here, but careful overlap advancement is still required; KMP gives a general linear guarantee.
- **Binary search each `a` occurrence:** Searching `resb` for neighbors costs $O(P\log Q)$; the monotone pointer is linear.
- **Reset the KMP state after a match:** Resetting to zero misses overlapping occurrences.
- **No `a` occurrences:** The outer loop is empty and the answer is empty.
- **No `b` occurrences:** No candidate can satisfy proximity, so the answer is empty.
- **`a == b`:** An occurrence can witness itself with distance zero.
- **Several nearby `b` starts:** Each `a` index is appended only once because the condition is existential.
- **Sorted output:** KMP discovery order and outer traversal already provide it.
- **Debug print:** The exact source leaks full occurrence arrays and should be cleaned in a separate solution-fix campaign.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+A+B)$. Let $N=|s|$, $A=|a|$, and $B=|b|$. Prefix construction costs $O(A+B)$. The two KMP scans cost $O(N)$ each. The monotone merge costs $O(P+Q)$ for occurrence counts $P,Q\le N$. Total algorithmic time is $O(N+A+B)$.
- **Auxiliary Space Complexity:** $O(N+A+B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
