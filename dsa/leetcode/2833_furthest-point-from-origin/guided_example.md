# Guided Example: Furthest Point From Origin

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"moves": "L_RL__R"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `moves` of length `n` consisting only of characters `'L'`, `'R'`, and `'_'`. The string represents your movement on a number line starting from the origin `0`.

The objective is to compute `3` from `{"moves": "L_RL__R"}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate fixed displacement from flexible moves.** Every `L` contributes one step left, or negative one. Every `R` contributes one step right, or positive one. Underscores can later be assigned either contribution.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"moves": "L_RL__R"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Let $L$, $R$, and $B$ be the counts of `L`, `R`, and underscore respectively. Before choosing underscore directions, the fixed endpoint is

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"moves": "L_RL__R"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Literal single loop:** Maintain a signed fixed displacement and underscore count in one traversal, then return absolute displacement plus blanks. This performs one physical pass with the same bounds.
- **Try both extremes:** Compute final coordinate when all underscores are left and when all are right, then take the larger absolute value. These are the only extreme assignments needed and yield the same formula.
- **Enumerate underscore choices:** Testing all $2^B$ assignments is unnecessary because the triangle inequality proves an extreme assignment is optimal.
- **No underscores:** The answer is simply the absolute difference between fixed left and right counts.
- **Only underscores:** All can point the same way, so the answer is the string length.
- **Balanced fixed moves:** Fixed displacement is zero; either uniform underscore direction reaches distance $B$.
- **More left moves:** Assign all underscores left.
- **More right moves:** Assign all underscores right.
- **One underscore:** It always adds one to the maximum fixed distance, including a fixed tie.
- **Move order:** It would matter for a maximum intermediate distance question, but not for the final coordinate asked here.
- **Three physical scans:** The exact count-based expression is still $O(n)$ even though it is not a single traversal internally.
- **Input preservation:** Strings are immutable, and no modified movement string is built.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(moves)`. Each call to `moves.count(character)` scans the string in $O(n)$ time. There are three calls, so exact work is $3n$ character checks up to implementation constants, which is $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
