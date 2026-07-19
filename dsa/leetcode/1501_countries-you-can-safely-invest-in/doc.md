# Countries You Can Safely Invest In

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1501 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/countries-you-can-safely-invest-in/) |

## Problem Description
### Goal

The `Person` table identifies people and stores each telephone number in the form `xxx-yyyyyyy`, where the first three digits are a country code. The `Country` table translates those three-character codes into country names. The `Calls` table records a caller, a different callee, and the call duration in minutes; duplicate call rows are permitted.

For each country represented by a participant in at least one call, consider every call endpoint belonging to that country. A domestic call therefore contributes its duration twice to that country's calculation, once for each participant, while an international call contributes once to each participant's country. Return the countries whose endpoint-weighted average duration is strictly greater than the global average duration across call rows. Name the only output column `country`; result rows may appear in any order.

### Function Contract
**Inputs**

Let $P$, $C$, and $L$ be the row counts of `Person`, `Country`, and `Calls`, and let $E=2L$ be the number of call endpoints.

**`Person`**

| Column | Type | Meaning |
|---|---|---|
| `id` | int | Unique person identifier. |
| `name` | varchar | Person's name. |
| `phone_number` | varchar | Ten-character number `xxx-yyyyyyy`; the prefix is a country code and digits may have leading zeroes. |

**`Country`**

| Column | Type | Meaning |
|---|---|---|
| `name` | varchar | Country name. |
| `country_code` | varchar | Unique three-digit code, including any leading zeroes. |

**`Calls`**

| Column | Type | Meaning |
|---|---|---|
| `caller_id` | int | Person who placed the call. |
| `callee_id` | int | Different person who received it. |
| `duration` | int | Call duration in minutes. |

The table has no uniqueness guarantee, so equal call rows count independently.

**Return value**

Return one column named `country`. Include exactly the country names whose average over all incident call endpoints is strictly greater than `AVG(Calls.duration)`. Countries with no call endpoint are absent. Row order is unrestricted.

### Examples
**Example 1**

With people in Peru (`051`), Morocco (`212`), and Israel (`972`), and call durations `33, 4, 59, 102, 330, 5, 13, 3, 1, 7`, the global average is $55.7$. Peru's six endpoint contributions average about $145.67$, while Morocco and Israel remain below the global value.

- Output: `[["Peru"]]`

**Example 2**

- People: `[[1,"A","001-0000001"],[2,"B","002-0000002"],[3,"C","002-0000003"]]`
- Countries: `[["Alpha","001"],["Beta","002"]]`
- Calls: `[[1,2,10],[2,3,30]]`
- Output: `[["Beta"]]`
- Explanation: The global average is $20$. Alpha has endpoint average $10$, whereas Beta has endpoint values $10,30,30$ and therefore exceeds $20$.

**Example 3**

- People: `[[1,"A","001-0000001"],[2,"B","002-0000002"]]`
- Countries: `[["Alpha","001"],["Beta","002"],["Unused","003"]]`
- Calls: `[[1,2,7]]`
- Output: `[]`
- Explanation: Both represented countries have average $7$, exactly equal to the global average, and the comparison is strict. The country without a participant is not considered.
