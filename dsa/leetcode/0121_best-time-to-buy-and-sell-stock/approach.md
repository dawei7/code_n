## General

The transaction must buy once and sell later. For a chosen selling day, the best possible purchase is therefore the smallest price strictly before that day. The selected solution maintains exactly that information while scanning prices chronologically.

`mi` stores the lowest price from earlier days, and `ans` stores the largest valid profit found so far. Each new price is considered first as a selling price and only afterward as a possible minimum purchase for future days.

**The mathematical reduction**

For sell index $j$, the best profit ending on that day is

$$
\texttt{prices}[j]
-
\min_{0\le i<j}\texttt{prices}[i].
$$

The complete answer is the maximum of this quantity over all selling days, with zero retained when every difference is negative.

There is no need to compare the current selling price with every earlier day separately. All earlier buying choices are summarized by their minimum.

**The state before processing a price**

Immediately before loop value `v` for day $j$:

- `mi` is the minimum price among days zero through $j-1$; and
- `ans` is the best nonnegative profit from every valid buy-sell pair whose selling day is before $j$.

The first iteration has no earlier price, so `mi` starts at positive infinity. `ans` starts at zero because declining all transactions is allowed and yields zero profit.

**Why profit is updated before the minimum**

`ans = max(ans, v - mi)` treats `v` as today's selling price and `mi` as an earlier buying price. Because today's value has not yet been folded into `mi`, a candidate always respects the strict buy-before-sell order.

On the first day, `v - inf` is negative infinity, so `ans` remains zero. There is correctly no possible transaction with only one observed day.

After considering a sale, `mi = min(mi, v)` admits today's price as a possible purchase for later days. It cannot be used for today's sale because the profit step has already finished.

**Why the invariant remains true**

The profit update compares the prior best with the best transaction that sells today. Those two groups cover all valid transactions ending no later than today: a transaction either sold earlier or sells today.

The minimum update then combines the old earlier-day minimum with today's price, producing the exact minimum across the newly processed prefix.

Both invariant statements therefore hold before the next iteration. Starting from the empty prefix and repeating this argument proves that final `ans` is the maximum profit across every ordered pair of distinct days.

**Tracing the profitable example**

For `[7, 1, 5, 3, 6, 4]`, the first day cannot sell, then sets `mi` to seven. Day two at price one offers a negative candidate and lowers `mi` to one.

Price five yields profit four. Price three yields two and leaves the answer four. Price six yields five, becoming the best. Price four yields three.

The final answer five corresponds to buying at one and selling later at six. The algorithm does not need to remember the day indices because the update order already preserves chronology.

**Tracing a decreasing sequence**

For `[7, 6, 4, 3, 1]`, every sell candidate is negative because every earlier minimum remains above the current price until the minimum is updated.

`ans` never falls below its initial zero. Returning zero means perform no transaction, which is better than accepting a loss.

**Why one transaction is enforced**

`v - mi` describes one purchase and one sale. Profits are never added together, and `mi` is a raw price rather than a balance after an earlier sale. Therefore the state cannot represent multiple transactions.

The algorithm also never sells before buying because only prior prices enter a candidate. Price values may be zero; buying at zero simply makes later positive prices fully profitable.

**Exact source dependencies**

The annotation `List[int]` requires `List` from `typing`. The initializer `inf` also requires a definition, commonly `from math import inf`.

Neither name is imported in the selected file. In a standalone environment, class definition can fail on `List`, or execution can fail on `inf`, unless the harness injects them. Replacing `inf` with `float("inf")` would remove one dependency.

## Complexity detail

Let $n$ be the number of prices. The loop visits each price once and performs a constant number of arithmetic operations and comparisons. Time is $O(n)$.

Only `ans`, `mi`, and the loop reference are retained. Their count does not grow with the input, so auxiliary space is $O(1)$.

The returned integer uses constant output space. No input element is modified, copied, sorted, or stored in another collection.

Reading every price is necessary in the worst case because the last price might create the unique best sale or the last earlier price might affect an extended setting. Thus the linear scan is asymptotically optimal for an unsummarized input array.

## Alternatives and edge cases

- **Brute-force pairs:** Test every buy day with every later sell day. It is direct but takes $O(n^2)$ time.
- **Suffix maximum prices:** Precompute the best future sale for every buy day, then maximize the differences. It runs in $O(n)$ time but uses $O(n)$ additional space.
- **Daily-difference maximum subarray:** Convert adjacent price changes into gains and find the maximum nonnegative contiguous sum. This is equivalent to choosing one buy-sell interval but is less direct.
- **Competitive update order:** Update the minimum before the profit. It considers a same-day zero candidate when today is a new minimum, but that cannot create an invalid positive answer.
- **One day:** No pair of distinct days exists, so the initialized zero is returned.
- **Strictly decreasing prices:** Every transaction loses money, so return zero.
- **Strictly increasing prices:** The first price remains the minimum and the last price gives the maximum profit.
- **Repeated equal prices:** Buying and selling at equal prices yields zero and does not displace a positive best.
- **Zero purchase price:** A later price `v` can produce profit `v`.
- **Multiple local rises:** Only the single largest buy-then-sell difference is retained; rises are not summed.
- **Chronology:** Updating profit before `mi` makes the earlier-buy requirement explicit.
- **No transaction:** The initial zero prevents a negative result.
- **Missing names:** `List` and `inf` must be supplied for standalone execution.
- **Input preservation:** The source only reads `prices`.
