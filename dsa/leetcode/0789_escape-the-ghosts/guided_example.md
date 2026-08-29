# Guided Example: Escape The Ghosts

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"ghosts": [[1, 0], [0, 3]], "target": [0, 1]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at the point `[0, 0]`, and you are given a destination point $target = [x_{target}, y_{target}]$ that you are trying to get to. There are several ghosts on the map with their starting positions given as a 2D array `ghosts`, where $\text{ghosts}[i] = [x_{i}, y_{i}]$ represents the starting position of the $i^{\text{th}}$ ghost. All inputs are **integral coordinates**.

The objective is to compute `true` from `{"ghosts": [[1, 0], [0, 3]], "target": [0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Measure shortest grid travel with Manhattan distance

On each turn, a participant may change one coordinate by one unit or stay still. The fewest turns between points `(x1, y1)` and `(x2, y2)` is therefore:

$$
\lvert x1 - x2 \rvert + \lvert y1 - y2 \rvert.
$$

This is Manhattan, or taxicab, distance. Every horizontal move can reduce the horizontal difference by at most one, and every vertical move can reduce the vertical difference by at most one, so at least this many turns are necessary. Moving along the two axes achieves exactly that bound.

The player's shortest time from origin `(0,0)` to `(tx,ty)` is:

`abs(tx) + abs(ty)`.

A ghost at `(x,y)` needs:

`abs(tx - x) + abs(ty - y)`

turns to reach the target.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"ghosts": [[1, 0], [0, 3]], "target": [0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reduce the adversarial game to a race to the target

At first, it may seem necessary to simulate every possible player path and every coordinated ghost pursuit. The key observation is that a ghost can defeat the player simply by reaching the target no later than the player.

If a ghost's distance to the target is less than or equal to the player's distance, it travels along a shortest route to the target. It arrives before or at the same turn. The player cannot escape, because arriving simultaneously with a ghost does not count.

Thus every successful strategy requires the player to have strictly smaller target distance than every ghost.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a farther ghost cannot intercept a shortest player path

The converse needs proof. Suppose the player follows a shortest path to target `T` from start `S`. Assume some ghost starting at `G` could meet the player at point `X` before or at the player's arrival there.

That means:

$$
\operatorname{dist}(G,X)
\le
\operatorname{dist}(S,X).
$$

By the triangle inequality:

$$
\operatorname{dist}(G,T)
\le
\operatorname{dist}(G,X)+\operatorname{dist}(X,T).
$$

Because `X` lies on a shortest player path:

$$
\operatorname{dist}(S,X)+\operatorname{dist}(X,T)
=
\operatorname{dist}(S,T).
$$

Combining the relations would give:

$$
\operatorname{dist}(G,T)
\le
\operatorname{dist}(S,T).
$$

Therefore any ghost capable of intercepting a shortest player path must also be able to reach the target no later than the player. The contrapositive is exactly what is needed: if every ghost is strictly farther from the target, none can intercept the player on a shortest route.

This proves that comparing only target distances is sufficient; no grid search or pursuit simulation is missing a more dangerous strategy.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"ghosts": [[1, 0], [0, 3]], "target": [0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Breadth-first search on the grid:** The grid is infinite and obstacles do not exist, so BFS replaces a constant-time distance formula with an unbounded search.
- **Simulate simultaneous turns:** There are many possible adversarial moves, but the direct-to-target proof makes simulation unnecessary.
- **Check collision only on one chosen path:** Target-distance comparison is stronger and proves safety for a shortest path through triangle inequality.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(g)$. Let $g$ be the number of ghosts. The player distance is computed once. Each ghost contributes a constant number of arithmetic and absolute-value operations, so time is $O(g)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
