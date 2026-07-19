## General
**Reduce deposits to monthly totals**

Filter `Transactions` to `type = 'Creditor'` before aggregation so withdrawals cannot inflate or reduce income. Convert each timestamp to its year-month period and group by both `account_id` and that period. Summing `amount` now produces exactly one income total per active account-month.

Join those monthly rows with `Accounts` and keep only totals strictly greater than the corresponding `max_income`. This creates a compact relation containing precisely the over-limit months; months with no creditor transactions and months at or below the threshold are absent.

**Detect adjacent periods**

Self-join the over-limit relation by `account_id`. Require the second period to be exactly one calendar month after the first, using `PERIOD_DIFF`. This arithmetic treats December followed by January as adjacent and rejects equal months or gaps such as January followed by March.

Every output row witnesses two consecutive over-limit months, so every reported account is suspicious. Conversely, the definition guarantees that a suspicious account has at least one adjacent pair in the filtered relation, which the self-join finds. `DISTINCT` returns that account only once even when a longer run contains several adjacent pairs.

## Complexity detail
Grouping and database ordering of $r$ transactions takes $O(r\log r)$ time in the general execution model. Joining the grouped month rows and deduplicating the result remain within that bound. The monthly relation and join state use $O(r)$ space in the worst case, when every transaction belongs to a different account-month.

## Alternatives and edge cases
- **Window `LAG`:** Order qualifying months per account and compare each period with its predecessor; this is equally valid but still requires explicit calendar-month arithmetic.
- **Correlated monthly sums:** Recompute an account-month total for many transaction rows; without supporting indexes this can revisit $O(r^2)$ row pairs.
- **Day difference:** Comparing timestamps by a fixed number of days is wrong because calendar months have different lengths.
- **Strict threshold:** Income equal to `max_income` does not qualify.
- **Withdrawals:** `Debtor` amounts never contribute to monthly income.
- **Multiple deposits:** Sum all creditor transactions in the same account-month before comparing with the threshold.
- **Missing month:** Two over-limit months separated by a non-qualifying or absent month are not consecutive.
- **Year boundary:** December and the following January are consecutive.
- **Long runs:** Three or more consecutive qualifying months still produce the account only once.
- **Any output order:** No final ordering is required by the contract.
