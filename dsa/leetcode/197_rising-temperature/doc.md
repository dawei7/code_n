# Rising Temperature

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 197 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/rising-temperature/) |

## Problem Description
### Goal
The `Weather` table records one observation per date, including a row identifier, calendar date, and temperature. Compare an observation only with the record from the previous day, exactly one calendar day earlier, rather than with whichever row has the next smaller identifier or date.

Return one column named `id` containing each current-day row whose temperature is higher than the previous day's temperature, in any order. A row does not qualify when no observation exists for the prior calendar day, when the temperatures are equal, or when the temperature fell. Return the warmer current row's identifier rather than its predecessor's.

### Function Contract
**Inputs**

- `Weather(id, recordDate, temperature)`: one observation per recorded date

**Return value**

One column named `id` containing qualifying current-day row ids.

### Examples
**Example 1**

- Temperatures on consecutive days: `10, 25, 20, 30`
- Output: ids for `25` and `30`

**Example 2**

- Equal consecutive temperatures
- Output: no id for the second day

**Example 3**

- Two records are separated by a missing date
- Output: no comparison across the gap

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

The comparison is between adjacent **calendar dates**, not adjacent ids or adjacent rows after sorting. Give `Weather` two aliases—`current` and `previous`—and self-join them only when the current date is exactly one day after the previous date.

Date arithmetic is dialect-specific. The native MySQL artifact can use `DATEDIFF(current.recordDate, previous.recordDate) = 1`; the app's SQLite adapter uses the equivalent Julian-day difference. Keeping the relationship as date arithmetic prevents a missing observation from being treated as yesterday merely because it is the preceding stored row.

After forming valid day pairs, filter with `current.temperature > previous.temperature` and project `current.id`. The comparison is strict: equal temperature is not a rise.

For observations on January 1, January 2, and January 4, only January 2 can compare with January 1. January 4 must not compare with January 2 because the difference is two days, even if those rows are consecutive in a sorted query result.

Every joined pair differs by exactly one calendar day, so a current row passes the temperature predicate only when it is warmer than its actual preceding day's observation. Thus every returned id qualifies. Conversely, any qualifying row has a recorded previous calendar day; those two rows satisfy the date join, and the higher current temperature satisfies the filter, so its id is returned. Missing dates form no pair and are correctly ignored.

#### Complexity detail

Without an appropriate date index, matching or ordering `n` observations generally takes $O(n \log n)$ work and up to $O(n)$ index or temporary state. A unique/indexed `recordDate` can support efficient predecessor lookup and may yield near-linear logical execution. Physical costs depend on the engine.

#### Alternatives and edge cases

- `LAG` over date order is concise, but it must also compare the two dates; otherwise it bridges gaps.
- Joining or ordering by `id` is incorrect because identifiers do not define calendar adjacency.
- A correlated lookup for `current_date - 1 day` mirrors the definition but may repeat searches without an index.
- The earliest recorded date has no predecessor. Equal or lower temperatures do not qualify.
- The one-observation-per-date contract avoids multiple previous-day matches.

</details>
