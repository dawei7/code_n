# Active Users

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1454 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/active-users/) |

## Problem Description
### Goal

`Accounts` identifies each user and stores the user's name. `Logins` records
the calendar dates on which an account logged in; the log may contain duplicate
rows, so multiple login events on one date still represent only one active
day.

An active user is an account that logged in on at least five consecutive
calendar days. Find every active user's `id` and `name`, and return the rows in
ascending order by `id`.

### Function Contract
**Inputs**

- `Accounts(id, name)`: one row per account. `id` is the primary key.
- `Logins(id, login_date)`: login events associating an account with a calendar
  date. Duplicate `(id, login_date)` rows may occur.

Let $A$ be the number of account rows and $L$ the number of distinct
account-date pairs after duplicate login events are removed.

**Return value**

Return a relation with columns `id` and `name`. Include an account exactly when
some run of at least five distinct login dates has no missing calendar day.
Produce at most one row per account and order rows by `id` ascending.

### Examples
**Example 1**

- Input: `Accounts = [(1, "Winston"), (7, "Jonathan")]`, `Logins = [(7, "2020-05-30"), (1, "2020-05-30"), (7, "2020-05-31"), (7, "2020-06-01"), (7, "2020-06-02"), (7, "2020-06-02"), (7, "2020-06-03"), (1, "2020-06-07"), (7, "2020-06-10")]`
- Output: `[(7, "Jonathan")]`
- Explanation: Account `7` has five consecutive distinct dates from May 30
  through June 3. Its duplicate June 2 event counts as the same day.

**Example 2**

- Input: `Accounts = [(2, "Ada")]`, `Logins = [(2, "2022-01-01"), (2, "2022-01-02"), (2, "2022-01-03"), (2, "2022-01-04"), (2, "2022-01-05")]`
- Output: `[(2, "Ada")]`

**Example 3**

- Input: `Accounts = [(3, "Lin")]`, `Logins = [(3, "2022-02-01"), (3, "2022-02-02"), (3, "2022-02-04"), (3, "2022-02-05"), (3, "2022-02-06")]`
- Output: `[]`
- Explanation: Five distinct dates exist, but the gap on February 3 prevents a
  five-day consecutive run.

### Required Complexity
- **Time:** $O(L\log L+A)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

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

#### Complexity detail

Deduplicating and partition-ordering $L$ account-date pairs requires
$O(L\log L)$ logical time without relying on an existing covering index. The
window scan, island aggregation, join over $A$ accounts, and final output work
are linear after their required ordering, giving $O(L\log L+A)$ overall.

The distinct dates, window state, and island groups require $O(L)$ working
space. Database engines may use indexes, external sorting, or streaming plans
that change physical constants, but the stated bound does not assume them.

#### Alternatives and edge cases

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

</details>
