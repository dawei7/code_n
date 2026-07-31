## General

**Turn the rule into adjacent transitions**

Partition transactions by `customer_id` and order each customer's rows by `transaction_date`. `LAG` supplies the preceding date and amount. The current row continues its predecessor's run exactly when its date is one calendar day later and its amount is strictly greater. Every first row, date gap, equal amount, or decrease starts a new run.

**Assign one identifier to each maximal run**

Mark a broken transition with `1` and a continuing transition with `0`. A cumulative sum of those markers within each customer partition stays constant while transitions qualify and increases precisely where a new run begins. The pair `(customer_id, sequence_id)` therefore identifies one maximal period; unrelated customers can never share a group.

Group by that pair and retain only groups containing at least three rows. Within a group, the earliest and latest transaction dates are the requested boundaries. A group of $k$ rows has $k-1$ qualifying adjacent transitions, so three rows are exactly the minimum needed for three consecutive transaction days. Conversely, any requested period has no broken adjacent transition, receives one sequence identifier, and survives the count filter. The final ordering follows all three required ascending keys.

## Complexity detail

Let $R$ be the number of rows in `Transactions`. Ordering the customer partitions costs $O(R\log R)$ time in the general case. The two window passes and aggregation are linear after ordering. Window, sort, and grouping state use $O(R)$ working space. The benchmark uses `size` as $R$ and contrasts this plan with a correct method that repeatedly searches later endpoints and can take quadratic time.

## Alternatives and edge cases

- **Self-join adjacent dates:** Joining each row to the next calendar day can identify increasing transitions, but discovering and extending every possible run through repeated joins or correlated searches can take $O(R^2)$ work.
- **Date minus row number:** Subtracting `ROW_NUMBER()` groups consecutive dates, but it does not by itself split a date-contiguous block when an amount stays equal or decreases.
- **Minimum and maximum only:** A customer's endpoints cannot prove that every intervening date exists or that every adjacent amount increases.
- A one-day date step is necessary; increasing amounts separated by a gap belong to different runs.
- The amount comparison is strict, so equal consecutive amounts start a new run.
- A run of exactly three rows qualifies, while one or two rows do not.
- A long qualifying run produces one maximal interval rather than every qualifying three-day subinterval.
- Ordering must use dates, not `transaction_id`, because identifiers do not determine chronological order.
