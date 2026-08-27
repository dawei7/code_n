# Guided Example: The Knight’s Tour

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"m": 1, "n": 1, "r": 0, "c": 0}`
- **Required output:** `[[0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two positive integers `m` and `n` which are the height and width of a **0-indexed** 2D-array `board`, a pair of positive integers `(r, c)` which is the starting position of the knight on the board.

The objective is to compute `[[0]]` from `{"m": 1, "n": 1, "r": 0, "c": 0}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent visit order directly on the board

Matrix `g` starts filled with `-1`, meaning unvisited.

The starting cell receives zero. Every later chosen cell receives one more than the current cell:

`g[x][y] = g[i][j] + 1`.

Thus, if a complete tour is found, board values zero through $mn-1$ encode the exact visit order.

The same matrix serves as both output and visited structure.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"m": 1, "n": 1, "r": 0, "c": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Enumerate all eight knight moves

The sequence passed to `pairwise` produces:

$$
(-2,-1),(-1,2),(2,1),(1,-2),
(-2,1),(1,2),(2,-1),(-1,-2).
$$

Each offset changes one coordinate by one and the other by two in absolute value, exactly matching a knight move.

For candidate $(x,y)$, the code requires:

- row within zero through $m-1$;
- column within zero through $n-1$;
- `g[x][y] == -1`.

The last condition prevents revisiting a cell.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The sequence passed to `pairwise` produces:

$$
(-2,-1),(-1,... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Depth-first search tries one path

At current cell, DFS loops through legal unvisited knight destinations.

It tentatively labels a destination with the next visit number and recursively continues from there.

This extends the current partial tour by exactly one cell. The recursion stack implicitly stores the chosen path.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"m": 1, "n": 1, "r": 0, "c": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Warnsdorff ordering:** Try the legal destinati:** - **Warnsdorff ordering:** Try the legal destination with fewest onward moves first; often dramatically faster and matches the manifest summary.
- **Bitmask visited state:** Useful for memoized Hamiltonian-path search, but state space can still be exponential.
- **Iterative backtracking:** Avoids recursion but needs an explicit path stack.
- **One-cell board:** Starting cell already completes the tour.
- **No revisits:** Only cells labeled `-1` are candidates.
- **Failed branch:** Its tentative label must be reset.
- **Successful branch:** Early returns must happen before reset to preserve output.
- **Fixed move order:** Affects runtime and which valid tour is returned, not correctness.
- **Guaranteed solution:** The function relies on it and has no separate failure return.
- **Small board:** At most 25 recursive levels fit comfortably.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(8^(mn))$. At each of up to $mn$ path positions, at most eight moves are attempted. A coarse worst-case bound is $O(8^{mn})$ time, though visited constraints substantially prune actual search.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
