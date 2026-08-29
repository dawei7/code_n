# Guided Example: Car Fleet

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"target": 12, "position": [10, 8, 0, 5, 3], "speed": [2, 4, 1, 1, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.

The objective is to compute `3` from `{"target": 12, "position": [10, 8, 0, 5, 3], "speed": [2, 4, 1, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Arrival time reveals whether a rear car catches the fleet ahead

If a car could drive alone without obstruction, its time to the target would be:

$$
\frac{\texttt{target}-\texttt{position}}{\texttt{speed}}.
$$

Cars cannot pass. Processing them from closest to the target toward farthest lets us compare each rear car's independent arrival time with the arrival time of the fleet directly ahead.

If the rear car would arrive no later, it must catch that fleet by or at the target and join it. If it would arrive later, it cannot catch up before the target and forms a new fleet.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"target": 12, "position": [10, 8, 0, 5, 3], "speed": [2, 4, 1, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort by starting position

`idx` contains car indices sorted by `position[i]` in increasing order. Iterating `idx[::-1]` visits cars from greatest position to smallest: frontmost to rearmost.

Positions are unique, so there is one clear order along the road.

The algorithm sorts indices rather than paired records, preserving access to both original `position` and `speed` arrays.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Meaning of `pre`

`pre` is the arrival time of the last distinct fleet formed among cars already processed ahead.

It starts at zero. Every car starts before the positive target and has positive speed, so every independent arrival time `t` is positive. The frontmost car therefore satisfies `t > pre` and creates the first fleet.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"target": 12, "position": [10, 8, 0, 5, 3], "speed": [2, 4, 1, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort paired position/time records:** This is equivalent and may be more direct. The exact source sorts original indices.
- **Simulate positions over time:** Continuous catch-up events make simulation unnecessarily complex and potentially slow.
- **Monotonic stack:** Arrival times in position order can be pushed and merged with stack logic. The scalar `pre` suffices when scanning from front to back.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of cars. Sorting indices by position takes `O(n\log n)` time. The reverse scan calculates one arrival time and performs constant work per car, taking `O(n)`. Total time is `O(n\log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
