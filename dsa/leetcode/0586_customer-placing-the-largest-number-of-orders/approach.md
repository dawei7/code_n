## General

The input has one row per order, not one row per customer. To discover which customer placed the most orders, the query must first turn repeated customer IDs into per-customer groups and count the rows in each group.

**One group represents one customer**

`GROUP BY customer_number` partitions all `Orders` rows according to their customer ID. If customer 3 appears in two rows, both rows belong to the same group. If customer 1 appears once, that group contains one row.

The aggregate `COUNT(1)` counts the number of rows in each group. The literal 1 is non-`NULL` for every row, so it contributes one every time. In this schema, `COUNT(*)` would give the same result. Counting `order_number` would also work because it is a non-`NULL` primary key, but `COUNT(1)` directly represents counting rows.

The query selects only `customer_number`. An aggregate used by `ORDER BY` does not have to appear in the output list, so the count can guide ranking without becoming an unwanted result column.

**Ranking groups instead of individual orders**

After grouping, the logical relation is equivalent to pairs such as:

```text
customer 1 -> 1 order
customer 2 -> 1 order
customer 3 -> 2 orders
```

`ORDER BY COUNT(1) DESC` places the group with the largest count first. Descending order is crucial; ascending order would select the customer with the fewest orders.

`LIMIT 1` retains only the first group. The input guarantee says exactly one customer has strictly more orders than every other customer. Therefore, there is no tie for first place and no secondary ordering key is needed.

The order in which SQL logically processes these clauses helps make the compact query understandable:

1. `FROM Orders` supplies individual order rows.
2. `GROUP BY customer_number` forms one group per customer.
3. `ORDER BY COUNT(1) DESC` ranks those groups by size.
4. `LIMIT 1` keeps the maximum group.
5. `SELECT customer_number` returns that group’s customer ID.

**Why a maximum of raw identifiers would be wrong**

Neither the largest `customer_number` nor the largest `order_number` says anything about how many orders a customer placed. IDs are labels. The frequency of a customer label across rows is the required measure, so aggregation must precede selection.

For the sample, the four order rows contain customer numbers 1, 2, 3, and 3. Group sizes are one, one, and two. Ordering by those sizes puts customer 3 first, and the result is the single value 3.

**Why the query is correct**

For every customer $c$ present in `Orders`, grouping creates exactly one group containing all and only rows whose `customer_number` is $c$. `COUNT(1)` therefore equals the complete number of orders placed by $c$.

Descending ordering puts any group with a greater order count before every group with a smaller count. The unique-maximum guarantee means precisely one group occupies the first position. `LIMIT 1` keeps that group, and selecting its `customer_number` returns exactly the uniquely most active customer.

No join is required because the requested identifier and all order-frequency evidence are already in `Orders`. No `DISTINCT` is required because grouping already produces one output candidate per customer.

The follow-up changes the contract. If ties were permitted and every tied leader had to be returned, `LIMIT 1` would no longer be sufficient. The exact solution is intentionally specialized to the stated unique-winner guarantee.

## Complexity detail

Let $n$ be the number of order rows and $c$ the number of distinct customers. A hash aggregation reads $n$ rows and maintains one counter per customer, taking expected $O(n)$ time and $O(c)$ space.

Sorting all $c$ groups by count costs $O(c\log c)$ time. A database optimizer can exploit `LIMIT 1` by tracking only the best group, potentially avoiding a full sort after aggregation, but a conservative conventional bound is $O(n+c\log c)$. Since $c\le n$, the manifest’s $O(n\log c)$ is a safe coarser upper bound. Working space is $O(c)$ for group counters and possible ranking state.

SQL is declarative, so indexes and optimizer choices affect the physical plan. An index on `customer_number` may permit streaming aggregation, while a hash plan may ignore ordering until after counts are built.

## Alternatives and edge cases

- **Window ranking:** Compute counts in a grouped common table expression and apply `ROW_NUMBER` ordered by count descending. This is explicit but longer for a guaranteed unique winner.
- **Maximum-count subquery:** Build customer counts, find their maximum, and return groups equal to it. This naturally solves the tie-inclusive follow-up but usually repeats or layers aggregation.
- **`RANK` for all leaders:** Use `RANK() OVER (ORDER BY order_count DESC)` and retain rank one. Unlike `LIMIT 1`, this returns every tied maximum.
- **Correlated count per customer:** Count one customer’s rows repeatedly from a distinct-customer list. Without an index, it can do much more work than one grouping pass.
- **Unique winner:** This guarantee is why an unspecified tie order is harmless. Remove the guarantee and the exact query may return an arbitrary tied leader.
- **One customer:** Its only group is necessarily the maximum and is returned.
- **One order per customer:** Such data would create a full tie, contradicting the unique-winner guarantee unless only one customer exists.
- **Multiple orders have unique IDs:** `order_number` uniqueness prevents duplicate order records under that primary key, but customer IDs are intentionally repeated.
- **Empty table:** `LIMIT 1` returns no row. The problem’s intended tests provide orders; an empty-input output policy is not otherwise specified.
- **Counting rows:** `COUNT(1)` and `COUNT(*)` are equivalent here. Counting a nullable expression could undercount and should be avoided.
- **No output ordering requirement beyond selection:** Once exactly one row remains, an additional final order is meaningless.
- **Follow-up with ties:** Replace top-one selection with a maximum comparison or rank-one filter; do not add an arbitrary customer-ID tie-breaker if the requirement is to return all leaders.
