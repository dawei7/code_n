## General

**Aggregate transactions at the reporting grain first.** The required output has one row per product and calendar year, not one row per transaction. CTE `T` extracts `YEAR(transaction_date)` and groups by `product_id` and year. `SUM(spend)` produces `curr_year_spend` for that product-year.

Doing this before previous-year matching is essential. Joining raw transactions from adjacent years could form every pair of transactions across the years and multiply spend totals. One annual row per side makes the later relationship one-to-one.

**Match the exact preceding calendar year.** CTE `S` takes each annual row `t1` and left joins another annual row `t2` when:

- product IDs are equal;
- `t1.year = t2.year + 1`.

Thus `t2.curr_year_spend` is the total for exactly the calendar year immediately before `t1.year`. It receives alias `prev_year_spend`.

The left join preserves every current product-year even when no previous-year row exists. In that case, columns from `t2` are `NULL`. An inner join would incorrectly discard the first recorded year and any year following a gap.

**Why an exact-year join differs from `LAG`.** A window expression such as `LAG(curr_year_spend) OVER (PARTITION BY product_id ORDER BY year)` returns the previous available row. If a product has data in 2019 and 2021 but none in 2020, that lag would pair 2021 with 2019. The exact source does not: its condition looks specifically for 2020 and leaves 2021's prior value null.

That exact-calendar behavior matches the phrase “previous year.” The manifest summary says a partitioned lag is used, but `solution.sql` uses a self-join, and the two methods are not semantically interchangeable when years have gaps.

**Calculate the percentage only after both annual totals are known.** The final expression is

`ROUND((curr_year_spend - prev_year_spend) / prev_year_spend * 100, 2)`.

Subtracting measures the absolute change. Dividing by the previous year's spend converts it to growth relative to the prior baseline. Multiplication by $100$ turns the ratio into a percentage, and `ROUND(..., 2)` applies the required two decimal places.

If `prev_year_spend` is null, SQL null propagation makes subtraction, division, multiplication, and rounding all null. That produces the expected null rate for a product's first year or a year after a missing calendar year without a separate `CASE`.

A negative result means spending decreased. For example, falling from $1500.60$ to $1000.20$ produces approximately $-33.35$ percent after rounding.

**Understand `SELECT *` safely in this CTE.** `S` defines its columns in the order `year`, `product_id`, `curr_year_spend`, `prev_year_spend`. The final `SELECT *` emits those four, then appends `yoy_rate`. This matches the requested output order. Adding or reordering columns in `S` would silently change the output, so explicit names would be more maintainable.

**Order at the final reporting grain.** `ORDER BY 2, 1` sorts by the second selected column, `product_id`, then the first, `year`. Both directions default to ascending. All rows for one product appear together chronologically.

**Why the result is complete and unique.** CTE `T` has one row for every product-year appearing in the source. `S` preserves each of those rows exactly once and can match at most one prior annual row because `T`'s grouping keys are unique. The calculation adds only derived columns. Therefore every observed product-year appears once with the correct current total, exact prior-calendar total when present, and corresponding growth rate.

## Complexity detail

Let $t$ be the number of transaction rows and $g$ the number of distinct product-year groups. Extracting years and aggregating can be $O(t)$ with hashing or $O(t\log t)$ with sort-based grouping. Joining the $g$ annual rows to themselves on indexed or hashed product/year keys can be $O(g)$ expected, while a sort-merge plan is $O(g\log g)$. Final ordering costs $O(g\log g)$.

The manifest's broad $O(t\log t)$ time and $O(t)$ space bounds reasonably cover common sort-based plans because $g\le t$. Engine choice, indexes, and physical execution determine actual constants and memory. Logically, the query materializes or streams annual aggregates and their self-join, requiring up to $O(g)$ intermediate state.

The manifest's algorithm summary is inaccurate even though its broad bounds are plausible: no window lag appears in the exact source.

## Alternatives and edge cases

- **Window `LAG` with gap check:** Compute lagged year and spend, then use the prior spend only when `previous_year = year - 1`. The explicit gap check makes it equivalent to the self-join.
- **Bare `LAG`:** Shorter, but incorrect for exact previous-calendar-year semantics when a product skips a year.
- **Correlated subquery:** Look up the same product at `year-1` for each annual row. It is readable but may execute less efficiently without suitable indexing.
- **First recorded year:** No exact prior row exists, so both `prev_year_spend` and `yoy_rate` are null.
- **Gap in years:** A 2021 row does not borrow 2019 merely because it is the previous available record.
- **Several transactions in one year:** `SUM` combines them before any growth calculation.
- **Several products:** Product equality in the join prevents one product's spend from becoming another's baseline.
- **Decreasing spend:** The numerator is negative and produces a negative percentage.
- **No change:** Equal totals produce zero percent.
- **Previous spend zero:** Division by zero yields null or an engine warning under MySQL settings; the exact source provides no special interpretation.
- **Null spend values:** `SUM` ignores null inputs under ordinary SQL semantics; all-null groups can produce null and propagate through the rate.
- **Rounding order:** Only the final ratio is rounded, preserving annual totals and intermediate precision.
- **Datetime extraction:** Transactions at any time within the same calendar year share the extracted year.
- **Positional ordering:** `ORDER BY 2,1` depends on select-column positions; explicit names would be safer during schema changes.
- **Manifest mismatch:** The exact implementation is annual aggregation plus exact-year self-join, not a partitioned lag.
