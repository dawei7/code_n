# Guided Example: Last Moment Before All Ants Fall Out of a Plank

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "left": [4, 3], "right": [0, 1]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We have a wooden plank of the length `n` **units**. Some ants are walking on the plank, each ant moves with a speed of **1 unit per second**. Some of the ants move to the **left**, the other move to the **right**.

The objective is to compute `4` from `{"n": 4, "left": [4, 3], "right": [0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why collisions look more complicated than they are

At first, simulating positions, collision times, and direction changes seems necessary. The key simplification is that every ant moves at the same speed and ants are indistinguishable for the requested answer.

When a right-moving ant meets a left-moving ant, both reverse direction. Geometrically, this produces the same occupied positions over time as allowing the two ants to pass through each other. In the collision interpretation, the physical ants exchange velocities. In the pass-through interpretation, each velocity continues straight. If the ants have no identity-dependent properties, these descriptions differ only in which label is attached to each trajectory.

The question asks only when the last ant falls, not which original ant falls at that time. Swapping identities at collisions cannot change the multiset of fall times. Therefore, every initial direction can be treated as continuing straight to its corresponding edge with no collision simulation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "left": [4, 3], "right": [0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Time for each straight trajectory

An ant at position `x` moving left travels distance `x` to coordinate zero. At speed one unit per second, its fall time is `x` seconds.

An ant at position `x` moving right travels distance `n - x` to the right endpoint at coordinate `n`. Its fall time is `n - x` seconds.

The last moment is simply the maximum of all these individual straight-line times.

The stored solution initializes `ans = 0`. It scans `left` and updates `ans = max(ans, x)`. It then scans `right` and updates `ans = max(ans, n - x)`. At least one ant exists, so some candidate is considered, although zero is also a valid fall time for an ant already at the endpoint and moving outward.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A more formal collision equivalence

Consider the spacetime trajectories of all ants if they pass through one another. At any meeting of opposite trajectories, the physical collision rule makes the incoming ant on one line leave along the other line. This is equivalent to swapping the identities assigned to the two continuous lines.

Apply that relabeling at every collision. The set of occupied positions at every time remains identical to the pass-through system. In particular, ants reach the plank endpoints at exactly the same collection of times in both systems.

Since taking a maximum ignores identities, the largest endpoint time from the pass-through trajectories is exactly the actual last fall time.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "left": [4, 3], "right": [0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Event simulation:** Computing the next collision or fall repeatedly is much more complex and can be quadratic or worse; identities are irrelevant to the answer.
- **Pass-through trajectory view:** This is the essential optimal model because direction swaps between identical equal-speed ants are equivalent to identity swaps.
- **Only left-moving ants:** The answer is the maximum value in `left`.
- **Only right-moving ants:** The answer is `n` minus the minimum value in `right`.
- **Ant at coordinate zero moving left:** It falls immediately at time zero.
- **Ant at coordinate n moving right:** It also falls immediately at time zero.
- **Ants at both endpoints moving inward:** Their straight trajectories can last the full plank length, regardless of later collisions.
- **Simultaneous collisions:** They do not change the set of unlabeled trajectories or fall times.
- **Last fall shared by several ants:** Returning the common moment still satisfies the question.
- **At least one ant:** The contract guarantees the combined arrays are nonempty, so the maximum concept is defined.
- **Unique starting positions:** No two ants begin at the same coordinate, avoiding an ambiguous initial collision.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L+R)$. Let $L$ be the number of initially left-moving ants and $R$ the number of initially right-moving ants. The two loops inspect each ant exactly once and perform constant work, so time is $O(L+R)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
