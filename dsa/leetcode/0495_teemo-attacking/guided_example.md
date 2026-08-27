# Guided Example: Teemo Attacking

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"timeSeries": [1, 4], "duration": 2}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly `duration` seconds. More formally, an attack at second `t` will mean Ashe is poisoned during the **inclusive** time interval `[t, t + duration - 1]`. If Teemo attacks again **before** the poison effect ends, the timer for it is **reset**, and the poison effect will end `duration` seconds after the new attack.

The objective is to compute `4` from `{"timeSeries": [1, 4], "duration": 2}` while avoiding redundant calculations and unnecessary overhead.

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

An attack at time `t` poisons the inclusive seconds from `t` through `t + duration - 1`. Although the statement uses inclusive integer seconds, each attack still contributes exactly `duration` seconds when its interval does not overlap another attack.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"timeSeries": [1, 4], "duration": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The array is already sorted in non-decreasing order, so poison intervals appear in chronological order. The task is equivalent to measuring the length of their union. Instead of constructing every interval or simulating every poisoned second, the solution measures how much new poisoned time each attack contributes before the next attack resets the timer.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The array is already sorted in non-decreasing order, so pois... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Contribution between consecutive attacks.** Consider attacks at times `a` and `b`, where `b >= a`. The poison started at `a` would last for `duration` seconds. There are two cases.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"timeSeries": [1, 4], "duration": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit interval merging:** Construct `[t, t :** - **Explicit interval merging:** Construct `[t, t + duration)` intervals and merge overlaps. It works but stores unnecessary interval data when chronological gaps alone determine the union length.
- **Simulate every second:** Marking poisoned timestamps can require work proportional to the numeric timeline rather than the number of attacks, which is wasteful for large times and durations.
- **Unsorted input:** The one-pass gap reasoning depends on non-decreasing times. Without that guarantee, sort first at $O(n\log n)$ cost.
- **Overlapping attacks:** Add only the gap to the next attack, preventing overlap from being counted twice.
- **Non-overlapping attacks:** A gap at least as large as `duration` contributes the full duration.
- **Duplicate timestamps:** Their gap is zero, so an immediate reset adds no separate earlier interval.
- **Zero duration:** Every contribution is zero and the result is zero.
- **Single attack:** `pairwise` yields nothing, and the initialized `duration` is exactly the answer.
- **Inclusive seconds:** `b - a` already counts the integer seconds from `a` through `b - 1`; no extra one belongs in the formula.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of attack times. `pairwise` yields $n - 1$ adjacent pairs lazily, and the loop does constant work for each one. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
