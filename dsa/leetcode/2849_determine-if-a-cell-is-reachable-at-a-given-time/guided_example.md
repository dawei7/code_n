# Guided Example: Determine if a Cell Is Reachable at a Given Time

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sx": 2, "sy": 4, "fx": 7, "fy": 7, "t": 6}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given four integers `sx`, `sy`, `fx`, `fy`, and a **non-negative** integer `t`.

The objective is to compute `true` from `{"sx": 2, "sy": 4, "fx": 7, "fy": 7, "t": 6}` while avoiding redundant calculations and unnecessary overhead.

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

**Find the minimum number of seconds first.** One move may change the x-coordinate by at most one and the y-coordinate by at most one. A diagonal move changes both simultaneously.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sx": 2, "sy": 4, "fx": 7, "fy": 7, "t": 6}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

$$
d_x=|\texttt{sx}-\texttt{fx}|,\qquad
d_y=|\texttt{sy}-\texttt{fy}|.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

At least `max(dx, dy)` moves are necessary because the larger coordinate difference can shrink by at most one per second.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sx": 2, "sy": 4, "fx": 7, "fy": 7, "t": 6}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Breadth-first search:** It can solve small bounded coordinates but is impossible on an infinite grid with billion-scale positions and time.
- **Simulate a shortest path:** This would take $O(t)$ time despite the direct distance formula.
- **Same cell, zero seconds:** No movement is needed, so true is correct.
- **Same cell, one second:** Mandatory movement makes it the unique false exception when distance is within time.
- **Same cell, at least two seconds:** An adjacent-cell detour returns to the start.
- **Different adjacent cells:** One second is sufficient; larger times can be padded.
- **Only one coordinate differs:** Chebyshev distance equals that straight-line difference.
- **Both coordinates differ equally:** Every shortest move can be diagonal.
- **Unequal coordinate differences:** Use diagonal moves for the smaller difference and continue along the larger dimension.
- **No parity restriction:** Eight-direction movement permits odd or even extra time for distinct endpoints.
- **Infinite grid:** Detours never encounter boundaries or obstacles.
- **Mandatory move each second:** This creates the same-cell one-second exception and forbids simply waiting.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method performs a constant number of equality checks, subtractions, absolute values, a maximum, and one comparison. Time is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
