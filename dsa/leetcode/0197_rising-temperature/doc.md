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
