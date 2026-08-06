## General
The comparison is between adjacent **calendar dates**, not adjacent ids or adjacent rows after sorting. Give `Weather` two aliases—`current` and `previous`—and self-join them only when the current date is exactly one day after the previous date.

The candidate computes `date(previous.recordDate, '+1 day')` and compares that value directly with `current.recordDate`. SQLite can build an automatic equality index for the unmodified current-date column, whereas applying `julianday` to both columns forces a pairwise scan. Calendar-aware `date` arithmetic still handles month ends, year ends, and leap days correctly.

After forming valid day pairs, filter with `current.temperature > previous.temperature` and project `current.id`. The comparison is strict: equal temperature is not a rise.

For observations on January 1, January 2, and January 4, only January 2 can compare with January 1. January 4 must not compare with January 2 because the difference is two days, even if those rows are consecutive in a sorted query result.

Every joined pair differs by exactly one calendar day, so a current row passes the temperature predicate only when it is warmer than its actual preceding day's observation. Thus every returned id qualifies. Conversely, any qualifying row has a recorded previous calendar day; applying the one-day transform to that previous date equals the current date, and the higher current temperature satisfies the filter, so its id is returned. Missing dates form no pair and are correctly ignored.

The immutable Accepted MySQL source uses `DATEDIFF` because SQLite's `date` modifier is dialect-specific. The candidate is staged only for the app-local SQLite contract and is not submission evidence.

## Complexity detail
SQLite scans the `previous` rows once and can build an automatic index on the unmodified `current.recordDate` column. Building that index costs $O(n \log n)$ work, and the $n$ equality lookups cost another $O(n \log n)$ in the worst case, for $O(n \log n)$ total logical work. The automatic index uses $O(n)$ auxiliary space. Exact physical costs remain database- and index-dependent.

## Alternatives and edge cases
- **Two-sided date functions:** The protected SQLite source compares two `julianday` expressions and the native MySQL source uses `DATEDIFF`; both express the rule directly, but neither side remains available for a plain equality index under the declared schema.
- **Window function:** `LAG` over date order is concise, but it must also compare the two dates or it incorrectly bridges gaps.
- **Correlated lookup:** Searching separately for `current_date - 1 day` mirrors the definition but may repeat scans without an index.
- **Identifier order:** Joining or ordering by `id` is incorrect because identifiers do not define calendar adjacency.
- **Missing predecessor:** The earliest represented date and every row after a date gap form no qualifying pair.
- **Strict comparison:** Equal or lower temperatures do not qualify.
- **Unique dates:** The one-observation-per-date contract ensures at most one previous-day match.
