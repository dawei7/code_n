## Examples

**Example 1**

- Input: `n = 5, brightness = 5, intervals = [[6,12]]`
- Output: `14`
- Explanation:
  - Turn on the bulbs at positions `1` and `4`, producing the state `0 1 0 0 1`.
  - Together they illuminate all five positions, meeting the required brightness.
  - The inclusive interval contains `12 - 6 + 1 = 7` time units.
  - Two bulbs used for seven time units consume `2 * 7 = 14` energy.

**Example 2**

- Input: `n = 2, brightness = 1, intervals = [[0,0],[2,2]]`
- Output: `2`
- Explanation:
  - One bulb is on during each active interval.
  - The two length-one intervals contribute `1 + 1 = 2` active time units.
  - One bulb over those two times uses `1 * 2 = 2` energy.

**Example 3**

- Input: `n = 4, brightness = 2, intervals = [[1,3],[2,4]]`
- Output: `4`
- Explanation:
  - A single bulb can illuminate at least two positions.
  - The intervals overlap, and their union is `[1,4]`, containing four time units.
  - One bulb used throughout that union consumes `1 * 4 = 4` energy.
