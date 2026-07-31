## Examples

**Example 1**

- Input: `items = [[1,6],[2,4],[3,5]], budget = 19`
- Output: `5`
- Explanation:
  - Buy two copies of type `0` and one copy of type `1`. The cost is `2 * 6 + 4 = 16`, which does not exceed `19`.
  - Use one purchased copy of type `0` to receive type `1` for free, since factor `1` divides factor `2`.
  - Use the other purchased copy of type `0` to receive type `2` for free, since factor `1` also divides factor `3`.
  - The result contains three purchased copies and two free copies, totaling `5`.

**Example 2**

- Input: `items = [[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]], budget = 35`
- Output: `7`
- Explanation:
  - Buy two copies of type `0`, one copy of type `1`, and one copy of type `2`. They cost `2 * 8 + 10 + 6 = 32`, within the budget.
  - The two type-`0` purchases award types `2` and `3`, because factor `2` divides factors `6` and `4`.
  - The type-`1` purchase awards another copy of type `2`, because factor `1` divides factor `6`. Receiving type `2` from both sources is permitted.
  - Type `2` cannot award a free copy because factor `6` divides no other indexed type's factor.
  - Four purchased copies and three free copies give a total of `7`.
