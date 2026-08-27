# Guided Example: Walking Robot Simulation II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["Robot", "getPos", "getDir"], "arguments": [[4, 3], [], []]}`
- **Required output:** `[null, [0, 0], "East"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A `width x height` grid is on an XY-plane with the **bottom-left** cell at `(0, 0)` and the **top-right** cell at $(width - 1, height - 1)$. The grid is aligned with the four cardinal directions (`"North"`, `"East"`, `"South"`, and `"West"`). A robot is **initially** at cell `(0, 0)` facing direction `"East"`.

The objective is to compute `[null, [0, 0], "East"]` from `{"operations": ["Robot", "getPos", "getDir"], "arguments": [[4, 3], [], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The robot always follows the perimeter

Starting at the bottom-left corner facing east, the robot moves along the bottom edge, then the right edge, then the top edge, then the left edge, and repeats.

It never enters an interior cell because a turn occurs only when forward movement would leave the rectangle. The complete state can therefore be represented by one distance around this perimeter cycle.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["Robot", "getPos", "getDir"], "arguments": [[4, 3], [], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Measure the side lengths in steps

`mx = width - 1` is the number of horizontal steps between the left and right edges. `my = height - 1` is the vertical step count.

One full circuit uses

`p = 2 * mx + 2 * my`

steps. With width and height at least two, this perimeter length is positive.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `mx = width - 1` is the number of horizontal steps between t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Accumulate steps modulo the perimeter

`cur` is the robot's distance along the cycle from the origin. `step(num)` performs

`cur = (cur + num) % p`.

Moving a full multiple of the perimeter returns to the same cell and post-movement direction, so discarding whole cycles is valid. Each call takes constant time even when `num` is large.

Successive calls compose naturally because each begins from the current cycle distance.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, [0, 0], "East"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["Robot", "getPos", "getDir"], "arguments": [[4, 3], [], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, [0, 0], "East"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Precompute every perimeter state:** Makes quer:** - **Precompute every perimeter state:** Makes queries constant time but uses $O(width+height)$ space.
- **Simulate one step at a time:** Can cost $O(num)$ per call and is unnecessary.
- **No movement yet:** Origin direction is east.
- **Complete positive cycle:** Origin direction is south.
- **Bottom-right corner:** Faces east until another step triggers the turn.
- **Top-right corner:** Faces north.
- **Top-left corner:** Faces west.
- **Large `num`:** Modulo removes complete circuits safely.
- **Several step calls:** Modular distances accumulate exactly.
- **Minimum two-by-two grid:** All four perimeter cells and corner directions remain covered.
- **Position return:** A new two-element list is produced each time.
- **No interior cells:** Boundary-turn rules keep the robot on the perimeter forever.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Q)$. Construction stores five scalar fields and runs in $O(1)$ time. Each `step`, `getPos`, and `getDir` call performs a fixed number of arithmetic operations and comparisons, so each is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
