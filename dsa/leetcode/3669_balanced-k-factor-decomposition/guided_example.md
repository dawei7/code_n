# Guided Example: Balanced K-Factor Decomposition

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 100, "k": 2}`
- **Required output:** `[10, 10]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integers `n` and `k`, split the number `n` into exactly `k` positive integers such that the **product** of these integers is equal to `n`.

The objective is to compute `[10, 10]` from `{"n": 100, "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The objective depends only on the smallest and largest factors

We need exactly `k` positive integers whose product is `n`. For one candidate list, the maximum difference between any two entries is

`maximum_factor - minimum_factor`.

There is no need to compare every pair separately. The source carries the minimum and maximum chosen so far and evaluates their spread after the last factor is determined.

Because `k <= 5` and `n <= 10^5`, exhaustive enumeration of divisor-based factorizations is feasible once divisors can be retrieved efficiently.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 100, "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Precompute divisors for every possible remainder

Outside the class, the source constructs `g` for all integers below `100001`:

`g[x]` is the list of every positive divisor of `x`.

The nested loops visit each `i` and append it to `g[j]` for every multiple `j` of `i`. Thus `i` is placed exactly in the lists of numbers it divides.

When the DFS has remaining product `x`, every valid next factor must divide `x`. The precomputed list `g[x]` supplies exactly those choices without testing all integers.

This table is global and built when the module is loaded, before `minDifference` runs. That fact materially affects the exact source’s standalone time and space even though the manifest omits it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Outside the class, the source constructs `g` for all integer... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build exactly `k` factors through a remaining product

The recursive state `dfs(i, x, mi, mx)` means:

- Positions `i + 1` through `k - 1` of `path` have already been chosen.
- Their product has been divided out.
- `x` is the product still needing decomposition.
- `mi` and `mx` are the smallest and largest chosen factors so far.
- Positions zero through `i` still need factors.

Initially `i = k - 1` and `x = n`, so all `k` positions remain.

When `i > 0`, the loop chooses any divisor `y` of `x`, writes it at `path[i]`, and recurses with remaining product `x // y`. Since `y` divides `x` exactly, no fraction or invalid remainder can appear.

The minimum and maximum are updated to include `y`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[10, 10]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 100, "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[10, 10]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate only non-decreasing factors:** Requi:** - **Enumerate only non-decreasing factors:** Require each next factor to respect an ordering bound. This removes permutation duplicates and matches the manifest summary more closely.
- **Generate divisors on demand:** Trial division up to `sqrt(x)` avoids the global `O(M log M)` table and may be preferable for one call.
- **Prime-factor distribution:** Factor `n` and distribute prime factors among `k` buckets. Searching balanced allocations can reduce redundant divisor recursion but is more involved.
- **Greedily choose factors near the `k`-th root:** Closeness is a useful heuristic but does not prove the minimum spread for arbitrary divisor structure.
- **Factor one:** Ones are valid positive factors and allow exactly `k` entries even when few nontrivial factors exist.
- **Perfectly balanced decomposition:** If all `k` factors can be equal, spread zero is optimal and cannot be improved.
- **Tied optimal decompositions:** The source updates only on a strict improvement and returns the first minimum-spread tuple encountered, which is allowed.
- **Order of returned factors:** The problem permits any order, so the source need not sort `ans`.
- **Global variable shadowing:** The nested parameter named `mx` shadows the module’s divisor-limit variable `mx` only within DFS; Python resolves each scope correctly.
- **Recursion depth:** It is at most `k <= 5` and is safe under ordinary Python limits.
- **Input range:** The table covers every permitted `n <= 10^5`.
- **Missing imports:** The stored source uses `List` and `inf` without imports. Standalone Python requires the corresponding `typing` and `math` imports unless provided by the harness.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M log M)$. Let `F` denote the number of divisor-choice recursion edges or states visited for the particular `(n, k)`. Each edge performs constant work, and each completed candidate copies `k <= 5` entries only when it improves the best. The per-call search is `O(F * k)` in the most literal bound and `O(F)` when fixed `k` is treated as a constant.
- **Auxiliary Space Complexity:** $O(M log M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
