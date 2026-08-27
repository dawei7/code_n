# Guided Example: Check if Every Row and Column Contains All Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[1, 2, 3], [3, 1, 2], [2, 3, 1]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An `n x n` matrix is **valid** if every row and every column contains **all** the integers from `1` to `n` (**inclusive**).

The objective is to compute `true` from `{"matrix": [[1, 2, 3], [3, 1, 2], [2, 3, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce “contains every number” to “has no duplicate”

Each row contains exactly $n$ positions. If all $n$ values in that row are distinct and every value belongs to the $n$-element set $\{1,2,\ldots,n\}$, then the row must contain that entire set. There is no room to omit a required value: omitting one would force some other allowed value to appear twice.

The same argument applies to each column, which also has exactly $n$ entries. Therefore the code only needs to test whether every row and column has `n` distinct values.

For any row or column sequence `row`, `set(row)` keeps one copy of each distinct value. The expression `len(set(row)) == n` is true exactly when that sequence has no duplicate. Under the stated value bounds, that is equivalent to containing all integers from `1` to `n`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[1, 2, 3], [3, 1, 2], [2, 3, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate rows and columns through one common pipeline

The matrix itself is iterable by rows, so `matrix` supplies the row sequences directly. The expression `zip(*matrix)` supplies the columns:

- `*matrix` passes the rows as separate arguments to `zip`;
- the first tuple produced takes element zero from every row, forming column zero;
- the second tuple takes element one from every row, forming column one;
- this continues for all $n$ columns.

For example, with

`[[1,2,3],[3,1,2],[2,3,1]]`,

`zip(*matrix)` yields the column tuples `(1,3,2)`, `(2,1,3)`, and `(3,2,1)`.

The expression `chain(matrix, zip(*matrix))` creates one iterable that first yields all rows and then all columns. This avoids duplicating the validation rule in two loops. The loop variable is named `row` in the generator even when it holds a column tuple, but the set test is identical for either kind of sequence.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The matrix itself is iterable by rows, so `matrix` supplies ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Require every sequence to pass

The generator

`(len(set(row)) == n for row in chain(matrix, zip(*matrix)))`

produces one boolean for each of the $2n$ required sequences. The outer `all(...)` returns true only if every boolean is true.

Python’s `all` short-circuits. As soon as a row or column produces fewer than $n$ distinct values, the final result is known to be false and the remaining sequences need not be inspected. If no failure occurs, all $n$ rows and all $n$ columns were checked, so the matrix is valid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[1, 2, 3], [3, 1, 2], [2, 3, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare with an expected set:** Build `set(ran:** - **Compare with an expected set:** Build `set(range(1, n + 1))` once and compare every row set and column set with it. This is equally clear and has the same $O(n^2)$ time and $O(n)$ auxiliary space, but the exact solution exploits the range constraint to compare only cardinalities.
- **Boolean seen array:** For each row and column, clear an $n$-element marker array and reject repeated values. This has deterministic $O(n^2)$ time but requires more explicit loops and reset logic.
- **Arithmetic sum only:** Checking whether each sequence sums to $n(n+1)/2$ is not sufficient in general because different repeated and missing values can have the same sum.
- **Rows only:** Valid rows do not imply valid columns. Both halves of `chain` are required.
- **Columns only:** The symmetric mistake can miss repeated values within a row.
- **One-by-one matrix:** The sole value is constrained to be `1`. The only row and column each form the set `{1}`, so the result is true.
- **First invalid row:** `all` stops immediately, potentially without constructing any column tuple. This is safe because one invalid row already disproves validity.
- **Rows valid but first invalid column:** After all rows pass, `chain` begins yielding zipped columns and the first invalid one stops evaluation.
- **Duplicate value:** In a length-$n$ sequence, any duplicate reduces the set size below $n$, because the sequence still contains only $n$ positions.
- **Constraint dependence:** If values outside `1` through `n` were permitted, `len(set(row)) == n` would need to be replaced by equality with the expected set. For legal inputs, the shorter condition is rigorous.
- **Square-shape guarantee:** `zip(*matrix)` truncates to the shortest input row in general Python code, but the contract guarantees an $n$ by $n$ matrix, so every column contains exactly $n$ entries.
- **Input preservation:** Sets and column tuples are newly created temporary objects; the original nested lists remain unchanged.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. There are $n$ rows and $n$ columns, and each contains $n$ values. Building a set for one sequence takes $O(n)$ expected time. Across all $2n$ sequences, the worst-case time is $O(n^2)$. Constructing the column tuples through `zip` also processes $n^2$ elements in total and does not change the bound.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
