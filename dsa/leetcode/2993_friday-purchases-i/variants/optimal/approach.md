## General

**Select only Fridays.** The contract fixes every date to November 2023, so
filter rows by their weekday and discard all other purchases before grouping.
The native MySQL query uses `DAYOFWEEK = 6`; SQLite represents Friday as
`strftime('%w') = '5'`.

**Aggregate each represented Friday.** Group the filtered rows by
`purchase_date` and sum `amount_spend`. Derive the one-based week number from
the day of month as $\lfloor(d-1)/7\rfloor+1$. For November 2023, the Fridays
on days 3, 10, 17, and 24 map to weeks one through four. Since grouping begins
only from existing Friday rows, weeks without purchases are naturally absent.
Ordering by the derived week completes the contract.

## Complexity detail

Let $R$ be the number of purchases. Filtering, grouping, and ordered output
take $O(R\log R)$ time in the general comparison-based model, with up to
$O(R)$ grouping state.

## Alternatives and edge cases

- **Calendar table:** Joining all November Fridays can support zero-filled reports, but this problem explicitly omits weeks without purchases.
- **Correlated date sum:** Summing the same Friday separately for every matching row is correct after `DISTINCT`, but can be quadratic.
- **Non-Friday rows:** They contribute nothing even when their week contains a Friday.
- **Multiple purchases on Friday:** Sum every row on that exact date.
- **Empty Friday week:** Do not synthesize a row with zero.
- **Month boundary:** The supplied date range is already restricted to November 2023.
