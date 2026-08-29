# Guided Example: Minimum Moves to Clean the Classroom

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"classroom": ["S.", "XL"], "energy": 2}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` grid `classroom` where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

The objective is to compute `2` from `{"classroom": ["S.", "XL"], "energy": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Assigning a bit to each litter cell

The initial grid scan finds the unique starting coordinate and numbers the `L` litter cells from zero through `L-1`. `d[i][j]` stores the bit index for a litter cell.

The starting mask is

`(1 << L) - 1`,

whose lowest `L` bits are all one. A one means that litter remains. On entering litter cell `(x,y)`, the update

`nxt_mask &= ~(1 << d[x][y])`

clears its bit. Visiting the same cell again leaves the bit zero, so litter is collected only once.

If the initial scan finds no litter, the answer is immediately zero. No movement is required, and avoiding state allocation is especially useful because the full visited structure is large.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"classroom": ["S.", "XL"], "energy": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why all three state dimensions matter

Two visits to the same coordinate and mask are not necessarily equivalent if one has more energy. The higher-energy visit can reach farther before needing a reset.

Likewise, equal position and energy do not make states equivalent when their masks differ. One route may already have collected litter that another still needs.

The exact visited key is therefore `(row,column,remaining_energy,remaining_mask)`. The four-dimensional `vis` array marks each such combination once.

The manifest summary says the source retains only the greatest remaining energy for each position-mask pair. That dominance optimization is not implemented. The exact source allocates and tracks every energy value from zero through the maximum separately. A higher energy can dominate a lower one at the same position and mask, but the current code does not exploit that fact.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: BFS layers represent move counts

`q` contains all states at the current distance `ans`. At the start, it holds the starting state with full energy and all litter bits set, while `ans=0`.

For each iteration:

- `t=q` freezes the current layer;
- `q=[]` becomes the next layer;
- every legal one-step successor is appended to the new `q`;
- after the layer is exhausted, `ans` increments.

Thus every state in `t` was reached in exactly `ans` moves. States are never mixed across distances.

The mask is checked before energy:

`if mask == 0: return ans`.

This ordering is important. The final move may collect the last litter while reducing energy to zero. That state is still a successful answer and must be returned even though it cannot make another ordinary move.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"classroom": ["S.", "XL"], "energy": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dominance pruning by maximum energy:** At the same position and mask, a state with more remaining energy can reproduce every continuation available to one with less. Storing only the maximum energy can reduce memory and repeated work; this is advertised by the manifest but absent from the source.
- **Shortest paths between special cells plus subset DP:** One can precompute energy-aware reachability among start, litter, and reset locations, then solve a smaller mask problem. Reusable resets make the compressed transitions more subtle than ordinary pairwise distances.
- **Priority-queue search:** Dijkstra’s algorithm is unnecessary because every physical move costs one; BFS has simpler ordering and lower overhead.
- **No litter:** The source returns zero before allocating the state space.
- **Last litter reached with zero energy:** Success is checked before expansion eligibility, so the route is accepted.
- **Zero energy away from a reset:** The state cannot move and is safely discarded.
- **Entering a reset with one energy:** The destination immediately restores full capacity, allowing further movement.
- **Repeated reset visits:** They are allowed; only an identical full state is suppressed by `vis`.
- **Litter revisited:** Its bit is already clear, so the mask remains unchanged.
- **Obstacle-separated litter:** If no state can reach it, BFS exhausts and returns `-1`.
- **Start next to litter:** The first next-layer state clears that bit and may finish in one move.
- **Different litter orders:** The mask lets BFS explore all reachable orders without prescribing one.
- **Exactly ten litter cells:** The mask has 1024 possibilities, which is why the energy and grid dimensions make careful state representation important.
- **Input preservation:** Litter collection is represented in the mask; the immutable classroom strings are never modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mnE2^L)$. Let `L` be the number of litter cells and `E` the maximum energy. There are at most
- **Auxiliary Space Complexity:** $O(mnE2^L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
