## General

**Compute a separate benchmark for each event type**

Activity values from different event types are not comparable through one global average. The derived table groups `Events` by `event_type` and computes `AVG(occurrences)` for each group.

Each derived row represents one event type and the average among only businesses that have a row for that type, exactly matching the definition.

**Join each business event to its matching average**

The outer Events row `t1` is joined to derived row `t2` on equal `event_type`. Every business-event occurrence value is therefore placed beside the correct benchmark.

The `WHERE` predicate retains only rows where the business’s value is strictly greater than that event average. Equality is excluded because the definition says “strictly greater.”

After this filter, every remaining row is one event type on which one business performs above average.

The join is inner because every outer Events row has an event type that necessarily appears in the grouped averages derived from the same table. No source row can lack a benchmark, so a left join would add no information.

**Count qualifying event types per business**

The source grain has composite primary key `(business_id, event_type)`, so one business has at most one row for an event type. Consequently, counting filtered rows after grouping by `business_id` is the same as counting distinct qualifying event types.

`HAVING COUNT(1) > 1` keeps businesses with at least two such types. A business above average for exactly one event is rejected.

Only `business_id` is selected, and result order is unrestricted.

Filtering belongs before the business grouping. If all rows were grouped first, a single aggregate could lose the per-event comparison needed to decide which types qualify. The query preserves the unique business-event grain until each row has been compared with its matching average, then counts only successful comparisons.

**Walk through the example**

Reviews average five, ads average eight, and page views average 7.5. Business one has seven reviews and eleven ads, so two joined rows survive. Its page-view value three does not.

The count for business one is two and passes. Other businesses have fewer than two qualifying rows and disappear in `HAVING`.

**Protected SQL contains a schema typo**

The documented column is `occurrences` with two consecutive r letters after “occu.” The exact protected query writes `occurences` in the derived AVG, the alias, and the outer comparison.

Against the documented schema, MySQL will report an unknown column and the query will not execute. The intended logic becomes executable only when those references are spelled `occurrences`, or when the actual table used a differently spelled column, which would contradict the local Reference.

This approach explains the intended optimal aggregation while accurately identifying that the protected source does not currently implement it against the stated schema. No solution file is changed in this documentation-only pass.

The alias may legally reuse the source column name after spelling repair. Qualifying it as `t2.occurrences` in the comparison distinguishes the average from `t1.occurrences`, the individual business value.

**Why the intended query is correct after spelling repair**

The derived grouping computes the exact per-type mean. The join associates every row with that mean, the strict filter identifies precisely the above-average business-event pairs, and the primary key ensures each pair represents a distinct type.

Grouping those pairs by business and requiring more than one returns exactly the active businesses.

Because the average includes the business’s own row, the comparison follows the stated population average rather than a leave-one-out benchmark. Removing the current business before averaging would answer a different question.

## Complexity detail

Let $R$ be the number of Events rows. A sort-based database plan can group by event type, join, and group by business in $O(R\log R)$ time, matching the manifest.

Materialized averages, join rows, and aggregation state can require $O(R)$ space in a conservative plan. Hash aggregation may provide expected linear time, and indexes can improve constants.

The exact misspelled query fails before these complexity properties become observable. Complexity describes the intended corrected query.

## Alternatives and edge cases

- **Window average:** Add `AVG(occurrences) OVER (PARTITION BY event_type)` to every row, filter above-average rows, then group by business.
- **Correlated average:** Compare each row with a subquery average for its type. Correct indexing matters to avoid repeated scans.
- **Count distinct event type:** `COUNT(DISTINCT event_type) > 1` is more defensive if uniqueness were absent; the primary key makes plain row count sufficient.
- **Global average:** Incorrect because each event type needs its own peer benchmark.
- **Equality with average:** It does not qualify due to the strict greater-than predicate.
- **Exactly one qualifying type:** The business fails `COUNT(1) > 1`.
- **Exactly two qualifying types:** It passes.
- **One row for an event type:** Its occurrence equals that type’s average, so it cannot qualify.
- **Duplicate business-event rows:** The primary key forbids them, protecting the row-count interpretation.
- **Any result order:** No `ORDER BY` is needed.
- **Empty table:** No averages, joined rows, or businesses are returned.
- **Column spelling:** Every intended `occurences` reference must match the actual schema name `occurrences` for execution.
