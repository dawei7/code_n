# Guided Example: Sparse Matrix Multiplication

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mat1": [[1, 0, 0], [-1, 0, 3]], "mat2": [[7, 0, 0], [0, 0, 0], [0, 0, 1]]}`
- **Required output:** `[[7, 0, 0], [-7, 0, 3]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two <a href="https://en.wikipedia.org/wiki/Sparse_matrix" target="_blank">sparse matrices</a> `mat1` of size `m x k` and `mat2` of size `k x n`, return the result of `mat1 x mat2`. You may assume that multiplication is always possible.

The objective is to compute `[[7, 0, 0], [-7, 0, 3]]` from `{"mat1": [[1, 0, 0], [-1, 0, 3]], "mat2": [[7, 0, 0], [0, 0, 0], [0, 0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the dimensions line up

For a fixed output row `i`, `mat1[i]` contains $k$ values. For a fixed output column `j`, taking `mat2[0][j]`, `mat2[1][j]`, through `mat2[k - 1][j]` also gives $k$ values.

The shared index selects corresponding positions along that row and column. Multiplying each pair and adding all $k$ products produces one scalar output cell.

The problem guarantees `len(mat1[0]) == len(mat2)`, so every access `mat1[i][k]` has a matching `mat2[k][j]`. No dimension validation is needed in the method.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mat1": [[1, 0, 0], [-1, 0, 3]], "mat2": [[7, 0, 0], [0, 0, 0], [0, 0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Creating the output

The source reads

- `m = len(mat1)` for the output row count;
- `n = len(mat2[0])` for the output column count.

It creates `ans` as $m$ distinct rows, each containing $n$ zeros. Starting with zero is necessary because every output cell is built as a running sum of products.

The list comprehension creates a new inner list for each row. This avoids aliasing: changing `ans[i][j]` affects only that row rather than accidentally modifying the same shared row object several times.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source reads

- `m = len(mat1)` for the output row count... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The three nested loops

The outer loop chooses output row `i` from 0 through $m-1$. The middle loop chooses output column `j` from 0 through $n-1$. Together, these loops visit every one of the $mn$ output coordinates exactly once.

For one fixed `(i, j)`, the inner loop iterates over every shared-dimension index from 0 through `len(mat2) - 1`. At each index it adds

`mat1[i][k] * mat2[k][j]`

to the current output cell.

When the inner loop begins, `ans[i][j]` is zero. After its first iteration, it contains the contribution through shared index 0. After shared index `t`, it contains

$$
\sum_{q=0}^{t}\texttt{mat1}[i][q]\cdot\texttt{mat2}[q][j].
$$

After the final iteration, this is exactly the complete dot-product formula. The next `(i, j)` cell starts from its own independent zero.

Although `k` is also conventionally used as the name of the shared dimension, in the Python source it is the loop variable. `len(mat2)` supplies the dimension size, and the loop variable takes each valid shared index in turn.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[7, 0, 0], [-7, 0, 3]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mat1": [[1, 0, 0], [-1, 0, 3]], "mat2": [[7, 0, 0], [0, 0, 0], [0, 0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[7, 0, 0], [-7, 0, 3]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Skip zero values from `mat1`:** Reorder loops :** - **Skip zero values from `mat1`:** Reorder loops as row `i`, shared index `t`, then output column `j`. If `mat1[i][t]` is zero, skip the entire column loop. This helps when the left matrix is sparse while retaining dense storage.
- **Compress both matrices by row:** Store only `(column, value)` pairs for every nonzero entry. For each nonzero `mat1[i][t]`, propagate products through nonzero entries in row `t` of `mat2`. This realizes the sparse behavior described by the manifest.
- **CSR for `mat1` and CSC for `mat2`:** Intersect sorted shared indices for each output row-column pair. This avoids zero products but adds compression and two-pointer machinery.
- **Transpose `mat2`:** Turning its columns into contiguous rows can make each dot product easier to express and can improve memory locality, but it still performs $O(mnk)$ arithmetic unless zeros are skipped.
- **Return a sparse product:** The contract requires a dense $m\times n$ list, so even a sparse multiplication strategy must eventually materialize zero output entries.
- **All-zero matrix:** Every multiply-add contributes zero, and the initialized output is returned unchanged.
- **One-by-one matrices:** The loops execute once and return the product of the two scalar entries.
- **Negative entries:** Ordinary signed multiplication and addition naturally handle negative contributions and cancellation.
- **Cancellation to zero:** An output zero may result from nonzero positive and negative products canceling, so a sparse algorithm cannot infer output sparsity merely from input positions.
- **Dense inputs:** The direct method performs the asymptotically expected $mnk$ work, and sparse metadata would offer little arithmetic reduction.
- **Sparse inputs:** The exact method still performs all $mnk$ multiplications, including products containing zero; this is its main limitation relative to the problem's title.
- **Compatible dimensions:** The source assumes at least one row and column and a matching shared dimension, all guaranteed by the constraints.
- **No input mutation:** The method only reads both matrices and writes a newly allocated result.
- **Integer magnitude:** Products and sums remain exact in Python integers, including negative totals.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mnk)$. There are $m$ choices for `i`, $n$ choices for `j`, and $k$ shared indices for each pair. The exact number of multiply-add iterations is $mnk$, so time complexity is $O(mnk)$ regardless of how many matrix entries are zero.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
