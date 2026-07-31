## Examples

**Example 1**

- Input: `nums = [1,2,3], target = [2,1,3]`
- Output: `2`
- Explanation:
  - Choose `x = 1`. Its only maximal segment is `[0, 0]`, so `nums` becomes `[2,2,3]`.
  - Choose `x = 2`. Its maximal segment is now `[0, 1]`. Position `0` stays `2`, while position `1` becomes `1`, producing `[2,1,3]`.

Thus, two operations transform `nums` into `target`.

**Example 2**

- Input: `nums = [4,1,4], target = [5,1,4]`
- Output: `1`
- Explanation:
  - Choose `x = 4`. The maximal segments are `[0, 0]` and `[2, 2]`. Position `0` becomes `5`, while position `2` stays `4`, producing `[5,1,4]`.

Therefore, one operation is sufficient.

**Example 3**

- Input: `nums = [7,3,7], target = [5,5,9]`
- Output: `2`
- Explanation:
  - Choose `x = 7`. Its maximal segments are `[0, 0]` and `[2, 2]`, so `nums` becomes `[5,3,9]`.
  - Choose `x = 3`. Its maximal segment is `[1, 1]`, so `nums` becomes `[5,5,9]`.

Hence, the transformation requires two operations.
