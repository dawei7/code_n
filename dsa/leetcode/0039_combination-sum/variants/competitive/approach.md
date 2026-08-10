## General

**Use one canonical order for every combination**

Candidates may be selected repeatedly, while different permutations of the same selected values must count as only one combination. The solution resolves both requirements with a lower-bound index named `start`. It first creates a sorted candidate list. A recursive frame may choose `candidates[start]` or any later value, but never an earlier one. The child receives the chosen index itself, so that value remains available for unlimited reuse.

This makes every partial combination non-decreasing. A multiset such as two `2`s and one `3` has exactly one non-decreasing representation, `[2, 2, 3]`. Paths corresponding to `[2, 3, 2]` or `[3, 2, 2]` cannot occur because recursion never decreases `start`. Uniqueness is therefore built into traversal rather than repaired afterward with a set.

**Understanding all recursive arguments**

`combinationSumRecu` receives the sorted candidates, shared result list, lower-bound index, mutable current path, and remaining target. At entry:

- `intermediate` contains the choices on the current root-to-frame path.
- Those choices sum to the original target minus the current `target` parameter.
- Their candidate indices are non-decreasing.
- Only indices at least `start` may be chosen next.

The public method establishes this state with `start = 0`, an empty path, and the full requested target.

When the remaining `target` equals zero, the current path is a completed combination. The code appends `list(intermediate)`, which creates a separate list containing the current values. Copying is necessary because `intermediate` is later shortened and reused. If the result stored the shared object directly, backtracking would change combinations that had supposedly already been recorded.

There is no explicit `return` immediately after appending. That is still safe: every candidate is at least 2, so the following `while` condition `candidates[start] <= target` cannot hold when `target` is zero. The function naturally reaches its end without adding anything more.

**The `while` loop is both enumeration and pruning**

The candidate list is sorted, and the loop continues only while the current candidate is no larger than the remaining target. If `candidates[start] > target`, every candidate after it is at least as large, so none can be used without overshooting. The entire suffix can be rejected at once.

If the candidate fits, the code appends it to `intermediate`, recursively searches with the same `start` and a reduced target, then pops it. Passing the same index is why the candidate can appear again. The subtraction strictly reduces the remaining target because all candidate values are positive, so recursion must eventually reach zero or a state where the smallest permitted value is too large.

After the recursive call returns, `pop` restores the exact parent path. The statement `start += 1` then advances the current frame to the next distinct candidate. It is helpful to distinguish these two movements: the child keeps `start` to represent “reuse this value,” whereas the parent increments it to represent “try a larger first choice at this position.”

Although mutating the local `start` inside a loop may look unusual, each recursive call has its own local parameter. Advancing it in the parent does not alter an already executing child's variable, and the child has returned before the increment happens.

**Tracing a small example**

For sorted candidates `[2, 3, 5]` and target 8, the root first selects `2`. Descendants may keep selecting `2`, producing `[2, 2, 2, 2]` when the remainder becomes zero. Backtracking then lets a frame advance from candidate `2` to `3`, which eventually records `[2, 3, 3]`. Once the root advances to `3`, it cannot return to `2`, so it explores `[3, 5]` but never generates permutations of the combinations already found.

When a remainder is 1, the loop condition fails because even the globally smallest candidate is at least 2. That branch returns immediately. This illustrates how sorting and positivity turn an overshoot check into early pruning.

**Why the result is correct and complete**

Every recorded path is sound. It contains only candidate values, allows reuse through the unchanged child index, and is appended only when the remaining target is zero. The invariant then proves its sum is exactly the original target.

For completeness, consider any valid combination and arrange its values in non-decreasing order. The root's loop eventually visits its first value. The recursive call retains that index, so the second value, being equal or greater, remains available. Repeating the argument constructs the whole ordered combination. At every step, the next value is no greater than the remaining sum because the rest of the valid combination consists of positive values, so the loop's `<= target` guard cannot prune this path.

No result is duplicated. Candidate values are distinct, and each combination has only one non-decreasing index sequence. Since the recursion never chooses a lower index after a higher one, no alternate permutation can reach the same multiset.

The use of `sorted(candidates)` also means the original input list is not rearranged. The new sorted list is passed through every recursive frame, while the caller's list retains its original order.

## Complexity detail

Let $n = \lvert\texttt{candidates}\rvert$, let $T$ be the original target, and let $m$ be the smallest candidate. Every recursive choice reduces the remaining target by at least $m$, so the maximum path length is $\lfloor T/m \rfloor$. With at most $n$ candidate branches per level, a conservative upper bound is $O(n^{T/m})$, matching the manifest. Sorting contributes $O(n \log n)$ time before the search.

The bound overstates typical work because each frame permits only a suffix of the candidate array and the sorted `<= target` condition prunes values that cannot fit. Still, enumerating all answers is inherently output-sensitive. If the returned combinations contain $P$ values in total, copying them requires $\Theta(P)$ time and storing them requires $\Theta(P)$ space. The promised limit of fewer than 150 unique answers bounds practical output count for the supplied cases but does not make backtracking conceptually constant-time.

The current path and call stack can each reach depth $\lfloor T/m \rfloor$, so auxiliary search space is $O(T/m)$. The sorted copy of the candidates adds $O(n)$ storage. The manifest focuses on depth; a complete Python accounting is $O(n + T/m)$ auxiliary space, plus $O(P)$ for the required returned results. No board of memoized subproblems is retained.

## Alternatives and edge cases

- **For-loop with a fixed lower bound:** A `for j in range(start, n)` loop can express the same suffix enumeration and break when `candidates[j] > target`. The selected `while` form instead advances the local `start` directly.
- **Include or exclude each candidate:** One recursive branch can take the current candidate and stay at its index, while another skips it and advances. This binary formulation is equally valid but may create a deeper decision tree.
- **Memoized suffix combinations:** Caching results for `(start, remaining)` can avoid repeated subproblems, but it must copy and prefix many stored combinations. For a bounded-output enumeration task, direct backtracking is simpler and avoids a potentially large cache.
- **Permutation search plus deduplication:** Allowing every candidate at every level and later deduplicating sorted paths wastes time on many orderings. The lower-bound index prevents those paths from existing.
- **Target smaller than the minimum:** The initial loop condition fails and the result remains empty.
- **Exact one-candidate match:** Choosing that candidate makes the recursive target zero, so a one-element path is copied to the result.
- **Repeated use:** The child receives the same `start`; changing it to `start + 1` would incorrectly turn the problem into one where each candidate may be used only once.
- **Positive values guarantee termination:** Every recursive choice strictly lowers the remaining target. A zero candidate could recurse forever, and negative candidates could invalidate the pruning rule, but the constraints exclude both.
- **Distinct candidates guarantee canonical uniqueness:** If the input contained duplicate values at different indices, identical combinations could be generated from those distinct positions. The contract explicitly rules that out.
- **Preserving the caller's input order:** `sorted(candidates)` allocates a sorted copy, unlike an in-place `.sort()`. This costs $O(n)$ memory but avoids mutating the input list.
- **Any result order is accepted:** Sorting determines a deterministic traversal and non-decreasing contents, but neither property is required for presentation; they are used to make generation unique and pruning safe.
