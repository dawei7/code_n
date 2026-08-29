# Guided Example: Increment Submatrices by One

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "queries": [[1, 1, 2, 2], [0, 0, 1, 1]]}`
- **Required output:** `[[1, 1, 0], [1, 2, 1], [0, 1, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n`, indicating that we initially have an `n x n` **0-indexed** integer matrix `mat` filled with zeroes.

The objective is to compute `[[1, 1, 0], [1, 2, 1], [0, 1, 1]]` from `{"n": 3, "queries": [[1, 1, 2, 2], [0, 0, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Avoid touching every cell for every query

A direct implementation would loop over every row and column inside each rectangle. With up to $10^4$ queries and a $500\times500$ matrix, that repeats too much work.

A two-dimensional difference array records only where a rectangle's effect begins and ends. After all queries are marked, one two-dimensional prefix-sum pass reconstructs the value of every cell.

The source reuses `mat` first as the difference array and then transforms it in place into the returned matrix.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "queries": [[1, 1, 2, 2], [0, 0, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Mark one inclusive rectangle with four corners

For rectangle

$$
[x_1,x_2]\times[y_1,y_2],
$$

the method applies:

- `+1` at `(x1,y1)` to begin the effect;
- `-1` at `(x2+1,y1)` to stop it below the rectangle;
- `-1` at `(x1,y2+1)` to stop it to the right;
- `+1` at `(x2+1,y2+1)` to restore the region subtracted twice below and right.

The last three updates are performed only when their coordinates remain inside the `n x n` array.

This is the two-dimensional version of marking an inclusive one-dimensional interval with `diff[left]+=1` and `diff[right+1]-=1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the bottom-right correction is positive

Imagine reconstructing prefixes after placing the first three markers. The below-stop marker removes the effect from every cell below `x2`, and the right-stop marker removes it from every cell right of `y2`.

Cells both below and right lie in both removed regions, so they receive $-2$ even though the original `+1` should be canceled only once. Adding one at the bottom-right outer corner corrects this double subtraction.

This is inclusion-exclusion:

$$
+\text{start}
-\text{below}
-\text{right}
+\text{below-and-right}.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 1, 0], [1, 2, 1], [0, 1, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "queries": [[1, 1, 2, 2], [0, 0, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 1, 0], [1, 2, 1], [0, 1, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Direct rectangle loops:** They can cost $O(qn^2)$ in the worst case.
- **Row-wise difference arrays:** Mark each affected row separately, costing $O(qn+n^2)$.
- **Full-matrix query:** Only the top-left start marker lies inside; its prefix spread covers everything.
- **Single-cell query:** Four corner updates isolate exactly that cell.
- **Bottom or right boundary:** Out-of-range stop markers are omitted safely.
- **Overlapping queries:** Their marker contributions add.
- **Inclusive coordinates:** Stops occur at `x2+1` and `y2+1`.
- **Diagonal subtraction:** It prevents double-counting the shared upper-left prefix.
- **In-place reconstruction:** Difference markers become final values.
- **Query order:** It cannot affect the additive result.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q)$. Let $q$ be the number of queries. Each query performs at most four constant-time updates, costing $O(q)$.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
