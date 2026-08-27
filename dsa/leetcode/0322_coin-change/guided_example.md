# Guided Example: Coin Change

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"coins": [1, 2, 5], "amount": 11}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

The objective is to compute `3` from `{"coins": [1, 2, 5], "amount": 11}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why this is an optimization problem, not a greedy counting problem.

For a target `amount`, many different combinations of denominations may produce the same total, and the task asks for the combination with the fewest coins. Taking the largest coin whenever possible is not reliable for arbitrary denominations. With `coins = [1,3,4]` and `amount = 6`, greedy selection takes `4 + 1 + 1`, which uses three coins, while `3 + 3` uses only two. A correct method must compare the possibilities created by every denomination.

The problem has useful optimal substructure. If an optimal combination for total $j$ uses a coin worth $x$, removing one copy of that coin leaves a combination for $j-x$. That remaining combination must itself use the minimum possible number of allowed coins. If it did not, replacing it with a better combination would improve the solution for $j$, contradicting optimality.

The exact source turns this observation into a two-dimensional dynamic program. The extra dimension makes the unlimited-use rule explicit and also gives a clean way to prove that every denomination choice has been considered.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"coins": [1, 2, 5], "amount": 11}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Define the state precisely.

Let $c$ be the number of denominations and let $A$ be `amount`. The table `f` has `c + 1` rows and `A + 1` columns. Its state means:

$$
f[i][j] = \text{the minimum number of coins needed to make total } j
\text{ using only the first } i \text{ denominations}.
$$

The word “only” is essential. Row `i` may use `coins[0]` through `coins[i - 1]`, each any number of times, but it may not use later denominations. When the algorithm finishes row $i$, it has solved every target from `0` through $A$ under exactly that set of allowed coin types.

Every cell initially contains infinity. Infinity is a sentinel meaning “this total has not been shown reachable.” With zero denominations, total zero is possible using zero coins, so the source sets

$$
f[0][0] = 0.
$$

Every positive total in row zero correctly remains unreachable because no coins are available. As later rows are filled, column zero is copied forward as zero: the empty selection always makes amount zero, regardless of how many denominations are allowed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let $c$ be the number of denominations and let $A$ be `amoun... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Derive the two choices for one cell.

When row $i$ is being processed, let `x` be its newly available denomination, `coins[i - 1]`. Any combination counted by `f[i][j]` falls into exactly one of two groups.

First, the combination may use no copy of `x`. Then it uses only the previous $i-1$ denominations, and its best coin count is already stored in `f[i - 1][j]`. The source begins by copying that value:

$$
f[i][j] = f[i-1][j].
$$

Second, the combination may use at least one copy of `x`. Remove one such copy. The remaining coins must make total $j-x$ while still being allowed to use all first $i$ denominations, including `x` again. Its candidate count is therefore

$$
f[i][j-x] + 1.
$$

This choice is legal only when $j \ge x$. The transition takes the smaller of the exclude and include candidates:

$$
f[i][j] = \min\bigl(f[i-1][j],\ f[i][j-x]+1\bigr).
$$

Notice that the include candidate reads from the current row, not the previous row. This is exactly how the source represents an unlimited supply. After using one `x`, the subproblem may use `x` again. If the transition used `f[i - 1][j - x]`, each denomination could be selected at most once, which would solve a different problem.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"coins": [1, 2, 5], "amount": 11}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One-dimensional bottom-up DP:** Keep `dp[j]` a:** - **One-dimensional bottom-up DP:** Keep `dp[j]` as the best count for total `j`, then for each denomination scan `j` upward from that coin value to $A$. This uses $O(A)$ space and the same $O(cA)$ time. It is a valid optimization because the current row only needs the previous-row value at `j` and the current-row value at `j-x`; however, it is not what the exact source allocates.
- **- **Amount-first one-dimensional DP:** For every t:** - **Amount-first one-dimensional DP:** For every total from `1` through $A$, try each denomination as the final coin. This also takes $O(cA)$ time and $O(A)$ space. It derives directly from the last-coin recurrence and allows unlimited reuse because all smaller totals are already known.
- **- **Top-down memoization:** Recursively try subtra:** - **Top-down memoization:** Recursively try subtracting each coin and cache the answer for each remaining amount. It has the same $O(cA)$ state-transition bound, but adds recursion overhead and can create a deep call stack when small denominations are present.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(cA)$. Let $c$ be `len(coins)` and $A$ be `amount`. The algorithm fills $(c+1)(A+1)$ table cells, and each cell performs only constant-time comparisons, indexing, and arithmetic. Its time complexity is $O(cA)$.
- **Auxiliary Space Complexity:** $O(cA)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
