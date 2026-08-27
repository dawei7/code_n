# Guided Example: Rotting Oranges

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[2, 1, 1], [1, 1, 0], [0, 1, 1]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` `grid` where each cell can have one of three values:

The objective is to compute `4` from `{"grid": [[2, 1, 1], [1, 1, 0], [0, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model each minute as one breadth-first layer

Rotting spreads one grid edge per minute: a rotten orange affects fresh oranges immediately above, below, left, or right. This is the same structure as shortest distances in an unweighted graph, where orange cells are vertices and four-directional adjacencies are edges.

Breadth-first search processes vertices by increasing distance. If all initially rotten oranges enter the queue at time zero, then the next BFS layer contains oranges that rot after one minute, the layer after that contains oranges that rot after two minutes, and so on.

This must be a multi-source BFS. Starting separately from each rotten orange and taking a minimum afterward would repeat work. Placing all sources in one queue lets their waves expand simultaneously, just as the physical process does.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[2, 1, 1], [1, 1, 0], [0, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan the grid to establish the initial state

The first nested loop performs two jobs:

- every cell containing `2` is appended to queue `q` as an initial rotten source;
- every cell containing `1` increments `cnt`, the number of fresh oranges still unrotted.

Empty cells need no stored state. Dimensions `m` and `n` support boundary checks later.

After this scan, `cnt` is the exact remaining work. It provides an efficient success test without rescanning the entire grid after BFS.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first nested loop performs two jobs:

- every cell conta... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Freeze the current minute's frontier

The main loop runs while both `q` and `cnt` are nonzero. At its start, all coordinates currently in `q` became rotten no later than the same current time frontier and are ready to spread during the next minute.

The code increments `ans` once, then executes

`for _ in range(len(q))`.

As with level-order tree traversal, `len(q)` is captured before processing the layer. Newly rotten neighbors appended during the loop are not processed until the next outer iteration. That delay is essential: an orange that rots at minute one cannot rot another orange during that same minute; its effect begins in the following minute.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[2, 1, 1], [1, 1, 0], [0, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Run BFS from each source separately:** It repe:** - **Run BFS from each source separately:** It repeats traversal and requires combining arrival times. One multi-source queue obtains nearest-source distances directly.
- **Depth-first search:** DFS does not naturally preserve simultaneous minute layers. It would need stored arrival times and repeated relaxations to recover shortest propagation times.
- **Minute delimiter in the queue:** A sentinel can mark layer endings. Freezing `len(q)` is simpler and avoids special coordinates.
- **Timestamp values in the grid:** Repeatedly scan for cells of the current timestamp to avoid a queue. This saves queue space but can make time quadratic in the number of cells.
- **No fresh oranges:** Return zero immediately through the skipped loop and final conditional.
- **Fresh oranges but no rotten source:** The empty queue cannot start propagation, so return `-1`.
- **Isolated fresh region:** Empty cells or boundaries may disconnect it from every source; `cnt` remains positive after the queue empties.
- **Several sources reaching one orange:** The first source marks it at enqueue time, so it is counted once at its minimum arrival minute.
- **Diagonal contact:** Diagonal positions are never generated by the four offsets and do not spread rot.
- **Single cell:** A fresh-only cell returns `-1`, while an empty or already-rotten cell returns zero.
- **Input mutation:** If the original grid must be preserved outside this call, the caller must provide a copy.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(A)$. Let `A = mn` be the number of grid cells.
- **Auxiliary Space Complexity:** $O(A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
