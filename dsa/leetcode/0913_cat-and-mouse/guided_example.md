# Guided Example: Cat and Mouse

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"graph": [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A game on an **undirected** graph is played by two players, Mouse and Cat, who alternate turns.

The objective is to compute `0` from `{"graph": [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Terminal states.

- If $m=0$, the mouse has reached the hole, so the state is a mouse win regardless of whose turn would be next.
- If $m=c$ at a non-hole node, the cat has caught the mouse, so it is a cat win.

Both turn versions of every terminal position are initialized and enqueued.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"graph": [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Invariant Preservation

Ensure every candidate decision satisfies the required constraints.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Ensure every candidate decision satisfies the required const... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"graph": [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Depth-limited minimax:** Choosing an arbitrary:** - **Depth-limited minimax:** Choosing an arbitrary move limit risks confusing long forced wins with draws and needs careful state repetition handling.
- **Naive recursion with a visited set:** A cycle on the current path does not alone determine the minimax outcome of the state; retrograde resolution is more reliable.
- **Value iteration:** Repeatedly update game states until stable. It can work but the degree queue processes only relevant changes.
- **Cat edge to hole:** It must be excluded from both degree and predecessor generation because it is illegal.
- **Mouse already in hole:** Mouse wins even if the next-turn field says cat.
- **Same mouse and cat node:** Cat wins for non-hole collision states.
- **Winning child:** One available winning move is enough because the current player chooses optimally.
- **Losing state:** It is established only after every legal move is proven to let the opponent win.
- **Draw option:** An unresolved/draw child prevents degree from reaching zero and lets the player avoid a forced loss.
- **Repeated graph position:** A state includes whose turn it is; identical positions with different turns are different states.
- **Both players can move:** The contract avoids zero-degree ordinary states, while cat-hole exclusion is handled explicitly.
- **Undirected graph:** Reverse predecessor enumeration can use the same adjacency lists as forward moves.
- **Initial answer zero:** It means optimal play leads to a draw, not that computation failed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^3)$. There are $2n^2$ possible position-and-turn states. Processing one resolved state may inspect up to $O(n)$ predecessor positions through an adjacency list.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
