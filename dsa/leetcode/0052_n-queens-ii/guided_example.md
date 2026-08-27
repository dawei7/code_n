# Guided Example: N-Queens II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

The objective is to compute `2` from `{"n": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count valid leaves instead of constructing boards

The search places one queen in each row from top to bottom. At recursion depth `i`, rows 0 through `i - 1` already contain conceptual queens, and the loop chooses the column for row `i`. Because a row is handled exactly once, row conflicts are impossible without any explicit row marker.

Unlike N-Queens I, this problem asks only for the number of configurations. The algorithm does not need a grid or a list of chosen columns. It records which attack lines are occupied, explores every safe placement sequence, and increments a counter whenever all $n$ rows have been assigned.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Three marker families cover every attack

`cols[j]` says whether an earlier queen occupies column `j`. Cells with equal row-plus-column values lie on the same top-right-to-bottom-left diagonal, so `dg[i + j]` identifies that direction.

Cells with equal row-minus-column values lie on the other diagonal direction. Since `i - j` may be negative, the source adds `n` and uses `udg[i - j + n]`. For an $n \times n$ board, the sum ranges from 0 through $2n-2$, and the shifted difference ranges from 1 through $2n-1$.

The code computes those two indices once as `a` and `b`. A candidate is safe only when its column, sum diagonal, and shifted-difference diagonal are all false. These constant-time checks cover every way a queen in an earlier row could attack the new position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `cols[j]` says whether an earlier queen occupies column `j`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Fixed marker capacities rely on the stated constraint

Rather than allocating arrays from `n`, the source uses lengths 10, 20, and 20. The contract limits $n$ to at most 9. Therefore, column index `j` is at most 8, `i+j` is at most 16, and `i-j+n` is at most 17. Every access fits.

This is safe for the official domain but not a general implementation for arbitrary board sizes. If `n` were greater than 10, the fixed arrays could be too short. Allocating `n` columns and roughly `2n` entries per diagonal family would express the generalized relationship directly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Return subtree counts:** Have each recursive c:** - **Return subtree counts:** Have each recursive call sum counts returned by its children instead of mutating a nonlocal counter. This makes data flow explicit and is the competitive branch's style.
- **Bit masks:** Store occupied columns and diagonals in integers and recurse over available set bits. It uses compact state and is often substantially faster.
- **Symmetry reduction:** Explore only half of the first-row columns and double mirrored counts, handling a center column separately for odd `n`. It improves constants but complicates the proof.
- **Full board construction:** It is unnecessary when only a count is requested and would add $O(n^2)$ active or per-leaf work.
- **`n = 1`:** The sole position is safe, one base case is reached, and the answer is 1.
- **A dead-end row:** Its loop finds no safe column and returns without changing `ans`, correctly contributing zero.
- **Fixed array sizes:** They are valid only because $n \le 9$. General-purpose code should allocate from `n`.
- **Unused diagonal slot:** The shifted-difference formula starts at 1, leaving index 0 unused; this is harmless.
- **No input mutation:** The integer argument is unchanged, and all search state is internal.
- **No result-order issue:** Only a scalar count is returned, so traversal order has no observable significance.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(nV)$. Let $V$ be the number of partial non-attacking states reached. Each such state scans $n$ candidate columns and performs constant-time checks, so a precise traversal expression is $O(nV)$. Column uniqueness bounds depth by $n$ and limits complete column orders to $n!$; diagonal pruning reduces the actual search drastically.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
