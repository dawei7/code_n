# Guided Example: Sliding Puzzle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [[1, 2, 3], [4, 0, 5]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

On an `2 x 3` board, there are five tiles labeled from `1` to `5`, and an empty square represented by `0`. A **move** consists of choosing `0` and a 4-directionally adjacent number and swapping it.

The objective is to compute `1` from `{"board": [[1, 2, 3], [4, 0, 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat every board arrangement as a graph state

The board always contains the six symbols zero through five exactly once. One legal move swaps zero with a side-adjacent tile. Therefore:

- A board arrangement is a graph vertex.
- A legal swap creates an undirected graph edge.
- Every edge costs one move.

The requested minimum is an unweighted shortest-path distance from the initial arrangement to `"123450"`, so breadth-first search is the natural algorithm.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [[1, 2, 3], [4, 0, 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Encode a board as a six-character string

The helper `gets` reads rows in row-major order and writes each tile into reusable list `t`, then joins it. For example, `[[1,2,3],[4,0,5]]` becomes `"123405"`.

Strings are immutable and hashable, so they work safely as visited-set keys and queue elements. A nested mutable list would require conversion or copying for the same purpose.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Restore a queued string into the working board

The implementation keeps one mutable `board` object for neighbor generation. Before expanding queued state `x`, `setb(x)` writes its six digits back into that board.

This avoids storing a separate matrix for every queued state. The queue remains authoritative through strings; the board is only temporary working memory for the state currently being expanded.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [[1, 2, 3], [4, 0, 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Precompute zero-index adjacency:** String positions can be swapped directly using a fixed neighbor table, avoiding repeated matrix restoration and zero scans.
- **Bidirectional BFS:** Searching from both start and target can reduce the explored frontier.
- **Depth-first search:** It may find a solution but does not guarantee the fewest moves.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V+E)$. Let `V` be the number of reachable board states and `E` the legal state transitions among them. BFS visits each state once and examines its outgoing transitions, giving `O(V + E)` time.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
