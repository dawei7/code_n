# Guided Example: Lucky Numbers in a Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[3, 7, 8], [9, 11, 13], [15, 16, 17]]}`
- **Required output:** `[15]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` matrix of **distinct **numbers, return *all **lucky numbers** in the matrix in **any **order*.

The objective is to compute `[15]` from `{"matrix": [[3, 7, 8], [9, 11, 13], [15, 16, 17]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Split the two conditions into two collections

A lucky number must satisfy two independent properties:

1. It is the minimum value of its row.
2. It is the maximum value of its column.

The exact solution computes the values satisfying each property separately and then intersects the two sets.

`rows = {min(row) for row in matrix}` examines every row and stores its minimum value. If the matrix has $m$ rows, this produces at most $m$ values. A matrix entry appears in `rows` exactly when it is a row minimum.

`cols = {max(col) for col in zip(*matrix)}` transposes the way the matrix is iterated. The star operator supplies all matrix rows to `zip`. The first tuple produced contains the first element of every row, which is column zero; the next tuple is column one, and so on. Taking `max` of each tuple therefore finds every column maximum.

The set intersection `rows & cols` contains values that occur in both categories. Converting it with `list(...)` produces the required list, and the arbitrary iteration order of a set is acceptable because the answer may be returned in any order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[3, 7, 8], [9, 11, 13], [15, 16, 17]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why comparing values is enough here

The code does not retain the row and column coordinates of an extremum. That is safe because all matrix elements are globally distinct. A value identifies exactly one cell.

Suppose value $x$ is in both sets. Since it occurs only once in the matrix, the row-minimum occurrence and column-maximum occurrence must be that same cell. Thus $x$ is simultaneously the minimum in its own row and the maximum in its own column, so it is lucky.

The distinctness guarantee is important. With duplicates, a value could be the minimum of one row at one coordinate and the maximum of an unrelated column at another coordinate. A value-only intersection could then report it even if neither occurrence satisfies both conditions. A coordinate-based check would be needed for that generalized input.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The code does not retain the row and column coordinates of a... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Walking through the first example

For `[[3, 7, 8], [9, 11, 13], [15, 16, 17]]`, the row minima are 3, 9, and 15, giving `rows = {3, 9, 15}`. The column maxima are 15, 16, and 17, giving `cols = {15, 16, 17}`. Their only common value is 15.

The unique cell holding 15 is the first element of the last row and the last element of the first column. It is smaller than 16 and 17 in its row, while larger than 3 and 9 in its column. The intersection returns `[15]`.

If the two sets have no common value, no cell can satisfy both requirements, and the result is an empty list.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[15]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[3, 7, 8], [9, 11, 13], [15, 16, 17]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[15]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Coordinate scan with precomputed arrays:** Sto:** - **Coordinate scan with precomputed arrays:** Store each row minimum and column maximum, then test every cell against both indexed values. It is also $O(mn)$ and works even when duplicate values require coordinate awareness.
- **Max of row minima versus min of column maxima:** Under distinct entries, these two scalar values are equal exactly when a lucky number exists. This uses $O(1)$ extra scalar space but needs a less immediate proof.
- **Check every candidate from scratch:** For each cell, rescan its row and column. It is simple but costs $O(mn(m+n))$.
- **One row:** Its row minimum is lucky because every column contains only one value, making that value its column maximum only for the minimum's column.
- **One column:** The column maximum is lucky because every row contains one value and therefore that cell is its row minimum.
- **One cell:** The sole value is both minimum and maximum and is returned.
- **No intersection:** The empty set becomes an empty list, correctly indicating no lucky number.
- **Distinct values:** This guarantee makes value-set intersection equivalent to coordinate-level conjunction.
- **Duplicate values outside the contract:** A value may satisfy the two properties at different coordinates, creating a false positive; retain coordinates or test cells directly.
- **Arbitrary output order:** Set iteration order is not guaranteed, but the contract explicitly permits any order.
- **Rectangular shape:** `zip(*matrix)` works because every row has the same stated length.
- **Input mutation:** `min`, `max`, `zip`, and set construction only read the matrix.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of rows and $n$ the number of columns. Finding all row minima examines $mn$ values. Creating and reducing the column tuples also examines $mn$ values. Set intersection takes $O(m+n)$ expected time in the worst collection-size description, which is dominated by matrix scanning. Total time is $O(mn)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
