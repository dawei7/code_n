## General

On each day, the valid choices depend on whether one share is currently held. The solution models this with a two-state, top-down dynamic program:

- `j = 0`: no stock is held;
- `j = 1`: one stock is held.

`dfs(i, j)` returns the maximum additional profit obtainable from day `i` onward, given that holding state at the start of the day.

Caching ensures each day-state pair is solved once.

**Why the holding state is necessary**

Knowing only the day is insufficient. On the same day:

- a person holding stock may sell or wait;
- a person holding no stock may buy or wait.

The legal action sets and cash effects differ. The Boolean state carries exactly the information required by the “sell before buying again” rule.

**The horizon base case**

When `i >= len(prices)`, no trading day remains, so the function returns zero additional profit.

If `j = 1` at this point, the earlier purchase cost has already been subtracted in the transition that bought the stock. Returning zero adds no sale proceeds, so an unfinished purchase remains unprofitable. The maximization can always avoid entering that bad path.

**Doing nothing**

Every state first considers:

`ans = dfs(i + 1, j)`.

This skips the current day and preserves whether a share is held. Including a wait choice is vital because an optimal strategy need not trade whenever an action is legal.

**Selling while holding**

If `j` is true, selling on day `i` earns `prices[i]`, pays the transaction fee, and changes the next state to not holding:

`prices[i] + dfs(i + 1, 0) - fee`.

The method compares this with waiting and keeps the larger value.

Charging the fee at sale is a bookkeeping convention. Charging it at purchase would produce the same profit as long as it is charged exactly once per completed transaction.

**Buying while not holding**

If `j` is false, buying costs `prices[i]` and changes the next state to holding:

`-prices[i] + dfs(i + 1, 1)`.

The negative sign represents cash spent. This choice competes with waiting.

There is no transition that buys while already holding or sells while empty, so simultaneous transactions are impossible.

**Why unlimited transactions need no transaction counter**

After a sale, the state returns to `j = 0`. A later day may buy again. The day index always moves forward, so transactions cannot overlap, but any number can occur within the array length.

The two-state recurrence naturally repeats the buy-sell cycle without tracking how many cycles have completed.

**Memoization**

`@cache` stores results by arguments `(i, j)`.

Many action sequences reach the same future state. For example, different earlier trades may both arrive at day ten holding no stock. Future optimal profit depends only on day and holding status, not on the path's historical details because all earlier cash effects have already been included.

Caching merges these repeated subproblems.

**A trace of the intended strategy**

For prices `[1,3,2,8,4,9]` and fee `2`:

- Buying at one contributes `-1`.
- Waiting through intermediate fluctuations and selling at eight contributes `8-2`.
- The first transaction nets `5`.
- Buying at four and selling at nine after the fee nets `3`.
- Total profit is `8`.

The recursion also considers selling earlier, buying at other days, and doing nothing. Cached maximization selects this best combination.

**Why local greedy choices are unsafe without reasoning**

A price rise tomorrow does not automatically mean selling today is optimal because paying a fee on each transaction can make two small trades worse than one longer trade. The DP compares complete future profit rather than deciding from one-day changes alone.


At state `(i,0)`, every legal strategy either does nothing on day `i` or buys. The recurrence evaluates the optimal continuation for both.

At `(i,1)`, every legal strategy either does nothing or sells, and both are evaluated.

The base case is correct when no days remain. Assuming future states are optimal, taking the maximum over the exhaustive legal first actions makes the current state optimal. Induction backward over `i` proves `dfs(0,0)` is the maximum profit starting with no stock.

## Complexity detail

There are at most `2(n+1)` distinct states: two holding values for each day. Each cached state performs constant work once, so time is

$$
O(n).
$$

The cache stores `O(n)` results. Recursive calls can also reach depth `O(n)` by advancing one day at a time. The exact implementation therefore uses

$$
O(n)
$$

auxiliary space.

The constant-space bound belongs to an iterative two-variable DP, not this cached recursive source.

## Alternatives and edge cases

- **Iterative two-state DP:** Maintain best cash while holding and not holding. It preserves `O(n)` time and reduces auxiliary space to `O(1)`.

- **Greedy effective buy price:** Fold the fee into an adjusted purchase threshold. It can be linear and constant-space but is less direct to prove.

- **One day:** Buying cannot be followed by a sale, so waiting yields zero.

- **Fee zero:** The recurrence captures every profitable rise without a fee penalty.

- **Very large fee:** All completed trades may be unprofitable; the skip choices return zero.

- **Repeated equal prices:** Buying and selling at equality loses the fee, so waiting dominates.

- **Fee charged once:** It appears only in the sell transition.

- **No simultaneous holdings:** State `j` is Boolean and buy is offered only at zero.

- **Ending while holding:** No terminal sale is invented; the purchase cost remains and an optimal path avoids it.

- **Recursion depth:** With up to fifty thousand days, ordinary Python recursion limits can be an operational problem. Iterative DP is safer despite equivalent recurrence.

- **Input not mutated:** Prices are only read.
