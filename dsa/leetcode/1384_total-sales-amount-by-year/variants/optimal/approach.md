## General

**Expand one sales interval into the years it overlaps**

Each `Sales` row describes one closed date interval and one average amount per day. The requested report needs a separate row for every calendar year touched by that interval. The exact query creates a tiny derived table `y` containing the only possible report years:

- 2018 with 365 days.
- 2019 with 365 days.
- 2020 with 366 days.

The 2020 value is different because 2020 is a leap year. Hard-coding these three rows is appropriate because the Reference explicitly bounds all dates to 2018 through 2020.

The first inner join matches a sales row with a year when

`YEAR(s.period_start) <= y.YEAR AND YEAR(s.period_end) >= y.YEAR`.

These inequalities say the sales interval begins no later than that year and ends no earlier than it. Equivalently, the interval overlaps that calendar year. A sale entirely within 2019 produces one joined row; a sale from late 2018 through early 2020 produces three.

An inner join is correct because a nonoverlapping year must not appear. Every valid sales interval overlaps at least one of the three allowed years.

**Convert overlap endpoints into day-of-year positions**

For each product-year overlap, the query needs the first and last included ordinal day inside that year.

The overlap's last day is:

- The year's final day when `YEAR(s.period_end) > y.YEAR`, because the sale continues beyond this report year.
- Otherwise `DAYOFYEAR(s.period_end)`, because the sale ends inside this report year.

The expression is

`IF(YEAR(s.period_end) > y.YEAR, y.days_of_year, DAYOFYEAR(s.period_end))`.

The overlap's first day is:

- Day one when `YEAR(s.period_start) < y.YEAR`, because the sale began in an earlier year and is already active on January 1.
- Otherwise `DAYOFYEAR(s.period_start)`, because the sale begins within this report year.

That expression is

`IF(YEAR(s.period_start) < y.YEAR, 1, DAYOFYEAR(s.period_start))`.

**Why the formula adds one**

Both `period_start` and `period_end` are inclusive. If ordinal start is $a$ and ordinal end is $b$, the number of included days is

$$
b-a+1.
$$

Without the final one, a one-day interval would incorrectly have zero days. The query multiplies this inclusive day count by `s.average_daily_sales` to obtain `total_amount`.

For the phone interval from 2019-01-25 through 2019-02-28, both endpoints lie in 2019. Their ordinal positions are 25 and 59, so the count is $59-25+1=35$. Multiplying by 100 produces 3500.

For the T-shirt interval from 2018-12-01 through 2020-01-01:

- The 2018 overlap begins at December 1 and ends at ordinal 365, giving 31 days.
- The 2019 overlap begins at day one and ends at day 365, giving 365 days.
- The 2020 overlap begins at day one and ends at January 1, also day one, giving one day.

The explicit `days_of_year` value makes the 2020 full-year boundary leap-year aware.

**Attach product names**

`INNER JOIN Product AS p ON p.product_id = s.product_id` adds the matching product name to every expanded sales-year row. The product ID is a key, so one name is attached per sale. Starting from `Sales` and using an inner join means products without sales intervals do not appear, exactly as the contract specifies.

The projection returns `s.product_id`, `p.product_name`, `y.YEAR AS report_year`, and the computed amount. `ORDER BY s.product_id, y.YEAR` gives the required primary ordering by product and secondary chronological ordering by year.

The year literals are written as strings such as `'2018'`, but MySQL converts them as needed in numeric year comparisons and arithmetic context. Numeric literals would communicate the type more directly, yet the exact query behaves as intended.

**Why the query is correct**

The overlap join produces exactly one row for each sales interval and calendar year with a nonempty intersection. For such a row, the two conditional expressions choose the later of the interval start and January 1, and the earlier of the interval end and December 31, expressed as ordinals. Inclusive subtraction yields exactly the number of active days in that intersection. Multiplication gives the requested yearly amount, and the product join supplies the correct name. Therefore every required product-year row has the correct total and no nonoverlapping year is emitted.

## Complexity detail

Let $P$ be the product count, $S$ the sales-row count, and $R$ the number of product-year rows produced. The report-year table has constant size three. Under hash or indexed joins, reading the source tables and generating overlaps costs $O(P+S+R)$ logical work, matching the manifest.

The explicit final ordering may require $O(R\log R)$ time when the database cannot produce rows in the requested order from an index or ordered plan. Thus a conservative physical bound includes sorting. With supporting order or a tiny constant number of rows per keyed sale, optimizer behavior may make row generation dominant.

Hash tables and intermediate joined rows can use $O(P+S+R)$ physical space; the manifest's $O(P+S)$ describes join-side auxiliary structures while treating returned rows as output. SQL execution details depend on indexes, statistics, and whether sorting spills to disk.

## Alternatives and edge cases

- **Recursive calendar expansion:** Generate every overlapping year from the dates instead of hard-coding three rows. It generalizes beyond 2020 but is unnecessary for the fixed domain.
- **Intersection with `GREATEST` and `LEAST`:** Construct year-start and year-end dates, clamp interval endpoints, and use `DATEDIFF + 1`. This is more general and can make date semantics explicit.
- **Daily calendar table:** Join every active date and group by year. It is flexible but expands one row per day and performs far more work.
- **Interval inside one year:** Both ordinal endpoints come directly from `DAYOFYEAR`.
- **Interval spans a full report year:** The start becomes one and the end becomes `days_of_year`.
- **One-day interval:** The final `+ 1` produces one day rather than zero.
- **Leap year 2020:** Its last ordinal is 366; hard-coding 365 would undercount a full-year overlap.
- **Boundary on January 1:** `DAYOFYEAR` returns one, and inclusive arithmetic handles it correctly.
- **Boundary on December 31:** The ordinal equals that year's day count.
- **Product without sales:** It is absent because `Sales` drives the query, matching the contract.
- **Missing product lookup outside the intended relationship:** The product inner join would discard that sales row; valid data is expected to reference an existing product.
- **Fixed year domain:** A date outside 2018–2020 would not be fully represented because `y` contains only those years; the stated constraints make this safe.
- **Required ordering:** The final `ORDER BY` is essential because joins and `UNION ALL` do not promise result order.
