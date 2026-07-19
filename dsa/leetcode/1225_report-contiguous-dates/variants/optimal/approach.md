## General
**Create one state-tagged date stream.** Project `fail_date` as `period_date` with state `failed`, project `success_date` with state `succeeded`, and combine them with `UNION ALL`. Apply the 2019 bounds inside both projections so outside rows never participate in grouping.

**Turn consecutive dates into a stable island key.** Within each state, order dates and assign `ROW_NUMBER()`. For consecutive calendar dates, both the date and row number increase by one, so subtracting that many days from the date produces the same anchor for every row in the run. A gap changes the anchor and begins another island even if the later row has the same state.

**Collapse each maximal island.** Group by the state and derived anchor. The minimum date is `start_date` and the maximum is `end_date`. Ordering those grouped rows by `start_date` interleaves failed and succeeded periods chronologically as required.

The primary keys prevent duplicate dates within either state, and the once-per-day model prevents an ambiguous date from carrying both states. Thus each in-range day contributes to exactly one numbered stream and exactly one maximal island.

## Complexity detail
Filtering and unioning touch $d$ in-range rows. The state-partitioned window ordering dominates the logical work at $O(d\log d)$; grouping is linear after ordering. The combined, numbered, and grouped intermediate state uses $O(d)$ space. A database engine may select an equivalent indexed physical plan.

## Alternatives and edge cases
- **Correlated earlier-date count:** Counting prior same-state rows separately for every date reproduces the row number but can take $O(d^2)$ time.
- **Self-join adjacent dates:** It can identify boundaries, but expanding each boundary into an end date is more cumbersome than the gaps-and-islands key.
- **Outside-year rows:** Filter them before numbering so they cannot shift island anchors.
- **One-day island:** Its minimum and maximum dates are equal.
- **Same state separated by a gap:** The changed date-minus-row-number anchor keeps the runs separate.
- **Year boundaries:** Only dates from `2019-01-01` through `2019-12-31`, inclusive, are reported.
- **Final ordering:** Grouped SQL output has no inherent order, so `ORDER BY start_date` is required.
