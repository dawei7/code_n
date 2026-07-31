## Examples

**Example 1**

- Input: `nums = [1,2,3,3], k = 2`
- Output: `3`
- Explanation:

  - Partition the cycle into `[2,3]` and `[3,1]`; the second part wraps from the array's end to its beginning.
  - The range of `[2,3]` is `max(2, 3) - min(2, 3) = 3 - 2 = 1`.
  - The range of `[3,1]` is `max(3, 1) - min(3, 1) = 3 - 1 = 2`.
  - The resulting score is `1 + 2 = 3`.

**Example 2**

- Input: `nums = [1,2,3,3], k = 1`
- Output: `2`
- Explanation:

  - Use the single part `[1,2,3,3]`.
  - Its range is `max(1, 2, 3, 3) - min(1, 2, 3, 3) = 3 - 1 = 2`.
  - The partition score is `2`.

**Example 3**

- Input: `nums = [1,2,3,3], k = 4`
- Output: `3`
- Explanation: As in Example 1, use `[2,3]` and the wrapped part `[3,1]`. A valid partition may contain fewer than `k` subarrays, so these two parts still achieve score `3`.
