## General
**Form one group per viewer and date.** The condition must hold within a single calendar date, so group rows by both `viewer_id` and `view_date`. Grouping by the viewer alone would incorrectly combine articles seen on different dates.

**Count articles rather than events.** Use `COUNT(DISTINCT article_id)` inside each group because duplicate rows or repeated views of one article do not establish that the person viewed more than one article. Retain only groups whose distinct count exceeds `1`.

**Collapse multiple qualifying dates.** One viewer may satisfy the condition on several dates, but the requested output contains people, not viewer-date pairs. Select `DISTINCT viewer_id AS id` from the retained groups, then explicitly sort by `id` ascending.

## Complexity detail
A comparison-based grouping and distinct-count plan can sort the $r$ rows in $O(r\log r)$ time and retain $O(r)$ grouping state. Hash aggregation may achieve expected linear work, and indexes may change the physical plan, without changing the query's logical result.

## Alternatives and edge cases
- **Self-join on viewer and date:** Pairing different article IDs is correct, but a busy viewer-date can generate quadratically many row pairs before deduplication.
- **Count all rows:** `COUNT(*) > 1` is wrong when the table repeats one article's event.
- **Group only by viewer:** This incorrectly combines different dates.
- **Same article on several dates:** The viewer does not qualify unless some one date contains another distinct article.
- **Several qualifying dates:** The viewer appears only once in the final output.
- **Author identity:** Whether the viewer authored an article is irrelevant to this problem.
