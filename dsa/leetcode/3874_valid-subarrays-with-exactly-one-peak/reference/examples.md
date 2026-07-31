## Examples

**Example 1**

- Input: `nums = [1,3,2], k = 1`
- Output: `4`

- **Explanation:** Index `1` is a peak because `3` is greater than both `1` and `2`. Every valid interval must contain index `1`, and each endpoint may be at most one position away. The valid subarrays are `[3]`, `[1, 3]`, `[3, 2]`, and `[1, 3, 2]`, giving `4`.

**Example 2**

- Input: `nums = [7,8,9], k = 2`
- Output: `0`

- **Explanation:** No interior value is greater than both of its neighbors, so the original array has no peak. Consequently, no subarray can contain exactly one peak.

**Example 3**

- Input: `nums = [4,3,5,1], k = 2`
- Output: `6`

- **Explanation:** Index `2` is a peak because `5` exceeds its neighbors `3` and `1`. The valid subarrays are `[5]`, `[3, 5]`, `[5, 1]`, `[3, 5, 1]`, `[4, 3, 5]`, and `[4, 3, 5, 1]`. Each contains that peak, contains no other peak, and keeps both endpoints within distance `2`, so the answer is `6`.
