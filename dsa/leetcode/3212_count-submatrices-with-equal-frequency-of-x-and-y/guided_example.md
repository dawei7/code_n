# Guided Example: Count Submatrices With Equal Frequency of X and Y

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [["X", "Y", "."], ["Y", ".", "."]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a 2D character matrix `grid`, where $\text{grid}[i][j]$ is either `'X'`, `'Y'`, or `'.'`, return the number of submatrices that contain:

The objective is to compute `3` from `{"grid": [["X", "Y", "."], ["Y", ".", "."]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**The top-left corner is fixed.** Every counted submatrix must contain `grid[0][0]`. With axis-aligned submatrices inside the grid, any such rectangle must begin at row zero and column zero. It is therefore uniquely determined by its bottom-right cell $(i,j)$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [["X", "Y", "."], ["Y", ".", "."]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Instead of considering four independent boundaries, the algorithm considers each of the $RC$ possible bottom-right corners and asks for the numbers of X and Y characters in prefix rectangle

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Store two two-dimensional prefix counts.** `s[i][j][0]` is the number of X characters in the first `i` rows and first `j` columns, while `s[i][j][1]` is the analogous Y count. Row and column zero of `s` are padding, so grid cell `grid[i-1][j-1]` corresponds to prefix coordinate `s[i][j]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [["X", "Y", "."], ["Y", ".", "."]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One rolling prefix row:** Keep previous and current rows for both channels, reducing space to $O(C)$ while preserving $O(RC)$ time.
- **Column accumulators plus horizontal totals:** Update per-column X/Y counts as each new row arrives and scan their prefix across columns. This also achieves the manifest's $O(C)$ space.
- **Balance plus X-presence:** Store X as $+1$, Y as $-1$, dot as zero, along with either an X count or Boolean presence. Balance zero plus presence is equivalent to two counts.
- **Rescan every anchored rectangle:** There are $RC$ corners and each rectangle may contain $RC$ cells, leading to much worse time.
- **All dots:** Equality alone is insufficient; `X > 0` correctly rejects them.
- **Equal positive counts:** Any value $q\ge1$ for both channels qualifies, regardless of dot count.
- **More X than Y or vice versa:** The prefix is rejected even if it contains both symbols.
- **`grid[0][0]` is a dot:** Larger anchored rectangles may still qualify; containing the top-left cell does not require it to be X or Y.
- **Single-cell grid:** X alone and Y alone have unequal counts; dot has no X, so the answer is zero in every one-cell case.
- **Character-code trick:** `ord(x) & 1` is correct specifically for uppercase X and Y. Explicit branches are safer for maintenance.
- **Padding row and column:** They remove boundary condition branches from the recurrence.
- **Input preservation:** Only the separate prefix table is written.
- **Manifest mismatch:** Attribute $O(C)$ space only to a compressed alternative; the exact artifact is $O(RC)$ space.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RC)$. Let $R$ be the number of rows and $C$ the number of columns. Every grid cell is visited once, with constant work for two prefix channels, so time is $O(RC)$.
- **Auxiliary Space Complexity:** $O(RC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
