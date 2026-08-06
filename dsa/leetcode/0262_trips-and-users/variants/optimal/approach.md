## General
**Eligibility depends on both participant rows**

Join `Trips` to `Users` once as the client and once as the driver. Filter both joined rows to `banned = 'No'`, and restrict request dates to the required inclusive range.

**A cancellation indicator turns the rate into an average**

Map `completed` to zero and every cancellation status to one. The average indicator within a date is exactly cancellations divided by eligible trips.

After participant and date filtering, every remaining row represents one eligible trip. Grouping by `request_at` therefore contains precisely the denominator for that day, and summing cancellation indicators gives its numerator.

**Filtering before grouping fixes the denominator**

The client and driver joins attach both ban flags to each trip, so the `WHERE` clause retains exactly trips whose two participants are unbanned and whose date is in range. Each surviving row contributes one to its day's denominator and contributes one to the numerator exactly when its status is cancelled. Averaging the indicator and rounding therefore produces the requested rate for each eligible date group.

## Complexity detail

Scanning `Trips` and performing two indexed participant lookups per row takes $O(t \log u)$ time. Filtering and
conditional aggregation add $O(t)$ work. At most three date groups survive the fixed range, so the final ordering is
$O(1)$. The user indexes occupy $O(u)$ space, while the aggregate state for the three dates is $O(1)$. A database
optimizer may instead choose equivalent hash joins with expected $O(t + u)$ time and $O(u)$ space.

## Alternatives and edge cases

- **Filter only clients:** incorrectly includes trips driven by banned users.
- **Integer division:** can collapse fractional rates; averaging numeric indicators avoids it.
- **Dates without eligible trips:** filtering removes every row, so no group and therefore no output row is produced.
- **Completed trips:** each contributes zero to the conditional average but still contributes to the denominator.
