## General

**Make missing Fridays explicit.** Construct a four-row calendar containing
November 3, 10, 17, and 24 with week numbers one through four. Starting from
this calendar guarantees that every required output week exists even when the
purchase table has no matching row.

**Attach and aggregate purchases.** Left join `Purchases` by exact date, group
each calendar row, and sum `amount_spend`. A Friday without matches still has
its calendar row; `SUM` is null there, so `COALESCE` converts it to zero.
Finally, order by the stored week number. Matching by date prevents weekday
purchases in the same week from affecting the Friday total, and the calendar
proves that the result contains exactly the required four dates.

## Complexity detail

Let $R$ be the number of purchases. The four-row calendar is constant-sized.
The join, grouping, and ordering take $O(R\log R)$ time in the general
comparison-based model and at most $O(R)$ auxiliary state.

## Alternatives and edge cases

- **Recursive date generation:** Advancing from November 3 by seven days is equivalent, but a fixed four-row calendar is clearer for this fixed contract.
- **Correlated Friday sums:** Computing a date total separately for every represented purchase is correct after deduplication but can be quadratic.
- **No purchases at all:** All four calendar rows still return with zero totals.
- **Non-Friday purchases:** They match no calendar date and contribute nothing.
- **Multiple Friday purchases:** Sum every row sharing that exact Friday date.
- **Zero-valued purchase:** It participates normally and does not remove the Friday row.
