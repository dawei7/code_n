## General

**Aggregate before comparing years**

Extract the calendar year from each transaction timestamp, then group by `product_id` and year. `SUM(spend)` produces one `curr_year_spend` value per group. Comparing raw transactions would be incorrect when a product has multiple purchases in one year.

**Attach the preceding annual total**

Apply `LAG(curr_year_spend)` over each product partition ordered by year. The first row in a product partition receives `NULL`; every later row receives the total from the preceding annual row in that ordering.

Place this window result in a second common table expression so both the displayed `prev_year_spend` and the percentage calculation use exactly the same value.

**Calculate and order the result**

For rows with a previous value, compute `(current - previous) / previous * 100` and round to two decimals. SQL null propagation naturally leaves the first year's rate `NULL`. Division by a zero previous total also yields `NULL` in the app-local SQLite runtime and MySQL.

Finally sort by `product_id` and `year`. Aggregation establishes the correct annual totals, the partitioned order pairs annual rows only within the same product, and the final ordering satisfies the output contract.

## Complexity detail

Let $t$ be the transaction count and $g$ the number of product-year groups. Grouping, ordering window partitions, and ordering the result have a conservative $O(t\log t)$ time bound. Database engines may use indexes or hash aggregation to improve individual stages.

Materializing grouped rows, window state, and sort buffers may use $O(t)$ auxiliary database storage. The output itself contains $g$ rows.

## Alternatives and edge cases

- **Window over raw transactions:** `LAG(spend)` before annual aggregation compares individual purchases rather than yearly totals.
- **Correlated previous-year lookup:** Searching the grouped table separately for each output row is correct but can repeat work and approach $O(g^2)$ time.
- **Self-join on exactly `year - 1`:** This treats a missing calendar year differently from the preceding available annual row produced by the required ordered comparison.
- **First year per product:** Both previous spend and growth rate must be `NULL` independently for every product partition.
- **Multiple transactions in one year:** Sum them before applying `LAG`.
- **Multiple products:** Window partitions prevent one product's spend from becoming another product's previous value.
- **Decrease:** A smaller current total produces a negative percentage.
- **Unchanged spend:** Equal annual totals produce `0.00`.
- **Zero previous total:** Percentage division is undefined and remains `NULL`.
- **Rounding:** Round only the final percentage to two decimal places, not the annual totals before comparison.
- **Ordering:** Sort product first and year second, both ascending.
