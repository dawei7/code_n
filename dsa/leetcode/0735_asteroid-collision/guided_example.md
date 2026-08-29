# Guided Example: Asteroid Collision

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"asteroids": [5, 10, -5]}`
- **Required output:** `[5, 10]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We are given an array `asteroids` of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

The objective is to compute `[5, 10]` from `{"asteroids": [5, 10, -5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Identify the only direction pattern that can collide

All asteroids move at the same speed. Two moving in the same direction keep their distance. A left-moving asteroid followed by a right-moving asteroid also separates: the left one moves farther left and the right one farther right.

A collision is possible only when an asteroid on the left moves right and a later asteroid moves left. In signs, that is a positive value followed somewhere to its right by a negative value, with no surviving asteroid between them that prevents contact.

The exact solution processes input from left to right and stores the already resolved surviving prefix in `stk`. Only the stack’s top can collide next with the current asteroid because it is the nearest surviving asteroid on the current one’s left.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"asteroids": [5, 10, -5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Positive asteroids can be pushed immediately

When the current value `x` is positive, it moves right. Every asteroid already processed lies to its left:

- A positive stack asteroid moves in the same direction.
- A negative stack asteroid moves left, away from the new positive asteroid.

Neither case creates an immediate collision, so the positive asteroid is appended.

It may collide later with a future negative asteroid, which is why it remains available on the stack.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A negative asteroid may trigger a collision chain

For `x < 0`, collision is possible while the stack is nonempty and its top is positive. The current asteroid’s size is `-x`.

The loop pops while

`stk[-1] > 0 and stk[-1] < -x`.

Each popped positive asteroid is smaller than the incoming negative one and therefore explodes. The negative asteroid survives that collision and continues left, so it must be compared with the new stack top. This is how one large left-moving asteroid can destroy several smaller right-moving asteroids.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[5, 10]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"asteroids": [5, 10, -5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[5, 10]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeatedly scan adjacent pairs:** Simulate one collision, rebuild or rescan, and continue. This can revisit large portions of the array and degrade to `O(n^2)`.
- **Linked list of live asteroids:** Removing neighbors can be made constant time, but selecting and revisiting collision candidates adds complexity. The stack directly matches the one-sided processing order.
- **Treat every opposite-sign pair as colliding:** A negative asteroid to the left of a positive one moves away from it. Only a positive-left, negative-right arrangement collides.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of asteroids. Each asteroid is considered once in the outer loop and appended at most once. Once popped, it never returns to the stack. Although one negative asteroid may execute many while-loop iterations, all pops across the complete run total at most `n`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
