## General
**Filter the calendar year before grouping**

Keep timestamps greater than or equal to `2020-01-01 00:00:00` and strictly less than `2021-01-01 00:00:00`. This half-open interval includes every possible 2020 timestamp while excluding both neighboring years. It also avoids applying a year-extraction function to the stored column, allowing a suitable timestamp index to support a range scan.

**Collapse each qualifying user**

Group the filtered rows by `user_id` and compute `MAX(time_stamp)` for each group. The aggregate returns the latest qualifying login, and the alias `last_stamp` gives the required output schema. Filtering first ensures that a later login from 2021 cannot replace a user's latest 2020 value.

Every returned group contains at least one 2020 row, so no ineligible user appears. Conversely, every user with a 2020 login contributes to exactly one group, and the maximum selects precisely that user's latest such timestamp.

## Complexity detail
Without relying on indexes, the query scans the $R$ login rows once and maintains aggregate state for at most $U$ qualifying users, giving $O(R)$ expected time with hash aggregation and $O(U)$ working space. A database engine that implements grouping by sorting may use $O(R\log R)$ physical time; an appropriate range or composite index can reduce scanning and grouping work.

## Alternatives and edge cases
- **Extract the year:** `YEAR(time_stamp) = 2020` is concise but may prevent a normal timestamp index from serving as a range predicate.
- **Correlated maximum per user:** It can produce the same result but may rescan `Logins` for every outer row and degrade to $O(R^2)$.
- **Group before filtering:** Taking the all-time maximum first incorrectly drops a user whose latest overall login is outside 2020.
- **Start boundary:** `2020-01-01 00:00:00` must be included.
- **End boundary:** `2021-01-01 00:00:00` must be excluded.
- **Only adjacent-year logins:** Such a user produces no output row.
- **Any-order result:** No `ORDER BY` is required by the contract.
