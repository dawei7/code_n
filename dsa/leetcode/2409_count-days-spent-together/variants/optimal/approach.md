## General

**Put every date on one axis.** Month and day components are awkward to compare across month boundaries. Store the cumulative number of days before each month, then convert `"MM-DD"` to `days_before_month[month - 1] + day`. Because the calendar is non-leap, this table is fixed and every valid date maps uniquely to an ordinal from 1 through 365.

**Intersect the inclusive intervals.** The shared stay begins at the later arrival and ends at the earlier departure. If the resulting start is after the end, the stays are disjoint. Otherwise the inclusive length is `overlap_end - overlap_start + 1`; the final `+ 1` is what counts a shared endpoint or a one-day stay.

## Complexity detail

Each input date has a fixed five-character representation and the calendar contains a fixed 12 months. Four conversions and a constant number of comparisons take $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate calendar days:** Marking or scanning all 365 dates is correct, but it obscures the direct interval-intersection formula and still depends on the fixed-year bound.
- **Date-library parsing:** A library can convert dates, but it adds timezone and year machinery that this fixed non-leap contract does not need.
- **Inclusive endpoints:** Equal overlap boundaries contribute one day, not zero.
- **Adjacent disjoint stays:** An end on one day and the other arrival on the following day have no shared day.
- **Month boundaries:** Ordinal conversion makes dates such as `"02-28"` and `"03-01"` consecutive in a non-leap year.
- **Containment:** When one stay contains the other, the result is exactly the shorter stay's inclusive length.
