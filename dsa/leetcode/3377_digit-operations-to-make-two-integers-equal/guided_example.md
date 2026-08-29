# Guided Example: Digit Operations to Make Two Integers Equal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 10, "m": 12}`
- **Required output:** `85`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integers `n` and `m` that consist of the **same** number of digits.

The objective is to compute `85` from `{"n": 10, "m": 12}` while avoiding redundant calculations and unnecessary overhead.

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

**Model every legal integer as a graph node.** A state is a fixed-width integer that is not prime. Two states share a directed edge when one digit can be increased or decreased by exactly one without creating a leading zero and the resulting number is also nonprime.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 10, "m": 12}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The transformation cost includes the original value and every value reached afterward. The source initializes the priority queue with distance `n`. Moving from `cur` to `next_` adds `next_`, so a path's accumulated distance is exactly the required sum of all visited values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Classify primes before searching.** `run_sieve` creates a Boolean array of length 100000. It marks zero and one nonprime, then for each still-prime `i` marks multiples `2*i,3*i,...` composite.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `85` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 10, "m": 12}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `85` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Breadth-first search:** It minimizes operation count rather than the weighted sum and can return the wrong path.
- **A* search:** A valid lower-bound heuristic could reduce exploration, but Dijkstra is simpler and exact for this small universe.
- **Share the sieve globally:** It avoids rebuilding the same 100000-entry classification for every object call.
- **Prime start:** Return `-1` before search.
- **Prime target:** It can never be entered and is rejected immediately.
- **Start equals target:** If nonprime, the heap pops it first and returns `n`, correctly including the initial value.
- **Leading digit one:** It cannot be decremented to zero because width must remain fixed.
- **Internal digit one:** It may be decremented to zero.
- **Digit nine:** It has no increment neighbor.
- **Digit zero:** It has no decrement neighbor.
- **Composite and one:** Both are treated as legal nonprime states.
- **Repeated heap entry:** `visited` discards stale higher-cost copies after the cheapest pop.
- **Unreachable target:** Exhausting the heap proves impossibility.
- **Sieve capacity:** 100000 safely covers all states generated from inputs below 10000.
- **Positive node costs:** They justify Dijkstra finalization and prevent negative cycles.
- **Input preservation:** Strings and temporary digit lists are local; numeric inputs are unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(dU\log U)$. Let $d$ be the digit count and $U$ the number of fixed-width integer states within the sieve range. Each finalized state generates at most $2d$ neighbors. Heap insertion/removal costs $O(\log U)$, giving search time $O(dU\log U)$ in the worst case.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
