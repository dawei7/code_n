# Guided Example: Next Greater Element II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1]}`
- **Required output:** `[2, -1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a circular integer array `nums` (i.e., the next element of $nums[\text{nums.length} - 1]$ is $\text{nums}[0]$), return *the **next greater number** for every element in* `nums`.

The objective is to compute `[2, -1, 2]` from `{"nums": [1, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

For one position `i`, the next greater value may lie later in the ordinary array or may appear after wrapping from the final position back to index zero. Conceptually concatenating `nums` with itself turns that circular search into an ordinary rightward search. The source simulates this doubled array with modular indices instead of allocating a second copy.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`ans` begins as `[-1] * n`. The sentinel is already correct for any value that never finds a strictly greater element. `stk` is a monotonic stack of values seen to the right in the conceptual doubled traversal.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The loop counts backward from `2 * n - 1` through zero, exactly `2n` iterations. Each raw loop index is replaced by `i %= n`, mapping the second conceptual copy and the first copy onto the real array positions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, -1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, -1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Brute-force circular scan:** For each position, inspect up to `n - 1` successors with modulo indexing. This costs $O(n^2)$ time.
- **Explicit doubled array:** Concatenate `nums + nums` and run a normal next-greater algorithm. It is correct but uses another $O(n)$ array that modular indexing avoids.
- **Forward unresolved-index stack:** Traverse two copies left to right and resolve indices when a greater value arrives. It also runs in $O(n)$ but requires care not to push first-copy indices repeatedly.
- **All values equal:** Every equal candidate is popped, so all answers remain `-1`.
- **Strictly decreasing ordinary order:** Several positions find answers only after wrapping; the maximum value still has no greater answer.
- **Single element:** Both conceptual occurrences are equal and pop each other, leaving the only answer `-1`.
- **Duplicate values:** Equality does not satisfy “greater,” so the pop condition must be `<=` rather than `<`.
- **Negative values:** Ordering comparisons work unchanged, and `-1` is an output sentinel rather than a candidate value. A legitimate next greater value can itself be `-1`, but the returned numeric result is still correct.
- **Answer overwritten twice:** The preliminary second-copy assignment may be incomplete. The final first-copy pass intentionally overwrites it after all wrapped candidates are available.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop performs `2n` iterations. Every pushed occurrence can be popped at most once. Although one iteration may pop many values, total pushes and pops are linear in the doubled traversal, so time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
