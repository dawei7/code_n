## Examples

**Example 1**

- Input: `lists = [[1,3,5],[2,4],[6,7,8]]`
- Output: `18`
- Explanation:
  1. Merge `a = [1,3,5]` with `b = [2,4]`. Their lengths are `3` and `2`, and their medians are `3` and `2`, so this merge costs `3 + 2 + abs(3 - 2) = 6`. The current lists become `[[1,2,3,4,5],[6,7,8]]`.
  2. Merge `a = [1,2,3,4,5]` with `b = [6,7,8]`. Their lengths are `5` and `3`, and their medians are `3` and `7`, so this merge costs `5 + 3 + abs(3 - 7) = 12`.
  3. The only remaining list is `[1,2,3,4,5,6,7,8]`, and the total cost is `6 + 12 = 18`.

**Example 2**

- Input: `lists = [[1,1,5],[1,4,7,8]]`
- Output: `10`
- Explanation:
  - The two lengths are `3` and `4`, while the medians are `1` and `4`. Their merge costs `3 + 4 + abs(1 - 4) = 10`.
  - The resulting list is `[1,1,1,4,5,7,8]`, so the total cost is `10`.

**Example 3**

- Input: `lists = [[1],[3]]`
- Output: `4`
- Explanation:
  - Both lists have length `1`, with medians `1` and `3`. Merging them costs `1 + 1 + abs(1 - 3) = 4`.
  - The resulting list is `[1,3]`, and the total cost is `4`.

**Example 4**

- Input: `lists = [[1],[1]]`
- Output: `2`
- Explanation:
  - The only merge costs `1 + 1 + abs(1 - 1) = 2`.
