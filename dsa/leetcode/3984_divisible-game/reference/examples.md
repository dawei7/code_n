## Examples

**Example 1**

- Input: `nums = [1,4,6,8]`
- Output: `36`
- **Explanation:** Alice can take `k = 2` and the inclusive range `[1,3]`. Its values `4`, `6`, and `8` are all divisible by `2`, so Alice receives `4 + 6 + 8 = 18` and Bob receives `0`. The difference `18` is the greatest attainable difference, and `2` is the smallest $k$ attaining it. Their product is `18 * 2 = 36`.

**Example 2**

- Input: `nums = [2,1,2]`
- Output: `6`
- **Explanation:** With `k = 2` and range `[0,2]`, the two values equal to `2` contribute `4` to Alice while the middle `1` contributes `1` to Bob. The difference is therefore `4 - 1 = 3`. This is maximal, and the smallest $k$ that reaches it is `2`, giving `3 * 2 = 6`.

**Example 3**

- Input: `nums = [1]`
- Output: `1000000005`
- **Explanation:** Alice must select an integer greater than `1`; the smallest legal choice is `k = 2`. The only array value is not divisible by `2`, so Alice scores `0`, Bob scores `1`, and the maximum possible difference is `-1`. The product is `-1 * 2 = -2`, whose residue modulo $10^9+7$ is `1000000005`.
