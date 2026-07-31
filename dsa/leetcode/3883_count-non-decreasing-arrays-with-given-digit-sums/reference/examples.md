## Examples

**Example 1**

- Input: `digitSum = [25,1]`
- Output: `6`
- Explanation: The values from `0` through `5000` whose digits sum to `25` and can start a valid pair are `799`, `889`, `898`, `979`, `988`, and `997`. To follow any of them with digit sum `1` without decreasing, the second value must be `1000`. The six valid arrays are `[799, 1000]`, `[889, 1000]`, `[898, 1000]`, `[979, 1000]`, `[988, 1000]`, and `[997, 1000]`.

**Example 2**

- Input: `digitSum = [1]`
- Output: `4`
- Explanation: The four one-element arrays are `[1]`, `[10]`, `[100]`, and `[1000]`; each value has decimal digit sum `1`.

**Example 3**

- Input: `digitSum = [2,49,23]`
- Output: `0`
- Explanation: No integer in the permitted range from `0` through `5000` has decimal digit sum `49`, so no value can occupy the second position and no valid array exists.
