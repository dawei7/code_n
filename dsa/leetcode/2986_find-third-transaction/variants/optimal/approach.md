## General

**Establish each user's chronology.** Partition the rows by `user_id` and
order each partition by `transaction_date`. `ROW_NUMBER` identifies exactly
the third transaction, while `LAG` with offsets one and two carries the two
preceding spends onto that row.

**Filter only the designated row.** Keep `transaction_number = 3`, then require
the current `spend` to be greater than both lagged values. Users with fewer
than three rows never produce row number three. Because the filter does not
inspect later row numbers, a fourth or later high spend cannot substitute for
a failing third transaction. Finally, project the required aliases and sort by
ascending user ID.

The window order agrees with the contract's unique timestamps. Consequently,
the row numbered three is the required transaction, and the two lag values are
exactly its predecessors; the two strict comparisons are therefore necessary
and sufficient for inclusion.

## Complexity detail

Let $R$ be the number of transaction rows. Partition ordering takes
$O(R\log R)$ time in the general case, and the subsequent window scan is
linear. Window and sort state use $O(R)$ auxiliary space.

## Alternatives and edge cases

- **Three correlated date searches:** Finding ordinal positions independently for each row is correct but can require quadratic work.
- **Aggregate by user:** Aggregation alone loses the spend and date attached to the chronological third row.
- **Fewer than three transactions:** Such a user has no candidate and must be absent.
- **More than three transactions:** Only row three matters, even when a later spend would pass.
- **Equal spend:** The third spend must be strictly greater than each predecessor; equality fails.
- **Input order:** Rows must be ordered by `transaction_date`, not by their fixture or storage order.
