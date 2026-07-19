## General
**Select only reports from the target day:** Filter with both `action_date = '2019-07-04'` and `action = 'report'`. A view on the target day and a report on another day must not affect the result.

**Group by the stored reason:** For report rows, `extra` is the semantic reason, so group by that column and expose it as `report_reason`.

**Count posts rather than report rows:** Apply `COUNT(DISTINCT post_id)` within each reason group. This deduplicates multiple users reporting the same post for the same reason while still counting different posts separately. Each output group therefore contains exactly the target-day report rows for one reason, and its distinct count is precisely the requested number.

## Complexity detail
Without indexes or engine-specific assumptions, filtering and sort-based grouping of $R$ rows costs $O(R \log R)$ time and up to $O(R)$ execution space. Hash grouping can provide expected $O(R)$ time, while an index on the filter and grouping columns may change the physical plan.

## Alternatives and edge cases
- **Pre-deduplicate reason-post pairs:** Select distinct `extra, post_id`, then group and count. It is correct and makes the two aggregation stages explicit.
- **Correlated distinct count:** Compute the count for each qualifying outer row and deduplicate afterward. It returns the same values but can rescan all $R$ rows repeatedly and take $O(R^2)$ time.
- **`COUNT(*)`:** It overcounts when several users report the same post for one reason.
- **Non-report activity:** Its `extra` value is irrelevant and the row must be filtered out.
- **Reports on other dates:** They do not contribute even if their reasons match target-day reports.
- **Same post, same reason, many users:** It contributes one distinct post.
- **Same post, different reasons:** It contributes once to each separate reason group.
- **No target-day reports:** The query returns no rows.
