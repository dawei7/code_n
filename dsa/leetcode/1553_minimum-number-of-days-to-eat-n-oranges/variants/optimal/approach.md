## General

**Compress runs of one-orange days**

From a state with `n` oranges, eating one orange is always available, but exploring that action one day at a time would create nearly every smaller state.

The useful decisions are the two bulk operations. Before using the divide-by-two operation, the remaining count must be divisible by two. The cheapest way to reach such a count through single-orange days is to eat `n % 2` oranges. That takes zero or one day.

Then one additional day performs the bulk action and leaves `n // 2` oranges.

Similarly, reaching divisibility by three requires `n % 3` single-orange days, followed by one bulk day that leaves `n // 3` oranges.

The recurrence compares those two complete strategies rather than branching through every single decrement.

**Define the recursive state**

`dfs(n)` is the minimum number of days needed to finish exactly `n` remaining oranges.

For zero oranges, zero days remain. For one orange, exactly one ordinary eating day remains. The source combines these facts as `if n < 2: return n`.

For larger `n`, it returns:

`1 + min(n % 2 + dfs(n // 2), n % 3 + dfs(n // 3))`.

The outer one is the chosen bulk-operation day. Inside each candidate, the remainder is the number of preliminary one-orange days, and the recursive value solves the reduced count.

**Why only the next divisible count matters**

Suppose an optimal plan's first bulk operation is division by two. Before it, only one-orange actions can occur because by definition no bulk action was earlier.

To make `n` divisible by two through decrements, the number of eaten oranges must be congruent to `n % 2` modulo two. Eating more than the smallest remainder adds unnecessary days and reaches a smaller even value that could instead be reached after applying the recurrence from the nearest even value.

Thus the best plan whose first bulk type is division by two is represented by the first candidate. The same reasoning applies to division by three.

Every optimal plan either has one of these bulk operations as its first bulk action or eats all oranges singly. Repeated recurrence eventually includes the single-only finish through the base states, while bulk operations always dominate long single runs for larger counts.

**Tracing ten oranges**

For ten, the division-by-two candidate needs no preliminary single day, then one bulk day leaves five.

The division-by-three candidate needs one single day to reach nine, then one bulk day leaves three.

The recurrence explores both reduced states through caching. The best route chooses ten to nine, nine to three, three to one, and one to zero, for four days.

Each arrow before the final one corresponds either to the counted preliminary single action or the outer bulk-action day in the recurrence.

**Why memoization is essential**

Different paths can reach the same remaining count. For example, divisions by two and three in different orders may converge to similar floor quotients.

The `@cache` decorator stores each computed `dfs(n)` result. Later calls with the same `n` return immediately rather than expanding another recursion tree.

Only the remaining orange count determines future possibilities, so it is a complete memoization key.

**Why the recurrence is correct**

The base values are exact. For `n >= 2`, classify an optimal plan by its first bulk operation. If it first uses division by two, the minimum necessary setup is `n % 2` single days, followed by the bulk day and an optimal plan for `n // 2`. The other class yields the analogous divide-by-three cost.

Taking the smaller covers every optimal first bulk choice. By induction on decreasing `n`, recursive subresults are optimal, so `dfs(n)` is optimal.

**Rapid state reduction**

Every recursive edge reduces the argument to its floor half or floor third. The numeric count therefore falls exponentially along any one call chain, allowing an input as large as two billion.

The cache contains combinations formed by repeated divisions by powers of two and three rather than every integer below `n`.

## Complexity detail

Reachable memoized states have the form of `n` reduced by combinations of divisions by two and three, with floor effects. There are $O(\log N)$ possible powers of two and $O(\log N)$ possible powers of three, giving the standard upper bound $O((\log N)^2)$ states.

Each state performs constant arithmetic and two cached calls, so time is $O((\log N)^2)$, matching the manifest.

The cache stores one result per state, using $O((\log N)^2)$ space. Recursion depth is $O(\log N)$ and fits within that overall bound.

## Alternatives and edge cases

- **Breadth-first search over counts:** It can find a shortest path but may visit far more states than the compressed recurrence.
- **Bottom-up DP to n:** It costs $O(N)$ time and space, infeasible for two billion.
- **Always divide by two:** It can be suboptimal when a small adjustment enables a much stronger division by three.
- **Always divide by three:** It likewise ignores cases where halving is better.
- **Zero oranges:** The internal base returns zero, though the public input begins at one.
- **One orange:** One ordinary day is necessary and sufficient.
- **Divisible by both:** Both candidates use zero setup days, and recursion chooses the better future.
- **Remainder one for division by two:** One single-orange day enables halving.
- **Remainder two for division by three:** Two single-orange days enable the divide-by-three bulk action.
- **Cache lifetime:** The nested cached function is fresh for each outer method call.
- **Floor division:** It exactly represents the oranges remaining after the permitted bulk action.
- **One action per day:** The recurrence separately counts setup days and one bulk day; it never combines them.
- **Large n:** Exponential argument reduction avoids iterating through all smaller counts.
