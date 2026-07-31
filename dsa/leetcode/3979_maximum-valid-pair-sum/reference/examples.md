## Examples

**Example 1**

- Input: `nums = [1,3,5,2,8], k = 2`
- Output: `13`
- **Explanation:** The valid pairs and their sums are `(0, 2)` with `1 + 5 = 6`, `(0, 3)` with `1 + 2 = 3`, `(0, 4)` with `1 + 8 = 9`, `(1, 3)` with `3 + 2 = 5`, `(1, 4)` with `3 + 8 = 11`, and `(2, 4)` with `5 + 8 = 13`. The greatest of these values is `13`.

**Example 2**

- Input: `nums = [5,1,9], k = 1`
- Output: `14`
- **Explanation:** With `k = 1`, every ordered index pair with `i < j` is valid. Pair `(0, 2)` gives the maximum sum, `nums[0] + nums[2] = 5 + 9 = 14`, so the answer is `14`.
