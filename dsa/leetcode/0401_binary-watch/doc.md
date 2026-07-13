# Binary Watch

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 401 |
| Difficulty | Easy |
| Topics | Backtracking, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-watch/) |

## Problem Description
### Goal
On a binary watch, four LEDs encode an hour from `0` through `11` and six LEDs encode minutes from `0` through `59`. Given `turned_on`, consider all valid times whose combined hour and minute representations contain exactly that many lit bits.

Return every matching time in any order. Format the hour without a leading zero and the minute with exactly two decimal digits, such as `"1:05"`. Exclude bit patterns that would represent invalid hours or minutes even when their total lit count matches. Each valid clock time appears once, and impossible LED counts produce an empty list.

### Function Contract
**Inputs**

- `turned_on`: the total number of lit hour and minute LEDs

**Return value**

- Return all valid times in any order. Format hours without a leading zero and minutes with exactly two digits.

### Examples
**Example 1**

- Input: `turned_on = 0`
- Output: `["0:00"]`

**Example 2**

- Input: `turned_on = 1`
- Output: `["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]`

**Example 3**

- Input: `turned_on = 9`
- Output: `[]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Enumerate the watch's finite display domain**

A valid watch time has an hour from 0 through 11 and a minute from 0 through 59, only 720 pairs in total. Visit each pair once rather than generating invalid 10-bit LED masks and decoding them afterward.

**Count lit LEDs through the represented values**

The hour LEDs encode the hour's binary bits and the minute LEDs encode the minute's bits. Therefore the display has exactly `bit_count(hour) + bit_count(minute)` lit LEDs. Keep a pair when that sum equals `turned_on`.

**Format only accepted times**

For each match, render the hour normally and the minute with two decimal positions. Since enumeration uses only valid clock ranges, no additional rejection for hours 12–15 or minutes 60–63 is needed.

**Why the output is complete and unique**

Every valid display corresponds to exactly one hour-minute pair in the enumerated ranges, and every such pair is examined. The bit-count test accepts precisely those with the requested LED total. Each pair occurs once, so the result has neither omissions nor duplicates.

#### Complexity detail

The watch always has exactly 12 times 60 candidate displays, independent of input magnitude, so enumeration takes $O(1)$ time. Apart from the required result strings, the algorithm uses $O(1)$ space.

#### Alternatives and edge cases

- **Backtrack over ten LED positions:** can generate masks with exactly the requested count, but must reject hour and minute bit patterns outside their valid ranges.
- **Enumerate all 1,024 bit masks:** is also constant for this fixed device but examines more invalid states.
- **Precompute by LED count:** makes repeated calls simple at the cost of storing all valid formatted times.
- With zero LEDs lit, the sole result is `0:00`.
- Counts above eight produce no valid time because the maximum valid display uses eight lit LEDs.
- Minute values below ten require a leading zero.
- Result order is not part of the contract.

</details>
