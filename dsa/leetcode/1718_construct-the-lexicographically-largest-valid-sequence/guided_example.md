# Guided Example: Construct the Lexicographically Largest Valid Sequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3}`
- **Required output:** `[3, 1, 2, 3, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, find a sequence with elements in the range `[1, n]` that satisfies all of the following:

The objective is to compute `[3, 1, 2, 3, 2]` from `{"n": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use a padded array to simplify indices

The required sequence length is $2n-1$: value one occupies one position, while each of the other $n-1$ values occupies two.

The source allocates `path = [0] * (n * 2)` and intentionally leaves index zero unused. Meaningful positions are one through `2n-1`, and the returned result is `path[1:]`.

This one-based layout makes the second occurrence of value `i` naturally land at `u+i` when its first occurrence is at `u`. The condition `u + i < n * 2` is exactly the requirement that the second position stay at or below `2n-1`.

Zero means an unfilled position; valid sequence values begin at one, so the sentinel cannot be confused with placed data.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track whether each number remains available

`cnt` is initialized with value two in every slot, then `cnt[1] = 1`. The implementation uses these values mainly as truthy availability flags:

- For `i >= 2`, a truthy `cnt[i]` means both required occurrences have not yet been placed. Placement writes both at once and sets `cnt[i] = 0`.
- For one, truthy `cnt[1]` means its single occurrence is still available. Placement sets it to zero.

On backtracking, a larger value is restored to two and one is restored to one. The precise positive number reflects required multiplicity even though the code never decrements one occurrence at a time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `cnt` is initialized with value two in every slot, then `cnt... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Always work on the earliest unfilled position

`dfs(u)` attempts to complete the sequence from position `u` onward. If `path[u]` is already filled as the second occurrence of an earlier placement, it immediately calls `dfs(u + 1)`.

Otherwise, `u` is the earliest still-empty position. Choosing its value decides the first location at which all completions of the current prefix can differ. This is exactly the location that matters next for lexicographic order.

The base condition `u == n * 2` means every meaningful position one through `2n-1` has been passed. Because recursion skips only filled positions and never advances past an unfilled one without placing it, reaching the base means a complete valid sequence exists.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 1, 2, 3, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 1, 2, 3, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Ascending candidate order:** It would find the:** - **Ascending candidate order:** It would find the lexicographically smallest first solution, not the largest.
- **Generate every solution then compare:** It wastes memory and search after the first descending-order completion is already known to be maximal.
- **Bitmask availability:** A bitmask can replace `cnt` and make availability copying compact, while preserving the same backtracking.
- **Choose another empty position:** Filling the earliest empty position gives the direct lexicographic proof and generally stronger pruning.
- **`n = 1`:** Only the single one is placed.
- **Partner out of bounds:** `u+i < 2n` rejects the placement before indexing.
- **Partner already occupied:** The candidate cannot satisfy its exact-distance pair at this start and is skipped.
- **Occupied current position:** It is a previously placed second copy and must be skipped, not overwritten.
- **Value one:** It has one occurrence and no partner position.
- **Successful branch:** Placements are intentionally not undone when true propagates.
- **Failed branch:** Both positions and availability must be restored before trying another value.
- **Padding index zero:** It is never returned and exists only to make positions one-based.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n!)$. The backtracking search can explore factorially many arrangements in the worst case. Using the standard bound from the manifest, time is $O(n!)$, with substantial pruning from occupied positions, distance checks, and stopping at the first solution.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
