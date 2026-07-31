## Examples

**Example 1**

- Input: `items = [[6,2],[2,6],[3,4]], budget = 9`
- Output: `4`
- Explanation:
  - Buy two copies of type `0` and one copy of type `2`. Their cost is `2 * 2 + 4 = 8`, which is within the budget.
  - Activating type `2` awards one copy of type `0` because factor `3` divides factor `6`.
  - The result consists of three purchased copies and one free copy, totaling `4`.

**Example 2**

- Input: `items = [[2,4],[3,2],[4,1],[6,4],[12,4]], budget = 8`
- Output: `10`
- Explanation:
  - Buy one copy each of types `0` and `1`, plus two copies of type `2`. The purchase cost is `4 + 2 + 2 * 1 = 8`.
  - Type `0` awards free copies of types `2`, `3`, and `4`.
  - Type `1` awards free copies of types `3` and `4`.
  - Type `2` awards another free copy of type `4`.
  - There are four purchased copies and six free copies, so the total is `10`.
