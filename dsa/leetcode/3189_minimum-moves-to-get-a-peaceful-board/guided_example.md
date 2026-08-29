# Guided Example: Minimum Moves to Get a Peaceful Board

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rooks": [[0, 0], [1, 0], [1, 1]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a 2D array `rooks` of length `n`, where $\text{rooks}[i] = [x_{i}, y_{i}]$ indicates the position of a rook on an `n x n` chess board. Your task is to move the rooks **1 cell **at a time vertically or horizontally (to an *adjacent* cell) such that the board becomes **peaceful**.

The objective is to compute `3` from `{"rooks": [[0, 0], [1, 0], [1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Decompose each move into one coordinate.** A rook at $(x,y)$ can move to an adjacent vertical or horizontal cell. A vertical move changes only $x$ by one; a horizontal move changes only $y$ by one. If that rook eventually reaches $(r,c)$, every route needs at least

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rooks": [[0, 0], [1, 0], [1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

moves, and a monotone route using exactly that many vertical and horizontal steps exists when considered geometrically.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

A peaceful $n\times n$ board with exactly $n$ rooks has exactly one rook in every row and every column. Therefore its final row coordinates must be the multiset $\{0,1,\ldots,n-1\}$, and its final column coordinates must be the same multiset. The total cost separates:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rooks": [[0, 0], [1, 0], [1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Counting rows and columns:** Count how many rooks occupy each row and column, then sweep the imbalance. If a prefix has $b$ excess rooks, exactly $\lvert b\rvert$ rooks must cross the next boundary; summing these absolute imbalances gives the minimum. This runs in $O(n)$ time and $O(n)$ space and is asymptotically faster than the exact sorting implementation.
- **Minimum-cost bipartite matching:** One could build assignment costs from rooks to complete destination cells and run a general matching algorithm. That obscures the separable one-dimensional structure and is dramatically more expensive.
- **Greedily move a rook to the nearest currently empty row and column:** Without sorted global matching, local tie choices can cross and increase later travel. The exchange argument is what justifies the rank-based assignment.
- **Duplicate rows:** Sorting places all equal row coordinates together and assigns them distinct target rows. No special duplicate handling is needed.
- **Duplicate columns:** The second sort handles them symmetrically and assigns distinct target columns.
- **Initially peaceful board:** Sorted row coordinates and column coordinates are both exactly $0,1,\ldots,n-1$, so every absolute difference is zero.
- **Single rook:** With $n=1$, its only legal position is $(0,0)$ under the coordinate constraints. Both sums are zero, and there is no collision issue.
- **Rooks may exchange relative identity:** The goal does not prescribe which rook must occupy which final square. Sorting exploits this freedom; assigning fixed labeled destinations could force unnecessary moves.
- **Collision restriction:** The arithmetic result assumes moves are sequenced, never that rooks pass through one another simultaneously. A temporarily blocked rook can wait while the blocking rook advances. Waiting costs no move, so it does not alter the minimum coordinate-distance total.
- **No initial duplicate cells:** This input guarantee is important for legal starting state and collision-free scheduling. Duplicate rows or columns are allowed; only the complete coordinate pair must be unique.
- **Input mutation:** The first lexicographic sort and second column-key sort both reorder `rooks`. Callers that need its original order must pass a copy.
- **Integer size:** The maximum total is safely small for the stated $n\le500$, and Python integer arithmetic would remain exact even without that small bound.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be both the number of rooks and the board dimension. The source sorts the list twice. Each Python sort takes $O(n\log n)$ worst-case time, and each following sum scans all rooks in $O(n)$ time. Constants from two sorts do not change the asymptotic result, so total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
