## Examples

**Example 1**

- Input: `n = 3, target = 0`
- Output: `[-3,1,2]`
- Explanation:

  The complete set of arrays whose sum is `0` and whose absolute values are a permutation of size `3` is:

  - `[-3,1,2]`
  - `[-3,2,1]`
  - `[-2,-1,3]`
  - `[-2,3,-1]`
  - `[-1,-2,3]`
  - `[-1,3,-2]`
  - `[1,-3,2]`
  - `[1,2,-3]`
  - `[2,-3,1]`
  - `[2,1,-3]`
  - `[3,-2,-1]`
  - `[3,-1,-2]`

  The lexicographically smallest member of this list is `[-3,1,2]`.

**Example 2**

- Input: `n = 1, target = 10000000000`
- Output: `[]`
- Explanation: No length-one array whose sole absolute value is `1` can sum to `10000000000`. Therefore, no valid array exists and the result is `[]`.
