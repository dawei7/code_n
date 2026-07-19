## General
**Partition by the calendar date**

Use `DATE(day)` as the window partition key. This removes the time component without merging equal day-of-month numbers from different months or years. Every transaction on the same full calendar date is therefore compared within one group.

**Rank amounts while preserving ties**

Within each date partition, order `amount` descending and apply `RANK()`. Every row with the maximum amount receives rank 1. Unlike `ROW_NUMBER()`, `RANK()` assigns the same rank to equal amounts, so filtering for rank 1 returns all daily co-maxima.

The common table expression retains each `transaction_id` beside its rank. The outer query filters to rank 1 and orders the surviving IDs numerically in ascending order, independently of date and input order.

**Why the filter returns exactly the required rows**

For a fixed date, descending amount order places no value ahead of a maximum, so each maximum row has rank 1. Any smaller amount has at least one maximum before it and receives a rank greater than 1. The filter therefore includes all and only maximum transactions in every partition; the final sort then satisfies the output-order contract.

## Complexity detail
For $r$ rows, partitioned ordering takes $O(r\log r)$ time in the general case, followed by a linear filter and result sort bounded by the same order. The window ranking and sort may retain $O(r)$ rows of working state.

## Alternatives and edge cases
- **Aggregate and join:** Compute `MAX(amount)` per `DATE(day)` and join it back to `Transactions`; this is correct and naturally preserves ties, but it performs a separate aggregation and matching step.
- **Correlated `NOT EXISTS`:** Select a transaction only when no larger amount exists on its date; without suitable indexing this can compare quadratically many row pairs.
- **`ROW_NUMBER()`:** It incorrectly discards all but one transaction when several IDs tie for the daily maximum.
- **Day-of-month extraction:** Grouping only by `DAY(day)` incorrectly merges dates from different months or years; use the complete calendar date.
- **Different times on one date:** Time-of-day does not split the daily partition.
- **Midnight boundary:** Timestamps immediately before and after midnight belong to different dates.
- **Tied maxima:** Every tied ID must appear once.
- **Single transaction date:** Its only row receives rank 1.
- **Output ordering:** Sort by ID, not by date, amount, rank, or insertion order.
