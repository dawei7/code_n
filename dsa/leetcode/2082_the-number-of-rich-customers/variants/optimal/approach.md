## General

**Filter qualifying bills before counting customers**

A customer is considered rich if at least one of their bills has an amount strictly greater than 500. The result must count customers, not bills. A customer with several qualifying bills still contributes only one to the answer.

The SQL query handles these two ideas in the natural order:

1. `WHERE amount > 500` keeps only bills that satisfy the strict threshold.
2. `COUNT(DISTINCT customer_id)` counts the different customers represented by those remaining bills.

The filter is applied logically before the aggregation. Bills of amount 500 do not qualify because “strictly greater” requires `>` rather than `>=`. Bills below the threshold are also removed. Once a row is filtered out, its customer does not influence the distinct count through that row.

For the example, the qualifying bills belong to customer 1 twice and customer 3 once. The sequence of qualifying customer identifiers is conceptually `[1, 1, 3]`. Applying `DISTINCT` reduces those identifiers to `[1, 3]`, and `COUNT` returns 2.

**Why `DISTINCT` is essential**

The table's primary key is `bill_id`, which means every bill row is unique. It does not mean `customer_id` is unique. The same customer can have many different bills, each with its own `bill_id`.

A plain `COUNT(customer_id)` after the filter would count qualifying bills. In the example, it would return 3 because customer 1 has two qualifying rows. That is not the requested number of customers.

`COUNT(DISTINCT customer_id)` first treats repeated occurrences of the same customer identifier as one distinct value, then counts those values. It precisely expresses “had at least one” because after the first qualifying bill establishes a customer's membership, further qualifying bills do not increase the count.

There is no need to group by customer and return one row per customer. The required result is a single total, and the distinct aggregate calculates it directly.

**Produce the required one-row schema**

The expression is aliased with

`AS rich_count`.

This alias is part of the result contract. It names the sole output column `rich_count` rather than exposing a database-generated aggregate label.

Because the query contains an aggregate and no `GROUP BY`, it returns one summary row for the entire filtered table. If there are no bills above 500, the distinct count is 0, and the result is still one row containing zero. This is preferable to a grouped query that might return no rows when nobody qualifies.

No `ORDER BY` is needed because the result contains only one row.

**Why the query is correct**

Let $F$ be the set of `Store` rows whose `amount` is greater than 500. The `WHERE` clause selects exactly $F$: every qualifying row satisfies the predicate, and every nonqualifying row fails it.

Now let $C$ be the set of customer identifiers appearing in $F$. A customer belongs to $C$ if and only if there exists at least one row for that customer with an amount above 500. That is exactly the definition of a rich customer.

`COUNT(DISTINCT customer_id)` returns the number of unique identifiers in $C$. Duplicate qualifying bills for one identifier do not change this cardinality, while every different qualifying customer contributes one. The query therefore returns exactly the number of rich customers.

The unique `bill_id` constraint helps define each row as a separate bill, but it does not appear in the query because the requested existence condition depends only on `amount` and `customer_id`.

**Understand SQL null behavior without changing the contract**

Under standard SQL semantics, `COUNT(DISTINCT customer_id)` ignores `NULL` values. The problem's customer records are intended to identify a customer, so valid rows provide meaningful customer identifiers. If a database allowed a qualifying row with a null customer identifier, that row would not identify a countable customer and would not increase `rich_count`.

Similarly, a null `amount` would not satisfy `amount > 500` because the comparison evaluates as unknown rather than true. These behaviors are consistent with using actual identified customers and qualifying numeric bills, though the intended problem data do not require extra null-handling expressions.

**Why no join is necessary**

All facts required by the result live in `Store`:

- `amount` determines whether a bill qualifies;
- `customer_id` determines which customer it belongs to.

There is no separate customer table to consult and no need to match rows to one another. Adding a self-join would multiply bill combinations and make deduplication harder without supplying new information.

The query is declarative, so the database may implement distinct counting with hashing, sorting, or an index-assisted plan. These physical choices do not alter its logical meaning.

## Complexity detail

Let $B$ be the number of bill rows in `Store`, and let $C$ be the number of distinct customers among bills whose amount exceeds 500.

The database examines bill rows to apply the filter. A comparison-based implementation may collect or sort qualifying customer identifiers to remove duplicates, giving the manifest's conservative $O(B\log B)$ time bound. A hash-aggregate execution plan commonly performs expected $O(B)$ time instead. An appropriate index may also change the physical scan, but the SQL does not require one.

The distinct aggregate must remember which qualifying customers have already been encountered. A hash-based implementation stores up to $C$ identifiers, matching $O(C)$ auxiliary space. A sorting plan may use storage proportional to the qualifying rows instead, depending on the engine and available memory.

The output is always one row and one scalar count, so result size is $O(1)$.

## Alternatives and edge cases

- **Plain `COUNT(customer_id)`:** This counts qualifying bill rows, so customers with multiple bills are overcounted. `DISTINCT` is necessary.
- **`GROUP BY customer_id` alone:** This yields one row per rich customer rather than the required single total. An outer count could repair it, but the direct distinct aggregate is simpler.
- **Nested grouped subquery:** Selecting qualifying customer IDs with `GROUP BY` and then counting those rows is correct, but it introduces an unnecessary query layer compared with `COUNT(DISTINCT ...)`.
- **`EXISTS` against a customer table:** If a separate complete customer table existed, an existence test could mark qualifying customers. No such table is needed here because qualifying identifiers can be obtained directly from `Store`.
- **Threshold exactly 500:** Such a bill does not qualify. Replacing `> 500` with `>= 500` changes the problem's strict boundary.
- **Several qualifying bills for one customer:** They contribute one distinct identifier and therefore one to the result.
- **Qualifying and nonqualifying bills for one customer:** The qualifying row is sufficient. Filtering individual bills before deduplication retains that customer once.
- **Only nonqualifying bills:** The filtered input is empty, but the aggregate still returns one row with `rich_count = 0`.
- **Empty table:** The same ungrouped aggregate behavior returns zero rather than no rows.
- **Unique bill identifiers:** `bill_id` prevents duplicate bill records by key, but customers may repeat. Counting bill IDs would answer a different question.
- **Null customer identifiers:** Standard `COUNT(DISTINCT ...)` ignores null. The intended data identifies customers, so no special null substitute is required.
- **Exact output alias:** The aggregate must be named `rich_count` to match the expected result schema.
