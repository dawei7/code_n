## General

**First restrict the population to one order per customer**

This version asks about first orders, not every delivery row. For each `customer_id`, the first order is the one with the smallest `order_date`.

The grouped subquery computes

`SELECT customer_id, MIN(order_date) FROM Delivery GROUP BY 1`.

`GROUP BY 1` groups by the first selected expression, `customer_id`. The result contains each customer and that customer's earliest order date.

The statement guarantees that every customer has precisely one first order. Therefore, the pair `(customer_id, minimum_date)` identifies exactly one delivery row.

**Filter with a composite row-value match**

The outer `WHERE` condition tests

`(customer_id, order_date) IN (...)`.

A delivery survives only when both its customer identifier and date match one earliest-date pair from the subquery. Matching only `order_date` would be wrong because different customers can share dates. Matching both fields selects each customer's own first order.

The uniqueness guarantee matters. If one customer could place two orders on the same earliest date, both rows would match and that customer would receive double weight. The problem explicitly excludes that ambiguity.

**Average the immediate indicators**

For every surviving first-order row, the Boolean expression

`order_date = customer_pref_delivery_date`

is one for an immediate order and zero for a scheduled order in MySQL numeric context.

`AVG(...)` sums those indicators and divides by their count. Because there is exactly one surviving row per customer, the average is the fraction of customers whose first order is immediate.

Multiplying by 100 converts the fraction to a percentage, and `ROUND(..., 2)` supplies the required two-decimal rounding. The output alias is `immediate_percentage`.

**Trace the example**

Customer one contributes the August 1 order, which is scheduled.

Customer two contributes the August 2 order, which is immediate.

Customer three contributes the August 21 order rather than the later August 24 order; that first order is scheduled.

Customer four contributes the August 9 immediate order.

Two of four first orders are immediate, so the average indicator is one-half and the returned percentage is `50.00`.

**Why the query is correct**

The grouped minimum date is exactly the definition of a customer's first order date. Composite membership retains all and only rows matching each customer's minimum. The uniqueness guarantee makes this a one-to-one correspondence between customers and filtered rows.

On that population, the equality indicator is one exactly for immediate first orders. Averaging zero-one values gives the number of immediate first orders divided by the number of customers. Multiplication and rounding produce the required percentage format.

Thus the query returns precisely the percentage of customers whose first order was immediate.

**Why filtering precedes averaging**

If the query averaged all orders and tried to correct afterward, customers with more deliveries would receive more influence. Restricting to one first row per customer ensures equal customer weight and exactly matches the problem's denominator.

The query returns one aggregate row and requires no output ordering.

**Keep customer weighting uniform**

The filtered relation is important not only for choosing the correct dates but also for weighting. Because each customer contributes precisely one row, `AVG` gives every customer one equal vote. A customer with ten later deliveries has no more influence than a customer with only one delivery.

The primary key `delivery_id` identifies source orders, but it is unnecessary in the tuple match because the contract already guarantees a unique first order for each customer. Under that guarantee, customer plus earliest date is a sufficient selector for this calculation.

## Complexity detail

Let `n` be the number of delivery rows and `c` the number of customers. A hash-based grouped minimum can scan `n` rows in `O(n)` expected time while storing one date per customer. Filtering and averaging scan or probe the rows with linear total logical work, matching the manifest's `O(n)` time.

The grouped subquery stores `O(c)` customer-date pairs, giving `O(c)` auxiliary space.

A sort-based database plan may use `O(n log n)` physical time instead, while indexes on customer and order date may improve access. The manifest describes the logical hash-aggregation bound.

## Alternatives and edge cases

- **Window function with `ROW_NUMBER`:** Partition by customer, order by date, keep row one, and average its indicator. This is explicit and also relies on or resolves tie rules.
- **Correlated minimum subquery:** Compare each row's date to a per-customer minimum. It can be concise but may repeat work without an index.
- **Average all deliveries:** Customers with later orders would be included and the result would answer version I, not version II.
- **Match only minimum date:** Different customers can share dates, so the customer identifier must be part of the comparison.
- **Two earliest orders on the same day:** The query would include both, but the contract guarantees precisely one first order per customer.
- **One customer:** The percentage is either `100.00` or `0.00` according to that first order.
- **Later immediate order after a scheduled first order:** It does not count; only the earliest order is evaluated.
- **Scheduled first order:** Its Boolean contributes zero.
- **Immediate first order:** Its Boolean contributes one.
- **No ordering requirement:** The aggregate returns one row, so final row order is irrelevant.
