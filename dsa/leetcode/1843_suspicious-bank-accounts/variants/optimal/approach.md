## General

**First label every creditor transaction with its month’s total-income status.** The common table expression `S` reads `Transactions`, left joins the matching `Accounts` row to obtain `max_income`, and filters to `type = 'Creditor'`. Debtor withdrawals must not contribute to income, so removing them before the window sum is essential.

`DATE_FORMAT(day, '%Y-%m-01')` normalizes every timestamp to a string representing the first day of its month. Using year and month together preserves calendar order across different years and makes every transaction in the same account-month share one value.

The window expression

`SUM(amount) OVER (PARTITION BY account_id, formatted_month)`

adds all creditor amounts for that account and month. Comparing the sum with `max_income` produces `marked`, a MySQL Boolean represented as one when income strictly exceeds the limit and zero otherwise. Equality is not suspicious because the contract says “exceeds.”

**The CTE retains transaction-level rows.** `S` selects `transaction_id AS tx` and uses `SELECT DISTINCT`. Since transaction identifiers are unique, rows from the same account and month do not collapse: each creditor transaction remains a separate row, although all rows in one account-month share the same normalized day and `marked` value.

This is different from an aggregated monthly CTE. It does not harm the basic existence logic, but it creates duplicate month representations and affects performance.

**Self-join adjacent months for the same account.** The outer query treats `S` as `s1` and left joins another copy `s2` when account identifiers match and

`TIMESTAMPDIFF(Month, s1.day, s2.day) = 1`.

Because both day strings denote the first of a month, a difference of one means `s2` is the immediately following calendar month, including a December-to-January transition.

The `WHERE` clause requires `s1.marked = 1 AND s2.marked = 1`. Although the syntax says `LEFT JOIN`, requiring a non-null marked value from `s2` makes it behave like an inner join for qualifying results. A row survives only when its account exceeded the threshold in its month and also in the next month.

`SELECT DISTINCT s1.account_id` collapses the many transaction pairs to one account identifier. Finding any adjacent pair is enough: “two or more consecutive months” necessarily contains at least one consecutive pair.

**Trace the sample.** Account three’s creditor transactions in June sum to 300100, above 21000, and July income 64900 is also above 21000. June rows join July rows with a one-month difference, both marked one, so account three survives. Account four exceeds in May and July but not June. May cannot join a marked June row, and June itself is unmarked, so no qualifying adjacent pair survives for account four.

**Why adjacent-pair detection is sufficient.** If an account exceeds its limit for a run of two or more consecutive months, take the first two months of that run; the self-join finds them. Conversely, any joined pair passing both marked filters witnesses exactly two consecutive over-limit months for one account. Therefore the distinct identifiers characterize suspicious accounts, assuming the query executes under the target SQL rules.

**Exact performance consequence of retaining `tx`.** Suppose an account has `x` creditor transactions in one over-limit month and `y` in the next. The CTE contains all `x + y` rows, and the self-join can produce `x * y` matching pairs for just those two months. Across the input, the intermediate join can therefore be quadratic in the number of creditor transactions. The final `DISTINCT` removes duplicate output identifiers only after this multiplication has occurred.

An aggregated CTE with one row per account-month would avoid that blowup and make the manifest’s near-sort-linear accounting more plausible. The exact source does not perform that aggregation.

**Exact ordering caveat.** The problem permits any result order, yet the query ends with `ORDER BY s1.tx` while selecting `DISTINCT s1.account_id`. `tx` is neither selected nor functionally unique per returned account after duplicate collapse. Some MySQL configurations reject an `ORDER BY` expression not present in a `SELECT DISTINCT` list; permissive behavior can still make the chosen transaction basis unclear. The ordering is unnecessary for correctness and is a portability risk in the exact SQL.

**Join-type detail.** The CTE uses a left join from transactions to accounts. Under the expected schema relationship, every transaction has a matching account and a threshold. If not, `max_income` would be null and `marked` would not become one, so such a transaction could not create a suspicious result.

## Complexity detail

Let `r` be the number of creditor transaction rows. Window partitioning normally requires sorting or equivalent grouping work, often `O(r log r)`, and stores `O(r)` rows. However, because `S` retains each transaction and the self-join pairs all rows from consecutive months, the exact query can generate `O(r^2)` intermediate rows in the worst case. Its worst-case time and intermediate-space behavior can therefore be quadratic, not the manifest’s `O(r log r)` and `O(r)`.

Database indexes, window execution, CTE materialization, and join strategy affect practical cost. Pre-aggregating to one row per account-month would bound the self-join by the number of active months instead of transaction multiplicities.

## Alternatives and edge cases

- **Monthly aggregation CTE:** Group creditor transactions by account and year-month, sum income, and retain only over-limit months before self-joining. This removes transaction-level duplication.
- **`LAG` over qualifying months:** After monthly aggregation, compare each over-limit month with the preceding month using a window function. Care is needed because filtering out nonqualifying months before checking gaps must still verify calendar adjacency.
- **`PERIOD_DIFF` self-join:** Formatting as `YYYYMM` and comparing periods is another direct way to recognize consecutive months.
- **Exactly equal to `max_income`:** The strict greater-than comparison marks it false, as required.
- **Debtor-only month:** It has no income row in `S` and cannot form an over-limit pair.
- **High months separated by a normal month:** Their month difference is two, so they do not join as consecutive.
- **December followed by January:** First-of-month normalization and `TIMESTAMPDIFF` correctly treat them as one month apart.
- **Three or more consecutive high months:** At least two adjacent pairs exist, and `DISTINCT` returns the account once.
- **Multiple transactions per month:** The window sum is correct, but the CTE repeats the month and the self-join multiplies rows.
- **No matching account row:** A null threshold prevents `marked = 1`, assuming ordinary SQL null semantics.
- **Left join in the outer query:** The marked condition on `s2` eliminates unmatched rows, so an inner join would express the effective requirement more clearly.
- **Final ordering:** Any order is allowed; `ORDER BY s1.tx` is unnecessary and can conflict with strict handling of `SELECT DISTINCT`.
