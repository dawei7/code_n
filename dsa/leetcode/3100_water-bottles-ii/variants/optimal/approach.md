## General

Drinking a full bottle never harms a future choice: it increases the total drunk count and replaces the full bottle with exactly one empty bottle, which is the only resource exchanges consume. Therefore, drink all `numBottles` initial bottles immediately. The total drunk count and the number of empty bottles both start at `numBottles`.

Whenever `empty >= numExchange`, spend exactly `numExchange` empties on the one allowed exchange. Drinking the resulting full bottle adds one to both the answer and the empty-bottle count, while the exchange price rises by one. This update has a net empty-bottle cost of `numExchange - 1` at the old price.

The simulation stops precisely when the current empty count is below the current price. At that point, drinking cannot create any more empties because no full bottles remain, and no exchange is affordable, so no further operation can increase the answer. Conversely, every simulated exchange is legal and its produced bottle is drunk, proving that the accumulated count is attainable and maximal.

If the initial price is $e$ and the algorithm performs $t$ exchanges, their successive net empty-bottle costs are

$$
e-1, e, e+1, \ldots, e+t-2.
$$

Thus, $t$ is the largest non-negative integer satisfying

$$
t(e-1) + \frac{t(t-1)}{2} \le n-1.
$$

This also explains why three empties at price one cannot all be exchanged at price one: after the first exchange, the next price is already two.

## Complexity detail

The cumulative net cost contains the quadratic term $t(t-1)/2$, so the number of exchanges is $O(\sqrt{n})$; the worst case occurs when the initial price is one. Each exchange takes constant time, giving $O(\sqrt{n})$ total time and $O(1)$ auxiliary space. For the legal bound $n \le 100$, at most 14 iterations are possible. The package therefore uses a bounded-domain certificate with exhaustive validation over all 10,000 legal input pairs instead of presenting a runtime trend over this tightly capped loop count.

## Alternatives and edge cases

- **Solve the quadratic inequality:** Derive $t$ directly from the positive root of the cumulative-cost inequality and correct for integer rounding. This can be $O(1)$, but the short simulation is less error-prone under the small legal bound.
- **Search operation sequences:** Explore choices of how many bottles to drink before each exchange. This adds unnecessary state because drinking earlier never decreases the empty-bottle supply available later.
- **Initial price one:** The first exchange consumes one empty and the produced bottle restores one empty, but the price still rises, so the process remains finite.
- **Exact affordability:** An exchange is legal when `empty == numExchange`; the comparison must include equality.
- **No affordable exchange:** If the initial empty count is below the initial price, only the original bottles can be drunk.
- **Single-batch price changes:** The price increments after every individual exchanged bottle, so multiple batches can never use the same price.
