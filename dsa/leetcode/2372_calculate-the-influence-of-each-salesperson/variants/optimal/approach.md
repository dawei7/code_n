## General

**Follow the ownership chain**

The value attributed to a salesperson does not appear directly in `Salesperson`. The three tables form a chain:

```text
Salesperson -> Customer -> Sales
```

A salesperson owns zero or more customers through `Customer.salesperson_id`. Each customer may then have zero or more sales through `Sales.customer_id`. The required total for one salesperson is the sum of `Sales.price` over every sale made by every customer assigned to that salesperson.

The result must also contain salespeople who have no customers or whose customers have no sales. That requirement determines the join direction and join type.

**Begin with every salesperson**

The query starts from `Salesperson AS sp`. This makes the salesperson table the preserved side of the operation. The first join is:

```sql
LEFT JOIN Customer AS c
    ON sp.salesperson_id = c.salesperson_id
```

A left join emits matching customer rows when they exist. When a salesperson has no customer, it still emits one row containing the salesperson columns and `NULL` for the customer columns. An inner join would discard that salesperson completely, making it impossible to report the required zero.

The second join is also a left join:

```sql
LEFT JOIN Sales AS s
    ON s.customer_id = c.customer_id
```

For a customer with several sales, this expands into one joined row per sale. For a customer with no sales—or for the null placeholder produced because there was no customer—it preserves the chain with null sales columns. This second preservation is important: using an inner join here would also remove salespeople whose customers have not purchased anything.

**Aggregate all expanded rows back to one salesperson**

After the joins, one salesperson may appear on many rows: once for each sale reachable through their customers. The query groups by:

```sql
GROUP BY 1
```

In MySQL, `1` is a positional reference to the first expression in the `SELECT` list, which is `sp.salesperson_id`. It is equivalent here to `GROUP BY sp.salesperson_id`.

The selected `name` is functionally determined by the unique `salesperson_id` in the `Salesperson` table. Thus, every joined row in one group carries the same name, and returning that name alongside the aggregate is unambiguous.

Within each group, `SUM(price)` adds every non-null sale price. If one customer has multiple sales, every sale row contributes. If a salesperson has multiple customers, the rows from all those customers share the salesperson group and contribute to the same sum.

**Turn an absent sum into the required zero**

SQL's `SUM` ignores null inputs, but when a preserved salesperson group has no actual sale prices, there is no numeric value to add and `SUM(price)` returns `NULL` rather than zero. The output contract specifically requires `0`. Therefore, the query wraps the aggregate:

```sql
COALESCE(SUM(price), 0) AS total
```

`COALESCE` returns the first non-null argument. A salesperson with real sales receives the numeric sum; one with no sales receives zero. The alias `total` supplies the required output column name.

**Trace the example**

Alice owns customers `1` and `2`. Joining through those customers finds sale prices `354` and `892`. Grouping them under Alice gives `1246`.

Bob owns customer `3`, whose two sale rows have prices `988` and `856`. The join creates two Bob rows and `SUM` gives `1844`.

Jerry has no customer. The first left join preserves Jerry with a null customer, and the second preserves that row with a null price. His aggregate is null, which `COALESCE` converts to `0`. All three salespeople therefore appear exactly once.

**Why the complete query is correct**

Fix a salesperson `p`. The first join associates `p` with exactly the customers whose foreign key names `p`, while retaining a placeholder if there are none. For every associated customer, the second join associates exactly that customer's sale rows, while preserving a placeholder if there are none. Consequently, the non-null `price` values in `p`'s joined rows are exactly the prices paid by `p`'s customers.

Grouping by salesperson isolates those values from every other salesperson. `SUM` adds exactly them. If the set is empty, `COALESCE` produces the mandated zero. Because the starting table contains every salesperson and left joins never discard its rows, every salesperson receives one result group. This proves both the totals and the coverage are correct.

The final query contains no `ORDER BY` because the problem accepts any row order. Avoiding unnecessary sorting does not change the content.

## Complexity detail

Let $S$ be the number of salesperson rows, $C$ the number of customer rows, and $R$ the number of sales rows. The manifest reports $O((S+C+R)\log(S+C+R))$ time and $O(S+C+R)$ space.

A sorting-based physical plan can organize join keys and salesperson groups within that bound. Temporary joined rows, indexes or hash tables, and aggregate state may require linear working storage. Foreign-key indexes or hash joins can make actual execution closer to expected $O(S+C+R)$, while a database optimizer may stream or materialize intermediate data differently.

The SQL text specifies the logical operation, not one mandatory physical algorithm, so the manifest gives a conservative general bound. The result itself contains exactly $S$ rows.

## Alternatives and edge cases

- **Inner joins:** They incorrectly remove salespeople without customers or without completed sales, violating the zero-total requirement.
- **Correlated subquery per salesperson:** It can calculate each total but may repeat lookup work and is less direct than one joined aggregation.
- **Pre-aggregate sales by customer:** Summing per customer before joining is valid and may reduce intermediate rows, but the current query already expresses the required logic clearly.
- **`COUNT` instead of `SUM`:** Counting sales would measure transactions, not the prices paid.
- **A salesperson with no customers:** Both left joins preserve a null chain and `COALESCE` returns zero.
- **A customer with no sales:** The customer is present but contributes no numeric price; the salesperson still remains in the result.
- **Several sales by one customer:** Each sale price appears on a separate joined row and all are included.
- **Several customers per salesperson:** Grouping by salesperson merges their sale rows into one total.
- **`GROUP BY 1`:** The positional `1` refers to `sp.salesperson_id`, not a constant group shared by the whole table.
- **Output order:** No ordering is promised or needed because any order is accepted.
