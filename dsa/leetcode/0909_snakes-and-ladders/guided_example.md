# Guided Example: Snakes and Ladders

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [[-1, -1], [-1, 3]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `n x n` integer matrix `board` where the cells are labeled from `1` to $n^{2}$ in a <a href="https://en.wikipedia.org/wiki/Boustrophedon" target="_blank">**Boustrophedon style**</a> starting from the bottom left of the board (i.e. $board[n - 1][0]$) and alternating direction each row.

The objective is to compute `1` from `{"board": [[-1, -1], [-1, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

Each die roll costs one move and creates at most six possible next states. The board therefore defines an unweighted directed graph whose vertices are square labels. Breadth-first search finds the minimum number of edges—dice rolls—from square 1 to square $n^2$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [[-1, -1], [-1, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Convert a label to matrix coordinates.** Labels begin at the bottom-left and alternate direction row by row. For label `y`, `divmod(y - 1, n)` returns:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Convert a label to matrix coordinates.** Labels begin at t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `i`: how many board rows upward from the bottom the label lies;
- `j`: its zero-based offset within that row's labeling direction.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [[-1, -1], [-1, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Depth-first search:** It can explore reachabil:** - **Depth-first search:** It can explore reachability but does not naturally guarantee the fewest rolls without additional distance relaxation.
- **Dijkstra's algorithm:** All moves have equal cost one, so BFS is simpler and faster.
- **Flatten the board first:** Building a label-to-destination array makes BFS coordinate lookup simpler at $O(n^2)$ preprocessing space and time.
- **Follow a chain of ladders in one roll:** Incorrect; only the initially selected destination triggers one snake or ladder.
- **Mark raw die landing as visited:** The meaningful state after a mandatory jump is `z`, which should be deduplicated.
- **Die near the end:** `min(x + 6, m)` prevents labels beyond the board.
- **Snake back to an earlier square:** Visited-state logic handles cycles without infinite traversal.
- **Ladder directly to the final square:** It is enqueued at the next level and returned with the correct one-roll increment.
- **Unreachable target:** Cycles and backward snakes may exhaust the queue, producing `-1`.
- **Alternating row direction:** Odd bottom-based rows reverse columns; even ones do not.
- **Start and final squares:** The contract guarantees neither begins a snake or ladder.
- **Smallest board:** The same coordinate formula and six-outcome cap work for $n=2$.
- **Level counter:** Check for the target when dequeuing before incrementing the next layer, so square 1 correctly has distance zero.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. There are $n^2$ square states. Each is enqueued at most once, and processing it examines at most six die outcomes.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
