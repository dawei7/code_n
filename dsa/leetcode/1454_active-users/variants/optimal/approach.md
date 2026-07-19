## General
**Deduplicate login days before measuring activity**

Start with `SELECT DISTINCT id, login_date FROM Logins`. The definition is
based on consecutive days, not event count. Without this step, two events on
the same date could occupy two row positions and either break the sequence
arithmetic or falsely help a group reach five rows.

**Turn consecutive dates into a constant gaps-and-islands key**

Within each account, order the distinct dates and assign
`ROW_NUMBER()` beginning at one. For a consecutive run, both the calendar date
and row number advance by one each row. Subtracting the row-number day offset
from the date therefore produces the same value throughout that run. After a
missing day, the date advances by more than the row number and the key changes.

For example, dates January 3, 4, and 5 with row numbers 1, 2, and 3 all map to
January 2 after subtracting their respective offsets. A following January 7
with row number 4 maps to January 3 and starts a new island.

The app-local SQLite query expresses the key as
`julianday(login_date) - ROW_NUMBER()`. The native MySQL query uses
`DATE_SUB(login_date, INTERVAL ROW_NUMBER() ... DAY)`. These are equivalent
representations of the same date-minus-position invariant.

**Select qualifying islands and recover account names**

Group the numbered rows by `id` and the island key. Any group with
`COUNT(*) >= 5` proves that the account has a qualifying consecutive streak.
An account may have multiple such groups, so reduce the qualifying rows to
distinct IDs before joining `Accounts`. Select `id` and `name`, and finish with
`ORDER BY id` because neither grouping nor joining guarantees presentation
order.

Deduplication makes each row one active calendar day. The island key groups
exactly consecutive dates: adjacent dates stay together, and every date gap
changes the key. A group count of at least five is therefore equivalent to a
streak of at least five consecutive login days. Joining those IDs to
`Accounts` returns every and only active user, with no duplicate output rows.

## Complexity detail
Deduplicating and partition-ordering $L$ account-date pairs requires
$O(L\log L)$ logical time without relying on an existing covering index. The
window scan, island aggregation, join over $A$ accounts, and final output work
are linear after their required ordering, giving $O(L\log L+A)$ overall.

The distinct dates, window state, and island groups require $O(L)$ working
space. Database engines may use indexes, external sorting, or streaming plans
that change physical constants, but the stated bound does not assume them.

## Alternatives and edge cases
- **Correlated five-day windows:** For every distinct login date, count the
  account's dates in the following four calendar days. This is correct but can
  repeatedly scan `Logins` and take $O(L^2)$ time without indexes.
- **Five self-joins:** Join a login day to rows one, two, three, and four days
  later. It expresses the threshold directly but is verbose, sensitive to
  duplicates, and awkward for streaks longer than five.
- **`LAG` plus cumulative breaks:** Mark where a date is not one day after its
  predecessor, prefix-sum those break flags, and group by the resulting island
  number. This is also correct but uses an additional window stage.
- **Duplicate login events:** Remove them before row numbering; one date counts
  once regardless of event multiplicity.
- **Exactly five days:** Include the account because the threshold is at least
  five.
- **Longer streak:** Include the account once, not once per qualifying window.
- **Multiple streaks:** A user still appears only once after distinct-ID
  reduction.
- **Month or year boundary:** Date arithmetic, rather than integer day-of-month
  subtraction, preserves true calendar consecutiveness.
- **Ordering:** Explicitly sort by account `id` ascending.
