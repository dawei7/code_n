## Description

Two 0-indexed arrays, `present` and `future`, describe the same collection of
stocks. For stock $i$, `present[i]` is its price now and `future[i]` is its
price one year from now. A stock may be bought at most once, and every purchase
must be paid for from the fixed amount `budget` available today.

Choose which stocks to buy without spending more than the budget. After one
year, sell every chosen stock and return the maximum possible total profit,
where a chosen stock contributes `future[i] - present[i]`. Buying nothing is
allowed, so the result is never negative.
