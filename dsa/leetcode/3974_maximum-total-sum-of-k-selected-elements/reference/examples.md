## Examples

**Example 1**

- Input: `nums = [6,1,2,9], k = 3, mul = 2`
- Output: `26`
- **Explanation:** One optimal selection consists of `nums[3] = 9`, `nums[0] = 6`, and `nums[2] = 2`. Process `9` first and multiply it by the current value `2`, contributing `18`; the multiplier then becomes `1`. Process `6` next and multiply by `1`, contributing `6`; the multiplier becomes `0`. Process `2` last using ordinary addition, contributing `2`. The resulting total is `18 + 6 + 2 = 26`.

**Example 2**

- Input: `nums = [3,7,5,2], k = 2, mul = 4`
- Output: `43`
- **Explanation:** Select `nums[1] = 7` and `nums[2] = 5`. Multiplying `7` by the initial multiplier `4` contributes `28` and lowers the multiplier to `3`. Multiplying `5` by `3` then contributes `15`, producing the optimal total `28 + 15 = 43`.

**Example 3**

- Input: `nums = [4,4], k = 1, mul = 1`
- Output: `4`
- **Explanation:** Select `nums[0] = 4`. Multiplication by the current value `1` contributes `4`, equal to ordinary addition, so the final total is `4`.
