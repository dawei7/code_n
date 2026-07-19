## General
The limit is on completed buy-then-sell pairs, and only one share may be held. A day-by-day dynamic program therefore needs to distinguish both how many transactions are being used and whether a share is currently held.

For transaction stage `t` from `1` through `k`, maintain:

- `buy[t]`: the best balance after buying the share for transaction `t` and still holding it.
- `sell[t]`: the best realized profit after completing at most `t` sales and holding no share.

Initially, every buy state is impossible ($-\infty$) and every sell state is zero: doing nothing is always allowed. At price $p$, the transitions are

`buy[t] = max(buy[t], sell[t - 1] - p)`

`sell[t] = max(sell[t], buy[t] + p)`.

The first option in each maximum skips today's action. The second buys using profit from at most $t - 1$ completed transactions or sells the share associated with stage `t`. Same-day buy and sell cannot create positive profit, so the in-place update order used by the reference implementation does not introduce an invalid advantage.

For $k = 2$ and prices `[3,2,6,5,0,3]`, the first transaction can buy at `2` and sell at `6` for profit `4`. The second buy state can then use that realized profit to buy at `0`, and its sale at `3` raises the total to `7`. A greedy choice based only on the single largest rise would miss the need to coordinate two non-overlapping intervals.

**Why a large k becomes unlimited**

Each completed transaction consumes at least two days, so no strategy can complete more than $\lfloor n/2 \rfloor$ transactions. When $k \ge \lfloor n/2 \rfloor$, the limit cannot bind. In that regime, collect every positive adjacent increase:

`sum(max(0, prices[i] - prices[i - 1]))`.

Every increasing run can be represented either as one buy at its start and sale at its end or as several adjacent profitable transactions with the same total. This shortcut avoids an unnecessary $O(nk)$ loop when `k` is very large.

After each processed price, `buy[t]` is optimal among all valid strategies that have initiated transaction `t` and currently hold one share, while `sell[t]` is optimal among strategies with no held share and at most `t` completed sales. The only way to enter a holding state is to retain an earlier holding or buy using `sell[t - 1]`; the only way to enter a non-holding state is to retain its earlier profit or sell from `buy[t]`. Thus the transitions consider every valid final action and no invalid holding pattern. Induction over days proves all states optimal, and `sell[k]` is the best allowed final profit because ending while holding cannot improve realized profit. In the unlimited regime, summing all positive daily changes captures exactly all upward movement and is optimal.

## Complexity detail
When the transaction limit binds, each of $n$ prices updates $k$ buy and sell pairs, taking $O(nk)$ time. The two arrays use $O(k)$ space. When $k \ge \lfloor n/2 \rfloor$, the shortcut runs in $O(n)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- A full table indexed by day, transaction count, and holding state makes dependencies explicit but uses $O(nk)$ space instead of rolling arrays.
- Enumerating all choices of buy and sell days is exponential.
- Summing positive differences is wrong when `k` is restrictive because it may use more transactions than permitted.
- $k = 0$, fewer than two prices, a constant sequence, or a strictly falling sequence all return zero.
- The answer uses at most `k` transactions; it never needs to force an unprofitable trade merely to use the full allowance.
