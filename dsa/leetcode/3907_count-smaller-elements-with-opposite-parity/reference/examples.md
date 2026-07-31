## Examples

**Example 1**

- Input: `nums = [5,2,4,1,3]`
- Output: `[2,1,2,0,0]`
- Explanation: At index `0`, the smaller opposite-parity values are `nums[1] = 2` and `nums[2] = 4`. At index `1`, only `nums[3] = 1` qualifies. At index `2`, both `nums[3] = 1` and `nums[4] = 3` qualify. Neither of the final two indices has a valid value to its right, producing `[2,1,2,0,0]`.

**Example 2**

- Input: `nums = [4,4,1]`
- Output: `[1,1,0]`
- Explanation: The last value, `1`, is smaller than each preceding `4` and has the opposite parity, so both of the first two scores are `1`. The final score is `0` because no index follows it.

**Example 3**

- Input: `nums = [7]`
- Output: `[0]`
- Explanation: A one-element array has no position to the right of index `0`, so its only score is `0`.
