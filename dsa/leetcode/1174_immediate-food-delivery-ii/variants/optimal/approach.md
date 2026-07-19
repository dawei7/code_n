## General
**Find one earliest date per customer.** Group `Delivery` by `customer_id` and compute `MIN(order_date)`. The distinct-date guarantee means the pair `(customer_id, first_date)` identifies exactly one delivery row for every customer.

**Restrict the percentage to those rows.** Keep a delivery only when its `(customer_id, order_date)` pair appears in the grouped result. This prevents later orders from influencing the calculation, even when a later order has a different immediate-or-scheduled classification.

**Aggregate the retained indicators.** For each first order, a `CASE` expression contributes `1.0` when the two dates match and `0.0` otherwise. Its average is the fraction of customers whose first order is immediate. Multiply by `100.0`, round to two decimal places, and expose the required `immediate_percentage` alias.

## Complexity detail
Logically, grouping and filtering process the $n$ delivery rows a constant number of times, for $O(n)$ time with hash aggregation. The grouped first-date relation stores one entry for each of the $c$ customers, using $O(c)$ auxiliary space. A database engine may instead choose sorting or indexed access with different physical costs.

## Alternatives and edge cases
- **Window `ROW_NUMBER`:** Partitioning by customer and ordering by `order_date` also isolates the first row, but generally introduces an explicit sort unless a supporting index exists.
- **Correlated minimum subquery:** Comparing every row to a per-row `MIN(order_date)` is concise, but without a suitable index it can rescan the table for every delivery and take $O(n^2)$ time.
- **Later immediate order:** It must be ignored when an earlier scheduled order exists for that customer.
- **Later scheduled order:** It does not change a customer's contribution when the first order was immediate.
- **One-order customer:** That sole row is necessarily the customer's first order.
- **Repeated customers:** The denominator is the number of customers, not the total number of deliveries.
