## Function Contract

**Input**

- `Visits`: the bank-visit table described above.
- `Transactions`: the guaranteed visit-linked transaction table described above.

Let $V$ be the number of visit rows, $T$ the number of transaction rows, and $N=V+T$.

**Return value**

Return a table with these columns:

- `transactions_count`: a consecutive integer bucket beginning at `0` and ending at the maximum number of transactions attached to one visit.
- `visits_count`: the number of distinct visit rows whose transaction total equals that bucket.

Count visits rather than distinct users: one user may have several visits on different dates. Return the buckets by ascending `transactions_count`.
