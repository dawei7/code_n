## General
**Count only the two rate-bearing actions**

Group rows by `ad_id`. Conditional sums count `Clicked` rows and `Viewed` rows; ignored rows still ensure that an all-ignored advertisement remains present, but they add to neither count.

Compute `100.0 * clicks / (clicks + views)`. Use `NULLIF` on the denominator to avoid division by zero, then `COALESCE` the resulting null to 0 and round to two decimal places. Finally, order the grouped rows by the computed rate descending and `ad_id` ascending.

Each source row contributes to exactly one advertisement's two counters. The formula therefore uses precisely the specified numerator and denominator, including the separately defined zero-denominator case, so every grouped rate is correct.

## Complexity detail
Grouping scans $r$ rows and stores $a$ aggregates. Sorting the result costs $O(a\log a)$, giving $O(r+a\log a)$ time and $O(a)$ intermediate space in the general model.

## Alternatives and edge cases
- **Correlated subqueries:** Counting clicks and views separately for every distinct ad is correct but can rescan the full table $a$ times and take $O(ar)$ time.
- **Average of a click indicator:** Filter out ignored rows and average 1 for clicks and 0 for views, but an outer advertisement list is still needed to retain all-ignored ads.
- **Only ignored actions:** The denominator is zero, and the reported CTR must be 0 rather than null or an error.
- **No clicks:** A positive number of views still yields 0.
- **No views:** At least one click yields 100.
- **Equal rates:** Resolve the tie with ascending `ad_id`.
