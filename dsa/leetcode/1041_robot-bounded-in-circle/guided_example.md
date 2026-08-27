# Guided Example: Robot Bounded In Circle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"instructions": "GGLLGG"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

On an infinite plane, a robot initially stands at `(0, 0)` and faces north. Note that:

The objective is to compute `true` from `{"instructions": "GGLLGG"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One execution tells us the repeated behavior

The instruction string repeats forever, but it is unnecessary to simulate forever. After one complete execution, only two facts matter:

- The robot's displacement from where that execution began.
- The direction the robot now faces relative to its starting direction.

If the displacement is zero, the robot is back at the same position after one cycle. Repeating the same finite path remains bounded, regardless of its ending direction.

If the displacement is nonzero but the ending direction has rotated, later cycles rotate that displacement. The rotated vectors cancel after at most four repetitions.

The only unbounded case is nonzero displacement while still facing the original direction. Every repetition then adds the same translation and carries the robot farther away along a straight sequence of cycle endpoints.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"instructions": "GGLLGG"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Direction encoding in the exact solution

The code uses:

- `k = 0` for north.
- `k = 1` for west.
- `k = 2` for south.
- `k = 3` for east.

This order moves counterclockwise as the index increases.

A left turn therefore uses `k = (k + 1) % 4`. From north it goes to west, and from east index three it wraps to north.

A right turn is one step clockwise, equivalent to three steps counterclockwise, so it uses `k = (k + 3) % 4`. Modulo keeps the direction inside zero through three.

The encoding differs from the common north-east-south-west order, but it is internally consistent.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The code uses:

- `k = 0` for north.
- `k = 1` for west.
- `... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count movement by direction instead of storing coordinates

`dist` contains four counters. Each `G` increments `dist[k]` for the direction currently faced.

After the whole string:

- Net vertical displacement is `dist[0] - dist[2]` because north and south oppose each other.
- Net horizontal displacement is `dist[3] - dist[1]` because east and west oppose each other.

The robot returns to the starting position exactly when north steps equal south steps and west steps equal east steps:

`dist[0] == dist[2] and dist[1] == dist[3]`.

Actual `x` and `y` coordinates are unnecessary because only a zero-versus-nonzero displacement test is needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"instructions": "GGLLGG"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Track explicit coordinates:** Use a four-direc:** - **Track explicit coordinates:** Use a four-direction vector array and update `x` and `y` on each `G`. This is equally correct; the exact solution's opposite-direction counts encode only the zero-displacement information needed.
- **Simulate four cycles:** After four repetitions, any changed orientation returns to north, and a bounded path returns to its starting state. This works in `O(M)` time with a larger constant but is unnecessary.
- **Search for repeated states indefinitely:** Position is unbounded in the false case, so open-ended simulation has no useful stopping rule. The one-cycle theorem supplies one.
- **Only `G` instructions:** Final direction remains north. The nonzero north displacement makes every nonempty such string unbounded.
- **Only turns:** All distance counters remain zero, so the robot stays at the origin and returns true.
- **Net rotation 180 degrees:** Two cycle displacement vectors cancel, so boundedness is detected by `k != 0`.
- **Net rotation 90 or 270 degrees:** Four rotated displacement vectors cancel.
- **Return to origin facing north:** The first condition returns true; every repetition traces exactly the same path.
- **Return to origin facing another direction:** It is still bounded, and both conditions may be true.
- **Nonzero displacement facing north:** This is the unique false case and causes linear drift.
- **Different direction index conventions:** North-east-south-west would use different left and right updates. The exact counter interpretation must stay aligned with north-west-south-east.
- **Modulo wraparound:** Four left or four right turns restore `k = 0`, correctly representing a full rotation.
- **Finite within-cycle excursions:** Even if one cycle travels far before returning or rotating, the instruction string has finite length. Periodic repetition still fits inside a sufficiently large circle.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M)$. Let `M = len(instructions)`. The loop reads every instruction once and performs constant work. Time complexity is `O(M)`, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
