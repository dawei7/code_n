## Examples

**Example 1**

- Input: `nums = [5,0,1,4], k = 3`
- Output: `3`
- Explanation:
  - At index `0`, the prefix `[5]` has maximum `5`, the suffix `[5, 0, 1, 4]` has minimum `0`, and the score is `5 - 0 = 5`.
  - At index `1`, the maximum of `[5, 0]` is `5`, the minimum of `[0, 1, 4]` is `0`, and the score remains `5 - 0 = 5`.
  - At index `2`, the prefix maximum is `5`, the suffix `[1, 4]` has minimum `1`, and the score is `5 - 1 = 4`.
  - At index `3`, the prefix maximum is `5`, the suffix `[4]` has minimum `4`, and the score is `5 - 4 = 1`.
  - Index `3` is the first score not exceeding `k = 3`, so it is returned.

**Example 2**

- Input: `nums = [3,2,1], k = 1`
- Output: `-1`
- Explanation:
  - The instability score at index `0` is `3 - 1 = 2`.
  - At index `1`, it is again `3 - 1 = 2`.
  - At index `2`, it is also `3 - 1 = 2`.
  - Every score is greater than `k = 1`, so there is no stable index and the result is `-1`.

**Example 3**

- Input: `nums = [0], k = 0`
- Output: `0`
- Explanation:
  - At index `0`, both the prefix maximum and suffix minimum are `0`. The score is therefore `0 - 0 = 0`, which meets `k = 0`, so index `0` is returned.
