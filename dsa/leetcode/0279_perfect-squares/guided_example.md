# Guided Example: Perfect Squares

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 12}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return *the least number of perfect square numbers that sum to* `n`.

The objective is to compute `3` from `{"n": 12}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View the problem as an unbounded minimum-combination problem

The usable values are the positive perfect squares no larger than `n`:

$$
1^2,2^2,3^2,\ldots,\left\lfloor\sqrt n\right\rfloor^2.
$$

Each square may be used any number of times. For example, the optimal representation of 12 uses `4` three times. This is the same structure as unbounded coin change, except the goal is to minimize the number of selected values rather than count combinations or minimize monetary coins.

The exact protected source solves this with a two-dimensional dynamic-programming table. The manifest describes a different number-theory algorithm with $O(\sqrt n)$ time and constant space. This explanation follows the actual table implementation and states its true bounds.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 12}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Define the table state precisely

Let

$$
m=\left\lfloor\sqrt n\right\rfloor.
$$

The source builds `f` with `m + 1` rows and `n + 1` columns. State `f[i][j]` means:

> the minimum number of square terms needed to make sum `j` when the allowed square values are only $1^2,2^2,\ldots,i^2$.

The row dimension controls which square types are allowed. The column dimension is the target subtotal. This definition makes the final answer `f[m][n]`, because row `m` permits every positive perfect square no larger than the requested target.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let

$$
m=\left\lfloor\sqrt n\right\rfloor.
$$

The source b... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Initialize impossible states and the empty sum

Every table entry begins as positive infinity. Infinity means that the subtotal has not been shown reachable with the currently permitted square types.

The one reachable state with zero square types is

$$
f[0][0]=0.
$$

Making sum zero requires choosing no terms, so its minimum count is zero. Any positive sum is impossible without square values and remains infinity in row zero.

This fictional empty-sum base case is what allows a perfect square to be recognized cleanly. When processing square $i^2$ and subtotal $j=i^2$, the include transition uses `f[i][0] + 1 = 1`, proving that one term is sufficient.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 12}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Number-theory classification:** Lagrange's fou:** - **Number-theory classification:** Lagrange's four-square theorem bounds the answer by four, and Legendre's three-square theorem identifies forced four-square cases; checking one and two squares distinguishes the rest. This achieves the manifest's $O(\sqrt n)$ time and $O(1)$ space but relies on deeper mathematical theorems and is not the exact source.
- **One-dimensional DP:** Initialize `dp[0] = 0`, then for each square update subtotals upward with `dp[j] = min(dp[j], dp[j-square] + 1)`. It preserves the unbounded recurrence while reducing space to $O(n)$.
- **Remainder BFS:** Treat each remainder as a node and subtract every usable square. The first level reaching zero gives the minimum term count. It is conceptually direct but requires a queue and visited-state storage.
- **Naïve recursion:** Trying every next square recomputes the same remainders many times and grows exponentially without memoization.
- **`n = 1`:** The square set contains 1, and `f[1][1]` becomes `f[1][0] + 1 = 1`.
- **`n` already a perfect square:** At row $i=\sqrt n$, the include transition from subtotal zero sets the answer to one.
- **Repeated square required:** The same-row transition and upward column order allow unlimited copies, which is essential for 12 as `4 + 4 + 4`.
- **Square larger than the subtotal:** The inclusion branch is skipped, preventing a negative column index and correctly carrying the smaller-square answer forward.
- **Infinity arithmetic:** Adding one to an unreachable infinity state remains infinity, so impossible partial choices cannot become falsely optimal.
- **Square 1 guarantees reachability:** Even if no larger square helps, `n` copies of 1 form `n`; the returned value is never infinity for legal positive input.
- **Positive-input guarantee:** The contract begins at 1. If zero were passed, the table would return `f[0][0] = 0`, which is the natural minimum empty sum.
- **Downward subtotal iteration:** This would block reuse of the current square within the same row and solve a different problem where each square is available once.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. There are $m=\lfloor\sqrt n\rfloor$ real square rows and $n+1$ subtotal columns. Each cell performs constant work, so the exact time complexity is
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
