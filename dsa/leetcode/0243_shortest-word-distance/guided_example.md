# Guided Example: Shortest Word Distance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"wordsDict": ["a", "b"], "word1": "a", "word2": "b"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `wordsDict` and two different strings that already exist in the array `word1` and `word2`, return *the shortest distance between these two words in the list*.

The objective is to compute `1` from `{"wordsDict": ["a", "b"], "word1": "a", "word2": "b"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the latest opposite occurrence is enough

Suppose the scan reaches a new occurrence of `word1` at index `k`. Every occurrence of `word2` seen so far has an index no greater than `k`. Among those indices, the largest one—the latest `word2` index—is closest to `k`, because subtracting a larger prior index produces a smaller distance. Any older occurrence lies even farther left and cannot form a better pair with this new `word1`.

The same argument holds symmetrically when the new word is `word2`: the latest prior `word1` is the closest `word1` on its left. Future occurrences do not need to be anticipated. When a future target is eventually encountered, it will be paired with the most recent opposite target then available.

This local rule covers the global optimum. Take any closest pair in the complete array and consider whichever of its two occurrences appears later. When the scan reaches that later occurrence, the earlier member of the pair is an occurrence of the opposite target. The stored latest opposite occurrence is either that member or an even later one, and therefore is at least as close. The algorithm evaluates that distance and cannot miss a globally minimum pair.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"wordsDict": ["a", "b"], "word1": "a", "word2": "b"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How each loop iteration updates the state

At index `k`, the current word is `w`.

- If `w == word1`, assign `i = k`.
- If `w == word2`, assign `j = k`.
- If both indices are no longer `-1`, evaluate `abs(i - j)` and minimize `ans` with it.

The source uses two independent `if` statements rather than `if` followed by `elif`. The contract guarantees `word1 != word2`, so one word cannot satisfy both conditions in the same iteration; under the valid input, the two forms behave identically. The separate checks also make the symmetry visible.

The distance check occurs on every iteration after both targets have first appeared, even if the current word matches neither target. In those iterations, neither `i` nor `j` changes, so the code simply compares `ans` with the same latest-pair distance again. This repeated constant-time comparison is harmless. An implementation could place the check only inside target-matching branches, but it would not improve the asymptotic bound.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At index `k`, the current word is `w`.

- If `w == word1`, a... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace through the examples

Use



with `word1 = "coding"` and `word2 = "practice"`.

- At index `0`, `practice` sets `j = 0`. Since `coding` has not appeared, there is no valid pair yet.
- Indices `1` and `2` match neither target, so the recorded state remains unchanged.
- At index `3`, `coding` sets `i = 3`. Both targets are now known, so the candidate distance is `abs(3 - 0) = 3`, and `ans` becomes `3`.
- Index `4` does not change either target index. The final answer remains `3`.

For `word1 = "makes"` and `word2 = "coding"`, index `1` first records `makes`, index `3` records `coding` and creates distance `2`, and index `4` replaces the latest `makes` position. The new distance is `abs(4 - 3) = 1`, so the answer becomes `1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"wordsDict": ["a", "b"], "word1": "a", "word2": "b"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare every cross-target pair:** Record or d:** - **Compare every cross-target pair:** Record or discover every `word1` position and every `word2` position, then test all combinations. It is correct but can take $O(n^2)$ time when both words occur frequently.
- **Store both position lists and merge them:** Since occurrence indices are sorted, a two-pointer merge can find the minimum in linear time after collection. It is also $O(n)$ overall but uses $O(n)$ extra space that the streaming method avoids.
- **Track only the last relevant word and index:** Another one-pass form stores the most recent occurrence of either target. Whenever the other target appears, update the distance. It is equivalent under `word1 != word2`, while the two-index form mirrors the contract directly.
- **Targets at adjacent positions:** Their distance is `1`, the smallest possible because the words are distinct and therefore cannot occupy the same index. An implementation could return immediately once `ans == 1`, although the exact source simply completes the scan.
- **Many repeated occurrences:** Replacing an old target index with the new one is safe; for every future opposite occurrence, the newer index is closer than any older index on the same side.
- **First valid pair appears late:** Until both sentinels are replaced, the solution correctly avoids computing a meaningless distance involving `-1`.
- **Targets at the two ends:** If no closer occurrences exist, `abs(0 - (n - 1))` correctly gives `n - 1`.
- **`word1 == word2`:** The source is not designed for that variant. Its two `if` statements would assign both indices to the same position and report zero. The problem explicitly guarantees that the target words are different; the related same-word variant requires tracking consecutive distinct occurrences.
- **A missing target:** The documented input excludes this case. Without the presence guarantee, `ans` could remain infinity and the API would need to define an alternate return value or exception.
- **Non-target words:** They do not affect the relevant indices. Recomputing the unchanged distance during such iterations is redundant but correct and constant time.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of strings in `wordsDict`. The algorithm performs one left-to-right pass and stores no occurrence lists. Assuming word equality is treated as constant time under the constraint that each word has length at most `10`, the running time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
