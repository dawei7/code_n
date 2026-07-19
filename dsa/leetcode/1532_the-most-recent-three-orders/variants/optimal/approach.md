## General
**Rank orders independently within each customer**

Use `ROW_NUMBER()` partitioned by `customer_id` and ordered by `order_date DESC`. Because a customer has at most one order per day, every order receives an unambiguous rank: 1 is newest, 2 is next, and so on.

Filtering to ranks at most 3 keeps exactly the requested prefix for each customer. A group containing one or two orders has no larger rank and therefore retains all its rows; a group with no orders contributes nothing because the final relation joins from ranked orders to customers.

**Attach names and enforce the specified presentation order**

Join the ranked orders to `Customers` by `customer_id`, select only the four requested columns, and sort by customer name ascending, customer ID ascending, and order date descending. The customer-ID key matters even though IDs are unique because different customers may share a name.

Every returned order is among its customer's top three by construction. Conversely, every top-three order receives a rank from 1 through 3 and survives the filter, proving that the result neither omits nor adds an order.

## Complexity detail
Partitioned ranking may sort the $m$ order rows, for a conservative $O(m\log m)$ cost. Joining customer data contributes $O(c+m)$ expected work with indexed or hashed IDs, and the required final ordering is also bounded by $O(m\log m)$. The combined bound is $O(m\log m+c)$.

The rank and sort stages can retain $O(m)$ rows. The returned relation itself is excluded from the auxiliary-space statement.

## Alternatives and edge cases
- **Correlated count of newer orders:** retain an order when fewer than three same-customer orders have a later date. It is correct but can compare $O(m^2)$ order pairs.
- **User variables in MySQL:** session-variable ranking is version-sensitive and less declarative than a window function.
- **Aggregate maximum dates:** three separate maximum-date queries can work but become cumbersome and duplicate logic.
- **Fewer than three orders:** all available orders must be returned.
- **Exactly three orders:** every order is returned, already sorted newest first.
- **More than three orders:** only ranks 1 through 3 survive.
- **No orders:** the customer contributes no row because there is no order to report.
- **Duplicate names:** customer ID ascending breaks the name tie before dates are considered.
- **Unique daily order:** no additional order-ID tie-breaker is needed within one customer.
