## Examples

**Example 1**

- Input: `nums = [3,1,2], k = 8, m = 2`
- Output: `6`
- Explanation:
  - A subset of two elements is required; choose indices `[0, 2]`.
  - Increase `nums[0]` from `3` to `6` with `3` operations, and increase `nums[2]` from `2` to `6` with `4` operations.
  - The total cost is `7`, which does not exceed `k = 8`.
  - The chosen values become `[6, 6]`, whose bitwise AND is `6`; no larger result is possible.

**Example 2**

- Input: `nums = [1,2,8,4], k = 7, m = 3`
- Output: `4`
- Explanation:
  - A subset of three elements is required; choose indices `[0, 1, 3]`.
  - Increase `nums[0]` from `1` to `4` using `3` operations, increase `nums[1]` from `2` to `4` using `2` operations, and leave `nums[3] = 4` unchanged.
  - These changes use `5` operations, within the budget `k = 7`.
  - The selected values become `[4, 4, 4]`, and their maximum possible bitwise AND is `4`.

**Example 3**

- Input: `nums = [1,1], k = 3, m = 2`
- Output: `2`
- Explanation:
  - Both indices `[0, 1]` must be selected because `m = 2`.
  - Increase each value from `1` to `2`, costing one operation per index.
  - The total cost is `2`, which is no more than `k = 3`.
  - The chosen values become `[2, 2]`, whose maximum possible bitwise AND is `2`.
