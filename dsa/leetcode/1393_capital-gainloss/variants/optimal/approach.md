## General
**Convert every operation to a signed cash flow.** Use a `CASE` expression that maps a `Buy` price to its negation and leaves a `Sell` price positive. Group rows by `stock_name` and sum those signed values.

For any stock, the aggregate contains every purchase exactly once with a minus sign and every sale exactly once with a plus sign. It therefore equals total sale proceeds minus total purchase cost, which is precisely the requested capital gain or loss. Grouping isolates the operations of different stock names.

The result does not depend on operation order: `operation_day` distinguishes rows and describes their chronology, but addition of the signed amounts is commutative.

## Complexity detail
A hash aggregation reads all $N$ rows once and maintains one accumulator per distinct stock, taking $O(N)$ expected time and $O(K)$ grouping space. A database may instead sort by `stock_name`, giving $O(N\log N)$ execution under a sort-based physical plan; the authored query expresses the linear grouping algorithm.

## Alternatives and edge cases
- **Separate buy and sell subqueries:** Aggregate each operation type and join the results. It is correct but scans and combines more intermediate data than one conditional sum.
- **Correlated aggregate per stock:** Select distinct names and rescan `Stocks` for every name. Without an index-assisted plan this costs $O(KN)$ time.
- **Net zero:** Equal total purchases and sales must produce `0`, not omit the stock.
- **Capital loss:** The signed result can be negative when purchase costs exceed sale proceeds.
- **Multiple trading cycles:** Sum every row rather than assuming one buy and one sell per stock.
- **Independent names:** Operations for one stock must never affect another stock's accumulator.
