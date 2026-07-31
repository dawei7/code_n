## Examples

**Example 1**

- Input: `cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2`
- Output: `3`
- Explanation:
  - Buy three type-3 items for `3 * 1 = 3`.
  - They contribute `3 >= need1 = 3` units toward type 1 and `3 >= need2 = 2` toward type 2.
  - Every other valid combination costs more, so the minimum is `3`.

**Example 2**

- Input: `cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3`
- Output: `22`
- Explanation:
  - Buy `need1 = 2` type-1 items and `need2 = 3` type-2 items.
  - The total is `2 * 5 + 3 * 4 = 10 + 12 = 22`.
  - Any use of the more expensive combined item gives a greater valid cost.

**Example 3**

- Input: `cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0`
- Output: `0`
- Explanation:
  - Both requirements are zero, so buying nothing is valid and costs `0`.
