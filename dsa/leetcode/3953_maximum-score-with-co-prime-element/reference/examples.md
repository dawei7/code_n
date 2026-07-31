## Examples

**Example 1**

- Input: `nums = [3,4,6], maxVal = 5`
- Output: `4`
- Explanation:
  - Change `nums[2]` from `6` to `5`, paying one modification.
  - Select the final value `5`, which is co-prime with both `3` and `4`.
  - Here `selectedValue = 5` and `modificationCost = 1`, so the score is `5 - 1 = 4`.

**Example 2**

- Input: `nums = [1,2,3], maxVal = 4`
- Output: `3`
- Explanation:
  - No element needs to change.
  - Select `nums[2] = 3`, which is co-prime with `1` and `2`.
  - With `selectedValue = 3` and `modificationCost = 0`, the score is `3 - 0 = 3`.

**Example 3**

- Input: `nums = [2,2], maxVal = 1`
- Output: `1`
- Explanation:
  - Change `nums[0]` from `2` to `1`, which costs one modification.
  - Select the unchanged `nums[1] = 2`; it is co-prime with the new value `1`.
  - Therefore `selectedValue = 2`, `modificationCost = 1`, and the score is `2 - 1 = 1`.
