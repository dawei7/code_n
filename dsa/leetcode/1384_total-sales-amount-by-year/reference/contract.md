## Function Contract

**Inputs**

- `Product(product_id, product_name)` contains $P$ products keyed by `product_id`.
- `Sales(product_id, period_start, period_end, average_daily_sales)` contains $S$ product sales intervals keyed by `product_id`.

Both endpoints of every sales interval count as sales days. The only report years are 2018, 2019, and 2020.

**Return value**

Return a table with these columns:

- `product_id`: the product's primary-key ID.
- `product_name`: the name from the matching `Product` row.
- `report_year`: a year whose closed calendar interval overlaps the product's sales interval.
- `total_amount`: the number of overlapping calendar days multiplied by `average_daily_sales`.

Emit one row for each product-year overlap and no row for a product without a sales interval. Order rows by `product_id` and then by `report_year`. Let $R$ be the number of returned rows.
