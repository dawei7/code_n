## General

**Separate invoice selection from line-item output**

The requested result is not one summary row. It is every purchased product line belonging to the winning invoice, with each line's extended price. Before those lines can be returned, the query must determine which invoice has the largest *total* value. The solution uses two common table expressions to separate these stages:

- `P` enriches every purchase line with its product's unit price.
- `T` aggregates those enriched lines, orders invoice totals according to the rules, and keeps the single winning invoice.

The final query joins the winner back to `P` to recover all of its detail rows.

**Enrich each purchase with its unit price**

`Purchases` contains `invoice_id`, `product_id`, and `quantity`, but the unit `price` lives in `Products`. The first CTE performs:

```sql
Purchases JOIN Products USING (product_id)
```

An inner join is appropriate because each purchase line refers to a product whose price is required. `USING (product_id)` matches equal identifiers and exposes one shared `product_id` column rather than two separately qualified copies.

After this join, every logical row in `P` has the invoice, product, quantity, and unit price needed for both total calculation and final output. The name `P` is local to the SQL query; it should not be confused with a complexity variable.

**Compute one total per invoice**

For one purchase row, `price * quantity` is the total price of that product line. Summing this product over all rows sharing an invoice gives that invoice's full amount:

```sql
SELECT invoice_id, SUM(price * quantity) AS amount
FROM P
GROUP BY invoice_id
```

Grouping only by `invoice_id` is correct because the goal at this stage is one total per invoice, not one total per product. The source table's primary key `(invoice_id, product_id)` guarantees at most one line for a particular product within an invoice, though the sum would remain correct even if lines were repeated.

**Apply both winner rules in the proper order**

The winning invoice is selected with:

```sql
ORDER BY 2 DESC, 1
LIMIT 1
```

The positional reference `2` means the second selected expression, `amount`, and `DESC` places the greatest total first. Positional reference `1` means `invoice_id` and uses ascending order by default. Therefore, invoices are ranked by decreasing amount and, among equal amounts, increasing identifier. `LIMIT 1` retains exactly the required winner.

Both ordering keys are necessary. Ordering only by amount would leave a tied result nondeterministic. Ordering invoice IDs descending would choose the opposite of the required tie-break.

**Recover all lines of the selected invoice**

CTE `T` contains only one row with the winning `invoice_id` and its total `amount`. The final

```sql
P JOIN T USING (invoice_id)
```

filters `P` to rows whose invoice matches that winner. Since `T` contains one invoice, every line from that invoice survives and all other invoices disappear.

The output expressions are `product_id`, `quantity`, and:

```sql
(quantity * price) AS price
```

This final `price` is the extended price for that line, not the unit price originally stored in `Products`. The alias deliberately gives the computed expression the output column name required by the problem.

The query does not select `invoice_id` or the aggregate `amount` because neither belongs in the requested detail table. It also omits `ORDER BY` in the final query because the output rows may appear in any order.

**Trace the example**

For invoice `2`, the enriched rows contain product `2` with unit price `200` and quantity `3`, plus product `1` with unit price `100` and quantity `4`. The grouping CTE computes:

$$
3\cdot200+4\cdot100=1000.
$$

Invoice `4` also totals `1000`. Ordering by total descending ties them, then ordering `invoice_id` ascending places invoice `2` first. The final join returns invoice `2`'s two enriched rows and computes line prices `600` and `400`.

**Why the query is correct**

The product join attaches the unique correct unit price to every purchase line. Thus, `price * quantity` is exactly that line's contribution to its invoice. Grouping and summing by invoice produces the exact total for every invoice.

The ordered one-row CTE chooses the invoice maximizing that total and uses the smallest identifier for ties, precisely matching the selection contract. Joining that identifier back to all enriched lines returns every and only line belonging to the selected invoice. Finally, multiplying each surviving quantity by its attached unit price produces the required per-product line price. Each stage therefore preserves the meaning needed by the next, establishing correctness of the full query.

## Complexity detail

Let $N_P$ be the number of rows in `Products` and $N_R$ the number of rows in `Purchases`. The variant manifest states $O((N_P+N_R)\log(N_P+N_R))$ time and $O(N_P+N_R)$ space.

A database may build an index or hash structure for the product join, materialize the enriched CTE, aggregate purchase rows, and sort the invoice summaries. In a conservative sorting-based model, these operations fit within $O((N_P+N_R)\log(N_P+N_R))$ time. Materialized joined rows, aggregation state, and sorting workspaces use linear space.

If indexes and hash aggregation are available, an actual MySQL plan may approach linear expected time, and sorting only the number of distinct invoices can be smaller than sorting every input row. Conversely, whether a CTE is materialized or inlined is an optimizer decision. The manifest bound is a safe high-level description rather than a promise of one physical plan.

The final output size equals the number of product lines in the winning invoice and is at most $N_R$.

## Alternatives and edge cases

- **Window functions:** Compute invoice totals with a window sum and rank invoices, then filter the winning rank. This can be correct but may repeat totals on every detail row and requires careful tie ordering.
- **Correlated subqueries:** Recomputing totals while filtering individual lines is usually harder to read and may repeat aggregation work.
- **`MAX(amount)` alone:** It identifies the highest total but does not select the smallest `invoice_id` among ties without additional logic.
- **Tie between invoices:** `ORDER BY amount DESC, invoice_id` guarantees that the smallest identifier wins.
- **One invoice only:** Its aggregate row is first automatically, and all its detail lines are returned.
- **One product line in the winner:** The invoice total and returned line price are the same `quantity * price` value.
- **Products absent from purchases:** The inner join contributes no rows for them, which is correct because they belong to no invoice.
- **Output ordering:** The final rows are intentionally unordered because any order is accepted.
- **Unit versus extended price:** The source `Products.price` is per unit; the returned `price` is multiplied by `quantity` for that invoice line.
- **Positional ordering references:** `2` means `amount` and `1` means `invoice_id` within CTE `T`; they are not numeric constants used to rank every row equally.
