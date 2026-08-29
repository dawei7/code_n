# Guided Example: Permutations II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 2]}`
- **Required output:** `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a collection of numbers, `nums`, that might contain duplicates, return *all possible unique permutations **in any order**.*

The objective is to compute `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]` from `{"nums": [1, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Duplicates change the meaning of different index paths

If all input values were distinct, choosing different indices at any position would necessarily create different permutations. With duplicates, two physical indices may contain the same value. For `[1a, 1b, 2]`, treating the two `1` copies as distinguishable would generate both `[1a, 1b, 2]` and `[1b, 1a, 2]`, even though both appear as `[1, 1, 2]` in the required output.

The solution still tracks physical indices so each input occurrence is used once, but it imposes one canonical order on equal occurrences. Sorting makes equal values adjacent. Along any recursion path, an earlier copy must be used before a later equal copy. This eliminates interchangeable index labelings while preserving every distinct value ordering.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The duplicate-skip condition in plain language

The loop rejects index `j` for either of two reasons:

- `vis[j]` is true, so that exact input occurrence is already in the partial permutation.
- `nums[j] == nums[j - 1]` and `vis[j - 1]` is false, so an equal earlier occurrence is still available and must represent this choice first.

The second rule is often misunderstood. It does **not** say “never choose adjacent equal values.” If the earlier copy is already used in the current path, `not vis[j - 1]` is false and the later copy is allowed. That is how a valid result can contain both `1`s.

At one recursion depth, after the branch using the earlier `1` has been fully explored and backtracked, that earlier flag becomes false. The later `1` is then skipped as a sibling first choice because it would generate exactly the same value suffixes. Thus the condition suppresses duplicate branches at each position while allowing multiplicity across positions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: State and path invariant

`dfs(i)` fills output position `i`. The preallocated list `t` has $n$ slots, and `vis` marks which sorted input indices have been used. At entry, `t[0:i]` contains the current prefix, exactly `i` flags are true, and equal selected occurrences respect their left-to-right canonical order.

For an allowed index `j`, the source writes `nums[j]` into `t[i]`, marks the index, and calls `dfs(i + 1)`. The child therefore has one more filled output position and one fewer available occurrence. After the child returns, clearing `vis[j]` restores the parent state.

The code does not clear `t[i]`. That is safe because the next allowed sibling overwrites the slot before recursion, and a result is copied only when all $n$ positions have been filled. The placeholder zeros and stale suffix entries are never interpreted as selections; `i` and `vis` define the active state.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Frequency-map backtracking:** Store each distinct value's remaining count and choose among keys. It removes occurrence labels entirely and naturally avoids duplicates, but needs a map and count restoration.
- **Depth-local set:** At each output position, remember which values have already begun a sibling branch. This works without the predecessor rule but allocates or clears additional sets throughout recursion.
- **In-place swapping with duplicate suppression:** Swap candidates into the current position and use a set to avoid equal swaps at that depth. It can remove `vis` but requires careful array restoration.
- **Post-generation set deduplication:** Generate all $n!$ labeled permutations and put tuples into a set. It is correct but wastes enormous work when multiplicities are high.
- **All values equal:** Only the earliest unused copy is allowed at each depth, producing exactly one permutation.
- **Earlier equal copy already used:** The later copy must be allowed; otherwise valid permutations containing multiple copies would disappear.
- **Single element:** One legal choice fills the path and records one result.
- **Negative values and zero:** Sorting and equality work identically; numeric sign has no special role.
- **Input mutation:** `nums.sort()` changes input order. A sorted copy would be needed if caller-visible preservation mattered.
- **Output order:** Canonical traversal happens to be lexicographic relative to sorted input, but only uniqueness and completeness are required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \cdot n!)$. Let value frequencies be $f_1, f_2, \ldots$. The exact number of unique permutations is
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
