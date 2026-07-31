## Examples

**Example 1**

- Input: `nums = [1,1,2,2,3,4]`
- Output: `[1,3]`
- Explanation:
  - The smallest present value is `1`, and it occurs twice.
  - Value `2` is the next larger value, but it also occurs twice, so `[1,2]` is not valid.
  - Value `3` occurs once. It is the smallest value greater than `1` whose frequency differs from the frequency of `1`, so the answer is `[1,3]`.

**Example 2**

- Input: `nums = [1,5]`
- Output: `[-1,-1]`
- Explanation: Both distinct values occur once. Their equal frequencies prevent the only possible pair from being valid, so no answer exists.

**Example 3**

- Input: `nums = [7]`
- Output: `[-1,-1]`
- Explanation: The array contains only one distinct value, so two distinct values cannot be selected.
