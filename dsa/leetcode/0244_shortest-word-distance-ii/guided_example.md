# Guided Example: Shortest Word Distance II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"wordsDict": ["a", "b", "a", "c"], "queries": [["a", "c"], ["c", "a"], ["a", "b"]]}`
- **Required output:** `[1, 1, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

The objective is to compute `[1, 1, 1]` from `{"wordsDict": ["a", "b", "a", "c"], "queries": [["a", "c"], ["c", "a"], ["a", "b"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why comparing every pair is wasteful

If `word1` occurs $a$ times and `word2` occurs $b$ times, a nested-loop comparison examines $ab$ pairs. Sorting changes what is necessary. Suppose the current positions are `a[i] = 4` and `b[j] = 10`. Keeping `4` while moving `j` forward cannot help, because every later `b` position is at least `10` and therefore at least as far from `4`. The only possible improvement involving these frontiers comes from advancing the smaller position `4` toward `10`.

This gives the merge rule:

- compute the current distance `abs(a[i] - b[j])`;
- if `a[i] <= b[j]`, increment `i`;
- otherwise, increment `j`.

At least one pointer advances on every iteration, so the scan always progresses.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"wordsDict": ["a", "b", "a", "c"], "queries": [["a", "c"], ["c", "a"], ["a", "b"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why discarding the smaller position is safe

Assume `a[i] <= b[j]`. All unexamined values in `b` are at indices `j` or later and satisfy `b[j'] >= b[j]`. Therefore,

$$
b[j']-a[i] \ge b[j]-a[i].
$$

The pair `(a[i], b[j])` is already the best possible pair involving `a[i]` and any not-yet-considered `b` value. Earlier `b` values were handled before pointer `j` reached its current position. Consequently, no future pair using `a[i]` can improve the answer, and advancing `i` loses nothing.

When `a[i] > b[j]`, the symmetric argument shows that every later `a` value is at least as far from this fixed `b[j]` as the current `a[i]`. Advancing `j` is safe.

By repeatedly finalizing the smaller frontier in this way, the loop considers enough neighboring cross-list positions to include a globally closest pair. It does not need to enumerate pairs whose ordering proves they are already worse.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Assume `a[i] <= b[j]`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A complete query trace

For the example mapping, call `shortest("makes", "coding")`. The lists are `a = [1, 4]` and `b = [3]`.

1. Start with `i = 0`, `j = 0`, comparing positions `1` and `3`. Their distance is `2`, so `ans` becomes `2`. Since `1 <= 3`, advance `i`.
2. Compare positions `4` and `3`. Their distance is `1`, so `ans` becomes `1`. Since `4 > 3`, advance `j`.
3. Pointer `j` has reached the end of `b`, so no further cross-list pair can be formed and the loop stops.

The method returns `1`, matching the adjacent occurrences at indices `3` and `4`.

For `shortest("coding", "practice")`, each list contains one position: `[3]` and `[0]`. The only distance is `3`, and advancing the pointer at `0` ends the loop.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 1, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"wordsDict": ["a", "b", "a", "c"], "queries": [["a", "c"], ["c", "a"], ["a", "b"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 1, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Rescan `wordsDict` for every query:** The one-:** - **Rescan `wordsDict` for every query:** The one-pass method from Shortest Word Distance uses $O(1)$ extra space and $O(n)$ time per call. It may be reasonable for one query, but repeated calls waste the opportunity to preprocess the fixed array.
- **Compare all occurrence pairs:** After indexing, testing every pair costs $O(ab)$ per query. The sorted two-pointer merge reduces this to $O(a+b)$.
- **Binary search the larger occurrence list:** For every position in the smaller list, find neighboring insertion positions in the larger list. This costs $O(\min(a,b)\log\max(a,b))$ and can be attractive when one word is extremely rare, though the implemented merge has a clean linear bound.
- **Cache query results:** If identical word pairs are requested repeatedly, an additional cache could return later answers in $O(1)$ expected time. It would require canonicalizing pair order and using extra space; the exact solution does not assume repeated queries.
- **Adjacent occurrences:** Distance `1` is the smallest legal answer because the query words are distinct. The loop could return immediately when it finds `1`, but continuing remains correct.
- **One occurrence per word:** Each list has length one, so the loop performs one comparison and returns their absolute index difference.
- **Highly frequent words:** The two lists may together contain much of the original array, making a query $O(n)$ in the worst case, but never quadratic.
- **Missing query word:** Valid input excludes this case. With `defaultdict`, an invalid lookup would create an empty list and leave `ans` as infinity, so a broader API should validate keys or define missing-word behavior.
- **Equal query words:** The contract forbids this. Supporting it would require the minimum gap between consecutive distinct entries within one occurrence list; comparing a list with itself would otherwise permit distance zero at the same occurrence.
- **Sortedness dependency:** The merge proof relies on each posting list being sorted. Appending indices during a left-to-right constructor pass guarantees that property without explicit sorting.
- **Input mutation after construction:** The class stores indices derived from the original snapshot. The interface provides no mutation operation; if the external array later changed, the index would not automatically update.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of words in `wordsDict`. The constructor visits each position once and performs an expected constant-time dictionary lookup plus list append, so preprocessing takes expected $O(n)$ time. Across the entire mapping, exactly $n$ indices are stored. Dictionary keys and lists add overhead proportional to the number of distinct words, which is at most $n$, so total retained space is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
