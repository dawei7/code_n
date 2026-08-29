# Guided Example: Count Servers that Communicate

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 0], [0, 1]]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a map of a server center, represented as a $m * n$ integer matrix `grid`, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

The objective is to compute `0` from `{"grid": [[1, 0], [0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace repeated row and column searches with counts

A server at `grid[i][j]` communicates if there is at least one *other* server in row `i` or column `j`. Checking every row and column anew for every server repeats the same work. The exact solution first counts servers in every row and column, then classifies each server with two constant-time lookups.

The arrays `row` and `col` are sized to the grid dimensions. `row[i]` will hold the number of servers in row `i`, while `col[j]` will hold the number in column `j`. Both begin filled with zero.

During the first nested traversal, the code adds `grid[i][j]` to both relevant counters:

`row[i] += grid[i][j]`

`col[j] += grid[i][j]`

Because every cell is either zero or one, adding its value is equivalent to conditionally incrementing when a server is present. An empty cell contributes nothing; a server contributes one to exactly its row and exactly its column.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 0], [0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Deciding whether a particular server communicates

After the first pass, the condition for cell `(i, j)` is straightforward. It must contain a server, and either `row[i] > 1` or `col[j] > 1` must hold. A count greater than one means the row or column includes the current server plus at least one other server.

Testing only for a positive count would be wrong. Every server makes its own row and column counts positive, even when it is completely isolated. The strict comparison with one is what enforces “any other server.”

The returned expression uses a generator:

`grid[i][j] and (row[i] > 1 or col[j] > 1)`.

If the cell is zero, Python's `and` short-circuits and the expression evaluates to zero. If the cell is one, the expression evaluates to the Boolean communication condition. Python Booleans behave as integers in `sum`, with `true` contributing one and `false` contributing zero. Thus the outer `sum` counts exactly the qualifying server cells.

The generator visits all grid cells but does not create a list of Boolean results. It calculates and adds one condition at a time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Tracing the examples

For `[[1,0],[0,1]]`, both row counts are one and both column counts are one. Each occupied cell fails both greater-than-one tests, so the answer is zero.

For `[[1,0],[1,1]]`, row counts are one and two, while column counts are two and one. The top-left server communicates through its column. The bottom-left server communicates through both its row and column, and the bottom-right server communicates through its row. All three are counted.

In the third example, the two servers in the first row see `row[0] = 2`, and the two servers in the third column see that column's count is two. The bottom-right server has both relevant counts equal to one and is excluded. A server qualifying through both a row and a column still contributes only once because the algorithm evaluates one Boolean per occupied cell rather than adding the two conditions separately.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 0], [0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Search each server's row and column directly:** This uses $O(1)$ space but can take $O(mn(m+n))$ time when many cells contain servers.
- **Group server coordinates by row and column:** Dictionaries or lists of coordinates can identify communicable groups, but storing the actual positions uses more information than the two count arrays need.
- **Count isolated servers instead:** Count all servers, subtract those whose row and column counts both equal one, and obtain the same result. It still needs the same precomputed counts.
- **Row-at-a-time constant-space scan:** For a row with one server, scan its column to decide communication. This removes count arrays but can perform $O(m^2+mn)$ work depending on dimensions; claims of universal $O(mn)$ need care when $m$ can exceed $n$.
- **Empty cells:** Even if their row or column has many servers, the leading `grid[i][j]` value makes them contribute zero.
- **One isolated server:** Its row and column counts are both one, so it is excluded.
- **One row:** Every server communicates if the row contains at least two; otherwise the answer is zero.
- **One column:** The symmetric rule applies through the column count.
- **Qualifies in both directions:** Logical `or` produces one Boolean, so the server is not double-counted.
- **All-zero grid:** Every counter remains zero and the sum is zero.
- **All-one grid:** If the grid has more than one cell, every server has a partner in its row or column and all $mn$ cells are counted.
- **Nonempty-grid assumption:** The exact source reads `grid[0]`, which is safe because both dimensions are at least one under the contract.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2V)$. Let $m$ be the row count, $n$ the column count, and $V=m\cdot n$ the number of grid cells. The counting pass visits all $V$ cells. The generator in the return statement visits all $V$ cells again. Each visit performs constant work, so total time is $O(2V)=O(V)$, equivalently $O(mn)$.
- **Auxiliary Space Complexity:** $O(m+n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
