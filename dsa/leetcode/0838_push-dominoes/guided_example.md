# Guided Example: Push Dominoes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"dominoes": "RR.L"}`
- **Required output:** `"RR.L"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

The objective is to compute `"RR.L"` from `{"dominoes": "RR.L"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model time explicitly with a multi-source breadth-first search

Every initially pushed domino begins falling at time zero. Its force moves one position per second in its direction. Because all initial pushes act simultaneously, the natural simulation starts from all `L` and `R` positions at once and expands them in increasing time order.

The queue `q` contains domino indices whose arriving forces are ready to process. Array `time` records the earliest second at which any force reaches each index; `-1` means no force has arrived.

Dictionary `force` stores the force or forces arriving at an index at that earliest time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"dominoes": "RR.L"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize every source

For each non-dot character:

- append its index to `q`;
- set `time[i] = 0`;
- append `L` or `R` to `force[i]`.

All source indices enter the queue before propagation begins. This is what makes the search multi-source and preserves simultaneity.

The answer list starts as all dots. A position changes only when exactly one earliest force controls it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Process only an unopposed force

When index `i` is removed from the queue, the code checks `len(force[i]) == 1`.

If exactly one force arrived at the earliest time, the domino falls in that direction. The code writes that character into `ans[i]` and computes the next index:

- `i-1` for `L`;
- `i+1` for `R`.

If two opposite forces arrived simultaneously, the length is two. The domino remains upright because forces balance, and it does not propagate either force farther. Leaving `ans[i]` as `.` and skipping expansion models both effects.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"RR.L"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"dominoes": "RR.L"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"RR.L"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Segment analysis between non-dot symbols:** Add virtual boundary symbols and resolve `L...L`, `R...R`, `L...R`, and `R...L` intervals directly. It is also linear and uses less explicit simulation state.
- **Net-force accumulation:** Sweep left-to-right for R influence and right-to-left for L influence, then compare magnitudes. This is linear but encodes timing less directly.
- **Second-by-second whole-string simulation:** Repeatedly updating all positions can require `O(n^2)` time before a long chain settles.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(dominoes)`. Each index is enqueued at most once, when its earliest arrival time is assigned. Processing an index and checking or appending forces takes constant time. Propagation examines at most one neighbor because a force moves in only one direction. Total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
