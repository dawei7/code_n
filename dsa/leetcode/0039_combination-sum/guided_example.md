# Guided Example: Combination Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"candidates": [2, 3, 6, 7], "target": 7}`
- **Required output:** `[[2, 2, 3], [7]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of *`candidates`* where the chosen numbers sum to *`target`*.* You may return the combinations in **any order**.

The objective is to compute `[[2, 2, 3], [7]]` from `{"candidates": [2, 3, 6, 7], "target": 7}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What makes the search difficult

The task is not merely to decide whether `target` can be formed. It must return every distinct combination, and each candidate may be reused any number of times. A straightforward choice sequence can create duplicates: choosing `2` and then `3` describes the same combination as choosing `3` and then `2`. The algorithm needs to explore repeated choices while treating order as irrelevant.

The central idea is to construct every combination in non-decreasing candidate-index order. After sorting `candidates`, a recursive call receives a lower-bound index `i`. It may choose only indices `j >= i`. Once candidate `j` is selected, recursion receives `j` again, not `j + 1`. Passing the same index permits unlimited reuse of that candidate; forbidding smaller indices prevents permutations of the same multiset from being generated later.

For example, after selecting `3`, the branch may select `3` again or move to a larger candidate, but it can never go back and select `2`. Therefore `[2, 2, 3]` is generated along the branch beginning with `2`, while `[3, 2, 2]` has no legal search path. This ordering rule enforces uniqueness structurally, without storing completed combinations in a set.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"candidates": [2, 3, 6, 7], "target": 7}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Meaning of the recursive state

The call `dfs(i, s)` has three pieces of state, even though only two are parameters:

- `t` is the current partial combination.
- `s` is the remaining sum still needed.
- `i` is the smallest candidate index that may be chosen next.

The key invariant is that the values in `t` have non-decreasing sorted indices and their sum is `target - s`. Every candidate before index `i` is intentionally unavailable because choosing it now would break that canonical order. Every candidate at or after `i` is still a possible next choice.

The initial call `dfs(0, target)` satisfies this invariant: `t` is empty, its sum is zero, the full target remains, and every candidate is available.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recognizing a completed combination

When `s == 0`, the values in `t` sum exactly to `target`. The code appends `t[:]`, a shallow copy, to `ans` and returns. The copy is essential. The same list object `t` is mutated throughout the entire depth-first search; storing `t` itself would make every answer entry refer to that one changing list, and after all backtracking they would all appear empty or otherwise corrupted.

Returning immediately is also correct because candidates are strictly positive. Adding another value would make the sum exceed `target`, so no longer extension of an already complete combination can be valid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[2, 2, 3], [7]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"candidates": [2, 3, 6, 7], "target": 7}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[2, 2, 3], [7]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Include-or-skip recursion:** At each candidate, one branch reuses it and another advances to the next candidate. This produces the same canonical combinations and can make the decision structure more explicit, though the loop form is compact.
- **Dynamic programming for existence or counts:** A one-dimensional table can decide reachability or count ways, but reconstructing every unique combination requires retaining predecessor structure and is less direct than backtracking for this output task.
- **Deduplicate permutations with a set:** Exploring candidates in arbitrary order and inserting sorted tuples into a set is correct with extra work, but it generates redundant paths and consumes hashing/storage that index ordering avoids.
- **Loop-level pruning:** Because candidates are sorted, the loop could stop as soon as `candidates[j] > s`. The selected source instead makes a short recursive call that immediately returns; adding `break` would improve constants without changing the search space of valid combinations.
- **`target` smaller than every candidate:** The initial `s < candidates[0]` test returns immediately, producing `[]`.
- **Candidate equals the target:** The root can choose it, the next call sees `s == 0`, and the one-element combination is copied into the answer.
- **Unlimited reuse:** Passing `j`, rather than `j + 1`, is the exact detail that permits combinations such as `[2, 2, 3]`.
- **Distinct positive candidates:** Distinctness supports the uniqueness proof, and positivity guarantees termination and pruning. Zero could cause recursion without reducing `s`; negative values would invalidate the overshoot argument. Both are excluded by the contract.
- **Mutation of the input:** `candidates.sort()` changes the caller's list order. The problem does not require preserving that order, but this observable side effect matters if the list is reused outside the judge.
- **Result order:** Depth-first traversal over sorted candidates happens to produce combinations in a regular order, but the contract allows any order, so correctness does not depend on it.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^{T/m})$. Let $n$ be the number of candidates, $T$ the target, and $m$ the smallest candidate. Because every choice contributes at least $m$, recursion depth is at most $\lfloor T/m \rfloor$. If one conservatively allows up to $n$ choices at every level, the search-tree bound is $O(n^{T/m})$, matching the manifest. Sorting first costs $O(n \log n)$ and is dominated by the exponential enumeration bound for nontrivial searches.
- **Auxiliary Space Complexity:** $O(T/m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
