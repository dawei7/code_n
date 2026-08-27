# Guided Example: Multi Source Flood Fill

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "m": 3, "sources": [[0, 0, 1], [2, 2, 2]]}`
- **Required output:** `[[1, 1, 2], [1, 2, 2], [2, 2, 2]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integers `n` and `m` representing the number of rows and columns of a grid, respectively.

The objective is to compute `[[1, 1, 2], [1, 2, 2], [2, 2, 2]]` from `{"n": 3, "m": 3, "sources": [[0, 0, 1], [2, 2, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Distance determines the arrival time

In an obstacle-free rectangular grid, the shortest number of orthogonal moves from source $(r_s,c_s)$ to cell $(r,c)$ is the Manhattan distance

$$
|r-r_s|+|c-c_s|.
$$

Because all sources start together and colors advance one edge per step, a cell's first coloring time is its minimum Manhattan distance to any source.

Sources farther away cannot overwrite it later, because spreading applies only to uncolored cells. Among sources at the same minimum distance, all arrivals occur simultaneously, and the maximum source color must win.

The BFS does not calculate these distances explicitly. Layer number represents time, and the per-layer maximum aggregation implements the equal-distance tie rule.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "m": 3, "sources": [[0, 0, 1], [2, 2, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initializing all sources as one layer

The answer matrix `ans` begins with zeros. Every source coordinate receives its positive initial color.

The source then sets



so the initial frontier contains all time-zero cells. Starting with every source in one queue is what makes the search multi-source rather than running one flood fill after another. Sequential single-source fills would incorrectly let whichever source ran first claim cells before simultaneous competitors were considered.

The value zero safely means “uncolored” because every allowed source color is positive.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The answer matrix `ans` begins with zeros.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Enumerating four orthogonal neighbors

The tuple



contains the coordinate offsets in cyclic form. Consecutive pairs are

$$
(-1,0),\ (0,1),\ (1,0),\ (0,-1),
$$

representing up, right, down, and left.

For every current frontier entry $(r,c,\text{color})$, the source checks those four neighbors. It discards:

- coordinates outside rows $0..n-1$ or columns $0..m-1$; and
- cells whose `ans` entry is already nonzero.

The second rule enforces first-arrival permanence. A cell colored in an earlier BFS layer has a strictly shorter route from some source and cannot be changed by a later arrival.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 1, 2], [1, 2, 2], [2, 2, 2]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "m": 3, "sources": [[0, 0, 1], [2, 2, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 1, 2], [1, 2, 2], [2, 2, 2]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Immediate neighbor coloring:** Writing proposa:** - **Immediate neighbor coloring:** Writing proposals directly into `ans` makes results depend on frontier iteration order and violates simultaneous maximum-color tie resolution.
- **Priority queue by distance and color:** Ordering states by minimum distance and then maximum color can solve the same nearest-source problem, but costs $O(nm\log(nm))$ instead of layered linear BFS.
- **Run one BFS per source:** This repeats grid work and requires later distance comparisons; multi-source initialization shares the traversal.
- **Single source:** No ties are possible, and its color eventually fills the connected grid.
- **Source coordinates are distinct:** Initialization never needs to resolve two colors already occupying the same cell.
- **Adjacent sources:** Each is already colored at time zero and cannot be overwritten by the other at time one.
- **Equal-distance tie:** `vis` keeps the numerically largest proposal, regardless of proposal order.
- **Later higher color:** It cannot replace a cell claimed earlier because spreading targets only uncolored cells.
- **Positive-color guarantee:** `ans[x][y] == 0` unambiguously means uncolored; allowing source color zero would break this test.
- **One-row or one-column grid:** The same four-direction loop works; out-of-bounds checks discard the unavailable directions.
- **Input-list destruction:** Because `q` aliases `sources` and is repeatedly cleared, `sources` is empty when the method returns.
- **Required helpers:** Standalone execution needs `defaultdict` and `pairwise` from the Python standard library.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(nm)$. Let $V=nm$ be the number of cells. Every cell enters a frontier at most once because it is committed to `ans` only while uncolored. When active, it inspects four neighbors. The total graph work is
- **Auxiliary Space Complexity:** $O(nm)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
