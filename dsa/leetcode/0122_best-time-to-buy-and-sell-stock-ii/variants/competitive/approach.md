## General

The competitive solution scans every adjacent pair of days and adds the price increase when it is positive. The resulting total is the maximum profit obtainable with unlimited transactions and at most one held share.

The method does not explicitly record purchases or sales. Each positive daily change represents profit that can be realized, and adjacent realized changes can be merged into longer transactions when desired.

**The contribution of one day-to-day step**

For days `i` and `i + 1`, the change is:

`prices[i + 1] - prices[i]`.

If it is positive, buying before the change and selling after it earns exactly that amount. If it is zero, the action makes no difference. If it is negative, holding through the step loses money, so an optimal unlimited strategy avoids it.

The source encodes all three cases with `max(0, difference)`.

**Why adding local gains is globally correct**

A transaction from day $b$ to day $s$ has telescoping profit:

$$
\texttt{prices}[s]-\texttt{prices}[b]
=
\sum_{i=b}^{s-1}
\left(\texttt{prices}[i+1]-\texttt{prices}[i]\right).
$$

Thus any complete strategy's profit is a sum of daily changes over the periods when it holds the stock.

No strategy benefits from selecting a negative change when it may sell before the fall and buy later. Consequently, the total of all positive changes is an upper bound: a strategy cannot extract more than the positive part of every available daily movement.

That bound is attainable by treating every positive step as a buy-on-`i`, sell-on-`i + 1` transaction. Consecutive steps can share a day because selling and buying on the same day is allowed. The strategy never holds more than one share.

Therefore the local sum is exactly the global optimum.

**Consecutive rising days**

For `[1, 2, 3, 4, 5]`, the loop adds four differences of one. Operationally, one could execute four adjacent transactions, but one transaction buying at one and selling at five is simpler.

The profits are equal because:

`(2 - 1) + (3 - 2) + (4 - 3) + (5 - 4) = 5 - 1`.

The algorithm counts profit, not the number or exact presentation of transactions, so either realization is valid.

**Rises separated by falls**

For `[7, 1, 5, 3, 6, 4]`, the loop sees `-6`, `4`, `-2`, `3`, and `-2`. Only four and three are added, producing seven.

The negative transitions indicate where one profitable holding interval should end and another may begin. The realized strategy buys at one, sells at five, buys at three, and sells at six.

**Why the loop range is exact**

`range(len(prices) - 1)` enumerates each adjacent starting index from zero through `len(prices) - 2`. The access `prices[i + 1]` is therefore always valid.

For a one-element input, the range is empty and profit remains zero. No special branch is needed.

Every adjacent difference appears once. There is no double counting because each daily interval has one unique start index.

**State and transaction rules**

`profit` starts at zero and only receives nonnegative additions, so the method never reports a loss. This represents the option to make no transactions.

The proof depends on unlimited transactions, no fee, no cooldown, and permission to sell and buy on the same day. Holding at most one share remains satisfied because each adjacent transaction closes before another opens.

The active method is `maxProfit`. `maxProfit2` is an unused expression-oriented alternative. Its slice and `map` behavior do not affect the selected method's execution.

## Complexity detail

For $n$ prices, the loop runs $n-1$ times. Each iteration performs constant arithmetic, comparison, and addition, so time is $O(n)$.

Only the integer `profit` and loop index are retained. Auxiliary space is $O(1)$, and the returned answer is one integer.

The method never allocates `prices[:-1]`; that slice appears only in the unused `maxProfit2`. Complexity for the active `maxProfit` must not include alternative-method allocations.

The input list is read in chronological order and not modified.

## Alternatives and edge cases

- **Generator over adjacent pairs:** Sum positive differences from `pairwise(prices)`. It is concise and constant-space but requires the proper import and Python version.
- **Peak-and-valley scan:** Skip declines to find a valley, climb to a peak, and add the peak-minus-valley profit. It explicitly identifies transactions.
- **Holding/cash state machine:** Maintains the best balance with and without a stock. It generalizes when transaction rules become more complex.
- **Brute-force transaction schedules:** Explores an exponential number of choices and repeats equivalent outcomes.
- **Single transaction logic:** Returns only the largest rise and can miss multiple separated opportunities.
- **One day:** The loop is empty and returns zero.
- **All falling:** Every `max` contributes zero.
- **All rising:** Adjacent gains telescope to the full rise.
- **Equal neighboring prices:** They add zero; trading there is optional.
- **Several valleys:** Every later positive slope is independent and contributes.
- **Same-day sell and buy:** Allows adjacent profitable segments to coexist without violating one-share ownership.
- **No transaction:** Zero initialization handles cases with no rise.
- **Transaction fee:** Would make small gains potentially unprofitable, so this greedy rule would need modification.
- **Cooldown:** Would couple adjacent opportunities and invalidate independent summation.
- **Transaction cap:** Would require choosing which rises to combine or keep.
- **Unused alternative:** `maxProfit2` should not be used to infer the active method's slicing space.
