## General

On each day, the legal actions depend on whether one share is currently held. That makes “day index alone” an incomplete state. The source uses a cached recursive state `dfs(i, j)`, where:

- `i` is the next day on which a decision may be made;
- `j = 0` means no share is held;
- `j = 1` means one share is held.

The return value is the maximum additional profit obtainable from day `i` onward under that holding condition. Purchase costs are subtracted when a buy occurs, and sale proceeds are added when a sale occurs. Therefore, the recursion can accumulate profits from any number of nonoverlapping transactions without separately counting transactions.

The local manifest describes three iterative scalars for hold, just-sold, and rest states. That is a valid constant-space formulation, but the exact `solution.py` implements the two-state memoized recursion explained here.

**The choice to do nothing**

From either holding state, the trader may take no action today. The next day has the same ownership condition, so the source begins with

`ans = dfs(i + 1, j)`.

When `j = 0`, this means remain out of the market. When `j = 1`, it means continue holding the existing share. Treating both as the same transition keeps the recurrence compact.

This option is always considered, so the trader is never forced to buy at a bad price or sell on an unfavorable day.

**The sell choice while holding**

If `j` is 1, buying another share is forbidden because multiple simultaneous transactions are not allowed. The only active transaction available is selling the held share at today's price.

Selling earns `prices[i]`. After the sale, no share is held. The next calendar day is the mandatory cooldown day, so no decision may occur at `i + 1`. The next legal decision state is day `i + 2` with holding flag 0:

`prices[i] + dfs(i + 2, 0)`.

The source compares this value with continuing to hold and keeps the larger one.

The jump by two is the complete cooldown implementation. There is no explicit cooldown flag or third recursive state because the forbidden day is skipped in the transition itself.

**The buy choice while not holding**

If `j` is 0, selling is impossible because there is no share. The active transaction choice is to buy one share today.

Buying pays `prices[i]`, so it contributes `-prices[i]` to profit. The next day begins while holding one share:

`-prices[i] + dfs(i + 1, 1)`.

There is no cooldown after buying. The next day may be used to sell or to keep holding.

The recurrence therefore is

$$
F(i,0)=\max\left(F(i+1,0),-p_i+F(i+1,1)\right)
$$

and

$$
F(i,1)=\max\left(F(i+1,1),p_i+F(i+2,0)\right),
$$

where $p_i=\texttt{prices}[i]$.

**The terminal condition**

When `i >= len(prices)`, no day remains on which money can be earned or spent, so the helper returns 0.

For a no-stock state, this clearly means no additional profit. For a holding state, it means an unsold share produces no future sale revenue. Its purchase cost was already subtracted on the earlier buy transition, so ending while holding does not erase that cost.

Because all prices are nonnegative and the trader always has a skip option, buying a share that is never sold cannot improve the root answer. On the last day, for example, the no-stock state compares skipping for zero with buying for `-prices[last]`; skipping is at least as good. Thus, the shared zero base case is safe even though an unfinished holding path may exist in the choice graph.

**Why caching is necessary**

Different action histories can reach the same future state. For example, several earlier rest choices may lead to the same `(i, 0)`, and different prior transaction timings may reach later days with the same holding flag.

Without memoization, the recursion would recompute the same suffix decision tree many times and grow exponentially. `@cache` stores the result for each `(i, j)` after its first evaluation. There are only two holding values for each relevant day, so only $O(n)$ distinct states.

The result depends only on the day and whether a share is held. Past purchase price does not need to be stored because the purchase cost was already included in accumulated profit at the moment of buying. The future recurrence needs only future cash flows.

**Tracing the example**

For `prices = [1, 2, 3, 0, 2]`, one optimal path is:

1. Buy on day 0, contributing $-1$.
2. Sell on day 1, contributing $+2$ and bringing profit to 1.
3. Day 2 is skipped automatically by the sale transition's jump from day 1 to day 3.
4. Buy on day 3 at price 0.
5. Sell on day 4 at price 2.

Total profit is

$$
-1+2-0+2=3.
$$

Selling the first share on day 2 would earn more in that individual transaction, but it would force cooldown on day 3 and lose the opportunity to buy at price 0. The dynamic program compares entire future outcomes, so it correctly prefers the globally better earlier sale.

**Why all legal strategies are represented**

At a no-stock state, every legal strategy either rests today or buys today; the recurrence compares exactly those two possibilities. At a holding state, every legal strategy either keeps holding or sells today; again, the recurrence compares exactly those choices. Illegal simultaneous buying and selling never appear.

After a sale, advancing by two enforces the one-day prohibition on buying. After a buy or a rest, advancing by one reflects the next normal day. Every transition adds exactly the cash flow of its action.

Therefore, each path through the recurrence corresponds to a legal trading strategy, and every legal strategy corresponds to one path. Taking the maximum at every state yields the greatest profit. The initial call `dfs(0, 0)` correctly starts before day 0 with no stock.

## Complexity detail

Let $n$ be the number of prices. The cached state is a pair `(i, j)`, with two possible holding flags and $O(n)$ relevant day values. There are $O(n)$ distinct states.

Each previously unseen state performs constant work and makes at most two recursive calls. Cached calls return in constant time. Total time complexity is $O(n)$.

The cache stores $O(n)$ results. A chain of rest or hold transitions can recurse through $O(n)$ days before returning, so the call stack is also $O(n)$. The exact source therefore uses $O(n)$ auxiliary space.

The manifest's $O(1)$ space bound belongs to the iterative three-scalar compression in the editorial, not to this cached recursion. Also, with up to 5000 days, a default Python recursion limit may be lower than the maximum call depth; an iterative version avoids that runtime concern.

## Alternatives and edge cases

- **Three-state scalar dynamic programming:** Maintain best profits for holding, just sold, and resting after each day, updating them from the previous day. It runs in $O(n)$ time and $O(1)$ space and matches the manifest summary.
- **Bottom-up two-state arrays:** Store `F(i, 0)` and `F(i, 1)` from right to left, padding indices `n` and `n + 1` with zero for the sale jump. It avoids recursion but uses $O(n)$ space.
- **Enumerate every buy and sell pair:** A nested transaction search repeats suffix decisions and can become quadratic or worse. The state recurrence reuses suffix optima.
- **Greedily take every positive adjacent increase:** That works without cooldown, but a sale may block a crucial low-price buy on the following day. Local positive differences do not capture this dependency.
- **Advance only one day after selling:** This would allow buying on the very next day, violating cooldown. The sell transition must use `i + 2`.
- **Buy while already holding:** This would create overlapping transactions, which the `j` branches deliberately forbid.
- **Sell while not holding:** There is no stock to sell, so that transition exists only when `j = 1`.
- **One price:** Buying cannot be followed by a sale, and skipping yields zero, so the answer is zero.
- **All prices decreasing:** Every completed transaction would be nonprofitable. Repeated rest choices produce zero.
- **All prices equal:** Selling after buying yields zero, so the maximum remains zero.
- **Price zero:** Buying at zero is legal. It may be optimal if a later positive sale exists, as in the example.
- **Repeated transactions:** After the cooldown jump, the state returns to no stock and can buy again, so the recurrence permits unlimited legal transactions.
- **Ending with stock:** Its purchase cost remains in the accumulated path and no terminal revenue is added. Such a path never improves over avoiding that final unprofitable purchase.
- **Empty list:** The stated input is nonempty, but the base case would return zero if called with no prices.
- **Large input and recursion:** The mathematical complexity remains linear, but an explicit bottom-up loop is safer than deep Python recursion when $n$ approaches 5000.
