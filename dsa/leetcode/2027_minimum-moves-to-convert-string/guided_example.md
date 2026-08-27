# Guided Example: Minimum Moves to Convert String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "XXX"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of `n` characters which are either `'X'` or `'O'`.

The objective is to compute `1` from `{"s": "XXX"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Always address the leftmost unresolved `X`

The scan index `i` represents the first position not already handled by an earlier conceptual move. If `s[i]` is `O`, that position needs no work, so the code advances by one.

If `s[i]` is `X`, at least one additional move is unavoidable. Earlier decisions have already handled every index before `i`, and leaving this `X` untouched cannot lead to an all-`O` string. The source counts one move and advances `i` by three.

That jump represents converting the current character and the following two positions to `O`. Their original values do not matter: an `X` becomes `O`, while an `O` remains `O`. Consequently none of those three positions can require another move.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "XXX"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why beginning at the current position is the best greedy choice

Suppose the leftmost unresolved `X` occurs at index `i` and there are at least three positions beginning there. Any successful solution must use some move whose length-three interval covers `i`. Starting the move earlier would spend part of its coverage on positions before `i`, which the scan has already resolved. Starting it at `i` covers `i` and reaches as far to the right as possible, through `i+2`.

There is no penalty for changing an already-`O` character again, so maximizing rightward coverage cannot make a future position harder. This greedy move handles the mandatory current `X` while covering at least as much still-unresolved territory as any alternative move that also covers it.

The code does not construct a mutable copy of the string. The jump is sufficient bookkeeping: after counting the conceptual move, it never inspects the two newly covered positions because their post-move values are known to be `O`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose the leftmost unresolved `X` occurs at index `i` and ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The special case near the right boundary

If the first unresolved `X` is one of the final two characters, a literal window starting at `i` would extend beyond the string. The count is still correct. Because the input length is at least three, choose the last valid window, covering indices `n-3` through `n-1`. It includes the tail `X` and may overlap positions the scan already considered.

That overlap is harmless: applying a move to `O` leaves it `O`, and there are no unprocessed positions beyond the end. The source's `i += 3` should therefore be understood as “this move finishes the remaining tail,” not as constructing an out-of-bounds substring.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "XXX"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Mutate a character array:** Explicitly write `:** - **Mutate a character array:** Explicitly write `O` into three positions after each move; it is still $O(N)$ but uses $O(N)$ space and performs unnecessary writes.
- **Dynamic programming:** One can model which recent positions are covered, but the forced leftmost-`X` choice makes that machinery unnecessary.
- **Count each run independently:** This can overlook a move that covers `X` characters on both sides of a short `O` gap.
- **All `O` characters:** The loop only takes one-step advances and returns zero.
- **Exactly three `X` characters:** The first iteration counts one move and jumps to the end.
- **A single `X` in the middle:** One move covers it and its two following positions whenever that start is in range.
- **A single `X` at the final index:** Use the final legal three-character window; the source's jump records the correct one move.
- **A tail of one or two unresolved positions:** One final move is enough because it may overlap already resolved positions.
- **Existing `O` inside a chosen block:** It remains `O` and does not waste correctness, even though it occupies coverage.
- **Overlapping moves:** Allowed and sometimes necessary near the end; repeated conversion to `O` has no adverse effect.
- **Long `X` run:** Each move handles the next three unresolved positions, giving the unavoidable ceiling of run length divided by three when no neighboring coverage changes the grouping.
- **Minimum input length:** The guarantee $N\ge3$ ensures a valid final three-character window exists for a tail `X`.
- **Input preservation:** The algorithm reasons about moves without modifying `s`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert s\rvert$. The index always increases, by one for an `O` or by three for an `X`. No position is revisited by the loop, so there are at most $N$ iterations and the running time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
