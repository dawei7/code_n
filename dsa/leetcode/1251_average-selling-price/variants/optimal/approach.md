## General

**A simple average of price periods would be wrong**

Each price applies during a date interval, and different numbers of units may be sold under different prices. The required average is weighted by units:

\[
\text{average price}
=
\frac{\sum(\text{price}\cdot\text{units})}
{\sum\text{units}}.
\]

A period with 100 units sold must contribute more weight than one with 15 units. The query joins every sale to the price interval active on its purchase date, then computes this weighted fraction per product.

**Match sales by product and inclusive date range**

The join condition has two parts:

- `p.product_id = u.product_id` ensures the price and sale belong to the same product.
- `purchase_date BETWEEN start_date AND end_date` ensures the sale date lies inside that price period, including both endpoints.

Price periods for one product do not overlap. Therefore, one sale matches at most one price row. This prevents the same sale from being multiplied by two prices.

**Why the query starts from `Prices` with a left join**

The output must include a product even if it has no sold units. A `LEFT JOIN` preserves every price-side product row when no sale matches, filling sale columns with null.

If a product has several price periods and no sales, several null-extended rows may exist before grouping, but they all belong to the same `product_id` and produce one output group.

**Compute revenue and unit totals together**

For every matched row, `price * units` is revenue from that sale record. `SUM(price * units)` gives total revenue across all periods for the product, while `SUM(units)` gives total units.

Dividing these sums yields the weighted average. Placing `SUM` around products before dividing is critical. `AVG(price)` would weight periods equally, and `AVG(price * units)` would average revenue records rather than unit price.

Duplicate `UnitsSold` rows are not removed. The table may contain duplicate records, and each row represents units sold; unless the contract explicitly calls for deduplication, their units contribute separately to both revenue and denominator.

**Handle products without sales**

For an unmatched left-join row, `units` is null. Both sums are null when a product has no matched sales, and their division is null. `COALESCE(..., 0)` replaces that null result with the required zero.

If a product has some matched sales and some price periods without sales, SQL aggregate functions ignore the null contributions from unmatched periods. The matched totals remain correct.

**Round only the final weighted result**

`ROUND(..., 2)` rounds the completed quotient to two decimal places. Rounding individual period contributions first could accumulate error, so rounding is deliberately outside both sums and the division.

MySQL’s numeric division behavior produces a decimal result for this expression. Other SQL engines may perform integer division when both operands are integers and would need an explicit cast or multiplication by a real literal.

**Following product 1**

Product 1 sells 100 units at price 5 and 15 units at price 20. Total revenue is

\[
100\cdot5+15\cdot20=800.
\]

Total units are 115, so the average is

\[
800/115\approx6.9565.
\]

Rounding to two decimals returns 6.96.

A simple average of the two prices would be 12.5, demonstrating why unit weighting is necessary.

**Grouping and output shape**

`GROUP BY 1` groups by the first selected expression, `p.product_id`. The query returns exactly one row per product ID represented in `Prices`.

The contract permits any output order, so no `ORDER BY` clause is required.


Every matched sale row is paired with the unique active price for its product and date. Multiplying price by units gives that row’s revenue. Grouped sums therefore equal total product revenue and total units, making their quotient the definition of average selling price.

The left join preserves products without matching sales, aggregate null behavior identifies their missing totals, and `COALESCE` returns zero. Final rounding satisfies the requested presentation.

## Complexity detail

Let \(r\) be the combined number of price and sales rows. With useful indexes on product and dates and an efficient join/group plan, the logical processing can be near \(O(r)\), matching the manifest’s abstraction.

Physical SQL complexity depends on the optimizer. Without supporting indexes, a nested-loop range join can approach the product of table sizes; grouping may use hashing or \(O(r\log r)\) sorting. Working hash tables, sort buffers, or materialized join rows can use \(O(r)\) space. SQL bounds therefore describe expected logical growth rather than a universal execution guarantee.

## Alternatives and edge cases

- **Correlated price lookup per sale:** Find the matching price row for every sale, then aggregate. It can be clear but may execute repeated searches without good indexes.
- **Pre-aggregate sales by product, date, and units:** Useful when many identical sale rows exist operationally, but duplicates represent additional units and must be summed, not discarded.
- **Use `AVG(price)`:** Incorrect because it weights price periods rather than units sold.
- **Average row revenue:** Also incorrect; the denominator must be total units.
- **No sold units:** Left join plus `COALESCE` returns zero.
- **Sale on a boundary date:** `BETWEEN` is inclusive, so the appropriate period matches.
- **Nonoverlapping periods:** This guarantee prevents one sale from joining to multiple prices.
- **Duplicate sales rows:** Their units and revenue are both counted, preserving the weighted unit price.
- **Dialect-specific division:** Engines with integer division require a decimal cast before division.
- **Rounding stage:** Round the final quotient, not individual contributions.
- **Any output order:** No explicit sort is necessary.
