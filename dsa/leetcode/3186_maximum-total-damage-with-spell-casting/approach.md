## General

**Turn individual spells into damage-value groups.** The restriction is based on a spell's damage value, not on its position in the input. If damage $v$ is selected, every spell of damage $v-2$, $v-1$, $v+1$, or $v+2$ becomes forbidden. Spells whose damage is also $v$ do not forbid one another. Because every damage value in this problem is positive, selecting one copy of $v$ while leaving another copy unused can never help: the extra copy adds $v$ damage and creates no new restriction. Therefore every optimal answer either selects all copies of a value or selects none of them.

The exact solution records the multiplicity of every value in `cnt = Counter(power)`. A group with value $v$ and frequency $\texttt{cnt}[v]$ is consequently worth

$$
v \cdot \texttt{cnt}[v].
$$

For example, four spells with damage $7$ form one decision worth $28$. Thinking in groups removes a misleading distinction between duplicate array elements.

**Put the groups in an order where conflicts become local.** The code sorts `power` in place. The resulting array still contains duplicates, but equal values are consecutive and all larger values lie to their right. For a current value $v$, every later value through $v+2$ conflicts with it, while the first value greater than $v+2$ and every value after that are compatible.

The list `nxt` stores that first compatible index. At sorted position `i`, the expression

`bisect_right(power, power[i] + 2, lo=i + 1)`

returns the first index whose value is strictly greater than `power[i] + 2`. “Strictly greater” is essential. Values $v+1$ and $v+2$ are forbidden, whereas $v+3$ is allowed. If no such value exists, binary search returns `n`, which naturally represents the empty suffix.

The source computes this binary search for every position, including duplicate positions that the dynamic program normally never visits. That is redundant but harmless. It also explains why the implementation sorts and searches the full length-$n$ array instead of constructing an explicit list of unique values.

**Define one suffix decision precisely.** The memoized function `dfs(i)` means: the maximum damage obtainable from the still-undecided groups beginning at sorted index `i`. Every reachable `i` is the first position of a damage group. The base case `i >= n` returns zero because no spell remains.

At a group beginning at `i`, let $v=\texttt{power}[i]$. There are exactly two meaningful choices:

1. Skip damage $v$. Since `cnt[v]` copies occur consecutively, the next group begins at `i + cnt[v]`. The resulting value is `dfs(i + cnt[power[i]])`.
2. Take damage $v$. Taking all its copies contributes `power[i] * cnt[power[i]]`. Values through $v+2$ must then be skipped, so the remaining compatible suffix starts at `nxt[i]`. The resulting value is `power[i] * cnt[power[i]] + dfs(nxt[i])`.

The function returns the larger of these values. Caching ensures that if several decisions lead to the same suffix index, that suffix is solved once.

**Why those two branches cover every valid answer.** Consider any valid selection using only values at or after the group at `i`. It either contains value $v$ or it does not. If it does not, it is entirely represented by the skip suffix. If it does, positivity lets us include every copy of $v$, and validity excludes all values at most $v+2$ to its right; what remains is exactly a valid choice from `nxt[i]` onward. There is no third category. Conversely, the skip branch adds no new restriction, and the take branch jumps over every conflicting value, so both branches construct valid selections.

Assume recursively that `dfs` returns the best result for its later suffixes. The skip branch then has the best possible value among selections omitting $v$, and the take branch has the best possible value among selections containing $v$. Their maximum is the optimum for suffix `i`. The base case is plainly optimal, so this reasoning applies backward to `dfs(0)`, which covers the entire sorted input.

**A small trace.** For `power = [1, 1, 3, 4]`, the groups are $1$ worth $2$, $3$ worth $3$, and $4$ worth $4$. At value $1$, taking it jumps past both $1$ and $3$ to value $4$, because $3=1+2$ conflicts but $4=1+3$ does not. That branch obtains $2+4=6$. Skipping $1$ leaves a choice between $3$ and $4$, whose best value is $4$. The maximum is therefore $6$. This trace also shows why merely taking the currently largest group is not a proof of optimality: each choice changes which future groups remain available.

## Complexity detail

Let $n$ be the number of spells and $u$ the number of distinct damage values, where $1 \le u \le n$.

Building `cnt` takes $O(n)$ expected time and up to $O(u)$ space. Sorting the length-$n$ input list takes $O(n\log n)$ time. The list comprehension performs `bisect_right` once for each of the $n$ sorted positions; each search costs $O(\log n)$, so constructing `nxt` also takes $O(n\log n)$ time. Although only group-start entries of `nxt` are needed by the recursion, the exact source allocates and computes all $n$ entries.

There are at most $u$ reachable memoized `dfs` states. Each state does constant work apart from its already-precomputed recursive results, so the dynamic-programming portion takes $O(u)$ time. The overall time is therefore $O(n\log n)$, matching the manifest. Hash-table operations are treated as expected $O(1)$ operations.

The sorted array is the caller-provided list itself, so sorting does not allocate a second explicit copy of all values, but Python's sort may use $O(n)$ temporary memory. The `nxt` list uses $O(n)$ space, the counter uses $O(u)$, and the cache plus recursion stack can use $O(u)$. Thus the auxiliary space is $O(n)$. The recursion stack is not merely an accounting detail in Python: with close to $10^5$ distinct groups, the call depth can exceed Python's normal recursion limit before the theoretical memory bound is reached.

## Alternatives and edge cases

- **Iterative dynamic programming on unique values:** Build sorted pairs `(value, frequency)` and compute the best prefix value iteratively, using a pointer or binary search for the last compatible group. This expresses the same recurrence without duplicate `nxt` entries and avoids recursion-depth failure. It is the safer production formulation, but it is not the exact source implemented here.
- **Monotonic-pointer transition:** The editorial keeps the best compatible prior state while scanning unique values. Because the pointer only moves forward, the DP after sorting is linear in the number of unique values. The overall bound remains $O(n\log n)$ because sorting dominates.
- **Quadratic comparison with every earlier group:** A direct DP can test all earlier values for compatibility. It is easy to derive but costs $O(u^2)$ after grouping and is unnecessary when sorted order permits a pointer or binary search.
- **Greedy choice of the largest immediate group:** Choosing the greatest group weight first is not reliable. A moderately valuable group can block two compatible groups whose combined damage is larger, so the skip/take future must be compared by dynamic programming.
- **Duplicate values:** All duplicates are deliberately taken or skipped together. The skip index `i + cnt[power[i]]` is correct only because sorting makes every copy consecutive and reachable states begin at group boundaries.
- **Gap of exactly two:** Values differing by one or two conflict. `bisect_right(..., v + 2)` correctly skips both boundaries; using a search for `v + 2` with the wrong inclusive/exclusive rule would allow an illegal pair.
- **Gap of exactly three:** Such values are compatible. The first value greater than $v+2$ may be $v+3$, so the take branch must be allowed to continue there.
- **One damage group:** The take branch receives the full positive group value and jumps to `n`, while the skip branch returns zero, so all copies are selected.
- **Large numeric values:** The total can exceed a 32-bit signed integer. Python integers grow automatically, so multiplication and addition remain exact for the stated constraints.
- **Input mutation:** `power.sort()` changes the order of the caller's list. LeetCode permits this because only the returned integer matters, but code that needs the original order must sort a copy.
- **Recursion-depth limitation:** The mathematical algorithm supports $u$ up to $10^5$, but the exact recursive Python source can raise `RecursionError` on a valid input with many distinct values. Memoization prevents repeated work; it does not reduce the longest chain of nested calls. An iterative DP is required to remove this implementation defect robustly.
