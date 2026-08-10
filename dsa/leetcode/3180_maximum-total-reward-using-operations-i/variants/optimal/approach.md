## General

**Current total is enough state**

After choosing reward value $v$, new total becomes $x+v>v$. That same value can never be chosen again because future totals only increase and the condition requires reward strictly greater than current total.

More generally, every previously chosen reward is at most current total, so it is automatically excluded by the eligibility test. Any unchosen reward already at most current total is also permanently unusable.

Therefore, the set of marked indices need not be stored. Given current total $x$, all future legal choices are exactly reward values greater than $x$.

**Sort and locate eligible rewards**

The source sorts `rewardValues` in place. `bisect_right(rewardValues, x)` returns the first index with value strictly greater than $x$.

`dfs(x)` loops over that suffix. For each legal value $v$, it gains $v$ now and then optimally continues from total $x+v$:

`v + dfs(x + v)`.

Maximum over choices is the greatest additional reward achievable. Starting answer zero represents stopping, which is always allowed.

The final result is `dfs(0)`.

**Duplicates need no marked mask**

If value 1 appears twice, after choosing one copy total is at least 1 and the other copy is not strictly greater, so it cannot be chosen. Iterating duplicate values from a state repeats an equivalent branch but does not produce an illegal double choice.

Memoization collapses identical resulting totals.


At total $x$, every valid continuation either stops or first chooses one value $v>x$. The recurrence considers every such value. After that choice, marked and newly ineligible rewards are completely characterized by new total $x+v$, as argued above, so `dfs(x+v)` gives exact remaining gain.

By induction over increasing totals—recursive calls always have larger $x$—the recurrence returns the exact optimal additional reward. Adding it to initial zero gives maximum total.

**Sorting does not imply a greedy order**

Sorting supports binary search, but the chosen sequence need not simply take the next smallest reward. At each state, DFS tries every value above current total. Choosing a large reward may permanently block several smaller ones, while collecting smaller legal rewards first may enable a larger final sum. The maximum comparison explores both tradeoffs.

**Why position and marked set are absent from the cache key**

The suffix start `bisect_right(x)` is determined solely by total $x$. Two histories reaching the same total have the same useful future choices: every value at most $x$ is ineligible forever, and a previously chosen value is necessarily at most $x$. Hence no eligible reward has secretly been marked in one history but not the other.

Every recursive edge increases total by a positive value greater than current total, so states form an acyclic increasing graph. Eventually no value is large enough and the empty suffix returns zero.

Equal rewards create repeated branches to the same cached total. They are harmless but deduplicating values would reduce repeated loop work.

**Bound on reachable totals**

Let $V$ be maximum reward. Before any final choice $v$, eligibility requires $x<v$. After choosing it,

$$
x+v<2v\le2V.
$$

Thus all reachable totals are below $2V$, limiting the number of cached integer states to $O(V)$.

Each choice more than doubles a positive current total because $v>x$, so recursion depth after the first choice is $O(\log V)$.

**Relation to the manifest**

The manifest describes a sorted distinct-value bitset that updates all reachable totals at once. The exact source is top-down memoized search with binary search and suffix iteration. It does not deduplicate rewards first and does not use bit operations as a reachability set.

**Input mutation and slicing**

Sorting changes the caller's reward list order. Also, `rewardValues[i:]` creates a new suffix list in every computed state. Iterating by index would avoid these temporary copies.

## Complexity detail

There are $O(V)$ reachable total states. A state may scan up to $n$ rewards and creates a suffix slice of comparable length. A conservative time bound is $O(nV+n\log n)$, including sorting.

Cache storage is $O(V)$. Active recursive frames can retain suffix slices; with $O(\log V)$ depth, a conservative temporary bound is $O(n\log V)$, though slices shrink and practical use is lower. Auxiliary space is $O(V+n\log V)$ in this exact Python formulation.

These bounds differ from the manifest's word-parallel bitset cost $O(n\log n+nV/w)$ and bitset space.

With $n,V\le2000$, memoized search may be feasible but is much less predictably efficient than the bitset method.

## Alternatives and edge cases

- **Integer bitset DP:** Track reachable totals as bits and update only totals below each reward, matching the manifest and usually much faster.
- **Boolean array DP:** Iterate reachable totals below $v$ in descending order; costs $O(nV)$ but avoids recursion.
- **Deduplicate rewards:** Equal values cannot both be chosen, so removing duplicates reduces repeated branches safely.
- **Greedy smallest reward:** It can leave room for more choices but is not always globally optimal without DP.
- **One reward:** It is chosen from total zero and returned.
- **Duplicate values:** At most one copy can ever be selected.
- **Strict inequality:** Reward equal to current total is ineligible; `bisect_right` enforces this.
- **Stop option:** Zero initialization allows no further choice when every value is too small.
- **Sorted input side effect:** Original ordering is destroyed even though ordering is irrelevant to the mathematical problem.
- **Total below 2V:** This bounds cache keys and supports pseudo-polynomial analysis.
- **Empty eligible suffix:** Loop does nothing and `dfs` returns zero.
- **Manifest mismatch:** The source is recursive search, not a bounded integer bitset.
