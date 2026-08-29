# Guided Example: Maximum Total Area Occupied by Pistons

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"height": 5, "positions": [2, 5], "directions": "UD"}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are several pistons in an old car engine, and we want to calculate the **maximum** possible area **under** the pistons.

The objective is to compute `7` from `{"height": 5, "positions": [2, 5], "directions": "UD"}` while avoiding redundant calculations and unnecessary overhead.

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

Each piston follows a triangular wave between zero and `height`. Its position changes linearly with slope plus one while moving up and minus one while moving down. The total area is the sum of positions, so it is also piecewise linear. A maximum of a linear segment occurs at an endpoint; only direction-change times need to be examined.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"height": 5, "positions": [2, 5], "directions": "UD"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

At time zero, `res` is the sum of all positions. `diff` is the total slope: add one for each upward piston and subtract one for each downward piston.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Dictionary `delta` stores how the total slope changes at future event times within one full period of length `2 * height`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"height": 5, "positions": [2, 5], "directions": "UD"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate every second:** The period can be $2\cdot10^6$ and there can be $10^5$ pistons, making direct simulation far too costly.
- **Evaluate every piston at every event:** There are $O(n)$ events and pistons, causing $O(n^2)$ work. Slope deltas update the total in constant time per event.
- **Use trigonometric formulas:** Motion is a triangular, not sinusoidal, wave; piecewise-linear events are exact and simpler.
- **All pistons move up:** Initial slope is positive until the earliest top event, which the sweep reaches directly.
- **All move down:** Time zero may already be the maximum; initializing `ans = res` preserves it.
- **Several simultaneous bounces:** Their deltas sum in one dictionary entry.
- **Piston at zero moving down:** A time-zero plus-two delta turns its effective slope upward.
- **Piston at height moving up:** A time-zero minus-two delta turns it downward.
- **One piston:** Its maximum is `height`, found at its top event or initially.
- **Flat total segment:** Zero total slope means every point on that segment has equal area, and either endpoint represents it.
- **Period endpoint:** The total returns to its time-zero value; including events through the period cannot introduce an unrepresented larger value.
- **Area interpretation:** Each piston's current position equals its area contribution under the stated model, so summing positions is the requested total.
- **Events beyond the first bounce:** Each piston needs exactly two events in one full period. Its later bounces are those same event phases shifted by `2 * height` and cannot create a new total pattern.
- **Slope update ordering:** `res` advances using the old slope up to `cur`, then `diff` changes. Applying the delta first would incorrectly use the post-bounce direction during the interval before the bounce.
- **Initial maximum:** `ans` is initialized before sweeping because a strictly decreasing total can be greatest at time zero, which may not otherwise appear as a positive-time event.
- **Dictionary cancellation:** Opposite slope changes from different pistons at the same time can sum to zero. Keeping the event is harmless; the value is still checked at a legitimate linear-segment boundary.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let $n$ be the piston count. Each piston contributes at most two event keys, so building state takes $O(n)$. Sorting at most $2n$ events costs $O(n\log n)$; the sweep is linear.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
