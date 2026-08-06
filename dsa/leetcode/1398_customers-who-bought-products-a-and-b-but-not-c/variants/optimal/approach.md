## General

**Reduce each order history to three presence tests.** Join `Customers` to `Orders` by `customer_id`, then group the joined rows by both selected customer columns. Each group now contains exactly one customer's purchases. Within that group, the expression

```sql
SUM(CASE WHEN o.product_name = 'A' THEN 1 ELSE 0 END)
```

counts A orders; the corresponding expressions do the same for B and C. Requiring the A and B counts to be positive implements the two existential conditions, while requiring the C count to equal zero proves that no disqualifying C row exists. Purchases of every other product contribute zero to all three sums.

**Emit one source customer row.** Aggregation collapses any number of repeated purchases into one group, so a qualifying customer appears exactly once. Grouping by `customer_id` and `customer_name` also keeps the returned name attached to the correct customer instead of deriving it from order data. The inner join safely omits customers without orders because they cannot satisfy both required-product conditions. Finally, sorting by `customer_id` produces the exact required order.

This establishes both directions of the filter: every emitted group contains A and B and contains no C, and every customer with those three properties has positive A and B sums, a zero C sum, and therefore survives `HAVING`.

## Complexity detail

Let $C$ be the number of customer rows, $O$ the number of order rows, and $R$ the number of returned customers. With an indexed or hash join and hash aggregation, reading the inputs, maintaining at most one group per customer, and emitting the result takes $O(C + O + R)$ time and $O(C)$ working space. A particular database plan may add sorting work to implement grouping or the required final order.

## Alternatives and edge cases

- **Three correlated predicates:** Separate `EXISTS` checks for A and B plus `NOT EXISTS` for C express the contract directly, but can rescan `Orders` for every customer and take $O(CO)$ time without useful indexes.
- **Self-join order aliases:** Joining A and B order subsets and anti-joining C can work, but repeated purchases may multiply intermediate rows unless they are deduplicated first.
- **Set cardinality alone:** Counting distinct names among A, B, and C is insufficient because `{A,B}` and `{A,C}` both have cardinality two; the individual presence and absence conditions matter.
- **Repeated A or B purchases:** Any positive count satisfies the corresponding requirement, and grouping still emits one customer row.
- **One C purchase:** A single C order makes the C sum positive and disqualifies the customer regardless of all other purchases.
- **Other products:** Product names outside A, B, and C contribute zero and neither qualify nor disqualify a customer.
- **Missing A or B:** Buying only one required product cannot pass both positive-count predicates.
- **No orders:** The inner join omits the customer, which is correct because neither required product was purchased.
- **Duplicate customer names:** Qualification and grouping are customer-ID-specific; equal names must not merge different customers.
