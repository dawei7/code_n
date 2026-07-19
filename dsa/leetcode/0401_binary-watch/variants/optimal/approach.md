## General
**Enumerate the watch's finite display domain**

A valid watch time has an hour from 0 through 11 and a minute from 0 through 59, only 720 pairs in total. Visit each pair once rather than generating invalid 10-bit LED masks and decoding them afterward.

**Count lit LEDs through the represented values**

The hour LEDs encode the hour's binary bits and the minute LEDs encode the minute's bits. Therefore the display has exactly `bit_count(hour) + bit_count(minute)` lit LEDs. Keep a pair when that sum equals `turned_on`.

**Format only accepted times**

For each match, render the hour normally and the minute with two decimal positions. Since enumeration uses only valid clock ranges, no additional rejection for hours 12–15 or minutes 60–63 is needed.

**Why the output is complete and unique**

Every valid display corresponds to exactly one hour-minute pair in the enumerated ranges, and every such pair is examined. The bit-count test accepts precisely those with the requested LED total. Each pair occurs once, so the result has neither omissions nor duplicates.

## Complexity detail
The watch always has exactly 12 times 60 candidate displays, independent of input magnitude, so enumeration takes $O(1)$ time. Apart from the required result strings, the algorithm uses $O(1)$ space.

## Alternatives and edge cases
- **Backtrack over ten LED positions:** can generate masks with exactly the requested count, but must reject hour and minute bit patterns outside their valid ranges.
- **Enumerate all 1,024 bit masks:** is also constant for this fixed device but examines more invalid states.
- **Precompute by LED count:** makes repeated calls simple at the cost of storing all valid formatted times.
- With zero LEDs lit, the sole result is `0:00`.
- Counts above eight produce no valid time because the maximum valid display uses eight lit LEDs.
- Minute values below ten require a leading zero.
- Result order is not part of the contract.
