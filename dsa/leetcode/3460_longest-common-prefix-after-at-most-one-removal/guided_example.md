# Guided Example: Longest Common Prefix After at Most One Removal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "madxa", "t": "madam"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `t`.

The objective is to compute `4` from `{"s": "madxa", "t": "madam"}` while avoiding redundant calculations and unnecessary overhead.

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

**Use two indices because only \(s\) may lose a character.** `i` points into `s` and `j` points into `t`. `j` is also the number of target-prefix characters successfully matched so far. `rem` records whether the one allowed deletion from `s` has already been used.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "madxa", "t": "madam"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

When `s[i] == t[j]`, the characters extend the common prefix. Both strings advance: the source increments `j` inside the equality branch and increments `i` at the end of the loop.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

When they differ and no removal has been used, the only way to continue matching this same `t[j]` is to delete `s[i]`. The source marks `rem = true`, leaves `j` unchanged, and advances only `i`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "madxa", "t": "madam"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try deleting every position:** Recomputing a prefix for each choice can take $O(n^2)$ time.
- **Dynamic programming:** A two-state matched-prefix DP works but is unnecessary because the first useful deletion is forced.
- **Delete from \(t\):** The operation permits removal only from `s`; `j` must never skip.
- **No mismatch:** No removal is needed, and the shorter-string length is returned.
- **Mismatch at index zero:** The source correctly tries deleting the first character of `s`.
- **Second mismatch:** With the budget spent, matching stops immediately.
- **\(s\) one character longer:** One deletion may allow all of `t` to match.
- **\(t\) longer than \(s\):** At most the available post-deletion characters can contribute.
- **At most one removal:** Leaving `rem` false is a valid outcome.
- **Input preservation:** Indices scan immutable strings without constructing modified copies.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\min(n,m+1)$. Each loop iteration advances `i`, and `j` never decreases. At most `len(s)` iterations occur, stopping no later than target exhaustion. Time is $O(\min(n,m+1))$, conventionally stated as $O(\min(n,m))$ up to the one possible skipped character.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
