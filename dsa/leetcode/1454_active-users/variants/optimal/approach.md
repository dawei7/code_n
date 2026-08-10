## General

**First reduce login events to login days.** A user may log in multiple times on the same date, but consecutive activity is measured in distinct calendar days. Counting raw rows could falsely turn several same-day events into a five-day streak.

The first common table expression, `T`, joins `Logins` with `Accounts` through their shared `id` and applies `SELECT DISTINCT *`. The join attaches the account name to each login. Because `Accounts.id` is a primary key, one login ID matches at most one name. `DISTINCT` then collapses duplicate joined rows for the same account and date.

After `T`, each user-date combination appears once. This makes a later `COUNT(*)` count calendar days rather than login events. Joining early also carries `name` into the later rows so the final result can return it.

**Turn consecutive dates into a common island key.** The second common table expression, `P`, assigns
`ROW_NUMBER() OVER (PARTITION BY id ORDER BY login_date)`
to each user's distinct dates. Row numbers restart at one for each account and increase in date order.

For each row, the query subtracts that row number in days from `login_date`. The result is named `g`. This subtraction creates the classic gaps-and-islands key.

Consider consecutive dates May 30, May 31, June 1, June 2, and June 3. Their row numbers are one through five. Subtracting one day from May 30 gives May 29. Subtracting two days from May 31 also gives May 29. The same is true for the remaining consecutive dates. Both the date and row number advance by one, so their difference stays constant.

Now suppose the next login is June 10 with row number six. Subtracting six days gives June 4, not May 29. The calendar gap advances the date by more than the row number advanced, so a new key appears. Thus equal `id, g` values identify one uninterrupted run of distinct login dates.

Partitioning the row number by `id` is essential. Different users may log in on the same date and obtain the same shifted date, but their streaks must never mix. The final grouping includes `id` as well as `g` for the same reason.

**Count the length of each island.** The outer query groups `P` by `id, g`. Every group is one consecutive-date streak for one user. Because duplicate same-day events were removed in `T`, `COUNT(*)` is exactly the number of days in that streak.

`HAVING COUNT(*) >= 5` retains only streak groups of at least five days. `HAVING` is used instead of `WHERE` because the condition depends on the aggregate count after grouping.

The selected columns are `id` and `name`. The account table guarantees one name for each ID, so every row in an ID's streak has the same name. MySQL can use that functional dependency even though `name` is not written in the `GROUP BY` list.

**Remove duplicates caused by multiple qualifying streaks.** One user might have two separate streaks of at least five days. Grouping by `id, g` produces one qualifying row for each streak. The output, however, should include the active user only once. The outer `SELECT DISTINCT id, name` collapses those multiple qualifying islands into one account row.

Finally, `ORDER BY 1` sorts by the first selected column, `id`, in ascending order as required.

**Trace the sample user.** User seven logs in on May 30, May 31, June 1, June 2, June 2 again, June 3, and June 10. `DISTINCT` removes the duplicate June 2 event. The first five distinct dates receive row numbers one through five and the same shifted key, forming a group of count five. June 10 has a different key and forms a one-day group. The five-day group passes `HAVING`, so user seven is returned.

User one has only May 30 and June 7. Their shifted keys differ because the dates are not consecutive, and each group has count one. Neither passes the threshold.

**Why subtracting row number works across months and years.** `DATE_SUB` performs calendar-day arithmetic, not subtraction on textual date components. May 31 followed by June 1 is one consecutive day, and December 31 followed by January 1 is also one. The database's date operations handle those boundaries.

**Why every returned user is active.** A returned row came from some group with one `id` and one shifted key `g` containing at least five distinct ordered dates. For any adjacent rows in a constant-key group, the row number increases by one. Equality of shifted dates then forces the login date also to increase by exactly one day. The group is therefore an uninterrupted sequence of at least five login days.

Conversely, take any user with at least five consecutive distinct login dates. Ordering gives those dates consecutive row numbers. Subtracting their corresponding row numbers produces the same `g` for all of them, so they enter one group whose count is at least five. That group passes `HAVING`, and `DISTINCT` preserves one output row for the user. Thus no active user is missed.

**Generalize the follow-up naturally.** If active meant at least some parameter `n` consecutive days, the grouping logic would not change. Only the threshold in `HAVING COUNT(*) >= n` would change. The gaps-and-islands key describes streaks independently of the chosen minimum length.

## Complexity detail

Let `A` be the number of account rows and `L` the number of distinct `id, login_date` pairs after duplicate removal. Joining accounts to logins and deduplicating requires reading the relevant rows; with suitable keys, this contributes roughly `O(A + L)` plus the work needed to eliminate raw duplicates.

The window function must order each user's dates. Across all users, comparison sorting is bounded by `O(L log L)`. Computing row numbers, shifted keys, grouping the resulting rows, and applying counts are linear expected work after ordering. The final result contains at most `A` users.

The conventional bound is therefore `O(L log L + A)` time. Intermediate distinct rows, ordered window data, and groups can require `O(L)` space, matching the manifest. The final output is at most `O(A)`.

A database optimizer may exploit indexes on `id, login_date`, combine sorts, use hash aggregation, or spill intermediates to disk. SQL complexity describes the logical sort-and-group strategy rather than requiring a particular physical plan.

If raw `Logins` contains many duplicates, reading and deduplicating those raw rows also costs time proportional to their actual count. The contract's symbol `L` denotes distinct pairs, while real execution must still scan the source events unless an index or prior uniqueness structure avoids that work.

## Alternatives and edge cases

- **LAG plus break markers:** Compare each date with the previous date, mark the start of a new streak, take a cumulative sum of breaks, and group by that island number. It is more verbose but expresses gaps explicitly.
- **Self-join five dates:** Join each distinct login date to dates one through four days later for the same ID. This can solve a fixed threshold but becomes cumbersome and duplicates work; the row-number key generalizes cleanly.
- **Correlated existence checks:** Test whether four required following dates exist for each date. Indexes can help, but the logic repeats lookups and is less convenient for a variable threshold.
- **Count raw login rows:** This is wrong because multiple logins on one day do not represent consecutive days. Deduplication must happen first.
- **Group only by g:** Different users can share the same shifted date. `id` must remain part of the grouping key.
- **Omit final DISTINCT:** A user with two separate qualifying streaks would appear twice. The result requires one account row.
- **Exactly five consecutive days:** The streak group count is five and passes the inclusive `>= 5` test.
- **Longer streak:** All of its dates share one key, and its larger count also passes.
- **Duplicate logins on a streak day:** `T` collapses them, so they neither inflate the length nor break the sequence.
- **Several separated streaks:** Different gaps create different `g` values. Any qualifying group makes the user active.
- **Five total days with gaps:** They form multiple smaller groups and do not pass merely because their total count is five.
- **Month boundary:** Calendar subtraction keeps adjacent dates in the same island.
- **Year boundary and leap day:** SQL date arithmetic handles actual consecutive calendar days across these boundaries.
- **Account with no login:** It has no row in `T` and cannot appear in the active result.
- **Login ID without an account outside the contract:** The inner join would discard it because no name can be returned. The expected relational data associates login IDs with accounts.
- **Same name for different IDs:** Grouping and identity use `id`, so two accounts may share a display name without being merged.
- **General threshold n:** Replace five in `HAVING` with the desired threshold; duplicate removal and island construction remain identical.
- **Ordered output:** `ORDER BY 1` refers to selected `id`. Writing `ORDER BY id` would be equivalent and more explicit.
