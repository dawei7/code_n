# Guided Example: Special Positions in a Binary Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mat": [[1, 0, 0], [0, 0, 1], [1, 0, 0]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` binary matrix `mat`, return *the number of special positions in *`mat`*.*

The objective is to compute `1` from `{"mat": [[1, 0, 0], [0, 0, 1], [1, 0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Restating “special” as two counts

A position `(i, j)` is special only when three facts hold:

- the cell itself contains one;
- row `i` contains no other one;
- column `j` contains no other one.

Because the matrix is binary, those facts have a compact numerical form. If `mat[i][j] == 1`, then the row condition is equivalent to the total number of ones in row `i` being exactly one, and the column condition is equivalent to the total number of ones in column `j` being exactly one.

The solution precomputes those totals in `rows` and `cols`. This avoids rescanning an entire row and column separately for every candidate one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mat": [[1, 0, 0], [0, 0, 1], [1, 0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: First pass: collect reusable summaries

`rows` has one entry for every matrix row and starts with zeros. `cols` has one entry for every matrix column and also starts with zeros.

The nested loops use `enumerate` twice. The outer loop yields the row index `i` and the row list itself. The inner loop yields column index `j` and cell value `x`. At each cell, the code executes:

`rows[i] += x`

`cols[j] += x`

Since every `x` is either zero or one, adding `x` directly counts ones. A zero changes neither total; a one increments both the total for its row and the total for its column. An explicit `if x == 1` would produce the same summaries, but binary arithmetic makes the two unconditional additions concise.

After this first complete traversal, `rows[i]` equals the sum of all cells in row `i`, which is exactly its number of ones. Similarly, `cols[j]` equals the number of ones in column `j`.

For the matrix `[[1,0,0],[0,0,1],[1,0,0]]`, the row totals are `[1,1,1]` and the column totals are `[2,0,1]`. This immediately shows why the one at `(0,0)` is not special: its row contains one one, but its column contains two. The one at `(1,2)` has both totals equal to one and is special.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `rows` has one entry for every matrix row and starts with ze... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Second pass: test every position in constant time

The second pair of nested loops visits every matrix cell again. It evaluates:

`x == 1 and rows[i] == 1 and cols[j] == 1`.

This Boolean expression is true exactly for a special position. It first ensures the current cell is the one represented by the unique row and column counts. This first condition is logically useful even though a row and column total of one strongly constrain their intersection; stating it directly follows the definition and prevents counting a zero at the crossing of an unrelated one in the row and an unrelated one in the column.

The code adds the Boolean result directly to `ans`. In Python, `true` has integer value one and `false` has integer value zero. Therefore, a special cell increments `ans` by one, while every other cell leaves it unchanged.

This use of Boolean arithmetic is not counting “truth values” as a separate concept. It is a concise conditional increment:

- when all three comparisons are true, add one;
- otherwise, add zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mat": [[1, 0, 0], [0, 0, 1], [1, 0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Scan a row and column for every one:** This us:** - **Scan a row and column for every one:** This uses $O(1)$ extra space but can take $O(RC(R+C))$ time in the worst case because the same lines are checked repeatedly.
- **Store coordinates of all ones:** One could record each one and then examine only those candidates after building row and column counts. That may reduce the second scan for sparse matrices, but it adds up to $O(RC)$ coordinate storage; the checked-in solution simply performs a predictable second pass.
- **Use sets of occupied rows and columns:** A set records presence but not whether a row or column contains exactly one one. Counts are required to distinguish one occurrence from several.
- **Mutate the matrix to store counts:** Reusing the first row and column can reduce auxiliary storage, but it complicates marker collisions and alters the input. Separate count arrays are clearer and match the checked-in source.
- **All-zero matrix:** Every row and column count is zero. The `x == 1` test is always false, so the answer is zero.
- **Single one in the entire matrix:** Its row and column totals are both one, so it is the sole special position.
- **One row:** A one is special only if that row contains exactly one one. Each column contains at most its single cell, so the row total is the deciding restriction.
- **One column:** Symmetrically, a one is special only if the column contains exactly one one.
- **Identity matrix:** Every row and every column contains one one, so every diagonal one is counted.
- **Two ones sharing a row:** That row’s count is two, so neither can be special even if their respective column counts are one.
- **Two ones sharing a column:** The column count of two rejects both positions.
- **Boolean addition in Python:** The final expression adds one for true and zero for false. A port to a language that does not treat Booleans numerically should use an explicit conditional increment.
- **Non-binary values:** The direct-sum counting technique depends on the zero-or-one guarantee. For arbitrary cell values, increment counters only when a cell equals one.
- **Rectangular rather than square input:** `rows` and `cols` have independent lengths, so the solution handles any valid $R\times C$ shape.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RC)$. Let $R$ be the number of rows and $C$ the number of columns.
- **Auxiliary Space Complexity:** $O(R+C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
