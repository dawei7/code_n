## General

**First aggregate orders into one row per customer-year**

The inner query groups by `customer_id` and `YEAR(order_date)`. `SUM(price) AS total` turns all orders from the same customer in the same calendar year into the required annual purchase total.

After grouping, each customer has one row for every year in which they ordered. Missing years have no row, so the later condition must reject gaps rather than silently ignoring them.

**Rank annual totals from smallest to largest**

Within each customer partition,

`RANK() OVER (PARTITION BY customer_id ORDER BY SUM(price))`

assigns rank 1 to the smallest annual total, rank 2 to the next strictly larger total, and so on. Equal totals receive the same rank, with later ranks potentially skipped.

For totals to be strictly increasing as years increase with no missing year, chronological year order and total-rank order must move together one step at a time.

**The constant-difference transformation**

The query computes

`rk = YEAR(order_date) - rank`.

Suppose a customer's considered years are consecutive:

$$
Y,\ Y+1,\ldots,Y+t.
$$

If totals are strictly increasing, their ascending ranks are

$$
1,\ 2,\ldots,t+1.
$$

Each difference is the same constant $Y-1$. Therefore a valid customer has exactly one distinct `rk` value.

The outer query groups these derived rows by customer and applies

`HAVING COUNT(DISTINCT rk) = 1`.

**Why the condition also rejects year gaps**

If purchase years skip a calendar year but totals remain strictly increasing, years increase by more than one while consecutive ranks increase by one. Their differences cannot remain constant.

For customer 2 in the example, years 2015 and 2017 with increasing totals receive ranks 1 and 2. Differences are 2014 and 2015, so the customer fails. This correctly models the missing 2016 total as zero: because the first year's total is positive, the sequence from 700 to 0 is not strictly increasing.

**Why equal or decreasing totals fail**

Equal annual totals receive the same rank. Different years minus the same rank produce different `rk` values, so equality violates the condition.

If totals decrease with time, rank order no longer matches chronological order. Year increments and rank changes cannot maintain one constant difference across all rows.

More formally, constant `year-rank=C` implies `rank=year-C`. Distinct customer-year rows therefore have ranks increasing by exactly the year difference. RANK behavior can satisfy that for every row only when years are consecutive and totals are strictly increasing.

**Single-year customers**

A customer whose first and last order occur in the same year has no adjacent-year comparison to violate. Strict increase over a one-element sequence is vacuously true. The inner query produces one row, and its distinct-difference count is one, so the customer is included.

**How the sample is classified**

Customer 1 has totals 2300, 3000, 3100, and 4700 in consecutive years 2019–2022. Their ranks are 1–4, so every difference is 2018.

Customer 2 has a year gap and fails constant difference. Customer 3 has equal totals in 2017 and 2018; both receive rank 1, producing different differences and failing.

**The exact SQL differs from the manifest summary**

The summary describes comparing adjacent totals with a window function and explicitly rejecting gaps. The protected SQL uses a rank-and-invariant trick instead of `LAG`. It does not generate missing-year rows or write an adjacent comparison.

The logic is compact but depends on understanding both RANK tie behavior and the constant year-minus-rank property.

## Complexity detail

Let $r$ be the number of order rows and $y$ the number of grouped customer-year rows. Grouping orders is typically $O(r)$ with hashing or $O(r\log r)$ with sorting. The window function must order annual groups within customer partitions, giving an overall plan commonly bounded by $O(r\log r)$.

The grouped rows and sorting/window work can require $O(r)$ intermediate space. Exact performance depends on the MySQL optimizer, indexes, partition sizes, and whether temporary tables spill to disk; the manifest's $O(r\log r)$ time and $O(r)$ space are reasonable logical bounds.

## Alternatives and edge cases

- **`LAG` adjacent comparison:** Aggregate annual totals, compare each year and total with the previous row, then reject any gap or non-increase. This matches the manifest wording and is often easier to read.
- **Recursive calendar expansion:** Generate every year between first and last and left join totals, filling gaps with zero. It models the statement literally but is much heavier.
- **Equal totals:** `RANK` ties them and the constant-difference test rejects the customer.
- **Missing intermediate year:** Consecutive total ranks cannot keep pace with the larger year jump, so the customer fails.
- **One active year:** It qualifies vacuously.
- **Multiple orders in one year:** `SUM(price)` combines them before ranking.
- **Order ID uniqueness:** It prevents duplicate row identity ambiguity but is not otherwise used by the query.
- **Any result order:** The outer query has no `ORDER BY`, which is allowed.
- **Positive prices:** A missing year's zero necessarily breaks increase after any positive prior annual total.
- **Rank versus row number:** `RANK` tie behavior is essential for rejecting equal totals; arbitrary row numbering could mask them.
