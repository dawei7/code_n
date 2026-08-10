## General

**Enrich every transaction with its product category.** CTE `T` joins `Transactions` to `Products` by `product_id`. Each resulting row contains transaction facts—customer, date, amount—and the corresponding category. The product price is available through `SELECT *` but is not used; loyalty is based on actual transaction amount.

The inner join relies on the product ID relationship being complete. A transaction whose product has no catalog row would disappear.

**Find category statistics at customer-category grain.** CTE `P` groups `T` by `customer_id` and `category`. It computes:

- `cnt = COUNT(1)`, the number of that customer's transactions in the category;
- `max_date = MAX(transaction_date)`, the most recent such purchase.

These are exactly the two ordering criteria for selecting a top category: highest frequency first, then most recent activity.

**Rank categories independently for each customer.** CTE `R` applies

`RANK() OVER (PARTITION BY customer_id ORDER BY cnt DESC, max_date DESC)`.

Partitioning resets ranks for each customer. Descending count gives rank one to the most frequently purchased category. When counts tie, descending latest date favors the category with the most recent transaction.

`R` retains only customer, category, and rank because the final aggregation needs the chosen category label, not its intermediate count/date.

**Attach the top category while aggregating all customer transactions.** The final query joins every `T` row to `R` on customer ID and restricts `r.rk = 1`. Under the intended assumption that one category has rank one, each transaction row is paired with that one category label.

Grouping by `t.customer_id` then computes:

- `SUM(amount)` for total spending;
- `COUNT(1)` for transaction count;
- `COUNT(DISTINCT t.category)` for number of purchased categories;
- `AVG(amount)` for average transaction amount;
- the joined `r.category` as `top_category`.

The total and average are rounded to two decimals only after aggregation.

**Compute loyalty from unrounded aggregates.** The expression

`COUNT(1) * 10 + SUM(amount) / 100`

adds ten points per transaction and one loyalty point per $100$ of total spending. `ROUND(..., 2)` produces `loyalty_score`. It uses the aggregate sum directly, not the already rounded display alias, avoiding extra rounding error.

**Order by the requested priorities.** `ORDER BY 7 DESC, 1` refers to the seventh selected column, loyalty score, and then first column, customer ID. Scores descend; IDs ascend by default. Positional ordering matches the current select list but is fragile if columns move.

**Trace customer 101.** The joined rows have categories A, B, and C, one transaction each. `P` assigns count one to all, while C has the most recent date. `R` makes C rank one. The final customer group sums $450$, counts three transactions and three categories, averages $150$, carries C as top category, and computes $30+4.5=34.5$ loyalty points.

**A material tie defect in the exact query.** `RANK` gives the same rank to rows tied on every ordering expression. If two categories for one customer have equal `cnt` and equal `max_date`, both receive `rk=1`. The final join matches every transaction to both rank-one rows. This multiplies transaction rows, inflating `SUM(amount)`, `COUNT(1)`, and loyalty score; `r.category` is also ambiguous under grouping only by customer.

The statement says a frequency tie is broken by most recent transaction, but does not specify a further rule when latest dates also tie. Even if either category label were acceptable, multiplying aggregates is not. The exact source is correct only when the first two criteria produce a unique top category per customer or the data has a hidden uniqueness guarantee.

**Grouping-mode dependence.** The final query selects `r.category` while grouping only by customer ID. If exactly one rank-one category exists per customer, it is functionally constant in the joined group. Some MySQL modes may not infer that dependency and can reject the query under strict `ONLY_FULL_GROUP_BY` rules. The accepted target environment permits it.

## Complexity detail

Let $t$ be the transaction count and $g$ the number of customer-category groups. The product join is typically $O(t)$ expected with indexed product IDs. Grouping into `P` can be $O(t)$ by hashing or $O(t\log t)$ by sorting. Window ranking requires ordering $g$ rows within customer partitions, bounded by $O(g\log g)$. The final join/group and result ordering add linear-to-sort costs.

The manifest's broad $O(t\log t)$ time and $O(t)$ space bounds cover common plans because $g\le t$. Intermediate CTEs, grouping state, ranking sort data, and the final aggregation may occupy $O(t)$-scale working space. Actual SQL cost depends on indexes, CTE materialization, and the optimizer.

## Alternatives and edge cases

- **`ROW_NUMBER` with a deterministic final key:** Order by count, latest date, then category (or another specified key) and keep row one. This prevents multiple top rows and aggregate multiplication.
- **Aggregate customer totals before joining the winner:** Build one CTE for customer metrics and another for exactly one top category, then join their one-row-per-customer results. This isolates totals from category-ranking multiplicity.
- **`DENSE_RANK`:** It has the same rank-one tie problem as `RANK` and does not fix the defect.
- **One transaction:** Its category is top, total equals average, and transaction count is one.
- **Frequency tie with different dates:** The latest category uniquely ranks first as intended.
- **Tie on count and latest date:** Multiple rank-one rows multiply final aggregates in the exact source.
- **Several products in one category:** They contribute to the same customer-category frequency.
- **Repeated product purchases:** Every transaction counts; the metric is purchase frequency, not distinct products.
- **Unique categories:** `COUNT(DISTINCT t.category)` avoids counting repeated purchases as new categories.
- **Catalog price:** It is correctly ignored because reported spending uses transaction `amount`.
- **Missing product row:** Inner join removes the transaction, relying on referential integrity.
- **Rounding:** Total, average, and loyalty are rounded independently after their underlying aggregates.
- **Output ties:** Equal loyalty scores are ordered by ascending customer ID.
- **Positional order references:** `7` and `1` depend on select-list layout and are less maintainable than explicit aliases.
- **Strict grouping mode:** Selecting top category outside `GROUP BY` may rely on permissive MySQL behavior or inferred functional dependence.
