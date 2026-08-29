# Guided Example: Baseball Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["5", "2", "C", "D", "+"]}`
- **Required output:** `30`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

The objective is to compute `30` from `{"operations": ["5", "2", "C", "D", "+"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The operations depend on the most recent valid scores

The record changes over time. A canceled score must disappear, and later `+` or `D` operations refer only to scores still valid after all earlier cancellations.

A stack represents this perfectly:

- its elements are the valid scores in chronological order;
- the top is the most recent valid score;
- the element below the top is the second most recent.

After processing each operation, `stk` is exactly the current record.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["5", "2", "C", "D", "+"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Ordinary integer operation

If `op` is not one of the three command strings, it represents an integer score. `int(op)` parses positive or negative text and the value is appended.

Appending places it at the end of the record and makes it available to future commands.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The plus command

For `+`, the new score is the sum of the previous two valid scores:

`stk[-1] + stk[-2]`.

The source guarantees at least two valid scores whenever this operation occurs. The sum is appended without removing either source score.

It is important that the expression is evaluated before the append. Both negative indices refer to the old record's last two entries.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `30` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["5", "2", "C", "D", "+"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `30` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **List of records with validity flags:** Keep canceled entries and search backward for valid scores. This complicates commands and can make repeated lookups slower than stack removal.
- **Stack plus running total:** Update a total on every append and subtract the popped value on `C`. This avoids the final linear sum but still needs the stack for `+` and `D`.
- **Recompute the record from the beginning for each command:** This repeats work and is unnecessary because stack state is incremental.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the number of operations and `V` the number of scores remaining at the end.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
