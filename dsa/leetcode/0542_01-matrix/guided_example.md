# Guided Example: 01 Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mat": [[0, 0, 0], [0, 1, 0], [0, 0, 0]]}`
- **Required output:** `[[0, 0, 0], [0, 1, 0], [0, 0, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` binary matrix `mat`, return *the distance of the nearest *`0`* for each cell*.

The objective is to compute `[[0, 0, 0], [0, 1, 0], [0, 0, 0]]` from `{"mat": [[0, 0, 0], [0, 1, 0], [0, 0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

Every zero is already at distance zero from a zero. Every one needs the shortest number of horizontal or vertical steps to **any** zero. This is a shortest-path problem on an unweighted grid, and starting breadth-first search from all zero cells at once finds all answers in one expansion.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mat": [[0, 0, 0], [0, 1, 0], [0, 0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Think of each matrix cell as a graph vertex. Two vertices share an edge when their cells share a side. Every edge has cost one, exactly matching the distance definition.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Think of each matrix cell as a graph vertex.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Use a separate answer matrix as both distance storage and visited state.** The solution creates `ans` filled with `-1`. Here, `-1` means that no shortest distance has been assigned yet.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 0, 0], [0, 1, 0], [0, 0, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mat": [[0, 0, 0], [0, 1, 0], [0, 0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 0, 0], [0, 1, 0], [0, 0, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two-pass dynamic programming:** A top-left pas:** - **Two-pass dynamic programming:** A top-left pass uses top and left neighbors, then a bottom-right pass uses bottom and right. It also runs in $O(RC)$ time.
- **BFS from every one:** Repeating a search for each cell can become quadratic in the number of cells.
- **BFS from one zero at a time:** It repeats overlapping exploration; multi-source initialization merges all waves.
- **Use the input as visited storage:** It can reduce one separate state structure but mutates the caller's matrix and requires safe sentinel choices.
- **All zeroes:** Every answer starts at zero; BFS performs no positive assignments.
- **One zero:** The wave expands Manhattan distances from that single source.
- **One row or one column:** The same four-direction logic reduces naturally to the valid two directions.
- **Multiple equally near zeroes:** The first source wave assigns the same minimum distance either way.
- **No diagonal movement:** The direction pairs include only common-edge neighbors.
- **Boundary cells:** Coordinate checks prevent invalid accesses.
- **At least one zero:** This guarantee ensures every cell has a finite answer.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RC)$. Let $R$ and $C$ be the dimensions. The initialization scans all $RC$ cells. Each cell enters and leaves the queue at most once, and each dequeue checks four neighbors. Time is therefore $O(RC)$.
- **Auxiliary Space Complexity:** $O(RC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
