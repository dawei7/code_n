## General
**End each day in one of three economic states**

Track the best profit for three mutually exclusive states:

- `hold`: one share is held after the day;
- `sold`: a share was sold today, so tomorrow is a cooldown day;
- `rest`: no share is held and buying is allowed after today.

Before any prices, resting profit is zero while holding and selling are impossible. For each price, compute all new states from the previous day's values rather than updating in place.

**The cooldown restriction is encoded in the buy transition**

A holding state either continues holding or buys today from yesterday's `rest` state:
`new_hold = max(hold, rest - price)`.
It must not buy from yesterday's `sold` state, which is exactly how the mandatory cooldown is enforced.

Selling today requires a share held yesterday:
`new_sold = hold + price`.
Resting today either continues resting or spends the cooldown day after a prior sale:
`new_rest = max(rest, sold)`.

For `[1,2,3,0,2]`, buy at one and sell the next day at two for profit one. Day two is the cooldown; buying at zero on day three and selling at two on day four adds two, for total profit three. The tempting sale at price three would make the zero-price day unavailable for buying.

**The three states retain every legal strategy**

After each day, classify every legal trading history by whether it ends holding, selling today, or resting. These classes are disjoint and exhaustive. The transitions enumerate every legal predecessor for each class: holding or a permitted buy, a sale from holding, and continued rest or cooldown after sale.

Taking the maximum over each complete predecessor set therefore preserves the best history in every class by induction. A final profit cannot use an unsold share, so `max(sold, rest)` is exactly the optimum.

## Complexity detail
Each of the `n` prices performs a constant number of arithmetic operations and comparisons, giving $O(n)$ time. Three previous-state values and three new values use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Try every buy/sell pair after every prefix:** is correct with dynamic programming but takes $O(n^2)$ time.
- **Sum every positive adjacent increase:** ignores cooldown and may select incompatible transactions.
- One day or monotonically decreasing prices yield zero. Repeated equal prices preserve the current best states without profit.
