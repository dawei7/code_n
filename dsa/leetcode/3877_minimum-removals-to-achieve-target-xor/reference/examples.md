## Examples

**Example 1**

- Input: `nums = [1,2,3], target = 2`
- Output: `1`

- **Explanation:** Remove `nums[1] = 2`, leaving `[nums[0], nums[2]] = [1, 3]`. Their XOR is `1 ^ 3 = 2`, which equals `target`. Keeping every element gives XOR `0`, so zero removals cannot work; therefore the minimum is `1`.

**Example 2**

- Input: `nums = [2,4], target = 1`
- Output: `-1`

- **Explanation:** None of the possible retained subsets has XOR `1`, so the target cannot be achieved and the answer is `-1`.

**Example 3**

- Input: `nums = [7], target = 7`
- Output: `0`

- **Explanation:** The XOR of all elements is already `nums[0] = 7`, which equals `target`. No removal is necessary.
