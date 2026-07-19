## General
**Aggregate visits before forming windows**

Group `Customer` by `visited_on` and sum `amount`. This produces exactly one revenue value per date, which is essential because a window frame over raw visits would count rows rather than calendar days when multiple customers share a date.

**Use ordered seven-row windows**

Because the contract guarantees at least one customer every day, seven consecutive rows in the daily table represent seven consecutive calendar dates. Over dates in ascending order, compute both `SUM(amount)` and `AVG(amount)` with `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW`. A row number in the same order identifies the first six dates, whose frames are incomplete; retain only rows numbered 7 or later.

The retained sum contains precisely the current daily total and the six preceding daily totals. The average of those same seven values equals the requested total divided by 7. Rounding it and ordering by the ending date produces the required relation.

## Complexity detail
Grouping scans $r$ visits and retains $d$ daily totals. Ordering those totals for the window functions costs $O(d\log d)$ in the general model, and the bounded rolling frame is evaluated in $O(d)$ additional time. The daily and windowed intermediate relations use $O(d)$ space.

## Alternatives and edge cases
- **Correlated date-range sums:** For each ending date, a subquery can sum the previous six calendar days, but without a supporting index it repeatedly scans the daily relation and can take $O(d^2)$ time.
- **Self-join by date range:** Joining every ending date to its seven source dates is correct after daily aggregation, but creates more intermediate rows and requires another grouping step.
- **Multiple visits on one date:** Sum them first; they must not create extra positions in the seven-day frame.
- **First six dates:** Their windows contain fewer than seven days and must not appear.
- **Exactly seven dates:** Produce exactly one result row.
- **Average denominator:** Divide the seven-day total by 7, not by the number of customer visits.
