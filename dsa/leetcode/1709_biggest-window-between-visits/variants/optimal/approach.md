## General
**Find each user's next chronological visit**

Partition rows by `user_id` and order each partition by `visit_date`. The window function `LEAD(visit_date)` attaches the following visit to every row without mixing users. For the last row in each partition, `LEAD` returns `NULL`; replace that missing date with the fixed terminal date `2021-01-01`.

The table's composite primary-key order matches `(user_id, visit_date)`, so an ordered index scan can feed the window operation in one pass. The logic remains correct regardless of the physical order in which fixture rows were supplied.

**Reduce the gaps to one value per user**

Compute the whole-day difference from each `visit_date` to its attached next date. Group these gap rows by `user_id` and take `MAX`. Every true consecutive pair contributes exactly once, and the replacement terminal date contributes exactly one final window per user. Therefore the maximum covers precisely all windows required for that user.

## Complexity detail
Let $R$ be the visit count and $U$ the user count. Scanning the composite primary-key order, attaching the next date, and updating one maximum per user takes $O(R)$ time. A general window implementation may materialize all $R$ rows, so the conservative space bound is $O(R)$; a streaming ordered implementation needs only $O(U)$ aggregate state.

## Alternatives and edge cases
- **Self-join every later visit:** joining each row to all later dates and then selecting the nearest can create $O(R^2)$ intermediate pairs.
- **Correlated next-date subquery:** searching the table separately for every visit repeats work unless the optimizer turns it into an ordered scan.
- **Global `LEAD`:** omitting `PARTITION BY user_id` can make another user's visit incorrectly close a window.
- **Unordered window:** omitting `ORDER BY visit_date` follows arbitrary row order rather than chronology.
- **Single visit:** its gap to `2021-01-01` is both its only window and its maximum.
- **Terminal gap wins:** the days after the last recorded visit must compete with all internal gaps.
- **Unsorted fixture rows:** chronological ordering belongs in the query, not in assumptions about input serialization.
- **Leap year:** use date arithmetic so February 29 and all cross-month gaps are counted correctly.
- **Output order:** no row order is required, so fixtures compare the result as an unordered table.
