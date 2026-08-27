# Guided Example: Rearrange String to Avoid Character Pair

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aabc", "x": "a", "y": "c"}`
- **Required output:** `"cbaa"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and two distinct lowercase English letters `x` and `y`.

The objective is to compute `"cbaa"` from `{"s": "aabc", "x": "a", "y": "c"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why a list is created

Python strings are immutable, so individual character swaps cannot be performed directly on `s`. The source creates:



This list contains exactly the same characters and multiplicities as the input.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aabc", "x": "a", "y": "c"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Boundary pointer invariant

The pointer `i` is the next position where a discovered `y` should be placed.

Before processing scan position `j`, the invariant is:

- positions `0` through `i-1` all contain `y`;
- processed positions `i` through `j-1` contain no `y`;
- positions `j` onward are not yet classified by the scan.

Initially `i=0` and the processed region is empty, so the invariant holds.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The pointer `i` is the next position where a discovered `y` ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handling a non-`y` character

If current `c` is not `y`, no swap occurs. It remains in the processed non-`y` region, and `i` does not move.

The invariant extends to include position `j`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"cbaa"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aabc", "x": "a", "y": "c"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"cbaa"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Build three explicit groups:** Concatenating a:** - **Build three explicit groups:** Concatenating all `y`, neutral characters, and all `x` is valid and matches the manifest summary, but the exact source uses one temporary list and a two-way partition.
- **- **Sort the entire string:** Sorting may place `x:** - **Sort the entire string:** Sorting may place `x` before `y` depending on alphabetic order and costs `O(n\log n)`. The required order is custom and much simpler.
- **- **Count characters and rebuild alphabetically:**:** - **Count characters and rebuild alphabetically:** This can work with special ordering but uses a frequency structure and imposes unnecessary order on neutral letters.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n=\lvert s\rvert`. Creating `t` takes `O(n)` time. The scan visits every position once and performs at most one constant-time swap per character, costing `O(n)`. Joining the list into a result string also costs `O(n)`. Total time complexity is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
