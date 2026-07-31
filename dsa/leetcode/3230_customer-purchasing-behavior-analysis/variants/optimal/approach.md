## General

**Join purchases to their categories.** Start by joining `Transactions` with `Products` on `product_id`. This shared purchase relation contains every field needed by both the customer totals and category ranking. The product's listed `price` is not used because spend metrics come from the transaction's `amount`.

**Rank categories within each customer.** Group the joined rows by customer and category. For every group, compute its purchase count and latest transaction date. Apply `ROW_NUMBER` within each customer, ordering first by purchase count descending and then by latest date descending. The first row is exactly the required top category. A final category ordering makes the query deterministic if both specified criteria are identical.

**Aggregate the customer metrics once.** Independently group the joined rows by customer to compute total amount, transaction count, distinct-category count, average amount, and loyalty score. Round only the requested displayed values. Join these totals to the rank-one category and order by loyalty score descending, then customer ID ascending.

The category grouping compares all purchases under the required frequency and recency rules, while the customer grouping includes every transaction exactly once. Joining one winning category to one totals row therefore produces exactly one complete row per customer.

## Complexity detail

Let $t$ be the transaction count and $c$ the number of customer-category groups. With indexed product identifiers, the join is linear in the input size. Grouping, window ranking, and final ordering have a conservative $O(t\log t)$ time bound, while database engines may use hash aggregation or indexes to improve individual stages.

The joined relation, grouped state, window state, and sort buffers may use $O(t)$ auxiliary database storage. The output contains one row per customer.

## Alternatives and edge cases

- **Correlated top-category subquery:** Recomputing category counts separately for every customer is correct but can repeatedly scan the transaction table and approach quadratic time.
- **Pairwise anti-join of category groups:** Eliminating every category outranked by another avoids a window function, but may compare all pairs and take $O(c^2)$ time.
- **Rank raw purchases by date:** This chooses the latest category without first honoring purchase frequency.
- **Order only by category count:** Tied frequencies require the category with the latest transaction.
- **Use product price for spend:** Totals and averages must use `Transactions.amount`, not `Products.price`.
- Multiple products in the same category count as one distinct category but each purchase still increases that category's frequency.
- Repeated purchases of one product are separate transactions.
- A customer with one transaction has one unique category and that category is automatically first.
- Round total amount, average amount, and loyalty score to two decimal places.
- Loyalty score uses the unrounded total amount before the final score is rounded.
- Equal loyalty scores are ordered by ascending customer ID.
