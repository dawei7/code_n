# Guided Example: Convert an Array Into a 2D Array With Conditions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 4, 1, 2, 3, 1]}`
- **Required output:** `[[1, 3, 4, 2], [1, 3], [1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`. You need to create a 2D array from `nums` satisfying the following conditions:

The objective is to compute `[[1, 3, 4, 2], [1, 3], [1]]` from `{"nums": [1, 3, 4, 1, 2, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Frequency determines the unavoidable number of rows

No row may contain the same integer twice. If a value $x$ occurs $f_x$ times in `nums`, its copies must occupy $f_x$ different rows. Therefore, every valid answer needs at least

$$
R=\max_x f_x
$$

rows. This is a lower bound: regardless of how other values are arranged, the most frequent value alone forces that many rows.

The central task is to show that exactly $R$ rows are also sufficient. The solution does so by placing the first copy of every distinct value in row zero, the second copy in row one, and in general the occurrence numbered $i+1$ in row $i$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 4, 1, 2, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count first, then distribute

`Counter(nums)` creates a mapping from each distinct value `x` to its frequency `v`. The answer starts as an empty list of rows.

For one mapping entry `x, v`, the inner loop visits row indices

$$
0,1,\ldots,v-1.
$$

At each index `i`:

- if row `i` does not exist yet, append a new empty row;
- append `x` to row `i`.

Thus a value occurring $v$ times appears once in each of the first $v$ rows. It can never appear twice in one row because the inner loop visits each row index only once for that value.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why rows are created exactly when needed

The condition `len(ans) <= i` means the requested row index is not yet present. Since `i` grows from zero upward without gaps, appending one row makes index `i` valid immediately.

Suppose the values processed so far have maximum frequency $M$. The answer then contains exactly $M$ rows. Processing a new value with frequency $v$ creates rows only for indices already at or beyond $M$, so the new count becomes $\max(M,v)$. After every distinct value has been processed, the number of rows is exactly $\max_x f_x=R$.

The construction therefore meets the lower bound proved earlier. It is not merely valid; it uses the minimum possible number of rows.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 3, 4, 2], [1, 3], [1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 4, 1, 2, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 3, 4, 2], [1, 3], [1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Process occurrences online:** Track the count already seen for each value and put the next copy directly into the row with that index. This also runs in $O(n)$ time and avoids a separate counting pass.
- **Repeatedly build sets:** Removing one distinct copy of every remaining value per round works conceptually but may rescan data and become quadratic.
- **Sort the array:** Equal values become grouped, but sorting adds $O(n\log n)$ time and is unnecessary.
- **All values distinct:** Maximum frequency is one, so exactly one row is produced.
- **All values equal:** Every row contains one copy, and the number of rows equals $n$.
- **Several values share the maximum frequency:** They coexist once per row across all $R$ rows without conflict.
- **Unequal row lengths:** Shorter-frequency values stop appearing in later rows, which the contract explicitly allows.
- **Input order:** The output need not reproduce it; only multiplicities and row validity matter.
- **Nonempty input:** At least one mapping entry exists, so the result always contains at least one row.
- **Input preservation:** `Counter` reads `nums`, and the construction never mutates the original array.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $n$ be the length of `nums` and $d$ the number of distinct values. Building `Counter` takes expected $O(n)$ time and stores $O(d)$ entries.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
