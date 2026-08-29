## General

**Rank transactions inside day groups.** The query uses a window function to compare each transaction with other rows assigned to the same group. The common table expression `T` selects the transaction identifier and computes

`RANK() OVER (PARTITION BY DAY(day) ORDER BY amount DESC)`.

Within each partition, ordering amounts in descending order places the greatest amount first. `RANK` assigns rank one to that first amount. If several transactions tie for the maximum, they all receive rank one, because `RANK` gives equal ordering values the same rank. This is exactly the tie-preserving behavior the result needs; `ROW_NUMBER` would arbitrarily keep only one tied transaction.

The outer query reads the ranked rows from `T` and retains `rk = 1`. It selects only `transaction_id`, then `ORDER BY 1` sorts by the first selected output column, which is the identifier. MySQL’s default direction is ascending, so this implements the requested final identifier order.

**Understand the intended grouping key.** Conceptually, transactions must be partitioned by their full calendar date. Time-of-day should be ignored, while year, month, and day must all remain significant. With the correct date grouping, the window has a useful row-level invariant: `rk = 1` exactly when no transaction on that same calendar date has a greater amount.

For the sample, every timestamp lies in April 2021. The day-of-month values three, 28, and 29 happen to identify the calendar dates uniquely. The partitions therefore contain transaction 8 alone, transactions 9 and 5 together, and transactions 1 and 6 together. Descending rank keeps 8, keeps 5 over 9, and keeps both 1 and 6 because they tie at 58. The final sort produces identifiers 1, 5, 6, and 8.

**Material exact-code mismatch: `DAY(day)` is not a full date.** In MySQL, `DAY(datetime_value)` returns only an integer from one through 31 representing the day of the month. It discards the month and year. Therefore the exact solution does not always form the calendar-date groups required by the description. It combines, for example, a transaction on 2021-04-03 and another on 2021-05-03 into the same partition merely because both occur on the third day of a month.

This is not a cosmetic distinction. Suppose transaction 1 occurs on April 3 with amount 50 and transaction 2 occurs on May 3 with amount 80. Each is the only transaction on its own calendar date, so both identifiers should be returned. The exact query places both rows in partition three, ranks amount 80 first and amount 50 second, and incorrectly returns only transaction 2.

The described technique satisfies the contract only if an unstated data condition guarantees that all timestamps share the same month and year, or otherwise guarantees that no day-of-month repeats across calendar dates. No such condition appears in the local description. To match the stated contract generally, the partition expression would need to preserve the full date, such as `PARTITION BY DATE(day)`. This approach document explains the checked-in SQL exactly and therefore cannot claim full correctness for cross-month or cross-year input.

**Why window ranking is otherwise the right operation.** If the partition key were the full date, every row would remain visible while being annotated with its relative amount rank. That is useful because the output needs original transaction identifiers, not one aggregated row per date. A plain `GROUP BY` with `MAX(amount)` would find the amount but would require a join or correlated comparison to recover every tied identifier. The window function performs the comparison without collapsing rows.

**Why `RANK` rather than `DENSE_RANK` or `ROW_NUMBER`.** Both `RANK` and `DENSE_RANK` would work when the query filters only rank one: each gives rank one to every tied maximum. Their different handling of ranks after a tie never affects the filter. `ROW_NUMBER` is different because it assigns distinct sequence numbers even to equal amounts and would keep only one maximum row. The current choice is therefore tie-safe.

**Logical execution flow.** It is helpful to read the query in two stages:

1. The common table expression scans `Transactions`, assigns each row to its `DAY(day)` partition, sorts by amount within that partition, and attaches `rk`.
2. The outer query discards every row whose rank is not one, projects the identifier, and globally sorts those surviving identifiers.

The output ordering is independent of the ranking order. Amount descending determines winners inside partitions; identifier ascending determines presentation after winners have been found.
For any fixed day-of-month partition, descending `RANK` gives rank one to exactly those rows whose amount equals the maximum amount in that partition. Filtering `rk = 1` therefore returns every tied maximum and no lower amount for each integer day-of-month group. Sorting by the selected identifier then puts that exact result in ascending order.

That proof is precise about what the code actually does. It is not a proof of the stated full-date requirement because separate dates sharing a day number can interfere. The ranking and filtering mechanics are sound; the grouping expression loses necessary information.

## Complexity detail

Let `r` be the number of rows in `Transactions`. A database typically sorts rows by partition key and descending amount to evaluate this window specification. The usual upper bound is `O(r log r)` time, followed by linear filtering and output sorting. Because the final `ORDER BY transaction_id` may require another sort of up to `r` surviving rows, the overall asymptotic bound remains `O(r log r)`.

Window evaluation and sorting may require `O(r)` working space, although the optimizer can use indexes, external sort files, or engine-specific execution strategies. The common table expression is a logical relation; whether it is physically materialized is a MySQL optimizer decision. The result itself can contain up to `r` identifiers when every row is a winner in its group.

Complexity does not repair the grouping mismatch: using `DAY(day)` and using `DATE(day)` have similar asymptotic costs, but they form different partitions and can return different rows.

## Alternatives and edge cases

- **Full-date window partition:** `PARTITION BY DATE(day)` preserves year, month, and day while ignoring time. It is the direct correction needed for the stated calendar-date contract.
- **Aggregate and join:** Compute each full date’s maximum amount, then join it back to `Transactions` on date and amount. This naturally retains all ties but requires an additional relational stage.
- **Correlated `NOT EXISTS`:** Keep a transaction when no row on the same full date has a greater amount. It also avoids `MAX()` for the follow-up, though indexing strongly affects performance.
- **Self anti-join:** Left join each row to a same-date row with a larger amount and retain rows with no match. This answers the follow-up without `MAX()` but needs careful date comparison and can create many intermediate pairs.
- **`DENSE_RANK`:** Filtering dense rank one gives the same winners as `RANK` because both preserve maximum ties.
- **`ROW_NUMBER`:** This is unsuitable when maximum amounts tie because only one tied row receives row number one.
- **Several maxima on one date:** `RANK` assigns one to all of them, so all identifiers survive.
- **Only one transaction on a date:** It is automatically the maximum and receives rank one.
- **Same day-of-month in different months:** The exact `DAY(day)` expression incorrectly merges these calendar dates and may discard valid winners.
- **Same day-of-month in different years:** The same defect occurs because the year is also discarded.
- **Different times on the same calendar date:** They should be grouped together; both `DAY(day)` and `DATE(day)` do that, but only `DATE(day)` also separates other months and years.
- **Output order:** `ORDER BY 1` refers to `transaction_id` in this one-column projection and sorts ascending by default, though spelling out the column name is more explicit for readers.
- **Null timestamps:** The local schema does not state a null rule. If nulls were possible, their partition behavior would require a separate contract decision rather than an assumption.
