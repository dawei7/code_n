# Guided Example: Combinations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "k": 2}`
- **Required output:** `[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integers `n` and `k`, return *all possible combinations of* `k` *numbers chosen from the range* `[1, n]`.

The objective is to compute `[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]` from `{"n": 4, "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Make one include-or-exclude decision per number

The recursive function `dfs(i)` considers the next available number `i`. The list `t` contains the increasing combination prefix chosen from numbers smaller than `i`. At each ordinary state, the source explores two exhaustive possibilities:

- Include `i`: append it, recurse on `i + 1`, then remove it.
- Exclude `i`: recurse on `i + 1` without it.

Every size-`k` subset of `[1, n]` makes exactly one such yes-or-no decision for each relevant number. Following those decisions reaches its unique recursive path. This binary decision view is easy to derive even without thinking about permutations or nested loops.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why combinations are increasing and unique

Numbers are considered strictly in order: every recursive call advances from `i` to `i + 1`. Once a number has been skipped or selected, the recursion never returns to a smaller value within the same path. Consequently `t` is always strictly increasing.

The increasing representation removes permutation duplicates. The subset containing 1 and 3 can appear only as `[1, 3]`; no path can produce `[3, 1]` because 1 is no longer available after the recursion reaches 3. Distinct decision paths choose distinct sets, so the same increasing combination is never emitted twice.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Numbers are considered strictly in order: every recursive ca... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Copy a complete combination before backtracking

When `len(t) == k`, the current prefix is a complete answer. The source appends `t[:]`, a shallow copy, and returns immediately. The copy is essential because `t` is the single mutable working list shared by all recursive calls. Appending `t` itself would make every result entry refer to that same list, which is later popped and reused.

Returning at size `k` is also safe. Adding more numbers would create an oversized selection, and excluding future numbers would only lead to the same already-recorded combination. One output is produced at the first moment the path reaches the required size.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Feasibility-pruned backtracking:** Stop when r:** - **Feasibility-pruned backtracking:** Stop when remaining values cannot fill the needed slots, or limit the choice loop to legal starts. This removes dead subtrees and supports the output-sensitive manifest time more closely.
- **Increasing-choice DFS:** Loop from the next minimum value through the last feasible choice rather than creating an explicit exclude branch. Its stack depth is bounded by `k`.
- **Lexicographic index successor:** Start with `[1, ..., k]` and repeatedly advance the rightmost movable index. It is iterative and output-sensitive.
- **Bitmask enumeration:** Test all $2^n$ subsets and output masks with `k` bits. It is simple for small `n` but explicitly exponential regardless of output count.
- **`k == 1`:** The include branch emits each singleton, while exclusion chains still reach depth proportional to `n`.
- **`k == n`:** Only one output exists, but missing feasibility pruning causes extensive dead exploration.
- **`n == 1`, `k == 1`:** The first include immediately records `[1]`.
- **Copy requirement:** `t[:]` prevents later pops from changing stored answers.
- **Any output order:** Depth-first order is acceptable without post-sorting.
- **No duplicate combinations:** Strictly increasing decisions create one representation per subset.
- **Contract excludes `k > n`:** If it occurred, the source would eventually return an empty answer after exploring failure paths.
- **Manifest discrepancy:** Both time and stack-space declarations require a pruned or different generator, not this exact unpruned binary recursion.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^n+k\binom{n}{k})$. Copying all outputs necessarily costs $\Theta(k\binom{n}{k})$. Beyond that output work, the unpruned search visits states for incomplete selections across growing prefixes. A useful bound is $O(\sum_{q=1}^{k}\binom{n+1}{q})$ recursive states; in the worst case, such as `k = n`, this is $O(2^n)$. Exact time is therefore safely described as $O(2^n+k\binom{n}{k})$ in the worst case, not the manifest's $O(k\binom{n}{k})$ for this source.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
