# Guided Example: Range Sum Query 2D - Mutable

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]], "operations": [["sum", 2, 1, 4, 3], ["update", 3, 2, 2], ["sum", 2, 1, 4, 3]]}`
- **Required output:** `[8, 10]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a 2D matrix `matrix`, handle multiple queries of the following types:

The objective is to compute `[8, 10]` from `{"matrix": [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]], "operations": [["sum", 2, 1, 4, 3], ["update", 3, 2, 2], ["sum", 2, 1, 4, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The one-dimensional Fenwick tree inside each row

Each `BinaryIndexedTree` uses one-based positions. Original column 0 maps to tree position 1, and original column `j` maps to position `j + 1`.

For a positive tree position $x$, the source computes

$$
\operatorname{lowbit}(x)=x\mathbin{\&}(-x).
$$

This isolates the least significant set bit. Entry `c[x]` stores the sum of the one-based interval

$$
[x-\operatorname{lowbit}(x)+1,\ x].
$$

For example, `c[6]` covers positions 5 and 6 because `lowbit(6) = 2`, while `c[8]` covers positions 1 through 8 because `lowbit(8) = 8`.

These aligned partial sums support two operations:

- add a delta to one column in logarithmic time;
- calculate the sum of a row prefix in logarithmic time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]], "operations": [["sum", 2, 1, 4, 3], ["update", 3, 2, 2], ["sum", 2, 1, 4, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Updating a row tree by a delta

`tree.update(x, delta)` adds `delta` to logical one-based position `x`. It updates `c[x]` and then repeatedly advances with

`x += lowbit(x)`.

Each destination is the next larger stored interval containing the original position. The loop stops after passing the number of columns. Consequently, every partial sum affected by the point change receives the delta, and no unrelated interval changes.

The tree operation is additive. It does not mean “replace this value with `delta`.” The public matrix operation is an assignment, so the source must first translate an assignment into the correct difference.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `tree.update(x, delta)` adds `delta` to logical one-based po... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reading one row prefix

`tree.query(x)` returns the sum of the first `x` values in that row, corresponding to original columns 0 through `x - 1`.

It adds `c[x]` to an accumulator and repeatedly retreats with

`x -= lowbit(x)`.

The current entry supplies the last still-unaccounted block of the prefix. Subtracting its block length moves immediately before it. The visited blocks are disjoint and together cover one-based positions 1 through the original `x`.

For a row interval with inclusive original columns `[col1, col2]`, the source subtracts two prefixes:

$$
\operatorname{rowSum}(col1,col2)
=
\operatorname{query}(col2+1)-\operatorname{query}(col1).
$$

The first prefix includes original column `col2`; the second removes every column before `col1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[8, 10]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]], "operations": [["sum", 2, 1, 4, 3], ["update", 3, 2, 2], ["sum", 2, 1, 4, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[8, 10]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **true two-dimensional Fenwick tree:** Store par:** - **true two-dimensional Fenwick tree:** Store partial sums across both row and column lowbit ranges. Point updates and prefix rectangles then cost $O(\log m\log n)$, and inclusion-exclusion answers a rectangle with four prefix queries. This matches the manifest, but it is not the exact source.
- **Avoid the row slice:** Iterate row indices or use `itertools.islice` so a query does not allocate $O(h)$ temporary references. Time remains proportional to the number of included rows.
- **Keep a matrix of current values:** Reading `prev` becomes $O(1)$ during assignment, at the cost of another $O(mn)$ structure. The exact source instead isolates the cell with two prefix queries.
- **One segment tree per row:** It gives the same broad tradeoff: logarithmic column updates and row intervals, but linear dependence on query height.
- **Static two-dimensional prefix matrix:** Rectangle queries are $O(1)$ but a point update invalidates many prefixes and may cost $O(mn)$ to repair.
- **Direct matrix storage:** Updates are $O(1)$ while a rectangle query costs its full area $O(hw)$. Row Fenwick trees reduce width dependence to logarithmic.
- **Passing `val` as the Fenwick delta:** This would add the new value to the old one. Assignment requires `val - prev`.
- **Zero-based tree position:** Fenwick position zero cannot advance because `lowbit(0) = 0`. Column indices must be shifted by one.
- **Inclusive `row2`:** Python slicing excludes its ending index, so the exact slice must end at `row2 + 1`.
- **Inclusive `col2`:** The ending prefix must be `query(col2 + 1)` to include the final column.
- **Single-cell rectangle:** One row is selected and neighboring prefixes isolate exactly one current cell.
- **Single-row rectangle:** Only one tree contributes, so the query costs $O(\log n)$ plus constant iteration overhead.
- **All rows with a narrow column interval:** The query still visits every row because no structure aggregates row sums, even when the width is one.
- **One-column matrix:** Each tree operation is constant in practice, but a rectangle query still sums $h$ row results.
- **Negative cell values:** Fenwick trees require only additive inverses, so negative values and negative update deltas are handled exactly.
- **Assigning the existing value:** The delta is zero; all rectangle sums remain unchanged.
- **Rectangular guarantee:** Every row has the same `n`, so each row tree uses a consistent column coordinate system.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn\log n)$. Let $m$ be the number of rows, $n$ the number of columns, $q$ the number of public operations, and $h=row2-row1+1$ the height of one queried rectangle.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
