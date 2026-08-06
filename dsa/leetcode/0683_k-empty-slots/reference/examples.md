## Examples

**Example 1**

- Input: `bulbs = [1,3,2], k = 1`
- Output: `2`
- Explanation: On day 1, `bulbs[0] = 1` turns on the first position, producing `[1,0,0]`. On day 2, `bulbs[1] = 3` turns on the third position, producing `[1,0,1]`. On day 3, `bulbs[2] = 2` turns on the second position, producing `[1,1,1]`. The answer is day 2 because positions 1 and 3 are on then, with exactly one bulb between them and that bulb still off.

**Example 2**

- Input: `bulbs = [1,2,3], k = 1`
- Output: `-1`
