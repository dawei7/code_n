## Examples

**Example 1**

- Input: `nums = [3,1,2,5,4], k = 3`
- Output: `0`
- Explanation: Examine all three subarrays of length `3`; the pair indices below are relative to the particular subarray.
  - `[3,1,2]` contains two inversions, `(0,1)` and `(0,2)`.
  - `[1,2,5]` contains no inversions.
  - `[2,5,4]` contains one inversion, `(1,2)`.

  Thus the minimum is `0`, attained by `[1,2,5]`.

**Example 2**

- Input: `nums = [5,3,2,1], k = 4`
- Output: `6`
- Explanation: The entire array, `[5,3,2,1]`, is the only length-`4` subarray. Its inversions are `(0,1)`, `(0,2)`, `(0,3)`, `(1,2)`, `(1,3)`, and `(2,3)`. There are six in total, so `6` is also the minimum.

**Example 3**

- Input: `nums = [2,1], k = 1`
- Output: `0`
- Explanation: Each length-`1` subarray has only one element, so it cannot contain a pair of indices and therefore cannot contain an inversion. The minimum is `0`.
