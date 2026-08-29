## General

Approved transactions and chargebacks are dated by different events. An approved metric belongs to the transaction’s original month, while a chargeback metric belongs to the chargeback’s month. The exact query converts both event types into one five-column stream with a common `state` label, then performs one grouped conditional aggregation.

**Preserve original transaction rows**

The first branch of CTE `T` is `SELECT * FROM Transactions`. In the documented column order, each row contributes `id`, `country`, its original `state`, `amount`, and the transaction `trans_date`.

Approved rows will later contribute to approved metrics. Declined rows contribute zero to all four requested aggregates, but keeping them temporarily is harmless because the final `HAVING` removes groups with no approved or chargeback amount.

Relying on `SELECT *` also relies on the table’s column order matching the second branch. Listing columns explicitly would make the union contract more robust.

**Create one pseudo-transaction per chargeback**

The second branch joins `Transactions AS t` to `Chargebacks AS c` on `t.id = c.trans_id`. The transaction row supplies country and amount; the chargeback row supplies its own event date.

It selects:

`id, country, 'chargeback', amount, c.trans_date`.

The literal state `'chargeback'` distinguishes this event from original approved and declined rows. The foreign-key relationship guarantees that the referenced transaction information exists.

This correctly attributes a June chargeback for a May transaction to June while retaining the original amount and country.

**Understand the exact union choice**

The two branches use `UNION`, which performs duplicate elimination, rather than `UNION ALL`. Original transaction states are limited to `'approved'` and `'declined'`, so an original row cannot be identical to a synthetic `'chargeback'` row.

Duplicate elimination could matter among chargeback rows if identical entries for the same transaction and date were allowed. The exact query would combine them into one pseudo-row. Correctness therefore relies on the source semantics treating such duplicate chargeback facts as absent or irrelevant. The editorial’s `UNION ALL` approach preserves every event and is generally safer when duplicate events are meaningful.

**Aggregate by the event month and country**

`DATE_FORMAT(trans_date, '%Y-%m')` normalizes whichever event date the unified row carries. `GROUP BY 1, 2` groups by that formatted month and country.

MySQL Boolean comparisons produce one for true and zero for false. Therefore:

- `SUM(state = 'approved')` counts approved rows.
- `SUM(IF(state = 'approved', amount, 0))` totals approved amounts.
- `SUM(state = 'chargeback')` counts synthetic chargeback rows.
- `SUM(IF(state = 'chargeback', amount, 0))` totals chargeback amounts.

Declined rows contribute zero to every metric. They remain useful only insofar as the unified stream is simple; they do not create reported rows by themselves.

**Remove groups whose requested metrics are all zero**

The query ends with `HAVING approved_amount OR chargeback_amount`. In MySQL, numeric zero is false and a nonzero amount is true. A group is retained when at least one of the two amount totals is nonzero.

Under the usual positive-amount data model, this is equivalent to retaining groups with an approved or chargeback count. If zero-amount events were legal and still needed to be counted, this predicate could incorrectly remove a group with positive counts but zero totals. A more direct all-zero test would include both count aliases.

For the example’s September group, the synthetic chargeback row carries the September date and amount 5000. There is no September approved row, so approved metrics are zero while chargeback metrics are one and 5000. The `HAVING` keeps it.

**Why successful groups contain the right metrics**

Every approved source transaction appears with its original date and amount. Every chargeback pseudo-row appears with its chargeback date and referenced amount. Conditional aggregation routes each row to exactly its event type’s pair of metrics, and month-country grouping puts it in exactly the required result row. Declined-only rows add zeros and are filtered.

## Complexity detail

Let $t$ be the number of transactions, $c$ the number of chargebacks, and $g$ the number of output groups.

Scanning transactions and joining chargebacks through the transaction ID can be $O(t+c)$ with suitable indexing. However, duplicate-eliminating `UNION` generally requires hashing or sorting up to $t+c$ rows. A sort-based implementation can take $O((t+c)\log(t+c))$ time, while a hash-based distinct step has expected linear time.

The final grouping similarly uses expected $O(t+c)$ hash work or sort-based overhead. Thus the manifest’s $O(t+c)$ time describes favorable hash/index execution; the exact SQL’s `UNION` can introduce a logarithmic physical-plan cost.

Unified-row and grouping state can require $O(t+c+g)$ memory or temporary storage, depending on materialization. A streaming plan may use less. The result itself uses $O(g)$ space.

## Alternatives and edge cases

- **`UNION ALL` two preaggregated streams:** Aggregate approved transactions and chargebacks separately, union their metrics, then sum by month and country. This preserves duplicate events and can reduce intermediate rows.
- **Full outer join of aggregates:** Combine the two month-country aggregate tables while keeping groups present on only one side. MySQL requires emulating a full outer join.
- **Chargeback month differs from transaction month:** The synthetic row deliberately uses `c.trans_date`, so the metrics appear in the chargeback month.
- **Chargeback of a declined transaction:** It still counts because the chargeback branch does not require original approval.
- **Declined-only month-country group:** All requested metrics are zero and `HAVING` removes it.
- **Only chargebacks in a reported month:** Approved metrics are zero, while chargeback metrics keep the row.
- **Zero amount:** The exact amount-based `HAVING` assumes positive relevant amounts. Count-based conditions are safer if zero-amount events are valid.
- **Duplicate chargeback facts:** `UNION` removes identical synthetic rows. Use `UNION ALL` when each duplicate row represents a distinct event.
- **Column-order dependence:** `SELECT *` must align with the five expressions in the second branch. Explicit columns are safer for schema evolution.
- **Any output order:** No `ORDER BY` is needed because the contract accepts arbitrary row order.
