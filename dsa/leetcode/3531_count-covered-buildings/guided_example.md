# Guided Example: Count Covered Buildings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "buildings": [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n`, representing an `n x n` city. You are also given a 2D grid `buildings`, where $\text{buildings}[i] = [x, y]$ denotes a **unique** building located at coordinates `[x, y]`.

The objective is to compute `1` from `{"n": 3, "buildings": [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the four directions into row and column inequalities

For building `(x,y)`:

- a left building has the same `x` and a smaller `y`;
- a right building has the same `x` and a larger `y`;
- an above building has the same `y` and a smaller `x`;
- a below building has the same `y` and a larger `x`.

The other building does not need to be immediately adjacent. Any coordinate farther in the required direction is sufficient.

Therefore, only the minimum and maximum occupied coordinates on the same row and column matter. A building is covered exactly when its `y` lies strictly inside its row's occupied range and its `x` lies strictly inside its column's occupied range.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "buildings": [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group coordinates by row and by column

The source creates two dictionaries:

- `g1[x]` contains every `y` coordinate of a building on row `x`;
- `g2[y]` contains every `x` coordinate of a building in column `y`.

For every input building, it appends once to each grouping. Unique coordinates ensure the same point is not duplicated, although different buildings naturally share rows or columns.

The grid size `n` is not used for array allocation. Dictionaries store only occupied rows and columns, which avoids `O(n)` storage when few buildings exist.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort each occupied line

The source sorts every list in `g1` and `g2`. After sorting:

- `g1[x][0]` is the leftmost occupied `y` on row `x`;
- `g1[x][-1]` is the rightmost;
- `g2[y][0]` is the topmost occupied `x` in column `y`;
- `g2[y][-1]` is the bottommost.

Intermediate sorted positions are not used. Sorting is one way to obtain the two extremes, though it is more work than necessary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "buildings": [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Track only four extremes:** Maintain min/max `y` per row and min/max `x` per column. This gives the same tests in `O(B)` expected time and is the direct way to achieve the manifest bound.
- **Use sets and search every direction:** Scanning coordinate-by-coordinate toward grid boundaries can cost `O(nB)` and ignores the fact that only extremes matter.
- **Sort all buildings globally:** A row-major and column-major sort can also derive neighbors, but two grouped extremes are simpler.
- **Require immediate adjacent cells:** The statement asks for a building somewhere in each direction, not necessarily at distance one.
- **Use non-strict inequalities:** The current extreme coordinate would then incorrectly serve as its own missing-side witness.
- **One building:** Its row and column extrema equal its coordinates, so it is not covered.
- **Two buildings on a row:** Neither lies strictly between row extremes; at least three row positions are needed for any covered building.
- **Several buildings share x but not y:** They provide horizontal witnesses only; vertical witnesses must come from the same column.
- **Several buildings share y but not x:** They provide vertical witnesses only.
- **Grid boundary coordinate:** A boundary building could still have some directions, but cannot have a building outside the city; the strict extrema test naturally prevents full coverage when a direction is impossible.
- **Sparse large n:** Dictionaries store occupied lines only, so the unused grid size does not affect memory.
- **Unique-coordinate guarantee:** It avoids duplicate copies of the same building in grouped lists.
- **Coordinate interpretation:** In the source, `g1[x]` varies `y` horizontally and `g2[y]` varies `x` vertically; swapping these meanings would test the wrong directions.
- **Manifest claim:** The source is correct but not linear due to sorting. Min/max aggregation is the relevant alternative when complexity fidelity matters.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B)$. Let row group sizes be `r_1,r_2,...` and column group sizes be `c_1,c_2,...`, each family summing to `B`.
- **Auxiliary Space Complexity:** $O(B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
