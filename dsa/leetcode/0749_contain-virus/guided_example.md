# Guided Example: Contain Virus

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"isInfected": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The objective is to compute `4` from `{"isInfected": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simulate one complete day at a time

The choice of which region to quarantine depends on the current grid, and every unquarantined region spreads before the next choice. The exact solution therefore repeats four phases:

1. Discover every active infected region.
2. Measure how many distinct uninfected cells each region threatens and how many walls would surround it.
3. Quarantine the uniquely most threatening region.
4. Let every other active region spread one layer.

The grid uses three states during the simulation:

- `0` is currently uninfected.
- `1` is actively infected and can spread.
- `-1` is infected but quarantined and can no longer spread.

The input begins with only zeroes and ones; `-1` is an internal marker introduced by the algorithm.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"isInfected": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Discover one four-directional region

At the start of each day, `vis` is reset because the active components may have changed after the previous spread. DFS begins at every unvisited cell whose value is one.

For the current component, the solution creates:

- `areas[-1]`: a list of all active infected coordinates in the component.
- `boundaries[-1]`: a set of distinct zero-valued cells threatened by the component.
- `c[-1]`: the number of infected-to-uninfected edges, which equals the required wall count.

DFS marks the infected cell visited, adds it to the area, and inspects its four side neighbors. An unvisited active infected neighbor continues the same DFS. A zero neighbor contributes one wall edge and is inserted into the boundary set.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At the start of each day, `vis` is reset because the active ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why wall count and threatened-cell count differ

One uninfected cell can touch the same infected region on two or more sides. It is still only one cell that would become infected tonight, so the boundary uses a set and counts it once when deciding which region threatens the most cells.

However, every shared side needs its own wall. The counter `c` increments for every infected-to-zero adjacency, including several sides around the same zero cell. This distinction explains why saving one central cell in a surrounding ring can require four walls.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"isInfected": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recompute walls from only distinct boundary ce:** - **Recompute walls from only distinct boundary cells:** This undercounts when one zero cell touches several infected sides. Threat size uses unique cells; wall cost uses edges.
- **- **Spread newly infected cells immediately:** Tha:** - **Spread newly infected cells immediately:** That would allow multiple layers in one night. Spread only from the areas recorded before mutation.
- **- **Build a separate next-grid copy:** It makes si:** - **Build a separate next-grid copy:** It makes simultaneous spread visually explicit but uses another `O(mn)` matrix. Fixed pre-spread area lists make in-place mutation safe.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((mn)^2)$. Let `N = mn` be the number of grid cells. One day’s discovery visits every active cell and examines four edges, and the quarantine/spread phase also performs `O(N)` work.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
