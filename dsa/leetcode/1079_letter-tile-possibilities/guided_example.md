# Guided Example: Letter Tile Possibilities

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tiles": "AAB"}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have `n`  `tiles`, where each tile has one letter $\text{tiles}[i]$ printed on it.

The objective is to compute `8` from `{"tiles": "AAB"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track letter multiplicities instead of physical tile identities

If two tiles both show `A`, swapping which physical tile was used does not create a new sequence. Treating tile positions as distinct would generate duplicates.

The solution begins:



For each distinct letter, `cnt[letter]` stores how many unused copies remain. The recursive state depends only on these counts, not on original tile indices.

For `"AAB"`, the state is two available `A` tiles and one available `B` tile. There is one choice named `A` at the first step, not two indistinguishable choices.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tiles": "AAB"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Interpret one recursive call

`dfs(cnt)` returns the number of distinct nonempty continuations that can be formed from the currently available tiles.

It initializes:



Then it considers every distinct letter key:



`i` is the letter and `x` is its available count at the start of this loop iteration. A letter with zero remaining copies cannot be chosen.

The Counter's keys do not change during recursion; only their numeric values are decremented and restored. Mutating values while iterating `cnt.items()` is safe because the dictionary size and key set stay fixed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count the sequence ending after the chosen next letter

For an available letter:



counts the sequence formed by appending that letter and stopping immediately.

This step is why the recursion counts sequences of every positive length, not only sequences that consume all tiles. Every chosen prefix is itself a valid nonempty result.

At the root for `"AAB"`, choosing `A` counts sequence `"A"`, while choosing `B` counts sequence `"B"`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tiles": "AAB"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Position-based backtracking plus a set:** It generates the same string through different identical tiles and needs a potentially huge set to deduplicate results.
- **Sorted tiles with duplicate skipping:** Backtrack over positions and skip equal unused choices at each depth. This also avoids duplicate sequences but requires more delicate used-index logic.
- **Memoize by remaining counts:** Different prefixes can reach the same remaining multiset, and the number of suffix continuations is identical. Caching can reuse that numeric result while still adding it under each distinct prefix.
- **Combinatorial frequency formula:** Enumerate how many copies of each letter a sequence uses, then count multiset permutations. It avoids spelling paths but requires careful enumeration and factorial arithmetic.
- **One tile:** The root has one available branch, counts one sequence, and the child returns zero.
- **All tiles identical:** There is exactly one sequence of each length from one through `n`, so the answer is `n`.
- **All tiles distinct:** Every partial permutation is unique, producing the largest recursion tree.
- **Counter keys with zero values:** They remain in the map and are skipped by `x > 0`.
- **No empty sequence:** The helper counts only after selecting a letter, so empty is excluded naturally.
- **Backtracking restoration:** Every decrement must be paired with an increment before the loop continues.
- **Uppercase alphabet:** Counter keys handle only letters actually present; the code does not waste iterations over all 26 possible letters.
- **Input preservation:** `tiles` is immutable, and only the separate Counter is modified and restored.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(DM)$. Let `n` be the number of tiles, `M` the number of distinct letters, and `D` the number of distinct nonempty sequences that can be formed.
- **Auxiliary Space Complexity:** $O(M + n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
