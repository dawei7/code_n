## General

**Filter qualifying orders before grouping**

Only orders whose `invoice` is strictly greater than twenty contribute to either requested count.

The `WHERE invoice > 20` clause removes all nonqualifying rows before monthly groups are formed. An invoice equal to twenty is excluded because the condition is strict, not greater-than-or-equal.

Filtering first has an important consequence: a month containing orders but no invoice above twenty produces no group and therefore no output row. This matches the example's omission of November.

**Convert each date into a year-month key**

`DATE_FORMAT(order_date, '%Y-%m')` produces a fixed-width string such as `2020-09`.

Every date in the same calendar month and year receives the same key. Dates in the same month number but different years remain separate because the year is included.

The formatted expression is aliased as `month` and is the first selected column.

Using a two-digit month is important for stable representation. January is `01` rather than `1`, and the output always follows the required `YYYY-MM` format.

**Group by the computed month**

`GROUP BY 1` refers positionally to the first selected expression, the formatted month.

After the qualifying filter, all remaining rows sharing that key form one group. No separate ordering is required because the contract permits any output order.

Positional grouping is concise, although it depends on the select-list order. Spelling out the date-format expression or its alias would communicate the same relational operation.

**Count qualifying orders**

`COUNT(order_id) AS order_count` counts non-null order identifiers in each monthly group.

`order_id` is the table's unique-value column, so every qualifying row represents a unique order. Counting it gives the number of qualifying unique orders without needing `DISTINCT`.

If the identifier could be null, `COUNT(order_id)` would omit null rows, but a unique order identifier in this schema serves as the row identity expected to be present.

**Count unique customers separately**

One customer may place several qualifying orders in the same month. Those orders all belong in `order_count` but that customer must contribute only once to `customer_count`.

`COUNT(DISTINCT customer_id)` deduplicates customer identifiers within each monthly group before counting.

The distinctness scope is per group. The same customer can correctly count once in September and once again in December because those are different result rows.

**Tracing September and December**

September 2020 has two qualifying orders, one from customer one and one from customer two. The order count is two and the distinct-customer count is two.

December has two qualifying orders but both belong to customer four. Its order count is two while its customer count is one.

This difference is why the two aggregate expressions cannot both be simple row counts.

**Why October includes only one order**

October contains invoices twenty and twenty-one. The strict filter removes the invoice of exactly twenty.

Only the twenty-one row reaches the group operation, producing both counts as one.

The query does not form an October group first and then selectively count expressions. It filters the underlying relation, which gives the same requested counts and automatically removes entirely nonqualifying months.

**Why the query is correct**

Each qualifying order maps to exactly one `YYYY-MM` key. Grouping partitions all and only qualifying orders by that key.

Within each group, unique `order_id` values correspond one-to-one with orders, while distinct `customer_id` values correspond one-to-one with customers who placed at least one qualifying order.

The projection names those two exact cardinalities and the group key. Therefore every output row has the required month and counts, and no unwanted month appears.

**Any-order contract**

The query deliberately has no `ORDER BY`. SQL does not promise an implicit ordering, but the problem explicitly permits any order.

Adding an order would be harmless to content but would perform work that the contract does not require.

## Complexity detail

Let $R$ be the number of order rows and $Q$ the number that pass the invoice filter.

The database must inspect relevant rows, format qualifying dates, and aggregate them. A sort-based group and distinct aggregation can cost $O(R+Q\log Q)$ time, summarized by the manifest as $O(R\log R)$.

A hash-based plan may achieve expected $O(R)$ grouping work, but actual behavior depends on indexes, the optimizer, date-expression evaluation, and distinct-aggregate implementation.

Grouping and distinct-customer tracking may retain up to $O(Q)$ values across working structures, fitting the manifest's $O(R)$ space upper bound. The engine may spill intermediate state to disk.

## Alternatives and edge cases

- **Conditional aggregation without WHERE:** Group all months and count qualifying rows with conditions, then remove zero-count groups. It is more verbose here.
- **COUNT star:** After filtering, `COUNT(*)` is equivalent to counting non-null unique order identifiers.
- **COUNT DISTINCT order id:** It is correct but redundant because order identifiers are already unique.
- **Count customer rows directly:** It is wrong when one customer has multiple qualifying orders in a month.
- **Invoice exactly twenty:** It is excluded by the strict greater-than condition.
- **Month with no qualifying invoice:** It does not appear in the result.
- **Several orders by one customer:** All count as orders, but the customer counts once that month.
- **Same customer across months:** The customer counts once independently in each month.
- **Same month across years:** Including the year keeps the groups separate.
- **Any output order:** No outer sorting clause is necessary.
- **Positional GROUP BY:** It relies on `month` remaining the first selected expression.
- **Date formatting:** Fixed-width `YYYY-MM` matches the required output type and value.
