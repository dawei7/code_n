## General

**Attach every activity to an age bucket.** `Activities` contains time and activity type, while `Age` contains the user's bucket. `JOIN Age USING (user_id)` combines rows with the same user identifier so every included activity carries its owner's `age_bucket`.

This is an inner join. An activity whose user has no `Age` row is excluded, and an age bucket with no joined activity produces no result row. Under the expected foreign-key-like data relationship, every relevant activity has exactly one matching age row because `Age.user_id` is unique.

**Group all activity time by age bucket.** `GROUP BY 1` groups on the first selected expression, `age_bucket`. Each group therefore represents all send and open activity from all users in that age category, not an average of per-user percentages.

That distinction matters. The required percentage is total send time divided by total activity time for the bucket. Averaging each user's percentage would give every user equal weight even when their activity durations differ.

**Use conditional aggregation for each numerator.** The send numerator is

`SUM(IF(activity_type = 'send', time_spent, 0))`.

For a send row, its duration contributes; for an open row, zero contributes. The open numerator uses the symmetric condition. Because the enum contains only `send` and `open`, these two conditional totals partition the overall `SUM(time_spent)`.

**Convert ratios to percentages and round.** Multiplication by 100 changes a ratio such as 0.378378 into 37.8378 percent. Division by the group's total time normalizes the conditional total. `ROUND(..., 2)` applies the required two-decimal rounding after the ratio is computed.

The two expressions are:

$$
\text{send percentage}
=100\frac{\text{send time}}{\text{all activity time}},
$$

$$
\text{open percentage}
=100\frac{\text{open time}}{\text{all activity time}}.
$$

When every duration is nonnegative and total time is positive, the unrounded percentages sum to exactly 100.

**A grouped trace.** Suppose one age bucket has send times 3.50 and 2.00 and open times 4.50 and 1.00. Its send total is 5.50, open total is 5.50, and overall total is 11.00. Each conditional sum divided by 11 and multiplied by 100 gives 50.00.

The query does this aggregation directly from joined activity rows. It does not need an intermediate per-user table because the requested weighting is by time.

**Why one pass of aggregates is enough.** All three needed quantities—send time, open time, and total time—are additive within a bucket. MySQL can maintain them while processing the same group. Separate subqueries for each activity type would repeat grouping and need another join to combine results.

**Zero-total caveat.** If a bucket's joined `time_spent` values sum to zero, division by zero in MySQL yields `NULL`, so both percentages become null. The local description does not explicitly guarantee positive time. The exact query has no `NULLIF`, `COALESCE`, or special policy for that case. With the ordinary intended positive durations, this caveat does not arise.

**No output ordering is necessary.** The contract permits any order, so the absence of `ORDER BY` is correct.

## Complexity detail

Let $A$ be the number of activity rows and $G$ the number of age buckets. With an indexed unique lookup on `Age.user_id`, joining and aggregating is logically $O(A)$ expected work, and the engine keeps $O(G)$ group state.

The enum defines only three possible buckets, so $G$ is actually bounded by three and can be regarded as constant under this schema. Physical behavior depends on indexes and whether MySQL chooses hash or sort aggregation.

The query is read-only and returns one constant-width row per represented age bucket.

## Alternatives and edge cases

- **Aggregate each activity type separately:** Two grouped subqueries plus a join can produce the same columns but repeat scans and require careful handling of buckets missing one type.
- **Average per-user percentages:** This is generally wrong because it weights users equally rather than weighting every duration in the bucket.
- **Use `CASE` instead of `IF`:** `SUM(CASE WHEN ... THEN time_spent ELSE 0 END)` is standard SQL and has the same logic.
- **Bucket has only sends:** Send percentage is 100.00 and open percentage is 0.00, provided total time is positive.
- **Bucket has only opens:** The symmetric result is 0.00 and 100.00.
- **Zero total time:** The exact expressions return null through division by zero; the source does not define a replacement.
- **Missing age row:** The inner join removes that user's activities.
- **Age row without activity:** It creates no group and therefore no output row.
- **Rounding order:** Totals are divided first and the final percentage is rounded, avoiding accumulated rounding error from per-row percentages.
- **Any result order:** Group order is unspecified, which is allowed by the contract.
- **Percentage type behavior:** Multiplying by 100 before division makes the intended scale obvious. Because `time_spent` is decimal, MySQL performs decimal-style division rather than accidental integer truncation.
- **Shared denominator:** Both output percentages divide by the same total activity time for the age bucket, so under the declared send/open activity domain their unrounded values sum to 100 percent.
