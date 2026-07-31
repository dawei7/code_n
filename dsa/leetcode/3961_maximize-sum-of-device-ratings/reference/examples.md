## Examples

**Example 1**

- Input: `units = [[1,3],[2,2]]`
- Output: `4`
- **Explanation:** Select device `0` and transfer its unit of capacity `1` to device `1`.
  - Device `0` becomes `[3]`, so its rating is `3`.
  - Device `1` becomes `[2, 2, 1]`, so its rating is `1`.
  - The resulting sum is `3 + 1 = 4`.

**Example 2**

- Input: `units = [[1,2,3],[4,5,6]]`
- Output: `6`
- **Explanation:** Select device `1` and transfer its unit of capacity `4` to device `0`.
  - Device `0` becomes `[1, 2, 3, 4]`, so its rating remains `1`.
  - Device `1` becomes `[5, 6]`, so its rating becomes `5`.
  - The resulting sum is `1 + 5 = 6`.

**Example 3**

- Input: `units = [[5,5,5],[1,1,1]]`
- Output: `6`
- **Explanation:** No transfer can increase the existing rating sum `5 + 1 = 6`, so performing zero operations is optimal.
