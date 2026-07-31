## Examples

**Example 1**

- Input: `nums = [2,3,1,4], target1 = 1, target2 = 5`
- Output: `1`
- Explanation:
  - The block `[2, 3]` has XOR `1`, matching `target1`.
  - The remaining block `[1, 4]` has XOR `5`, matching `target2`.
  - No other partition has the required alternating XOR values, so the answer is `1`.

**Example 2**

- Input: `nums = [1,0,0], target1 = 1, target2 = 0`
- Output: `3`
- Explanation:
  - The single block `[1, 0, 0]` has XOR `1`, so it matches `target1`.
  - The two blocks `[1]` and `[0, 0]` have XOR values `1` and `0`, matching `target1` and `target2`.
  - The two blocks `[1, 0]` and `[0]` also have XOR values `1` and `0`.
  - These are the three valid partitions; therefore, the result is `3`.

**Example 3**

- Input: `nums = [7], target1 = 1, target2 = 7`
- Output: `0`
- Explanation:
  - The only possible block, `[7]`, has XOR `7` rather than `target1 = 1`, so no valid partition exists.
