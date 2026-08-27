# Guided Example: Range Sum Query 2D - Immutable

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[3, 0], [1, 2]], "queries": [[0, 0, 1, 1]]}`
- **Required output:** `[6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a 2D matrix `matrix`, handle multiple queries of the following type:

The objective is to compute `[6]` from `{"matrix": [[3, 0], [1, 2]], "queries": [[0, 0, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Building one prefix entry

Suppose the constructor is processing original value `v = matrix[i][j]`. The desired `s[i + 1][j + 1]` must contain every cell from the origin through `(i, j)` inclusively.

Two already-computed rectangles cover almost all of that area:

- `s[i][j + 1]` covers all included columns in rows above `i`;
- `s[i + 1][j]` covers all included rows in columns left of `j`.

Adding them counts their shared top-left rectangle `s[i][j]` twice. Subtracting that overlap once restores a single copy. Finally, add the current cell `v`, which belongs to neither earlier rectangle:

$$
\texttt{s}[i+1][j+1]
=
\texttt{s}[i][j+1]
+
\texttt{s}[i+1][j]
-
\texttt{s}[i][j]
+
\texttt{matrix}[i][j].
$$

This is inclusion-exclusion during construction: add the region above, add the region to the left, remove their double-counted overlap, and add the new corner cell.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[3, 0], [1, 2]], "queries": [[0, 0, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the loop order supplies every dependency

The constructor processes rows from top to bottom and columns within a row from left to right.

When it computes `s[i + 1][j + 1]`, the entries in prefix row `i` were completed while processing earlier original rows. The entry `s[i + 1][j]` was completed one column earlier in the current row. The diagonal overlap `s[i][j]` is also already available. No future value is needed, so one forward pass fills the whole table.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The constructor processes rows from top to bottom and column... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Deriving a query by inclusion-exclusion

A query includes original rows `row1` through `row2` and columns `col1` through `col2`. Because the prefix table uses exclusive ending boundaries, the origin-based rectangle through the query's lower-right cell is

`s[row2 + 1][col2 + 1]`.

This rectangle includes the desired region, but it also includes cells above it and to its left.

First subtract the left strip:

`s[row2 + 1][col1]`.

It contains rows before `row2 + 1` but only columns before `col1`.

Then subtract the upper strip:

`s[row1][col2 + 1]`.

It contains rows before `row1` across all columns through `col2`.

The top-left rectangle `s[row1][col1]` belongs to both removed strips. It was present once in the original large prefix, then subtracted twice, leaving it counted negative once. Add it back once to make its net contribution zero.

The final query formula is

$$
\begin{aligned}
\operatorname{sumRegion}
={}&\texttt{s}[row2+1][col2+1]\\
&-\texttt{s}[row2+1][col1]\\
&-\texttt{s}[row1][col2+1]\\
&+\texttt{s}[row1][col1].
\end{aligned}
$$

Every cell inside the requested rectangle remains once. Cells only above or only left are removed once. Cells in the top-left overlap are added, removed twice, and restored once, for a net count of zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[3, 0], [1, 2]], "queries": [[0, 0, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sum every query cell:** It uses no prefix stor:** - **Sum every query cell:** It uses no prefix storage but costs $O(hw)$ for a queried rectangle of height $h$ and width $w$, reaching $O(mn)$ per query.
- **One prefix array per row:** Precompute horizontal sums, then subtract two prefixes for each row in the query. Construction is $O(mn)$ and space is $O(mn)$, but each query still costs $O(row2-row1+1)$.
- **Precompute every rectangle:** Constant-time lookup is possible, but the number of possible row and column boundary pairs leads to $O(m^2n^2)$ time and space.
- **Two-dimensional Fenwick tree:** It supports updates and region queries in logarithmic time. With no updates, the static prefix matrix gives simpler and faster $O(1)$ queries.
- **Two-dimensional segment tree:** It also supports mutable data but is far more complex and cannot improve on constant-time immutable queries.
- **Forgetting the overlap restoration:** Subtracting the upper and left strips removes their shared top-left rectangle twice. Failing to add it back makes the answer too small or otherwise numerically wrong when values are negative.
- **Using `row2` or `col2` without plus one:** The prefix convention is half-open, so this excludes the last requested row or column.
- **Adding one to the lower boundaries:** `row1` and `col1` already count the rows and columns before the query. Incrementing them would fail to subtract part of the unwanted prefix.
- **Single cell:** The four-corner formula isolates exactly that value, including when it is negative or zero.
- **Full matrix:** With upper-left `(0, 0)`, all subtractive border terms are zero, and the result is `s[m][n]`.
- **First row only:** `row1 = 0` makes both upper-prefix terms refer to zero row 0, so no special case is needed.
- **First column only:** `col1 = 0` similarly uses the zero column.
- **One-row matrix:** The method becomes the one-dimensional leading-zero prefix pattern while retaining the same formula.
- **One-column matrix:** It likewise reduces to vertical prefix subtraction.
- **Negative values:** Prefix totals are not required to be monotone. Inclusion-exclusion relies on exact addition and subtraction, not ordering.
- **Immutable-data requirement:** Changing one matrix entry after construction would invalidate every prefix covering that cell. This class deliberately exposes no update operation.
- **Valid query bounds:** The source omits defensive checks because the contract guarantees ordered, in-range inclusive corners.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of rows, $n$ the number of columns, and $q$ the number of calls to `sumRegion`.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
