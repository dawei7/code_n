# Guided Example: Matrix Similarity After Cyclic Shifts

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "k": 4}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` integer matrix `mat` and an integer `k`. The matrix rows are 0-indexed.

The objective is to compute `false` from `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "k": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Odd-indexed rows

Odd rows shift right. The source checks

`mat[i][j] == mat[i][(j + k) % n]`.

One may expect a right-shift comparison with `j - k` instead. For the question “does the row remain unchanged?”, the two directions are equivalent. A row invariant under rotation by $k$ is also invariant under the inverse rotation by $-k$, because both moves traverse the same cycles of column positions in reverse order.

Thus checking equality along the $+k$ permutation correctly decides invariance under the stated right shift.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "k": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Even-indexed rows

Even rows shift left. The source checks

`mat[i][j] == mat[i][(j - k + n) % n]`.

Again this follows the inverse direction of the physical move, but invariance under a cyclic permutation equals invariance under its inverse. Adding $n$ before modulo keeps the expression visibly nonnegative, though Python's modulo would also handle a negative value.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every cell comparison is sufficient

A shifted matrix equals the original exactly when every row equals its shifted version at every column. The loops visit every cell. If a mismatch exists, the method returns `false` immediately.

If all comparisons succeed, values are constant along every cycle formed by advancing $k$ columns modulo $n$. Applying the corresponding left or right rotation only permutes equal values within those cycles, so every row and therefore the matrix remains identical.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "k": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Construct the shifted matrix:** It is straightforward but uses $O(RC)$ extra space and writes values that comparison can address directly.
- **Slice each row:** Python slicing can express rotations but allocates new row lists, increasing auxiliary space.
- **Reduce `k %= n` first:** This improves readability and avoids repeated large-modulus operands, but the exact expressions already produce correct indices.
- **One column:** Every cyclic shift maps the only position to itself, so the result is always true.
- **All row values equal:** Any shift leaves that row unchanged.
- **Repeated pattern:** A row may remain invariant even when $k$ is not a multiple of $n$ if its values repeat with the required period.
- **Even versus odd direction:** Directions differ physically, but equality under a rotation is equivalent to equality under its inverse.
- **Rectangular guarantee:** The source takes column count from the first row and assumes every row has that length, as the matrix contract provides.
- **Large $k$:** Modulo indexing automatically reduces it by the row width.
- **Input preservation:** The method performs comparisons only and does not mutate `mat`.
- **Why inverse invariance holds:** If applying rotation $P$ leaves a row $r$ unchanged, then applying $P^{-1}$ to both sides of $P(r)=r$ gives $r=P^{-1}(r)$. The converse follows symmetrically.
- **Cycle length:** Each positional cycle has length $C/\gcd(C,k)$. Checking one equality per edge around these cycles proves all values in a cycle match.
- **Different rows are independent:** A shift never moves a value between rows, so failure or success can be decided row by row and combined with logical AND.
- **Early return location:** The first mismatch proves the final matrix differs at that cell; inspecting later cells cannot restore whole-matrix equality.
- **Parity check:** Row zero is even and uses the second branch. The explicit `i % 2` tests follow zero-based indexing from the contract.
- **No repeated simulation:** Performing $k$ one-position shifts would cost $O(kRC)$ and mutate data. Modular indexing collapses all steps into one comparison per cell.
- **Modulo with `j-k+n`:** Adding only one $n$ is still safe in Python even when $k>n$, because Python's modulo returns a nonnegative residue for negative dividends.
- **Zero-based row parity:** The first row shifts left, exactly as the even-index rule requires.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RC)$. Let $R$ be row count and $C$ column count. In the worst case, both nested loops inspect all $RC$ cells, so time complexity is $O(RC)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
