## General

**Attach each activity to its age bucket.** Join `Activities` with `Age` on
`user_id`. Grouping the joined rows by `age_bucket` then makes every aggregate
describe the complete activity of that bucket, including activity from several
different users.

**Accumulate both categories in the same pass.** A conditional sum contributes
`time_spent` only for `send` rows, and a second conditional sum does the same
for `open` rows. The denominator is the sum of all activity time in the group.
Multiplying each category sum by `100.0` before division produces a percentage
without integer truncation. Round only the final ratios to two decimal places,
so intermediate rounding cannot distort the result.

Every activity has exactly one of the two allowed types. Consequently, the two
conditional numerators partition the denominator, and the reported
percentages account for all snap time in that age bucket.

## Complexity detail

Let $n$ be the number of activity rows and $g$ the number of represented age
buckets. With indexed or hash-based user lookup and grouping, the join and
aggregation take expected $O(n)$ time and store $O(g)$ aggregate state. The
final table has one row per represented bucket. Physical database plans may
use sorting instead of hashing without changing the query's single grouped
aggregation structure.

## Alternatives and edge cases

- **Aggregate per user first:** This can be correct, but the intermediate grouping is unnecessary because the requested ratios are defined over the whole age bucket.
- **Average user percentages:** This gives equal weight to users rather than activity time and is wrong when users have different total durations.
- **Two separate category queries:** Joining separate send and open aggregates adds work and requires careful handling when one category is absent.
- Conditional sums must use zero for the nonmatching type so a bucket containing only one activity type still produces both output columns.
- Multiply before dividing and round only the completed percentage to avoid truncation and accumulated rounding error.
- The contract allows any row order, so no result sort is required.
