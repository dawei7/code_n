## General

**Translate simultaneous painting into a capacity balance**

Whenever wall `i` is assigned to the paid painter, money `cost[i]` is spent. The paid painter covers that wall and remains busy for `time[i]` units, during which the free painter can cover up to `time[i]` other walls.

Thus choosing a paid wall creates free-painting capacity. Assigning a wall to the free painter consumes one unit of that capacity.

The exact recursive DP tracks the balance between capacity earned from paid choices and walls assigned free.

**State meaning**

`dfs(i, j)` is the minimum additional money after decisions have been made for walls before index `i`, where:

$$
j=(\text{free capacity earned})-(\text{walls assigned free}).
$$

Positive `j` means unused free-painter time remains. Negative `j` means the choices so far assigned more free walls than paid time currently covers; later paid choices may still repair that deficit.

Starting state `dfs(0, 0)` has no decisions and no capacity.

**Option one: pay for the current wall**

If wall `i` uses the paid painter:

- add `cost[i]` to the money;
- earn `time[i]` units of capacity;
- advance to `i+1`.

This gives:

`dfs(i + 1, j + time[i]) + cost[i]`.

The paid wall itself does not consume free capacity. Its own painting is already covered by the paid choice.

**Option two: assign the current wall free**

If wall `i` uses the free painter, no money is added, but one unit of available-or-future capacity is consumed:

`dfs(i + 1, j - 1)`.

Allowing `j` to become negative is important. Decisions are an accounting device, not a chronological schedule. If the final chosen paid walls provide enough total occupied time, their free capacity can be arranged to cover all free-assigned walls.

**Early success condition**

There are `n - i` undecided walls. If `j >= n - i`, existing unused capacity can paint every remaining wall for free. The condition is written:

`if n - i <= j: return 0`.

No later paid choice can improve on zero additional money, so the recursion stops immediately.

This also caps useful positive balance. Nonterminal states always have `j < n-i <= n`, which helps bound the memo table despite `time[i]` reaching 500.

**Failure condition**

If `i >= n` while the success condition did not trigger, some free assignments remain uncovered. There are no walls left to choose for paid work, so the decision sequence is infeasible and returns infinity.

The success condition is checked first. At `i=n`, it accepts exactly states with `j>=0` and rejects negative balances.

**Why minimizing the two branches is complete**

Every wall must be painted by exactly one of the two painters. At index `i`, the two recursive branches represent those exhaustive choices. The balance updates preserve total feasibility, and money is added exactly for paid walls.

Memoization with `@cache` ensures the same pair `(i,j)` is solved once even when many different earlier assignment sequences produce the same balance.

**Trace the first example conceptually**

Paying for walls zero and one costs one plus two and earns one plus two equals three free-time units. Two remaining walls can be assigned free, consuming two units. The final balance is nonnegative, so total cost three is feasible.

The DP also explores every other paid/free subset and takes the least feasible cost, proving that no cheaper assignment was missed.

**Equivalent coverage interpretation**

A paid choice for wall `i` effectively accounts for `1 + time[i]` painted walls: the paid wall plus that many free walls. The task is a minimum-cost 0/1 knapsack reaching coverage $n$.

The exact source expresses this through a signed balance rather than a one-dimensional coverage array. Both formulations encode the same feasibility inequality:

$$
\#\text{free walls}\le\sum_{\text{paid }i}\texttt{time}[i].
$$

**Exact source versus manifest**

The manifest's $O(n)$ space corresponds to a space-optimized iterative knapsack. This source is top-down and caches states for many `i` and `j` pairs. Its actual memo storage is $O(n^2)$.


At each state, the recursion considers paying for wall `i`, correctly adding its price and capacity, or painting it free, correctly consuming capacity. The terminal conditions return zero exactly when accumulated capacity can cover every remaining or already free-assigned wall and infinity otherwise. By induction backward over `i`, `dfs(i,j)` is the minimum feasible remaining cost. Therefore `dfs(0,0)` is the global minimum.

## Complexity detail

For a fixed `i`, reachable nonterminal `j` values are bounded below by $-i$ and above by $n-i-1$, giving $O(n)$ relevant balances. Across $n$ indices, the cache contains $O(n^2)$ states.

Each state performs two constant-time transitions, so time is $O(n^2)$. Memoized entries require $O(n^2)$ space, and recursion depth is $O(n)$.

The exact space bound is therefore $O(n^2)$, not the manifest's $O(n)$ optimized-DP bound.

## Alternatives and edge cases

- **One-dimensional knapsack:** Track minimum cost for capped painted-wall coverage in $O(n^2)$ time and $O(n)$ space.
- **Two-dimensional remaining-wall DP:** Easier to interpret but also uses $O(n^2)$ storage.
- **Greedy by low cost or high time:** Fails because the best choice depends on the combined price-capacity tradeoff.
- **One wall:** Paying for it is necessary because the free painter cannot work without paid activity.
- **Large time value:** One paid wall may create enough capacity for every remaining wall, triggering early success.
- **Negative balance:** Allowed temporarily; later paid choices can restore feasibility.
- **Exactly zero final balance:** Feasible because all free walls are covered.
- **No walls left with negative balance:** Returns infinity.
- **Memoization:** Essential to avoid exploring all $2^n$ paid/free subsets independently.
- **Manifest mismatch:** The recursive cache grows quadratically even though an iterative variant can use linear space.
