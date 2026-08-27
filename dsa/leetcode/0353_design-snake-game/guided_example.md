# Guided Example: Design Snake Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"width": 1, "height": 2, "food": [[1, 0]], "directions": ["R"]}`
- **Required output:** `[-1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a <a href="https://en.wikipedia.org/wiki/Snake_(video_game)" target="_blank">Snake game</a> that is played on a device with screen size `height x width`. <a href="http://patorjk.com/games/snake/" target="_blank">Play the game online</a> if you are not familiar with the game.

The objective is to compute `[-1]` from `{"width": 1, "height": 2, "food": [[1, 0]], "directions": ["R"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Initial state and persistent fields.

The constructor translates the interface's `height` and `width` into `m` and `n`. Rows are valid from `0` through `m - 1`; columns are valid from `0` through `n - 1`. The snake starts at `(0, 0)`, so both `q` and `vis` initially contain that one coordinate.

`food` remains in its given appearance order. `idx` points to the next food item that has not yet been eaten, and `score` counts consumed items. These two values advance together, but both are kept explicitly: `idx` locates the next coordinate and `score` is the required return value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"width": 1, "height": 2, "food": [[1, 0]], "directions": ["R"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Computing the proposed head.

Every call begins from the current head `q[0]`. The variables `x` and `y` start as its row and column. The `match` statement changes exactly one coordinate: up subtracts one from the row, down adds one to the row, left subtracts one from the column, and right adds one to the column.

At this point `(x, y)` is only a proposed new head. The source first checks whether it lies outside the grid. A row below zero or at least `height`, or a column below zero or at least `width`, hits a wall. In that case the method immediately returns `-1` without changing the deque, occupancy set, score, or food index.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every call begins from the current head `q[0]`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Food changes whether the tail moves.

The next uneaten food is active only when `idx < len(food)`. The snake eats it only if the proposed head matches both its row and column. Later food coordinates are intentionally ignored until earlier food has been eaten, exactly matching the one-at-a-time appearance rule.

On a food move, the score and food index increase. The old tail remains in place, while a new head will be added, so the snake grows by one cell.

On an ordinary move, the snake's length stays fixed. The source removes `q.pop()`, the old tail coordinate, and removes the same coordinate from `vis`. It then plans to add the proposed head at the front. The body therefore slides forward by one cell.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[-1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"width": 1, "height": 2, "food": [[1, 0]], "directions": ["R"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[-1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Deque without an occupancy set:** The body ord:** - **Deque without an occupancy set:** The body order remains efficient, but checking whether the proposed head overlaps a body coordinate requires scanning up to $L$ cells, making one move $O(L)$.
- **- **Occupancy set without ordered body storage:** :** - **Occupancy set without ordered body storage:** Collision checks are fast, but the algorithm no longer knows which coordinate is the tail that must leave on a non-food move. Both representations serve distinct needs.
- **- **Grid occupancy array:** A Boolean `height * wi:** - **Grid occupancy array:** A Boolean `height * width` matrix gives deterministic constant-time membership but consumes $O(height\cdot width)$ space, potentially enormous compared with the at-most-`f + 1` snake cells.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q)$. Let $q$ be the number of calls to `move`, let $f$ be the number of food items, and let $L$ be the current snake length.
- **Auxiliary Space Complexity:** $O(f)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
