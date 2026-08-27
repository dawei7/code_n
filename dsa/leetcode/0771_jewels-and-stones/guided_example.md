# Guided Example: Jewels and Stones

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"jewels": "aA", "stones": "aAAbbbb"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

The objective is to compute `3` from `{"jewels": "aA", "stones": "aAAbbbb"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert jewel types into a membership set

Each character in `jewels` names one stone type that should be counted. The question for every owned stone is simply whether its character belongs to that collection.

The solution creates

`s = set(jewels)`.

Set membership is expected constant time, so the jewel description is processed once instead of rescanned for every stone.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"jewels": "aA", "stones": "aAAbbbb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count stones, not distinct types

The generator tests every character `c` in `stones` independently:

`c in s`.

If three owned stones have jewel types, all three must count even if some share the same character. This is why `stones` itself is not converted to a set.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The generator tests every character `c` in `stones` independ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sum Boolean results

Membership returns `true` for a jewel and `false` otherwise. Python treats these as one and zero in arithmetic. `sum` therefore adds one for every jewel stone and zero for every ordinary stone.

The generator is lazy, so it does not allocate a list of Boolean values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"jewels": "aA", "stones": "aAAbbbb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Nested scans:** Check each stone against every:** - **Nested scans:** Check each stone against every jewel character. This costs `O(jslen)` and repeats work.
- **- **Frequency counter for stones:** Count every st:** - **Frequency counter for stones:** Count every stone type, then sum jewel frequencies. It is correct but stores more information than necessary.
- **- **Convert stones to a set:** This is incorrect b:** - **Convert stones to a set:** This is incorrect because repeated physical stones must each count.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(slen)$. Let `j` be the jewel-string length and `slen` the stone-string length. Building the set takes expected `O(j)` time, and scanning stones takes expected `O(slen)`. Total expected time is `O(j + slen)`.
- **Auxiliary Space Complexity:** $O(j)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
