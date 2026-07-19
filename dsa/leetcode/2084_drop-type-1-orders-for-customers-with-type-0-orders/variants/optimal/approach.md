## General
**Summarize each customer's available types**

Compute `MIN(order_type)` as a window aggregate partitioned by `customer_id`. Because the only possible types are 0 and 1, a partition minimum of 0 proves that the customer has at least one preferred type 0 order. A minimum of 1 proves that every order in the partition is type 1.

**Retain rows matching the partition priority**

The window value is attached to every original row without collapsing the partition. Filter to rows where `order_type = minimum_type`. For a customer whose minimum is 0 this keeps every type 0 row and removes every type 1 row; when the minimum is 1 it keeps all rows. These are exactly the two contract branches.

**Project only the original columns**

The computed minimum is internal evidence and must not appear in the result. Select `order_id`, `customer_id`, and `order_type` from the filtered relation. Since the problem permits any order, no final `ORDER BY` is required.

## Complexity detail
A typical window implementation groups or sorts the $N$ rows by customer, taking $O(N\log N)$ time and $O(N)$ execution space. Hash-partitioned execution may be linear expected time. The exact physical plan is database-dependent, while the logical query processes each original row once after its customer minimum is known.

## Alternatives and edge cases
- **Precompute type 0 customers:** A subquery of distinct customers with type 0, followed by an anti-join for type 1 rows, expresses the same rule without a window.
- **Correlated `NOT EXISTS`:** Keep every type 0 row or a type 1 row whose customer has no type 0 row. It is correct, but an unoptimized plan can rescan `Orders` for every outer row and take $O(N^2)$ time.
- **Group and join back:** Computing `MIN(order_type)` per customer and joining to the original table is equivalent but requires an explicit second relation step.
- **Several type 0 orders:** Retain all of them, not just one representative.
- **Only type 1 orders:** Retain every order for that customer.
- **Mixed customers:** The priority decision is independent for each `customer_id`.
