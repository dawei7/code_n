## General

**Reduce each advertisement to the two counts in the formula**

The output has one row per `ad_id`, so group the input by that identifier. Within each group, one conditional sum counts `Clicked` rows and another counts all rate-bearing interactions—`Clicked` or `Viewed`. An `Ignored` row adds to neither sum, but it remains in the group; this is essential because an advertisement with only ignored actions must still appear.

Multiply the click count by `100.0` before division so the percentage uses decimal rather than integer arithmetic. `NULLIF` converts a zero click-plus-view denominator to null, `COALESCE` maps that one exceptional result to the required zero, and `ROUND(..., 2)` produces the reported CTR.

For a fixed advertisement, every click contributes one to both numerator and denominator, every view contributes only to the denominator, and every ignored action contributes to neither. If the denominator is positive, the expression is therefore exactly $100C/(C+V)$; if it is zero, the expression follows the separately defined zero branch. Grouping preserves one result for every represented advertisement, proving both the values and result membership.

**Apply the contract's order to the reported rate**

Sort by the rounded `ctr` alias descending, then by `ad_id` ascending. This orders the values actually returned and deterministically resolves equal rates.

## Complexity detail

Let $r$ be the number of rows in `Ads` and $a$ the number of distinct advertisements. A hash-based grouping pass takes expected $O(r)$ time and $O(a)$ aggregate space. Sorting the $a$ result rows takes $O(a\log a)$ time, for total expected time $O(r+a\log a)$ and $O(a)$ working space.

## Alternatives and edge cases

- **Correlated counts:** Starting from the distinct advertisements and separately counting clicks and views for each one is correct, but it can rescan all $r$ rows for every advertisement and take $O(ar)$ time.
- **Average a click indicator:** After excluding ignored rows, averaging `1` for clicks and `0` for views gives the same positive-denominator rate, but a separate advertisement relation or outer join is needed to retain all-ignored advertisements.
- **Filtering ignored rows before grouping:** This silently removes advertisements whose only actions are ignored, violating required result membership.
- **Integer division:** Using an integer numerator can truncate every non-integral rate before multiplication or rounding; `100.0` forces decimal arithmetic.
- **Zero denominator:** An all-ignored advertisement must produce numeric zero rather than null or a division error.
- **Clicks only and views only:** A positive click count with no views yields `100.00`; views with no clicks yield `0.00` without taking the zero-denominator branch.
- **All three actions:** Ignored rows leave the click-to-click-plus-view ratio unchanged even when clicks and views are both present.
- **Tied rounded rates:** Equal reported CTR values are ordered by ascending `ad_id`.
- **Empty input:** With no advertisement rows, there are no groups and therefore no output rows.
- **Composite-key scope:** A `user_id` may occur under several advertisements; only the (`ad_id`, `user_id`) pair is unique, and grouping depends solely on `ad_id`.
