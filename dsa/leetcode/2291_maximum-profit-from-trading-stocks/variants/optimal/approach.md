## General

**Turn each stock into a knapsack item**

Buying stock $i$ consumes `present[i]` units of today's budget and contributes
`future[i] - present[i]` profit one year later. Each stock is available only
once, so these are exactly the weight, value, and single-use rules of 0/1
knapsack. A losing stock never has to be selected because skipping every stock
is permitted and yields zero profit.

**Store the best profit for every budget limit**

Let `best[money]` be the greatest profit obtainable from the stocks processed
so far while spending at most `money`. Initially every entry is zero. For a
stock with current price `price` and profit `gain`, update every affordable
budget from `budget` down through `price`:

`best[money] = max(best[money], best[money - price] + gain)`.

Descending iteration is essential. The source state at `money - price` still
belongs to the previous set of stocks, so the current stock cannot be bought
twice. This remains correct when `price` is zero: each entry updates exactly
once for that stock and can collect its gain without consuming budget.

For each state, the transition compares the only two possibilities for the
current stock—skip it, or buy it and combine it with an optimal earlier
selection that fits in the remaining budget. Induction over the processed
stocks therefore makes every entry optimal for its budget limit. The entry at
`budget` is the requested maximum.

## Complexity detail

Let $n$ be the number of stocks and $B$ be `budget`. Every stock examines at
most $B+1$ budget states, so the running time is $O(nB)$. The one-dimensional
table contains $B+1$ integers and uses $O(B)$ space.

## Alternatives and edge cases

- **Two-dimensional knapsack:** A table indexed by both stock count and budget gives the same recurrence and $O(nB)$ time, but uses $O(nB)$ space.
- **Subset enumeration:** Trying all selections is correct but takes $O(2^n)$ time and is infeasible for $n=1000$.
- **Greedy by profit or ratio:** A locally attractive stock can consume budget needed by a more profitable combination, so neither ordering is generally correct for 0/1 choices.
- **Zero current price:** A profitable zero-price stock must be collected once even when `budget` is zero; descending updates still enforce the single-purchase rule.
- **Non-positive profit:** Such a stock cannot improve an at-most-budget optimum and is naturally ignored by the maximum transition.
- **Budget larger than useful costs:** The final state selects every positive-profit stock whose combined current price fits; unused money has no value of its own.
