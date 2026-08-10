## General

**First identify customers for whom type 1 must be suppressed**

The rule is customer-wide: seeing even one type 0 order changes which rows should be reported for that customer's entire collection. A row cannot be decided by looking only at its own `order_type`.

The common table expression `T` computes the set of customers who have at least one type 0 order:

`SELECT DISTINCT customer_id FROM Orders WHERE order_type = 0`.

The `WHERE` clause selects type 0 rows, and `DISTINCT` collapses multiple such orders for the same customer into one identifier. The resulting derived table is conceptually a set of “customers with a preferred type 0 order.”

For the example:

- customers 1, 2, and 3 appear in `T` because each has at least one type 0 order;
- customer 4 does not appear because both of that customer's orders are type 1.

The main query then evaluates every original order against this set.

**Express the two ways an order may be kept**

The main predicate is

`order_type = 0 OR NOT EXISTS (...)`.

An order is returned when either of these conditions holds:

1. The order itself has type 0. Such orders must always be reported, whether the customer has one or many.
2. No row in `T` has the same `customer_id`. This means the customer has no type 0 order at all, so all of that customer's orders must be reported.

The correlated subquery

`SELECT 1 FROM T AS t WHERE t.customer_id = o.customer_id`

asks only whether a matching customer exists. The selected literal 1 has no special value; `EXISTS` cares only whether the subquery produces at least one row. `NOT EXISTS` reverses that answer.

The outer alias `o` distinguishes the current `Orders` row from the CTE alias `t` and supplies the current customer's identifier to the correlated test.

**Understand the predicate for each customer category**

Suppose a customer has at least one type 0 order. That customer appears in `T`.

- Each of the customer's type 0 rows passes the left side of the `OR` and is returned.
- Each type 1 row fails `order_type = 0`. Its matching row in `T` makes `NOT EXISTS` false, so it is excluded.

Now suppose a customer has no type 0 order. Under the problem's two-type guarantee, all of their orders are type 1. The customer is absent from `T`, so `NOT EXISTS` is true for every one of those rows. All their orders are returned.

These are exactly the two rules in the statement.

**Why `DISTINCT` is useful but not what enforces the filter**

If a customer has several type 0 orders, the raw filtered CTE input contains that customer several times. `DISTINCT` reduces it to one row and makes `T` explicitly represent a set.

`EXISTS` would have the same Boolean result even if duplicates remained: one or ten matches are both “exists.” Thus `DISTINCT` is not required for logical correctness of this particular existence test, but it can reduce the materialized CTE and makes the intent clear.

The unique `order_id` guarantee does not make `customer_id` unique. Many orders can belong to one customer, which is why a customer-level set is needed.

**Why the query returns complete original order rows**

The outer `SELECT * FROM Orders AS o` returns the columns from the original order row: `order_id`, `customer_id`, and `order_type`. The CTE is used only for filtering and does not add a column to the result.

No `ORDER BY` appears because the result may be returned in any order. Adding a sort would impose unnecessary work and a presentation rule that the contract does not request.

**Why the complete query is correct**

Let $Z$ be the set of customer identifiers having at least one order with `order_type = 0`. The CTE returns exactly $Z$ because it filters to type 0 rows and deduplicates their customer identifiers.

For an arbitrary order row $o$:

- if $o$ has type 0, the first disjunct includes it, as required;
- if $o$ has type 1 and its customer lies in $Z$, the first disjunct is false and `NOT EXISTS` is false, so the row is excluded, as required;
- if $o$ has type 1 and its customer does not lie in $Z$, `NOT EXISTS` is true, so the row is included, as required.

The problem guarantees orders are only type 0 or type 1, so these cases are exhaustive. Every desired row passes and every forbidden type 1 row fails.

The use of `OR` is essential. Requiring both conditions with `AND` would exclude all type 0 orders for customers in `T`, which is the opposite of the intended behavior.

## Complexity detail

Let $N$ be the number of rows in `Orders`.

The CTE scans rows to find type 0 orders and removes duplicate customer identifiers. A comparison-sort implementation of `DISTINCT` can require $O(N\log N)$ time, matching the manifest's conservative bound. A hash-based distinct operation may take expected $O(N)$ time.

The outer query scans the orders and performs a membership-style existence check for each customer. A typical optimizer materializes `T` with an index or hash structure and implements this as an anti-join, allowing expected linear outer work. Physical plans vary by database, but the conservative overall bound remains $O(N\log N)$ under the manifest's model.

The CTE can contain up to $N$ different customer identifiers, so its materialized representation uses $O(N)$ auxiliary space. The result itself may also contain up to $N$ rows.

## Alternatives and edge cases

- **Correlated minimum order type:** Since types are only 0 and 1, one could compare each row with the customer's minimum type. That requires grouping or a window computation; the explicit type 0 customer set states the rule more directly.
- **Window function:** Computing a per-customer flag such as whether any type 0 exists and filtering on it can be correct. It may retain repeated flag values on every row and is more machinery than the CTE existence test.
- **`NOT IN` subquery:** `customer_id NOT IN (...)` can express set exclusion, but null values can give surprising three-valued logic. `NOT EXISTS` is the safer existence formulation.
- **Joining `T` and testing null:** A left join followed by a null test can implement the same logic. The correlated `NOT EXISTS` avoids adding join columns and duplicate concerns to the outer rowset.
- **Omitting `DISTINCT`:** The result remains logically correct because `EXISTS` ignores multiplicity, but the CTE may carry redundant customer rows.
- **Customer with only type 0 orders:** Every row passes the first condition and is returned.
- **Customer with both types:** All type 0 rows are returned, and all type 1 rows are suppressed.
- **Customer with only type 1 orders:** The customer is absent from `T`, so all orders are returned.
- **Several type 0 orders:** They all remain in the output; the rule never asks to deduplicate orders.
- **Empty table:** The CTE and outer result are empty, which is the correct set of reported orders.
- **Any output order:** No ordering is guaranteed or required, so downstream comparison should treat rows as an unordered result set.
- **Exact two-type guarantee:** The proof uses the fact that every order is type 0 or 1. The query would also include a hypothetical other type for a customer absent from `T`, but such rows are outside the valid input domain.
