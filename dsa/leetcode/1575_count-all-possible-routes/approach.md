## General

**A route state needs city and remaining fuel**

Future choices depend only on the current city `i` and remaining fuel `k`. The earlier sequence of visits does not otherwise constrain movement because cities may be revisited.

`dfs(i, k)` returns the number of valid routes that start in this state and eventually finish at `finish` without negative fuel.

The `@cache` decorator memoizes results by both arguments, merging many route prefixes that reach the same state.

**Count stopping at finish as one route**

`ans = int(i == finish)` contributes one when the current city is already the destination.

That one represents choosing to stop now. The function does not return immediately, because the rules allow leaving `finish` and later returning. Every such longer route is counted through recursive moves in addition to the stop-now route.

This detail is essential in examples where routes visit the destination multiple times before finally ending there.

**Try every different next city**

For each city `j != i`, movement cost is:

`abs(locations[i] - locations[j])`.

The source subtracts that cost and calls `dfs(j, remaining)`. The returned route count is added to `ans` modulo $10^9+7$.

It does not explicitly test whether the move is affordable before calling. Invalid or hopeless child states are rejected by the helper's first condition.

Distinct location coordinates ensure every move to a different city costs at least one. Remaining fuel strictly decreases along recursion, so revisiting cities cannot create an infinite recursive cycle.

**Prune states that cannot reach finish**

Before counting or branching, the helper checks:

`k < abs(locations[i] - locations[finish])`.

On a number line, the direct distance between current city and finish is a lower bound on the total cost of every multi-city route by the triangle inequality.

If remaining fuel is below that direct distance, no possible detour can succeed, so the state returns zero.

This also rejects negative fuel because a negative `k` is less than every nonnegative direct distance, including zero at the finish.

**Why direct-distance pruning is safe**

For any sequence from current coordinate $x$ through intermediate coordinates to finish coordinate $y$, the sum of absolute step distances is at least $\lvert x-y\rvert$.

Intermediate cities may equalize or increase the traveled distance but can never make it less than the direct separation.

Therefore the source discards only states with no valid completion.

**A recurrence view**

For a nonpruned state:

$$
\operatorname{dfs}(i,k)
=
[i=\textit{finish}]
+
\sum_{j\ne i}
\operatorname{dfs}\left(j,k-\lvert location_i-location_j\rvert\right).
$$

Every route either stops immediately when allowed or chooses one unique next city and then follows a recursively counted route.

These categories are disjoint by their first action and collectively exhaustive.

**Why memoization matters**

A city can be revisited with the same remaining fuel through different route prefixes. Without caching, those repeated states expand into an exponential recursion tree.

With caching, each distinct key is evaluated once; later visits reuse its completed count.

Modulo reduction occurs after every addition, keeping cached values within the required range.

**Tracing start equal to finish**

If `start == finish`, the empty-move route is immediately counted as one.

The method still considers trips to other cities and back when fuel permits. Each return to finish creates another state whose stop-now option counts a distinct route.

This exactly matches the statement's permission to revisit both start and finish.


The direct-distance test removes only impossible states. For every remaining state, one route exists for stopping now exactly when current city is finish.

Every nonempty route has a unique first destination `j`, pays the exact movement cost, and leaves a suffix route counted by the corresponding recursive state.

Induction on remaining fuel is valid because every move costs positively and decreases `k`. The recurrence therefore counts every valid finite route exactly once.

**Exact handling of unaffordable calls**

Because the loop calls every other city before checking affordability, it can invoke `dfs` with negative or otherwise insufficient fuel.

Those calls return zero immediately through the lower-bound condition. They are logically harmless, though the cache decorator may retain their keys.

## Complexity detail

There are at most $O(NF)$ expandable states with city in `N` and nonnegative fuel through `F`. Each loops over all $N$ cities, giving $O(N^2F)$ time, matching the manifest.

The usual optimized implementation checks move affordability before recursion and stores $O(NF)$ states. The exact source caches the early-return states too. Since every expandable state can generate up to $N$ distinct insufficient child keys, a conservative exact cache upper bound is $O(N^2F)$ rather than the manifest's $O(NF)$.

In typical data many invalid calls collide or are eliminated by the direct-distance bound, but the source does not guarantee only the ideal state grid is cached.

Recursion depth is at most $O(F)$ because each legal move costs at least one. That is below the conservative cache bound.

## Alternatives and edge cases

- **Bottom-up DP:** Fill counts by increasing fuel and avoid recursion, using the standard $O(NF)$ table.
- **Affordability guard:** Skip a city when movement cost exceeds `k`, avoiding negative cached states and realizing the manifest space bound.
- **No memoization:** Repeated visits create an exponential route tree.
- **Start equals finish:** The zero-move route counts once, and longer return routes may also count.
- **Insufficient direct fuel:** The lower-bound check returns zero immediately.
- **Exact direct fuel:** The direct move can reach finish and is counted.
- **Revisiting cities:** It is legal; decreasing fuel ensures finitely many visits.
- **Distinct locations:** Every intercity movement has positive cost.
- **Finish is not terminal:** The recursion may leave it and return.
- **Negative child fuel:** It is rejected by the direct-distance condition.
- **Modulo:** Every accumulated state count is reduced after each transition.
- **Triangle inequality:** It justifies pruning even when routes can use many intermediate cities.
- **Cache scope:** The nested cached function and its stored states belong to one outer method call.
