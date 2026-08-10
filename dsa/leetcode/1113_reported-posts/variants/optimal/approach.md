## General

**Filter to the exact event type and date first**

The report asks about posts reported yesterday, where the assumed current date makes yesterday July 4, 2019. A row qualifies only when both:

- `action_date = '2019-07-04'`, and
- `action = 'report'`.

The `WHERE` clause applies both predicates before grouping. Views, likes, reactions, comments, and shares on that date are irrelevant. Reports on any other date are also irrelevant.

Filtering first ensures later aggregation sees only evidence that can contribute to the answer.

**Use the report reason as the grouping key**

For report actions, `extra` contains the reason. The query selects it as `report_reason` and uses `GROUP BY 1`, meaning group by the first selected expression.

Every qualifying row with the same reason enters the same group. A reason with no qualifying report rows creates no group, which naturally omits zero-count reasons as required.

**Count posts rather than rows or reporters**

The table may contain duplicate rows. Several users may also report the same post for the same reason. The requested quantity is the number of posts, not the number of report actions.

`COUNT(DISTINCT post_id)` counts each post identifier at most once inside one reason group. Two spam reports for post four contribute one spam-reported post. Reports for posts two and five under racism contribute two.

Distinctness is scoped to each group. If the same post is reported for two different reasons, it may correctly contribute once to each reason because the problem asks for a separate count per reason.

This scope can be viewed as deduplicating ordered pairs `(report_reason, post_id)`. Rows with the same pair collapse to one logical contribution, while rows differing in either component remain separate. User ID and the number of physical rows do not participate in that logical identity, which exactly matches the requested statistic.

**Why user ID is not counted**

Counting distinct users would answer how many reporters used a reason, which is different. One user could report several posts, or several users could report one post. Only distinct `post_id` matches the contract.

Likewise, `COUNT(*)` would count duplicate report rows and repeated reporters, potentially inflating the result.

**Aliases shape the required output**

`extra AS report_reason` gives the grouping value its required output name. `COUNT(DISTINCT post_id) AS report_count` names the aggregate.

The result order is unrestricted, so the query intentionally omits `ORDER BY`. If no row passes the two filters, no groups are formed and the result is empty.

**Complete correctness argument**

After `WHERE`, every remaining row and only those rows represents a report made on the required date. Grouping partitions those rows by reason. Within each partition, distinct counting maps any number of reports for one post to one contribution and maps different posts to different contributions.

Therefore, each output row pairs one represented reason with exactly the number of distinct posts reported for that reason yesterday. No unrelated action, date, duplicate row, or repeat reporter can change the count.

The query also avoids inventing categories. Only reasons present on at least one qualifying report appear, so the result contains no zero-valued rows that would require a separate reasons table.

## Complexity detail

Let $R$ be the number of Actions rows. The database must inspect or index-filter the relevant rows. A general sort-based grouping and distinct aggregation can take $O(R\log R)$ time, matching the manifest.

Tracking groups and distinct post IDs may require $O(R)$ space in the worst case when every qualifying row has a different reason-post combination. A hash-based plan may have expected linear time, while indexes can reduce scanned data, but the conservative manifest bound remains valid.

The output has no more rows than the number of qualifying reasons and therefore at most $R$ rows.

## Alternatives and edge cases

- **Subquery with `SELECT DISTINCT extra, post_id`:** Deduplicate reason-post pairs first, then count rows per reason. This is equivalent but uses an extra query layer.
- **`COUNT(*)`:** Incorrect when duplicate rows or multiple users report the same post.
- **`COUNT(DISTINCT user_id)`:** Counts reporters, not reported posts.
- **Group by post first:** Possible in a two-stage query, but grouping directly by reason with a distinct post aggregate is simpler.
- **Same post reported by many users:** It contributes once for that reason.
- **Duplicate report rows:** Distinct post counting neutralizes them.
- **Same post with different reasons:** It contributes once within each separate reason group.
- **Non-report action with non-null extra:** It is removed by the action predicate and cannot create a reason group.
- **Report on July 3 or July 5:** It is removed by the exact-date predicate.
- **One qualifying report:** Its reason receives count one.
- **No qualifying reports:** No groups form, yielding an empty result.
- **Null reason on a report:** SQL would group null reasons together if such rows exist; the local contract describes `extra` as optional but does not specify excluding null report reasons, so the exact query preserves that group.
- **Any result order:** No sort is needed because the contract explicitly permits arbitrary order.
