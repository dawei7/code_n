# Guided Example: Sort the Matrix Diagonally

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mat": [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]}`
- **Required output:** `[[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **matrix diagonal** is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the **matrix diagonal** starting from $\text{mat}[2][0]$, where `mat` is a `6 x 3` matrix, includes cells $\text{mat}[2][0]$, $\text{mat}[3][1]$, and $\text{mat}[4][2]$.

The objective is to compute `[[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]` from `{"mat": [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A constant key for each diagonal

For cell `(i, j)`, the source uses key:

`m - i + j`.

Moving to `(i + 1, j + 1)` gives:

$$
m-(i+1)+(j+1)=m-i+j,
$$

so the key remains constant along a bottom-right diagonal.

Different parallel diagonals have different values of `j - i` and therefore different shifted keys. Adding `m` makes every used index positive, allowing a list of buckets instead of a dictionary.

`g` has `m + n` lists. Its index zero is unused, while all actual keys fit from one through `m+n-1`.

The extreme keys make that range concrete. The bottom-left cell `(m - 1, 0)` has key one. The top-right cell `(0, n - 1)` has key `m + n - 1`. Every other cell lies between them. This proves both that the allocation is large enough and that no negative indexing accidentally addresses a bucket from the end of the Python list.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mat": [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Collecting matrix values

The nested loops visit every matrix cell in row-major order. `g[m - i + j].append(x)` places its value in the matching diagonal bucket.

At this stage, the matrix remains unchanged, and all $mn$ values are stored exactly once across the buckets.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why buckets are sorted in reverse

Each bucket executes `e.sort(reverse=true)`, placing its largest value first and smallest value last.

The write-back phase uses `pop()`, which removes the final list element in constant amortized time. Because the final element is currently smallest, successive pops yield ascending values.

If buckets were sorted in ordinary ascending order, popping from the end would produce descending diagonals. Removing from index zero would preserve ascending order but cost linear time per removal because Python must shift remaining list elements.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mat": [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Min-heaps by diagonal:** Heapify each bucket and pop minima during write-back. It has the same broad time bound but more per-pop overhead.
- **Sort one diagonal at a time:** This reduces auxiliary storage to $O(L)$ while preserving $O(mn\log L)$ time.
- **Counting sort:** Values lie from 1 through 100, so frequency counting can achieve linear matrix time under the bounded value range.
- **Ascending bucket plus front removal:** It is logically correct but inefficient in Python because removing index zero shifts the list.
- **One row:** Every diagonal has length one, so the matrix is unchanged.
- **One column:** Likewise, every diagonal contains one cell.
- **Duplicate values:** Sorting and popping preserve their multiplicity.
- **Unused bucket zero:** The shifted key never uses it; this wastes only one empty list.
- **Input mutation:** The same matrix is overwritten and returned.
- **Key choice:** `j - i` would also identify diagonals but needs a dictionary or offset for negative values.
- **Reverse sort:** It is paired deliberately with end-pop to emit ascending values.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn\log L)$. Let $m$ and $n$ be matrix dimensions and $L=\min(m,n)$, the maximum diagonal length.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
