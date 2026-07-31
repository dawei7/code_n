## Examples

**Example 1**

- Input: `nums = [5,0,1,4], k = 3`
- Output: `3`
- Explanation:
  - At index `0`, the maximum of `[5]` is `5`, the minimum of `[5, 0, 1, 4]` is `0`, and the instability score is `5 - 0 = 5`.
  - At index `1`, the prefix `[5, 0]` still has maximum `5`, the suffix `[0, 1, 4]` has minimum `0`, and the score remains `5 - 0 = 5`.
  - At index `2`, the prefix maximum is `5`, the minimum of `[1, 4]` is `1`, and the score becomes `5 - 1 = 4`.
  - At index `3`, the prefix maximum is `5`, the suffix `[4]` has minimum `4`, and the score is `5 - 4 = 1`.
  - Index `3` is the first index whose score does not exceed `k = 3`, so the result is `3`.

**Example 2**

- Input: `nums = [3,2,1], k = 1`
- Output: `-1`
- Explanation:
  - At index `0`, the instability score is `3 - 1 = 2`.
  - At index `1`, the score is again `3 - 1 = 2`.
  - At index `2`, it remains `3 - 1 = 2`.
  - All three scores exceed `k = 1`; therefore, no stable index exists and the result is `-1`.

**Example 3**

- Input: `nums = [0], k = 0`
- Output: `0`
- Explanation:
  - At index `0`, the prefix maximum and suffix minimum are both `0`. The resulting score `0 - 0 = 0` is at most `k = 0`, so index `0` is returned.
