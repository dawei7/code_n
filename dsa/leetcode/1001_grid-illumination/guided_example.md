# Guided Example: Grid Illumination

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "lamps": [[0, 0], [4, 4]], "queries": [[1, 1], [1, 0]]}`
- **Required output:** `[1, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a 2D `grid` of size `n x n` where each cell of this grid has a lamp that is initially **turned off**.

The objective is to compute `[1, 0]` from `{"n": 5, "lamps": [[0, 0], [4, 4]], "queries": [[1, 1], [1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent only active lamps, never the enormous grid

The grid side length can be as large as one billion, so constructing even one row is impossible. Fortunately, illumination depends only on the at most twenty thousand listed lamps and queries.

The solution stores active lamp coordinates in a set and maintains how many active lamps lie on each relevant row, column, and diagonal. A query can then be answered with four counter lookups instead of scanning any cells.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "lamps": [[0, 0], [4, 4]], "queries": [[1, 1], [1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Deduplicate the initial lamp list

The set comprehension

`s = {(i, j) for i, j in lamps}`

stores each physical lamp once even if its coordinate appears repeatedly in the input. This matches the statement: listing the same lamp multiple times still turns on only one lamp.

Deduplication must occur before the line counters are built. Otherwise, counters would claim multiple active lamps at one coordinate, and turning that lamp off once would leave false positive counts.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Identify rows, columns, and both diagonal families

Four `Counter` objects store active-lamp counts:

- `row[i]` counts lamps with row coordinate `i`;
- `col[j]` counts lamps with column coordinate `j`;
- `diag1[i - j]` counts lamps on a top-left to bottom-right diagonal;
- `diag2[i + j]` counts lamps on a top-right to bottom-left diagonal.

Why do these diagonal keys work? Moving one step down and right increases both coordinates by one, leaving `i - j` unchanged. Moving down and left increases the row and decreases the column, leaving `i + j` unchanged.

Every active lamp in the deduplicated set increments one entry in each counter.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "lamps": [[0, 0], [4, 4]], "queries": [[1, 1], [1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Materialize the grid:** Impossible when `n` can be one billion; sparse lamp state is mandatory.
- **Scan all active lamps per query:** It can test shared lines directly but costs `O(LQ)` in the worst case.
- **Store Boolean line presence only:** Counts are necessary because turning off one lamp must not clear a line still illuminated by another.
- **Duplicate input lamps:** The set collapses them before counters are incremented, preventing phantom multiplicity.
- **No lamps:** All counters return zero, every answer is zero, and neighborhood scans remove nothing.
- **No queries:** The preallocated answer is empty and returned after initialization.
- **Lamp on the queried cell:** It illuminates the query first, then is removed during the centered neighborhood scan.
- **Lamps sharing one line:** Removing one decrements the count but the line remains illuminated while another count is positive.
- **Edge and corner queries:** Out-of-range neighborhood coordinates fail set membership harmlessly.
- **Repeated queries:** Each uses the current state after all earlier shutdowns; previously removed lamps cannot be removed twice.
- **Two diagonal types:** Checking only `i - j` or only `i + j` would miss half of diagonal illumination.
- **Input preservation:** The original `lamps` and `queries` lists are not modified; the active set is separate.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Q)$. Let `L` be the number of listed lamps, `U` the number of unique lamp coordinates, and `Q` the number of queries.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
