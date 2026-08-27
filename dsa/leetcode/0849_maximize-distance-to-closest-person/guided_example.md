# Guided Example: Maximize Distance to Closest Person

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"seats": [1, 0, 0, 0, 1, 0, 1]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array representing a row of `seats` where $\text{seats}[i] = 1$ represents a person sitting in the $$i^{\text{th}}$$ seat, and $\text{seats}[i] = 0$ represents that the $$i^{\text{th}}$$ seat is empty **(0-indexed)**.

The objective is to compute `2` from `{"seats": [1, 0, 0, 0, 1, 0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every empty seat lies in one of three gap types

Occupied seats divide the row's empty seats into:

- a leading gap before the first occupied seat;
- internal gaps between two occupied seats;
- a trailing gap after the last occupied seat.

The best distance formula differs at the ends because an end gap has a person on only one side. Scanning occupied-seat indices is enough to measure all three types.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"seats": [1, 0, 0, 0, 1, 0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track first, last, and largest occupied-to-occupied gap

`first` stores the first occupied index encountered. `last` stores the most recent occupied index. Both begin as `null`.

When a new occupied seat at index `i` is found:

- if `last` exists, `i-last` is the distance between consecutive occupied seats; `d` retains the maximum such distance;
- if `first` is still `null`, set it to `i`;
- update `last=i`.

Only occupied seats matter as boundaries. Runs of zeroes need no per-run counter because their length follows from adjacent occupied indices.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `first` stores the first occupied index encountered.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Leading gap

If the first occupied seat is at index `first`, seats 0 through `first-1` are empty. Sitting at index 0 maximizes distance within this gap, and the nearest person is `first` seats away.

Thus, the leading candidate is simply `first`.

For `[0,0,1]`, `first=2` and the best leading distance is two.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"seats": [1, 0, 0, 0, 1, 0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Distance array from two passes:** Compute near:** - **Distance array from two passes:** Compute nearest occupied distance from left and right for every seat. It is linear-time but uses `O(n)` space.
- **- **Store all occupied indices:** Then inspect gap:** - **Store all occupied indices:** Then inspect gaps. It works but the running `first`, `last`, and `d` values are sufficient.
- **- **Expand from every empty seat:** Searching outw:** - **Expand from every empty seat:** Searching outward separately can become quadratic.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(seats)`. The algorithm scans the array once and performs constant work at occupied positions. Time complexity is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
