# Guided Example: Maximum Good People Based on Statements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"statements": [[2, 1, 2], [1, 2, 2], [2, 0, 2]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are two types of persons:

The objective is to compute `2` from `{"statements": [[2, 1, 2], [1, 2, 2], [2, 0, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Encode an assignment as a mask

For a mask `mask`, bit `i` is one when person `i` is assumed good and zero when assumed bad. The expression `mask >> i & 1` extracts that bit.

The outer generator tests masks from `1` through `(1 << n) - 1`. These are all non-empty candidate good sets. The all-bad mask is omitted, but its good-person count would be zero. Every invalid mask also returns zero from `check`, so omitting the all-bad assignment cannot increase or decrease the maximum numeric answer.

Since $n \ge 2$, the range of non-empty masks itself is not empty.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"statements": [[2, 1, 2], [1, 2, 2], [2, 0, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Ignore statements from assumed bad people

The helper loops through people `i` and their statement row. It enters the inner validation loop only when `mask >> i & 1` is one.

This is not an optimization that weakens the rules. It exactly reflects the definition: a bad person might make either a true or false statement, so no observation from that row can contradict an assignment. Requiring bad people to lie would be incorrect.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The helper loops through people `i` and their statement row.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Validate every informative statement from a good person

For each entry `x = statements[i][j]`:

- `x == 0` says person `j` is bad;
- `x == 1` says person `j` is good;
- `x == 2` gives no information.

The condition `x < 2` selects only actual claims. For such a claim, `mask >> j & 1` is the assumed status of person `j`. If it differs from `x`, a person assumed good has made a false statement, so the entire mask is impossible and `check` returns zero immediately.

Statements with value two are skipped. The diagonal is always two, but the same logic safely handles every no-statement entry.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"statements": [[2, 1, 2], [1, 2, 2], [2, 0, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Backtracking with propagation:** Assign people:** - **Backtracking with propagation:** Assign people one by one and propagate statements from those declared good. Contradiction pruning can reduce practical work but requires more mutable state.
- **Precompute row masks:** Encode each person’s good and bad claims into bitsets, then validate a candidate with bitwise operations. This can improve constants while keeping exponential subset enumeration.
- **Assume bad people always lie:** This is wrong; bad people may tell the truth or lie, so their rows must be ignored rather than inverted.
- **All-good mask:** It is valid only if every explicit statement made by every person labels everyone consistently with good status.
- **All-bad assignment:** It is always logically possible because no truth constraints remain. The code omits mask zero, but invalid non-empty checks return zero, so the maximum still correctly can be zero.
- **One assumed-good person:** Only that person’s row constrains the assignment; every assumed-bad row is irrelevant.
- **No-statement value two:** It must never be compared with a status bit. The `x < 2` guard excludes it.
- **Self entries:** They are guaranteed to be two, so no person constrains their own status directly.
- **Mutually supportive people:** If two assumed-good people call each other good, those claims are consistent when both bits are one.
- **Contradictory good rows:** If two assumed-good people give opposite statuses for the same person, at least one comparison fails and rejects the mask.
- **Bad truthful statement:** It has no effect, exactly as allowed by “might tell the truth.”
- **Bad false statement:** It likewise has no effect.
- **Early return value zero:** Zero serves both invalid-mask signaling and the size of the omitted all-bad assignment; only the maximum count is needed, so this ambiguity is harmless.
- **Generator memory:** `max(check(i) for i in ...)` streams results rather than allocating an exponential list.
- **Input preservation:** Validation reads the statement matrix and never changes it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^n n^2)$. There are $2^n-1$ tested masks. In the worst case, `check` inspects all $n$ rows and all $n$ entries in each good row, so one mask costs $O(n^2)$. Total worst-case time is $O(2^n n^2)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
