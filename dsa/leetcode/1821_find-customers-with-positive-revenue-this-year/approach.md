## General

**The requested condition is entirely row-local**

Each `Customers` row already contains the three facts needed:

- which customer it describes;
- which year it belongs to;
- that customer's revenue for the year.

The query needs no aggregation or join. It filters rows using both required predicates and projects only `customer_id`.

**Filter to the requested year**

The first condition is `year = '2021'`.

Column `year` has integer type, while the exact query writes 2021 as a quoted string literal. In MySQL, type coercion converts this numeric string for comparison, so it matches integer year 2021.

Writing `year = 2021` without quotes would express the schema type more directly and portably, but the protected source's comparison is correct in its MySQL environment.

Rows from every other year are rejected regardless of revenue. A customer with positive revenue in 2020 but no 2021 row must not be returned.

**Require strictly positive revenue**

The second condition is `revenue > 0`.

Strict inequality matters:

- positive values qualify;
- zero does not;
- negative values do not.

The source explicitly notes that revenue may be negative, so testing only that revenue is nonzero would be incorrect.

**Combine conditions with `AND`**

Both facts must hold on the same row. `AND` ensures that a qualifying customer has positive revenue specifically in 2021.

Using `OR` would wrongly include positive revenue from other years and nonpositive 2021 rows.

**Why no grouping or `DISTINCT` is needed**

The composite primary key `(customer_id, year)` guarantees at most one row for a particular customer and year.

After filtering to 2021, each customer can therefore appear at most once. Selecting `customer_id` cannot create duplicates, so `DISTINCT` would add unnecessary work.

**Following the sample**

Customer 1 has several yearly rows. Only the 2021 row is considered, and its revenue 30 is positive, so ID 1 is returned.

Customer 2 has a 2021 row, but revenue -50 fails the strict positivity test.

Customer 3 has positive revenue in other years but no 2021 row, so no row satisfies the year predicate.

Customer 4 has 2021 revenue 20 and is returned.

The result is IDs 1 and 4.

**Why projection returns only the requested schema**

`SELECT customer_id` omits `year` and `revenue` from the result. They are used to decide membership but are not requested output columns.

SQL permits filtered columns to be absent from the projection.

**Why the result is correct**

Every returned row passed `year = 2021` and `revenue > 0`, so every returned customer meets the definition.

Conversely, any customer with positive 2021 revenue has a unique corresponding row by the primary key. That row passes both predicates and its ID is selected. Thus no qualifying customer is omitted.

No `ORDER BY` appears because the problem accepts any result order.

**Why rows from different years must never be combined**

Revenue in this table is already the finished value for one customer-year pair. The request is not asking for lifetime revenue, a sum across transactions, or a comparison with earlier years. For example, a customer with -10 in 2021 and 1,000 in 2020 still fails, because the positive historical value cannot offset the requested year's negative value. Evaluating the predicates on one row preserves this distinction exactly and explains why neither `SUM` nor `GROUP BY` belongs in the protected query.

## Complexity detail

Let $r$ be the number of rows in `Customers` and $o$ the number of output rows.

Without a supporting year/revenue index, the database scans all rows and evaluates constant-time predicates, giving $O(r)$ logical time. Producing the result requires $O(o)$ output storage. This matches the manifest's $O(r)$ time and $O(o)$ result-space framing.

An appropriate index beginning with `year` may let the optimizer inspect only 2021 rows, while the declared primary key begins with `customer_id` and is not naturally ordered by year alone. Actual physical cost depends on indexes and the optimizer.

The query itself creates no explicit temporary grouping or sorting structure.

## Alternatives and edge cases

- **Unquoted numeric literal:** `year = 2021` avoids relying on MySQL string-to-integer coercion.
- **`BETWEEN 1 AND ...` for revenue:** It is unnecessary; `> 0` directly states strict positivity.
- **Aggregate by customer:** It could accidentally mix years and is unnecessary because each customer-year row is unique.
- **`DISTINCT customer_id`:** It is redundant after filtering one year under the composite primary key.
- **Positive revenue in another year:** It does not qualify without a positive 2021 row.
- **Negative 2021 revenue:** It is explicitly excluded.
- **Zero 2021 revenue:** It is not positive and is excluded.
- **Missing 2021 row:** The customer produces no result.
- **Multiple historical rows:** Only the 2021 row is tested.
- **Composite primary key:** It prevents duplicate output IDs for the same year.
- **Null revenue:** The schema does not describe nulls; if present, `revenue > 0` would evaluate unknown and exclude it.
- **Any result order:** No sorting is required.
- **Projection:** Only `customer_id` is returned, exactly matching the requested table.
- **Index dependence:** Performance may improve with a year-leading index without changing query semantics.
