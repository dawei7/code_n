## General

**Start from a calendar so missing purchases still have rows**

Version II must return every Friday of November 2023, assigning zero when no purchase occurred. A query driven only by `Purchases` cannot produce a date absent from that table. The exact solution therefore constructs all November dates first.

Recursive CTE `T` begins with `'2023-11-01'`. Its recursive branch adds one day:

`purchase_date + INTERVAL 1 DAY`

while the current date is before `'2023-11-30'`. The generated relation contains one row for each of the 30 calendar dates from November 1 through November 30 inclusive.

The query uses `UNION` rather than `UNION ALL`. Dates are inherently unique in this increasing sequence, so duplicate removal changes no membership, though `UNION ALL` would express the fact more cheaply.

**Preserve calendar dates with a left join**

`T LEFT JOIN Purchases USING (purchase_date)` matches every purchase to its date while retaining a calendar row even when no match exists.

For a date with purchases, the join produces one row per purchase. For a date without purchases, it produces one row whose purchase-side columns, including `amount_spend`, are `NULL`.

An inner join would discard exactly the missing dates that this version must show, so join direction is central to correctness.

**Keep only Fridays after building the calendar**

`WHERE DAYOFWEEK(purchase_date) = 6` filters the calendar to MySQL Fridays. Because `USING` exposes one coalesced join column and every retained row has a CTE date, the function remains defined even when there is no purchase.

The four generated dates are November 3, 10, 17, and 24. Filtering after the left join is safe because the condition refers to the preserved date, not a nullable purchase-side field. A condition on `amount_spend` in `WHERE` could accidentally turn the left join into an inner join, but this query avoids that.

**Aggregate totals and replace missing sums**

`GROUP BY 2` groups by the second selected column, `purchase_date`. Multiple purchases on one Friday are summed.

For an unmatched Friday, `SUM(amount_spend)` sees only `NULL` and returns `NULL`. `COALESCE(..., 0)` changes that null aggregate to the required numeric zero.

This distinction matters: `SUM` does not itself return zero for a group containing no non-null values.

**Derive week numbers**

`CEIL(DAYOFMONTH(purchase_date) / 7)` maps days 1–7 to week one, 8–14 to week two, 15–21 to week three, and 22–28 to week four. The four November Fridays consequently receive week numbers one, two, three, and four.

`ORDER BY 1` sorts that week number ascending, giving chronological weekly output.

**Why the complete query is correct**

The recursive CTE supplies every possible November date independently of purchase data. Filtering selects exactly every Friday. The left join attaches all purchases from each selected date without eliminating unmatched Fridays. Grouped `SUM` computes actual totals, and `COALESCE` gives zero precisely when no amount exists.

Thus every required Friday appears exactly once with the correct amount. No non-Friday or out-of-month date can appear because the calendar bounds and weekday filter exclude them.

**Relation to version I**

Version I starts with purchases and naturally omits empty Fridays. Version II starts with required dates and enriches them with optional purchases. This “dimension table left joined to facts” pattern is broadly useful whenever a report must display zero-activity periods.

**Why the CTE generates every day**

The source could seed November 3 and advance by seven days, but it deliberately generates all 30 dates and applies the weekday predicate afterward. That makes the recursive rule a simple consecutive-calendar rule and leaves weekday selection in the reporting query. It performs a few more fixed-size rows of work while keeping each responsibility easy to verify.

## Complexity detail

Let $D=30$ be the generated day count and $R$ the purchase-row count. Calendar generation is $O(D)$. Joining can be expected $O(D+R)$ with hashing or indexed date lookup, while a sort/merge or grouping plan may cost $O((D+R)\log(D+R))$.

Grouping and ordering only four Friday groups is constant for this fixed month. The manifest’s $O(R\log R)$ time and $O(R)$ space treat $D$ as fixed and safely cover general database execution. Logical calendar storage is $O(D)$, plus join/group work.

## Alternatives and edge cases

- **Drive from `Purchases`:** This cannot emit Fridays with no rows and would solve version I instead.
- **Hard-code four `UNION ALL` dates:** It works for this fixed month but is less systematic than generating the calendar.
- **Use a permanent calendar table:** In production analytics this is often preferable and avoids recursive generation.
- **Use an inner join:** It drops zero-purchase Fridays and violates the core requirement.
- **Place a purchase-side filter in `WHERE`:** It can null-reject unmatched rows and unintentionally undo the left join.
- **Omit `COALESCE`:** Empty Friday groups would display `NULL` rather than zero.
- **Multiple purchases on one date:** The left join creates multiple rows and `SUM` combines all amounts.
- **MySQL weekday numbering:** Friday is six because Sunday is one.
- **Recursive termination:** The strict “less than November 30” condition generates November 30 once and stops before December.
- **Output order:** `ORDER BY 1` gives weeks one through four.
