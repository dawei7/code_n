## Examples

**Example 1**

- Input: `n = 3, k = 1`
- Output: `["000","010","100"]`
- Explanation:
  - The length-three strings without consecutive ones are `"000"` with cost `0`, `"100"` with cost `0`, `"010"` with cost `1`, `"001"` with cost `2`, and `"101"` with cost `0 + 2 = 2`.
  - Only `"000"`, `"010"`, and `"100"` have cost at most `1`, so exactly those three strings are valid.

**Example 2**

- Input: `n = 1, k = 0`
- Output: `["0","1"]`
- Explanation:
  - Both length-one binary strings, `"0"` and `"1"`, avoid consecutive ones.
  - The only index is zero, so either string has cost `0` and both are valid.
