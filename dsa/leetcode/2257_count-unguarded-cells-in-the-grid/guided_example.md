# Guided Example: Count Unguarded Cells in the Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"m": 4, "n": 6, "guards": [[0, 0], [1, 1], [2, 3]], "walls": [[0, 1], [2, 2], [1, 4]]}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integers `m` and `n` representing a **0-indexed** `m x n` grid. You are also given two 2D integer arrays `guards` and `walls` where $\text{guards}[i] = [\text{row}_{i}, \text{col}_{i}]$ and $\text{walls}[j] = [\text{row}_{j}, \text{col}_{j}]$ represent the positions of the $$i^{\text{th}}$$ guard and $$j^{\text{th}}$$ wall respectively.

The objective is to compute `7` from `{"m": 4, "n": 6, "guards": [[0, 0], [1, 1], [2, 3]], "walls": [[0, 1], [2, 2], [1, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Encode the only three cell states needed

The grid `g` begins with zeros:

- zero means empty and not yet known to be guarded;
- one means an empty cell seen by at least one guard;
- two means an obstruction, either a guard or a wall.

Both guards and walls receive value two because both stop line of sight. The separate `guards` input is retained so only actual guards cast rays.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"m": 4, "n": 6, "guards": [[0, 0], [1, 1], [2, 3]], "walls": [[0, 1], [2, 2], [1, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate the four cardinal directions

`dirs = (-1, 0, 1, 0, -1)` and `pairwise(dirs)` produce:

`(-1,0)`, `(0,1)`, `(1,0)`, and `(0,-1)`.

These are north, east, south, and west. No diagonal direction is generated.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `dirs = (-1, 0, 1, 0, -1)` and `pairwise(dirs)` produce:

`(... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Cast one ray until an obstruction

For every guard and direction, `x,y` begins at the guard position. The while condition examines the next cell:

- it must remain inside the grid;
- `g[next] < 2` means it is not a guard or wall.

The ray advances and assigns `g[x][y] = 1`. A previously guarded cell already has one and may be assigned one again. It does not stop sight, which is correct: visibility from one guard is not an obstacle to another.

The loop stops at the boundary or before a value-two cell. It never overwrites guards or walls.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"m": 4, "n": 6, "guards": [[0, 0], [1, 1], [2, 3]], "walls": [[0, 1], [2, 2], [1, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Four whole-grid sweeps:** Carry active visibil:** - **Four whole-grid sweeps:** Carry active visibility across rows and columns, resetting at walls and guards. It is also `O(mn)` and matches the manifest summary.
- **Cast rays without treating guards as blockers:** That violates the contract; value two stops at both object types.
- **Stop at already guarded cells:** Guarded emptiness is not an obstruction. Stopping there would miss cells farther along the same line.
- **Use a visibility set:** It can work but still needs obstacle handling and has more hashing overhead than a state grid.
- **Cell seen by several guards:** Reassigning one is harmless and it is counted as guarded once.
- **Guard surrounded by walls:** All four rays stop immediately.
- **One-row grid:** Horizontal rays work normally; vertical directions fail bounds.
- **One-column grid:** The symmetric case is handled.
- **Adjacent guard or wall:** The next-cell test stops before entering it.
- **Occupied cells:** Both guards and walls use state two and never count as unguarded.
- **No line of sight to an empty cell:** It remains zero and contributes one.
- **Input preservation:** Only the newly allocated state grid is modified.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn + G + W)$. Initializing `g` takes `O(mn)` time and space. Marking `G` guards and `W` walls takes `O(G + W)`.
- **Auxiliary Space Complexity:** $O(m n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
