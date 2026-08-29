# Guided Example: Letter Combinations of a Phone Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"digits": "2"}`
- **Required output:** `["a", "b", "c"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

The objective is to compute `["a", "b", "c"]` from `{"digits": "2"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build the Cartesian product one digit at a time

Each input digit contributes one independent choice of letter. A complete result selects exactly one letter from the mapping for position `0`, one for position `1`, and so on. Mathematically, the answer is the Cartesian product of the per-digit letter sets.

The list



stores mappings for digits `2` through `9`. Because list index zero represents digit `2`, a digit character `i` maps to index `int(i) - 2`. The constraints guarantee no `0` or `1`, so every access is valid.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"digits": "2"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Start with one empty partial combination

The algorithm initializes



This is not a completed answer for non-empty input. It is the identity element for concatenation: there is exactly one way to choose letters from zero processed digits, namely the empty prefix.

Starting with `[]` would fail because the nested comprehension would have no existing prefix to extend and would remain empty forever.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Extend every old prefix with every current letter

For one digit, let `s` be its mapped letters. The update is



The outer comprehension loop chooses every partial prefix `a`; the inner loop attaches each possible current letter `b`. If `ans = ["a", "b", "c"]` and `s = "def"`, the new list is



No prefix is lost, and no current choice is omitted.

Notice that this update does not modify strings already inside the old `ans`. Strings are immutable, so every `a + b` expression creates a separate extended prefix. Rebinding the name `ans` happens only after the entire new list has been constructed. Consequently, the comprehension can safely read every old prefix while producing the next layer, with no risk that newly created prefixes will themselves be extended during the same digit.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["a", "b", "c"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"digits": "2"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["a", "b", "c"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive backtracking:** Append one choice, recurse to the next digit, then pop. It has the same output time and $O(n)$ auxiliary path space excluding results.
- **Mixed-radix enumeration:** Number combinations from `0` to `P - 1` and decode each position using the corresponding choice count. This avoids recursive state but requires careful index arithmetic.
- **Queue-style breadth-first expansion:** Repeatedly remove partial prefixes and append extensions. It expresses the same Cartesian product with more mutation.
- **One digit:** The empty identity prefix expands directly to that digit's three or four letters.
- **Digits `7` and `9`:** They have four choices and determine the worst-case branching factor.
- **Repeated digits:** Positions are independent; `"22"` correctly includes `"aa"`, `"ab"`, and all nine ordered choices.
- **No `0` or `1`:** The contract excludes unmapped digits, so no missing-mapping policy is needed.
- **Input preservation:** The digit string and mapping are read-only; every result string is newly created.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(nP)$. Let $n$ be the number of digits and let
- **Auxiliary Space Complexity:** $O(nP)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
