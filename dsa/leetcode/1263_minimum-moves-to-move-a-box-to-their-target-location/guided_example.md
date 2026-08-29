# Guided Example: Minimum Moves to Move a Box to Their Target Location

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [["#", "#", "#", "#", "#", "#"], ["#", "T", "#", "#", "#", "#"], ["#", ".", ".", "B", ".", "#"], ["#", ".", "#", "#", ".", "#"], ["#", ".", ".", ".", "S", "#"], ["#", "#", "#", "#", "#", "#"]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The objective is to compute `3` from `{"grid": [["#", "#", "#", "#", "#", "#"], ["#", "T", "#", "#", "#", "#"], ["#", ".", ".", "B", ".", "#"], ["#", ".", "#", "#", ".", "#"], ["#", ".", ".", ".", "S", "#"], ["#", "#", "#", "#", "#", "#"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the box position alone is not a complete state

The objective counts pushes, not ordinary player steps. Even so, the player's location cannot be discarded. To push the box in a direction, the player must stand immediately behind it, and walls or the box itself may prevent the player from reaching that side. Two situations with the box in the same cell but the player in different regions can permit different next pushes.

The exact solution therefore represents a state as the ordered pair of the player's cell and the box's cell. Function `f(i, j) = i * n + j` flattens a coordinate into one integer, so a queue entry `(s, b, d)` contains the flattened player position, flattened box position, and the number of pushes used to reach that state.

The dimensions `m` and `n` are assigned before `f` is first called. Python closures resolve `n` when the helper executes, not when it is defined, so this ordering works. The initial scan records `S` and `B`; the target need not be stored separately because the code later checks the grid character under the box.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [["#", "#", "#", "#", "#", "#"], ["#", "T", "#", "#", "#", "#"], ["#", ".", ".", "B", ".", "#"], ["#", ".", "#", "#", ".", "#"], ["#", ".", ".", ".", "S", "#"], ["#", "#", "#", "#", "#", "#"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Modeling moves with costs zero and one

From a state, the player may try the four cardinal directions. The tuple `dirs = (-1, 0, 1, 0, -1)` combined with `pairwise(dirs)` yields `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)`. Helper `check` accepts a coordinate exactly when it is inside the grid and is not a wall.

If the player's candidate cell `(sx, sy)` is not the box, the move is ordinary walking. The box stays at `(bi, bj)`, the push count remains `d`, and the resulting state is inserted at the front of the deque with `appendleft`.

If the candidate cell is the box, walking into it is possible only by pushing. The box's candidate destination `(bx, by)` lies one more step in the same direction. If that cell is outside the grid or a wall, the move is rejected. Otherwise the player's new cell is the box's old cell `(sx, sy)`, the box moves to `(bx, by)`, the push count becomes `d + 1`, and the state is inserted at the back with `append`.

These edge costs are zero for walking and one for pushing. Processing zero-cost edges from the front and one-cost edges from the back is zero-one breadth-first search. It gives walking freedom without charging it toward the answer while still exploring states in nondecreasing push count.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Preventing impossible movement and repeated work

The player never occupies the same cell as the box. When `(sx, sy)` equals the box, the code enters only the push branch; a blocked push is skipped rather than treated as a walk. For a successful push, `check` ensures the box destination is valid. The player's destination is the old box cell, already known to be a non-wall in bounds.

The matrix `vis[player][box]` marks every discovered ordered state. It is initialized at the pair containing the original `S` and `B`. Ordinary motion changes only the first index, while a push changes both. This distinction allows the search to revisit the same box position with a strategically different player position but prevents it from cycling forever through identical configurations.

The grid itself is not modified. Characters `S` and `B` are treated as walkable because `check` rejects only `"#"`. After positions have been captured, those letters merely denote floor cells for movement purposes. The target is also walkable.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [["#", "#", "#", "#", "#", "#"], ["#", "T", "#", "#", "#", "#"], ["#", ".", ".", "B", ".", "#"], ["#", ".", "#", "#", ".", "#"], ["#", ".", ".", ".", "S", "#"], ["#", "#", "#", "#", "#", "#"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dijkstra's algorithm:** The same player-box graph can be searched with a priority queue using edge weights zero and one. It is correct but adds a logarithmic queue factor that zero-one BFS avoids.
- **Push-level BFS with reachability checks:** Store the box cell and the side occupied by the player, then run a flood fill to decide which pushing sides are reachable. This can reduce persistent states toward $O(V)$ but repeats or caches walking reachability logic and differs from the exact source.
- **Sparse visited set:** Storing only reached `(player, box)` pairs avoids eagerly allocating invalid wall combinations. Worst-case asymptotic space remains $O(V^2)$, though practical memory may improve.
- **Ordinary BFS that counts every move:** Treating walking and pushing equally minimizes total player steps, not pushes, and can return the wrong answer.
- **Box begins on target:** The first dequeued state passes the target check and returns zero, although the standard grid uses distinct marker characters and normally provides separate starting cells.
- **Blocked push:** If the player reaches the box but the cell beyond is a wall or outside the grid, that direction produces no successor.
- **Player cannot pass through the box:** Entering the box cell always invokes the push rule; it never becomes a zero-cost walking state.
- **Dead corners:** A box pushed into a non-target corner naturally creates no useful future pushes. The search needs no special deadlock rule for correctness, though such pruning could improve speed.
- **Unreachable target:** Exhausting the deque returns `-1` after all legal configurations have been ruled out.
- **Same box, different player:** These must remain separate states because only some player positions may reach the side needed for the next push.
- **Target and lettered cells are traversable:** `check` excludes only walls, so `S`, `B`, `T`, and `.` cells are all treated as floor after their semantic positions are known.
- **Missing markers are outside the contract:** The exact scan assumes one `S` and one `B` exist; without them, the saved coordinates would be undefined.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(4V^2)$. Let $V=m\cdot n$ be the total number of grid cells. The exact state representation permits up to $V$ player positions for each of $V$ box positions, or $O(V^2)$ ordered pairs. Each discovered state is processed once, and processing tries four directions, so the worst-case time is $O(4V^2)=O(V^2)$.
- **Auxiliary Space Complexity:** $O(V^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
