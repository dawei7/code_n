## General

Let $B=\texttt{maxAmount}$ and $k=\texttt{maxCoupons}$. Maintain `best[c][b]`, the maximum tastiness obtainable from the fruits processed so far while spending at most budget $b$ and using at most $c$ coupons. Initializing every state to zero correctly represents buying nothing.

For a fruit with price `cost` and tastiness `value`, each state has three choices: skip it, buy it for `cost`, or—when a coupon is available—buy it for `cost // 2`. The two purchase transitions add `value` to the appropriate earlier state.

Process coupon counts and budgets in descending order. A full-price transition then reads a smaller-budget state that has not yet used the current fruit, while a discounted transition reads the previous coupon row before that row is updated for this fruit. Thus no fruit can be purchased twice, including when either price is zero. After every fruit is processed, `best[k][B]` contains the best valid purchase.

## Complexity detail

The algorithm visits each of the $n$ fruits, all $k+1$ coupon allowances, and all $B+1$ budgets. Its time complexity is $O(nkB)$ and its auxiliary space is $O(kB)$. The descending updates compress away the fruit dimension that a direct three-dimensional table would store.

## Alternatives and edge cases

- **Three-dimensional dynamic programming:** A state for every fruit prefix, coupon count, and budget is straightforward but uses $O(nkB)$ space.
- **Enumerate purchased subsets:** Checking every subset and choosing its best coupon placements is exponential in $n$.
- **No coupons:** The method reduces to ordinary 0/1 knapsack.
- **Odd prices:** A coupon charges `price[i] // 2`, so a price of 7 becomes 3.
- **Zero-price fruit:** It may be purchased without budget, and descending iteration still adds it only once.
- **Zero tastiness:** Such a fruit never improves an objective value, even if it is free.
- **Unused resources:** The state means at most the listed budget and coupons, so neither must be exhausted.
