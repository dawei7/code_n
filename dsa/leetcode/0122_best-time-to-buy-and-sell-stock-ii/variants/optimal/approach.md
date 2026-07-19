## General
**Every rising edge is independently realizable profit**

Whenever today's price exceeds yesterday's, add that positive difference. It can be realized by holding stock across exactly that edge. A nonpositive edge contributes nothing because selling before the decline and buying afterward is never worse than holding through it.

**Adjacent rising-edge profits telescope into valley-to-peak profit**

For prices $a < b < c$, profit $c-a$ equals $(b-a) + (c-b)$. Therefore collecting daily rises is financially equivalent to one transaction from the valley to the peak. The apparent sell and rebuy on an intermediate day can be merged, so the one-stock-at-a-time rule is respected.

**Processed positive edges form an attainable optimal schedule**

After day `i`, the accumulated sum is the maximum profit achievable using only days through `i` while ending with no stock held.

**Trace climbs separated by declines**

For `[7,1,5,3,6,4]`, collect rises `1 -> 5` for `4` and `3 -> 6` for `3`. Declines separate the transactions, producing total `7`.

**Transaction profit decomposes into positive daily rises**

For a buy at day `a` and sale at day `b`, the profit telescopes into the sum of adjacent changes from `a` through `b`. Negative changes can be avoided by closing before the decline and reopening afterward, so an optimal schedule never needs to include them.

Every positive adjacent change can be realized as its own transaction, and consecutive rises may be merged into one transaction with the same total. Summing all positive changes is therefore attainable and at least as large as any legal schedule's decomposed profit.

## Complexity detail
The algorithm examines each adjacent pair once, giving $O(n)$ time. The running profit is the only state, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Dynamic programming with hold/cash states:** is correct but unnecessary for the unlimited, fee-free contract.
- **Enumerate transaction schedules:** is exponential.
- **Keep only the single best rise:** solves Problem 121 and misses separated opportunities.
- Constant and decreasing prices yield zero. Same-day sell-and-buy boundaries between adjacent rises can be merged without changing profit.
- Transaction fees, cooldowns, or limits invalidate this simple edge decomposition and require additional state.
