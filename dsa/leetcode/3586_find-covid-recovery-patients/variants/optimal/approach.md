## General

The recovery definition has two dependent minima. First determine the earliest `Positive` date for every patient by filtering `covid_tests`, grouping by `patient_id`, and applying `MIN(test_date)`. This produces at most one anchor row per patient.

Join those anchors back to `covid_tests`, restricting the joined rows to `Negative` results whose `test_date` is strictly greater than the anchor. Group again and take the minimum joined date. Patients without a qualifying later negative disappear through the inner join, while earlier negatives, same-date negatives, and inconclusive results cannot enter the aggregate.

Join each surviving recovery interval to `patients`, compute the calendar-day difference between its two dates, and project the required demographic columns. Ordering by that difference and then by `patient_name` implements both specified sort keys. Because each minimum is computed once as a set operation, multiple infection cycles do not replace the first positive or the first recovery following it.

## Complexity detail

Let $T$ be the number of test rows and $P$ the number of patient rows. Without assuming supporting indexes, grouping and joining can require $O(T\log T)$ comparison work, while ordering at most $P$ output rows costs $O(P\log P)$. Total time is $O(T\log T+P\log P)$ with $O(T+P)$ working space. An index such as `(patient_id, result, test_date)` can let the database reduce sorting and lookup work.

The benchmark defines $S=P$ and creates $T=5S$ tests. Every patient has an earlier negative, a first positive, an inconclusive result, and two later negatives. The accepted query aggregates the test relation in set-oriented passes. A calibrated slower query repeats correlated minimum-date scans of the full test table for every patient, creating quadratic rescanning without suitable indexes.

## Alternatives and edge cases

- **Correlated subqueries per patient:** Repeating the positive and negative minimum searches in `SELECT` and `WHERE` is compact but may rescan `covid_tests` several times per patient.
- **Self-join all positive/negative pairs:** It can produce many redundant date pairs before aggregation; anchoring the first positive first keeps the intermediate relation focused.
- **Window transitions:** `LEAD` over test rows does not suffice because inconclusive rows and negative-positive-negative sequences can separate the two dates that define recovery.
- **Negative before positive:** It is ignored because recovery requires a strictly later negative.
- **Same-date negative:** It does not qualify; the date predicate must use `>`, not `>=`.
- **Multiple positives:** The globally earliest positive remains the anchor even if another positive occurs before the qualifying negative.
- **Multiple later negatives:** Only the earliest one determines `recovery_time`.
- **Missing result type:** Patients with no positive or no strictly later negative are excluded.
- **Ordering tie:** Equal recovery times are resolved by ascending patient name.
- **Date arithmetic:** Use the database's calendar-day difference function rather than subtracting formatted strings or day-of-month components.
