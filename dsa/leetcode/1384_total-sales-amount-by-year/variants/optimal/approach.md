## General

**Represent the report years once.** The legal sales domain contains only 2018, 2019, and 2020. Materialize those three closed calendar intervals in a small `years` common table expression instead of repeating an almost identical query branch for every year. A sales interval belongs to a report year precisely when the two closed intervals overlap:

$$
\text{period start} \le \text{year end}
\quad\text{and}\quad
\text{period end} \ge \text{year start}.
$$

**Measure the closed intersection.** For each overlapping product-year pair, the first counted date is the later of the two starts and the last counted date is the earlier of the two ends. If those dates are $a$ and $b$, respectively, the number of included days is

$$
\operatorname{days}(a,b) + 1.
$$

The added one is required because both source endpoints are inclusive. Multiplying that count by `average_daily_sales` gives exactly the product's amount for that year. The candidate uses SQLite's `julianday` difference and `MIN`/`MAX` scalar functions to implement the same calculation.

**Use the source key.** `Sales.product_id` is a primary key, so each product contributes at most one sales interval. Consequently, every joined product-year pair is already the single required output row: no `SUM`, `GROUP BY`, or duplicate-elimination step is needed. Joining `Product` supplies the name, and sorting by `product_id` and `report_year` satisfies the required order. Because the three year intervals are disjoint and exhaustive over the legal date domain, every sales day is counted once in exactly one output year.

## Complexity detail

Let $P$ be the number of `Product` rows, $S$ the number of `Sales` rows, and $R$ the number of returned product-year rows. The `years` relation has constant size three. With ordinary indexed or hash joins, the query takes $O(P + S + R)$ time and $O(P + S)$ working space. Since each sales row overlaps at most three fixed years, $R \le 3S$.

## Alternatives and edge cases

- **One branch per year:** Three `UNION ALL` branches can compute the same intersections, but duplicate the overlap predicate and date arithmetic, making boundary fixes and review more error-prone.
- **Expand every calendar day:** Generating one row per covered day and grouping is correct, but its work depends on total interval length rather than the number of source and result rows.
- **Correlated product-year scans:** Repeatedly scanning `Sales` for every product and year is correct but can take $O(PS)$ time without a usable index.
- **Unnecessary aggregation:** Treating `Sales` as if a product could have several periods contradicts its primary key and adds grouping work without changing valid-source results.
- **Inclusive endpoints:** A one-day interval contributes one daily amount, and a period from December 31 through January 1 contributes once to each adjacent year.
- **Leap day:** Date arithmetic must include February 29 in 2020, so a full 2020 interval contains 366 days.
- **Products without sales:** An unsold `Product` has no product-year overlap and must not produce a null or zero row.
- **Zero daily sales:** A valid overlapping interval with `average_daily_sales = 0` still produces its product-year row with `total_amount = 0`.
