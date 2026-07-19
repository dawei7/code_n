## General
**Materialize the three year intervals.** Create a small common table expression containing each report-year label, its first date, and its last date. Join a sales row to a year exactly when their closed intervals overlap:
$$
\text{period start} \le \text{year end}
\quad\text{and}\quad
\text{period end} \ge \text{year start}.
$$

**Measure only the intersection.** For an overlapping pair, the first counted date is the later of the two starts and the last counted date is the earlier of the two ends. The inclusive day count is the date difference plus one. Multiply it by `average_daily_sales`, then sum these contributions by product and report year.

Join `Product` by `product_id` to obtain the name, and order by the hidden product identifier followed by year. Every covered day belongs to exactly one calendar-year intersection, so cross-year periods are split without omission or double counting.

## Complexity detail
The year relation has fixed size three. With indexed or hash joins, reading the $P$ products and $S$ sales rows and producing $R$ grouped overlaps takes $O(P + S + R)$ time. Join and grouping state use $O(P + S)$ space. The app artifact uses SQLite Julian-day arithmetic; the native artifact uses equivalent MySQL `DATEDIFF`, `LEAST`, and `GREATEST` functions.

## Alternatives and edge cases
- **Expand every calendar day:** Generate one row per covered day and group afterward. It is correct but makes work proportional to total interval length.
- **Correlated scan per product-year:** Revisit all sales rows for each product and year. Without an index this takes $O(PS)$ time.
- **Inclusive endpoints:** Add one after subtracting dates; a one-day period must contribute one daily amount.
- **Leap day:** Calendar arithmetic must count `2020-02-29`.
- **Cross-year period:** Split it at each year boundary and use the same daily rate for both portions.
- **Multiple periods:** Sum every overlapping contribution for the same product and year.
- **No sales overlap:** Do not emit a product-year row with a null or zero amount.
