## General

**What makes the search difficult**

The task is not merely to decide whether `target` can be formed. It must return every distinct combination, and each candidate may be reused any number of times. A straightforward choice sequence can create duplicates: choosing `2` and then `3` describes the same combination as choosing `3` and then `2`. The algorithm needs to explore repeated choices while treating order as irrelevant.

The central idea is to construct every combination in non-decreasing candidate-index order. After sorting `candidates`, a recursive call receives a lower-bound index `i`. It may choose only indices `j >= i`. Once candidate `j` is selected, recursion receives `j` again, not `j + 1`. Passing the same index permits unlimited reuse of that candidate; forbidding smaller indices prevents permutations of the same multiset from being generated later.

For example, after selecting `3`, the branch may select `3` again or move to a larger candidate, but it can never go back and select `2`. Therefore `[2, 2, 3]` is generated along the branch beginning with `2`, while `[3, 2, 2]` has no legal search path. This ordering rule enforces uniqueness structurally, without storing completed combinations in a set.

**Meaning of the recursive state**

The call `dfs(i, s)` has three pieces of state, even though only two are parameters:

- `t` is the current partial combination.
- `s` is the remaining sum still needed.
- `i` is the smallest candidate index that may be chosen next.

The key invariant is that the values in `t` have non-decreasing sorted indices and their sum is `target - s`. Every candidate before index `i` is intentionally unavailable because choosing it now would break that canonical order. Every candidate at or after `i` is still a possible next choice.

The initial call `dfs(0, target)` satisfies this invariant: `t` is empty, its sum is zero, the full target remains, and every candidate is available.

**Recognizing a completed combination**

When `s == 0`, the values in `t` sum exactly to `target`. The code appends `t[:]`, a shallow copy, to `ans` and returns. The copy is essential. The same list object `t` is mutated throughout the entire depth-first search; storing `t` itself would make every answer entry refer to that one changing list, and after all backtracking they would all appear empty or otherwise corrupted.

Returning immediately is also correct because candidates are strictly positive. Adding another value would make the sum exceed `target`, so no longer extension of an already complete combination can be valid.

**Sorting enables safe pruning**

Before searching, the source sorts `candidates` in place. In `dfs(i, s)`, candidate `candidates[i]` is the smallest value still allowed. If `s < candidates[i]`, every permitted candidate is too large, so the branch cannot reach zero and returns immediately. Positivity is what makes this conclusive: adding a positive value can only reduce the remaining sum further below zero; there is no negative candidate that could compensate later.

The `for` loop itself still visits every `j` from `i` onward, even when some later candidate exceeds `s`. Such a candidate creates a recursive call with a negative remaining sum, and that child returns through the same `s < candidates[i]` check. A loop-level `break` could avoid those calls because the array is sorted, but their presence affects only efficiency, not correctness.

**Choose, explore, undo**

For a selected index `j`, the source appends `candidates[j]` to `t`, calls `dfs(j, s - candidates[j])`, and then removes the appended value with `t.pop()`. These three actions form one backtracking transaction.

Appending before recursion makes the child state reflect the choice. Subtracting from `s` preserves the sum invariant. Passing `j` allows the same value to be selected again. Finally, `pop` restores `t` to exactly its parent contents so the next loop iteration explores an independent alternative. Without the `pop`, choices from one branch would leak into later branches.

As a trace for `candidates = [2, 3, 6, 7]` and `target = 7`, the first branch repeatedly chooses `2`, reaching remaining sums 5, 3, and 1. The next `2` is too large for remainder 1, so that path backs up. From partial list `[2, 2]`, choosing `3` reaches zero and records `[2, 2, 3]`. Much later, the root loop chooses `7` directly and records `[7]`. The ordering restriction prevents alternate arrangements of `[2, 2, 3]`.

**Why every answer appears exactly once**

Soundness follows from the remaining-sum invariant. An entry is appended only when `s == 0`, so its values total exactly `target`. All values come from `candidates`, and passing `j` permits repetitions allowed by the contract.

For completeness, take any valid combination and sort its members by their positions in the sorted candidate array. The root loop can select its first member. Because recursion passes that selected index, the next member—equal or larger—remains available. Repeating this reasoning follows a search path matching the entire combination, and its positive values reduce `s` exactly to zero. The pruning test cannot eliminate that path because its next required value is no greater than the remaining sum.

For uniqueness, the non-decreasing-index sequence of a multiset is unique. Since the search permits no other index order, one combination cannot reach the result through two different permutations. The input candidates themselves are distinct, so equal values at different indices cannot create a second representation.

## Complexity detail

Let $n$ be the number of candidates, $T$ the target, and $m$ the smallest candidate. Because every choice contributes at least $m$, recursion depth is at most $\lfloor T/m \rfloor$. If one conservatively allows up to $n$ choices at every level, the search-tree bound is $O(n^{T/m})$, matching the manifest. Sorting first costs $O(n \log n)$ and is dominated by the exponential enumeration bound for nontrivial searches.

That bound is intentionally coarse. The start index shrinks the available choice set, positivity prunes overshoots, and the problem caps the number of returned combinations below 150. Conversely, output production has an unavoidable cost: if $R$ combinations are returned and their total number of elements is $P$, copying them into `ans` costs $\Theta(P)$. A precise output-sensitive description is the cost of visited search states plus $P$.

The active path contains at most $\lfloor T/m \rfloor$ values, and the call stack has the same maximum depth. Excluding returned answers, auxiliary space is therefore $O(T/m)$, as stated in the manifest. The actual result list occupies $O(P)$ space and cannot be avoided because it is the required return value. Sorting is in place and may also use implementation-dependent temporary stack or buffer space, normally at most $O(n)$ in Python; the dominant conceptual search storage remains the path and recursion stack.

## Alternatives and edge cases

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
