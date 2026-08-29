## General

**A streak continues only through a qualifying predecessor**

For a transaction on date $D$ to continue an existing streak, the same customer must have a transaction on exactly $D-1$ whose amount is strictly smaller.

The CTE self-joins current row `t1` to potential predecessor `t2` with three conditions:

- equal `customer_id`;
- `t1.amount > t2.amount`;
- `DATEDIFF(t1.transaction_date, t2.transaction_date) = 1`.

The schema guarantees one transaction per customer and date, so a current row has at most one such previous-day row.

**Use a left join so broken rows remain visible**

An inner join would discard every row that begins a streak. The query instead uses `LEFT JOIN`.

When no qualifying predecessor exists, the `t2` columns are null. That happens for:

- a customer's first transaction;
- a gap of more than one day;
- a previous-day amount that is equal or greater;
- no transaction on the previous day.

Each of these conditions must begin a new candidate run.

**Mark every new run**

The `CASE` expression returns one when `t2.customer_id IS NULL` and zero otherwise.

Viewed in customer/date order, these values are boundary markers:

- one means “this row starts a new streak”;
- zero means “this row continues the preceding streak.”

Strictly increasing amounts are enforced by `t1.amount > t2.amount`. Equality is correctly treated as a break.

**Turn boundary markers into an island identifier**

The windowed cumulative sum:

`SUM(marker) OVER (ORDER BY customer_id, transaction_date)`

is stored as `s`.

The sum stays constant across continuation rows and increases whenever a break row appears. Rows belonging to one uninterrupted increasing-day streak therefore share the same `s`.

The sum is global rather than partitioned by customer, but the first row of each new customer necessarily has no qualifying predecessor and increments it. Grouping later includes `customer_id` as well, so groups cannot cross customers.

**Trace one uninterrupted run**

Suppose customer 101 has amounts 100, 150, and 200 on May 1, 2, and 3.

May 1 has no previous-day row, so its marker is one. May 2 joins May 1 because 150 is greater than 100; May 3 joins May 2 because 200 is greater than 150.

Their markers are one, zero, zero. The cumulative value `s` is constant across all three rows, so aggregation treats them as one run.

**Trace a date gap**

Suppose customer 102 transacts on May 1 and May 3.

The May 3 row cannot join May 1 because `DATEDIFF` is two, not one. Its joined predecessor is null and its marker starts a new island.

A later increasing transaction on May 4 can join May 3, but that island contains only two rows and fails the minimum-length condition.

**Trace a non-increasing amount**

If consecutive dates have amounts 200 then 150, the later row fails `t1.amount > t2.amount`.

The left join supplies null for `t2`, causing a new group. A later sequence can grow from 150 independently.

This prevents a date-consecutive but amount-decreasing transition from remaining inside a qualifying streak.

**Aggregate each island**

The final query groups by `customer_id, s`.

Within one island:

- `MIN(transaction_date)` is its first date;
- `MAX(transaction_date)` is its last date;
- `COUNT(1)` is its number of daily transactions.

Because every continuation step is exactly one day, count at least three means at least three consecutive dates.

**Filter after grouping**

`HAVING COUNT(1) >= 3` applies to aggregate groups.

Using `WHERE` for this condition would be too early because the row count does not exist until grouping is complete.

Each surviving island becomes one result row, so a customer can correctly produce several separate periods.

**Exact ordering caveat**

The requirement asks for ascending `customer_id`, `consecutive_start`, and `consecutive_end`.

The exact source ends with only `ORDER BY customer_id`. It orders different customers correctly but does not explicitly guarantee the relative order of multiple periods belonging to the same customer.

To satisfy the stated ordering literally in every execution plan, the final clause should include all three requested columns. This document does not pretend those missing secondary keys are present.


By uniqueness of customer/date rows, the left join identifies exactly whether each transaction has the required immediately previous, lower-amount predecessor. The marker is therefore one exactly at every streak boundary.

Cumulative markers assign one stable identifier to each maximal streak. Grouping recovers each streak's endpoints and size, and `HAVING` retains exactly those with at least three rows. Apart from the documented secondary-order omission, the returned row contents are the required periods.

## Complexity detail

Let $R$ be the number of transactions. With effective lookup support for customer/date, the self-join, window ordering, and grouping are commonly implemented in $O(R\log R)$ time and $O(R)$ working space, matching the manifest.

Without useful indexes, a physical nested-loop self-join can degrade toward $O(R^2)$ comparisons. SQL runtime depends on the optimizer and indexes; the window sort itself requires $O(R\log R)$ time in the general case.

## Alternatives and edge cases

- **`LAG` previous date and amount:** Can mark breaks directly after ordering each customer, avoiding the self-join.
- **Date minus row-number islands alone:** Detects consecutive days but needs an additional break marker for non-increasing amounts.
- **One transaction:** Forms a one-row island and is filtered out.
- **Exactly three days:** Qualifies because `HAVING` is inclusive.
- **Equal amount on the next day:** Breaks the streak because increase must be strict.
- **Missing day:** Breaks the streak even if the later amount is larger.
- **Several periods for one customer:** Group identifiers keep them separate.
- **Customer transition:** The new customer's first row starts a fresh marker value.
- **Unique customer/date guarantee:** Prevents multiple predecessor matches from duplicating rows.
- **Final ordering:** The exact query lacks explicit start/end tie ordering within one customer.
- **Source table:** The query reads and groups it without mutation.
