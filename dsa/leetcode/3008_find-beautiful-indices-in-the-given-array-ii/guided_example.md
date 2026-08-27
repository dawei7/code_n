# Guided Example: Find Beautiful Indices in the Given Array II

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

### Step 1: Find all starts without quadratic matching

An index `i` is eligible only when pattern `a` starts there. It is beautiful when at least one start `j` of pattern `b` satisfies `|i-j| <= k`.

The large constraints make repeated substring comparison unsuitable. The exact solution uses KMP twice to obtain sorted occurrence lists `resa` and `resb`, then merges those lists with one forward-only proximity pointer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "isawsquirrelnearmysquirrelhouseohmy", "a": "my", "b": "squirrel", "k": 15}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Prefix functions capture reusable pattern borders

For each pattern, the prefix function at index `i` stores the longest length that is both a proper prefix of the pattern and a suffix of the prefix ending at `i`.

During construction, mismatch fallback `j = prefix_function[j - 1]` tries the next viable border. Characters already known to match are not reread from scratch. Both `i` and total fallback movement are linear in pattern length.

Patterns `a` and `b` receive independent prefix arrays.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each pattern, the prefix function at index `i` stores th... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: KMP reports overlapping matches

During text search, `j` is the current matched pattern-prefix length. Mismatches follow prefix links; matches advance `j`.

When a complete pattern ends at text index `i`, the start `i - j + 1` is appended. Then `j` falls back to the longest border rather than zero. This permits overlaps, such as both starts of `"aaa"` inside `"aaaa"`.

Each text scan is linear because fallback never causes the text index to move backward. Occurrences are appended in ascending start order.

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

- **- **Naive substring comparisons:** They can cost $:** - **Naive substring comparisons:** They can cost $O(N(A+B))$ in the large version.
- **Z algorithm:** It can find each occurrence list in linear time and is a valid alternative to KMP.
- **Binary-search `resb` for every `a`:** This costs $O(P\log Q)$; the monotone pointer uses list ordering more fully.
- **Overlapping pattern matches:** KMP’s post-match fallback preserves them.
- **`a` or `b` longer than `s`:** Its occurrence list is empty and the result is naturally empty.
- **`a == b`:** Every occurrence witnesses itself at distance zero.
- **Many witnesses:** A beautiful start appears only once.
- **Sorted result:** Occurrence discovery and append order already satisfy it.
- **Debug print:** Exact source emits potentially huge internal lists and is not production-clean.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+A+B)$. Let $N=|s|$, $A=|a|$, $B=|b|$, with $P$ and $Q$ occurrences. Prefix construction is $O(A+B)$; both searches total $O(N)$ up to a constant factor; merging is $O(P+Q)$. Algorithmic time is $O(N+A+B)$ because $P,Q=O(N)$.
- **Auxiliary Space Complexity:** $O(N+A+B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
