## General

**The qualifying unit is a viewer-date pair**

The condition says a person must view more than one article on the same date. Neither a viewer's total across all dates nor an article's total viewers answers that question. The query must examine each combination of `viewer_id` and `view_date` independently.

`GROUP BY viewer_id, view_date` forms exactly those groups. All events for one viewer on one calendar date enter the same group, while a different viewer or a different date enters another group.

The `author_id` column does not participate. Qualification depends only on who viewed, which article was viewed, and when. Whether the viewer authored any of those articles is irrelevant to this problem.

**Count distinct articles rather than rows**

The table may contain duplicate rows, and one person may generate multiple records involving the same article on the same date. “More than one article” means at least two different `article_id` values, not at least two view-event rows.

Within each viewer-date group, `COUNT(DISTINCT article_id)` measures the number of unique articles. A duplicated view of article three still contributes one. Views of articles one and three contribute two even if either event is repeated.

`HAVING COUNT(DISTINCT article_id) > 1` retains only groups whose unique-article count is at least two. `HAVING` is necessary because this condition depends on an aggregate computed after grouping. A `WHERE` clause cannot directly filter on that group count.

**Deduplicate viewers who qualify on multiple dates**

After `HAVING`, one row conceptually remains for each qualifying viewer-date group. A person who views several articles on two different dates creates two qualifying groups, but the output should contain that person's identifier only once.

`SELECT DISTINCT viewer_id AS id` performs this second kind of deduplication. The inner distinctness in `COUNT(DISTINCT article_id)` answers “how many different articles in one group?” The outer `SELECT DISTINCT` answers “how many different qualifying people in the final result?” They solve separate duplicate problems and are both needed.

The alias `id` gives the single output column its required name. `ORDER BY 1` sorts that first selected expression in ascending order, satisfying the presentation requirement.

**Trace the example**

Viewer five on `2019-08-01` has article identifiers one and three, so that group has distinct count two and survives. Viewer six on `2019-08-02` has article identifiers one and two, so that group also survives.

Viewer four has two identical rows for article three on `2019-07-21`. A raw count would be two and would incorrectly qualify the viewer. The distinct article count is one, so the group is correctly rejected.

Viewer seven's group contains only article two, and viewer one's group contains only article four. They are rejected as well. The surviving viewer identifiers are five and six, already unique in this example, and sorting returns them in ascending order.

**Why the query is correct**

For every output identifier, at least one viewer-date group for that person survived `HAVING`. Survival proves the group contains more than one distinct article identifier, so the person satisfies the problem condition.

Conversely, suppose a person viewed at least two distinct articles on some date. All corresponding rows share that `viewer_id` and `view_date` and therefore enter one group. Its distinct article count exceeds one, so `HAVING` retains it and the person's identifier enters the selected result. Final `DISTINCT` cannot remove the person entirely; it only merges repeated qualifying appearances.

Thus the query returns exactly the qualifying people, once each, under the correct output name and order.

The grouping solution avoids comparing rows pairwise. It summarizes each viewer-date population directly, making the duplicate-row semantics explicit.

## Complexity detail

Let `r` be the number of rows in `Views`. Grouping by viewer and date and deduplicating article identifiers can require sorting `r` records, giving the manifest's conservative `O(r log r)` time bound. The final distinct projection and ordering do not exceed that worst-case order because there can be at most `r` qualifying group rows.

Aggregation, distinct-article state, and result sorting may retain information proportional to the source size, so auxiliary space is `O(r)`.

A database may use hash aggregation, indexes, or a combined sort to improve actual execution. Complexity for SQL is plan-dependent, but these bounds do not assume favorable physical structures.

## Alternatives and edge cases

- **Use `COUNT(*) > 1`:** Duplicate views of the same article would create a false qualification. The count must be over distinct `article_id` values.
- **Group only by viewer:** That combines articles viewed on different dates and can qualify someone who never viewed two articles on one day.
- **Group only by date:** That mixes different people and answers how many articles everyone viewed collectively.
- **Self-join `Views`:** Joining rows on equal viewer and date with different article IDs can prove that a qualifying pair exists. It is valid but can create many row pairs and demands careful deduplication.
- **Use `WHERE` for the aggregate threshold:** `WHERE` is evaluated before grouping and cannot test the distinct count. `HAVING` filters completed groups.
- **Omit outer `DISTINCT`:** A viewer qualifying on multiple dates could appear once per date even though only one identifier is requested.
- **Duplicate rows:** They are neutralized by `COUNT(DISTINCT article_id)` and cannot manufacture a second article.
- **Repeated views of two articles:** The group qualifies because its distinct set has size two, regardless of the number of repeated events.
- **Self-views:** They count exactly like any other article view; author identity does not affect this task.
- **No qualifying viewer-date group:** The result is an empty table with the column named `id`.
- **Required ordering:** `ORDER BY 1` sorts the final distinct viewer identifiers, not the underlying events.
