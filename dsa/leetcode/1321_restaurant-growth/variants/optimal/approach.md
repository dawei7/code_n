## General

The input may contain several customer rows on the same date, while the requested moving window is defined by days. The exact SQL therefore has two logical stages:

1. combine all transactions from the same date into one daily amount;
2. compute a rolling sum over seven consecutive daily rows.

Only after those stages does it discard the first six dates, whose windows do not yet contain seven days.

**Creating one row per day**

The innermost derived table performs:

`SELECT visited_on, SUM(amount) AS amount FROM Customer GROUP BY visited_on`.

Every customer payment on one date contributes to the same daily total. This is essential for dates such as 2019-01-10 in the example, where two customers paid $130$ and $150$. The daily row must contain $280$ before the moving window is calculated.

If the window operated directly on customer rows, “six preceding rows” would mean six transactions rather than six days and would give incorrect results whenever a day had multiple customers.

The statement guarantees at least one customer every day. After daily grouping, adjacent rows in date order therefore represent adjacent calendar dates. This guarantee is what makes a seven-row frame equivalent to a seven-day frame.

**Computing the seven-row sum**

The CTE `t` applies:

`SUM(amount) OVER (ORDER BY visited_on ROWS 6 PRECEDING)`.

`ROWS 6 PRECEDING` is shorthand for a frame beginning six rows before the current row and ending at the current row. Once enough dates exist, it contains seven daily rows:

$$
\text{current day}+\text{six preceding days}.
$$

For the first date, the frame contains only one row. For the second, it contains two. The seventh date is the first whose frame contains all seven required daily totals.

The resulting rolling total is also aliased `amount`. Inside `t`, that name now refers to the window sum rather than the one-day sum from the derived table.

**Numbering dates to remove incomplete windows**

The query also computes:

`RANK() OVER (ORDER BY visited_on ROWS 6 PRECEDING) AS rk`.

Ranking functions are based on the window order and do not meaningfully use the frame bounds. After grouping, `visited_on` is unique, so `RANK` produces $1,2,3,\ldots$ without gaps.

The outer `WHERE rk > 6` removes ranks one through six. Every surviving row has at least six earlier daily rows and therefore a complete seven-day window.

`ROW_NUMBER() OVER (ORDER BY visited_on)` would state the intended numbering more directly. With unique dates, it gives the same values as `RANK`.

**Calculating the average**

For every surviving row, the frame has exactly seven daily totals, so:

`ROUND(amount / 7, 2) AS average_amount`

divides the rolling total by seven and rounds to two decimal places. It is correct to divide by seven rather than by the number of customer rows, because the requested metric is a daily moving average.

The selected `visited_on` is the last date of the window. Thus, the row for January 7 summarizes January 1 through January 7.

**Why the numerical result is correct**

Daily grouping preserves the total paid on each date. The ordered seven-row window then sums exactly the current daily total and the six immediately preceding daily totals. Continuous-date input makes those precisely the seven calendar days required.

Filtering removes every partial frame and retains every complete frame. Dividing its exact sum by seven gives the requested moving average, and `ROUND` supplies the required precision.

**The missing final ordering guarantee**

The contract requires result rows ordered by `visited_on` ascending. The exact source has ordering clauses inside window definitions but no outer `ORDER BY`.

Window order determines frame membership and rank calculation. It does not guarantee final presentation order. A particular MySQL plan may emit rows in date order because it already sorted them for the windows, but SQL does not promise that behavior.

Therefore, the exact query computes the right values but does not fully guarantee the required row order. A compliant final query needs:

`ORDER BY visited_on`

after `WHERE rk > 6`.

## Complexity detail

Let $r$ be the number of customer transaction rows and $d$ the number of distinct dates.

Daily aggregation scans $r$ rows. With hash aggregation it takes expected $O(r)$ time and $O(d)$ space; a sort-based aggregation may add sorting cost.

The window operators require date order over $d$ daily rows. Without a suitable ordering index or reusable grouped order, that costs $O(d\log d)$ time. Running window accumulation afterward is $O(d)$.

Total intended complexity is $O(r+d\log d)$ with $O(d)$ working space, matching the manifest. The result has at most $d-6$ rows.

Adding the required outer ordering remains within $O(d\log d)$ worst-case time, and a database may reuse the existing window order.

## Alternatives and edge cases

- **Self-join date ranges:** Join each date to transactions in the previous six days and group. It is direct but can create a much larger intermediate relation.
- **Correlated subquery:** Sum a seven-day range separately for each date. Indexes may help, but repeated range work is less elegant than one window pass.
- **`RANGE INTERVAL 6 DAY` frame:** A date-based frame can handle missing calendar days more explicitly, though MySQL syntax and exact requirements must be considered.
- **`ROW_NUMBER` instead of `RANK`:** Dates are unique after grouping, so both number rows identically; `ROW_NUMBER` communicates the filtering purpose better.
- **Several customers on one day:** The inner aggregation must combine them before the seven-row frame.
- **Continuous-day guarantee:** It is what makes seven rows equal seven calendar days. Without it, the exact query could span more than seven days.
- **First six dates:** Their frames are incomplete and are correctly removed.
- **Exactly seven dates:** The result contains one row for the seventh date.
- **Rounding:** The total is divided by seven before rounding, preserving the requested two-decimal average.
- **Required output order:** The exact source needs an outer `ORDER BY visited_on`; window-local order is insufficient.
- **Window frame on `RANK`:** The frame clause does not change ranking and is unnecessary.
