## Examples

**Example 1**

- Input: `nums = [1,4,2,8], k = 3`
- Output: `2`
- Explanation:
  - Choose residue `x = 1` for the even indices and residue `y = 2` for the odd indices.
  - Increment `nums[1] = 4` once, producing `[1,5,2,8]`.
  - Decrement `nums[2] = 2` once, producing `[1,5,1,8]`.
  - The even-index values now all have remainder `1`, while the odd-index values all have remainder `2`.
  - Exactly two operations were used, so the answer is `2`.

**Example 2**

- Input: `nums = [1,1,1], k = 3`
- Output: `1`
- Explanation:
  - Increment `nums[1]` once to obtain `[1,2,1]`.
  - The even indices then use residue `x = 1`, and the odd index uses the distinct residue `y = 2`.
  - Therefore one operation is sufficient and minimal.

**Example 3**

- Input: `nums = [6,7,8], k = 2`
- Output: `0`
- Explanation: The array already qualifies with residue `x = 0` at the even indices and residue `y = 1` at the odd index, so no operation is necessary.

