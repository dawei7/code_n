## General

The requested people are all salespersons for whom *no* associated order belongs to a company named `RED`. This is an anti-condition: one RED order disqualifies a salesperson, while zero orders must still qualify.

The query preserves every salesperson with left joins, groups all of each person’s orders, counts RED matches through conditional summation, and retains groups whose RED count is zero.

**Why the query starts from `SalesPerson`**

`SalesPerson AS s` is the complete universe of people who may need to appear. The first left join:

```sql
LEFT JOIN Orders USING (sales_id)
```

attaches all orders for a salesperson. If none exist, the salesperson row remains and order columns become `NULL`. An inner join would discard no-order salespersons even though they clearly had no RED order and should be returned.

The second left join attaches each order’s company through `com_id`:

```sql
LEFT JOIN Company AS c USING (com_id)
```

Foreign keys guarantee valid IDs for real orders. The left form continues preserving the already retained salesperson row when there is no order.

**Collapsing all orders per salesperson**

`GROUP BY sales_id` creates one group per salesperson after joining. A person with several orders has several joined rows in the same group; a person with no orders has one synthetic left-join row.

Selecting `s.name` is sound because `sales_id` is the primary key of `SalesPerson`, so it determines exactly one name. Some SQL systems require the name in the grouping list for strict portability, but MySQL recognizes the functional dependency.

**Counting RED orders with a Boolean sum**

In MySQL, `c.name = 'RED'` behaves as one for a RED company and zero for another non-null company name. Summing it gives the number of RED-related joined order rows.

Three cases matter:

- at least one RED order: the sum is positive;
- orders exist, but none target RED: every comparison is zero, so the sum is zero;
- no orders: `c.name` is `NULL`, comparison is `NULL`, and `SUM` over only null values returns `NULL`.

The predicate:

```sql
HAVING COALESCE(SUM(c.name = 'RED'), 0) = 0
```

maps the no-order null sum to zero. Therefore, both “no orders” and “only non-RED orders” qualify, while any RED order disqualifies the entire group.

`HAVING` is the correct clause because the decision depends on an aggregate over all rows in a salesperson’s group. A row-level `WHERE c.name != 'RED'` would be wrong: a salesperson with one RED and one GREEN order would retain the GREEN row and falsely appear eligible.

**Tracing the sample**

John’s group contains a RED order, so its sum is one and fails. Pam has a YELLOW order and a RED order; comparisons sum to one, so she also fails despite having a non-RED order. Alex has a GREEN order only, giving zero and passing. Amy and Mark have no joined orders, so `COALESCE` turns each null sum into zero and both pass.

**Why the query is correct**

For each salesperson, left joining guarantees one group whether or not orders exist. Each actual RED order contributes one to that group’s sum, while each non-RED order contributes zero. Thus, the sum is positive if and only if the salesperson has at least one RED order; after null replacement, it is zero if and only if no RED order exists.

The `HAVING` equality retains exactly the latter groups. Selecting their names returns every and only salesperson required by the problem. Multiple RED orders do not change the Boolean decision: any positive sum is excluded.

No output order is required, so no sorting clause is necessary.

## Complexity detail

Let $S$, $O$, and $C$ be row counts for `SalesPerson`, `Orders`, and `Company`. With hash/indexed joins, processing can be expected linear in $S+O+C$, followed by grouping over joined rows. Sort-based joins or aggregation can require $O((S+O+C)\log(S+O+C))$, matching the conservative manifest.

Materialized join rows, hashes, or group state can use $O(S+O+C)$ working space. Suitable primary/foreign-key indexes may reduce temporary work. SQL specifies relations rather than a fixed physical plan.

The result has at most $S$ names.

## Alternatives and edge cases

- **`NOT EXISTS` correlated subquery:** For each salesperson, reject if an order joined to company RED exists. It directly expresses the anti-condition and can short-circuit after one match.
- **`NOT IN` of RED salesperson IDs:** Works when the subquery cannot return `NULL`. `NOT EXISTS` is safer under nullable data.
- **Filter non-RED rows in `WHERE`:** Incorrect because it can hide a RED row while leaving another order from the same salesperson.
- **Inner join:** Incorrectly removes salespersons with no orders.
- **One RED among many orders:** Positive Boolean sum excludes the salesperson.
- **Only non-RED orders:** Sum is zero and the salesperson qualifies.
- **No orders:** Left join preserves the person; null sum becomes zero.
- **Several companies named RED:** Every matching order contributes one; the condition still behaves correctly.
- **Duplicate names:** Selection is by salesperson groups, so distinct people with the same display name may yield repeated name values; do not add `DISTINCT` without a requirement.
- **Functional dependency:** Grouping by primary key `sales_id` determines `s.name` in MySQL.
- **No required order:** Avoid unnecessary `ORDER BY`.
- **Why `COALESCE` matters:** `NULL = 0` is unknown, so no-order groups would otherwise fail the `HAVING` test.
