## General
**For each sale day, only the cheapest legal earlier buy matters**

Scan prices in chronological order while storing the minimum price seen so far. For a fixed current sale day, every earlier buy produces `current_price - buy_price`, so the minimum earlier price dominates every more expensive choice.

**Evaluate the best transaction ending today before moving on**

Subtract the running minimum from the current price and update the best profit. Then include the current price in the running minimum for future sale days. Initializing best profit to zero represents choosing no transaction when all differences are negative.

Whether the current price is incorporated immediately before or after its zero-profit sale evaluation does not change the answer, but stating the earlier-buy interpretation keeps chronological legality clear.

**The scan summarizes all legal buy-sale pairs in two values**

Before processing day `i`, `lowest` is the minimum price among days through `i`, and `best` is the maximum legal one-transaction profit whose sale occurs no later than `i`.

**Trace a new minimum followed by the optimal sale**

After price `1`, the minimum becomes `1`. Later price `6` offers profit `5`, exceeding the earlier profit `4` at price `5`; no later price improves it.

**The cheapest prefix price is optimal for each sale day**

Fix a sale day. Among all legal earlier buy days, subtracting the smallest price produces the greatest profit, and the running minimum stores exactly that choice. Comparing the current price against it therefore evaluates the best transaction ending on this sale day.

Every valid transaction has one sale day, so taking the maximum of these endpoint-optimal profits covers the global optimum. Keeping zero also represents making no trade when every price declines.

## Complexity detail
Each of `n` prices is processed once, giving $O(n)$ time. Two scalar values provide all state, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Try every buy-sale pair:** is correct but takes $O(n^2)$ time.
- **Sort prices:** loses chronological order and can place the sale before the buy.
- **Add every positive rise:** permits multiple transactions and solves Problem 122.
- A decreasing or constant sequence returns zero. A single price cannot form a buy-then-later-sell pair and also returns zero.
- Sorting prices is invalid because day order is part of every legal transaction.
