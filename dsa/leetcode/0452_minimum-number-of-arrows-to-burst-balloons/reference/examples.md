## Examples

**Example 1**

- Input: `points = [[10,16],[2,8],[1,6],[7,12]]`
- Output: `2`
- **Explanation:** Fire one arrow at `x = 6` to burst `[2,8]` and `[1,6]`. Fire a second at `x = 11` to burst `[10,16]` and `[7,12]`.

**Example 2**

- Input: `points = [[1,2],[3,4],[5,6],[7,8]]`
- Output: `4`
- **Explanation:** The four intervals are disjoint, so each balloon needs its own arrow.

**Example 3**

- Input: `points = [[1,2],[2,3],[3,4],[4,5]]`
- Output: `2`
- **Explanation:** An arrow at `x = 2` bursts `[1,2]` and `[2,3]`. Another at `x = 4` bursts `[3,4]` and `[4,5]`.
