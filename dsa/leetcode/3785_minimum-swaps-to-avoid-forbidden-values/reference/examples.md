## Examples

**Example 1**

- Input: `nums = [1,2,3], forbidden = [3,2,1]`
- Output: `1`
- Explanation:
  - One optimal choice swaps indices `i = 0` and `j = 1`.
  - This changes `nums` to `[2,1,3]`, where every value differs from the forbidden value at its index.

**Example 2**

- Input: `nums = [4,6,6,5], forbidden = [4,6,5,5]`
- Output: `2`
- Explanation:
  - First swap indices `i = 0` and `j = 2`, producing `nums = [6,6,4,5]`.
  - Then swap indices `i = 1` and `j = 3`, producing `nums = [6,5,4,6]`.
  - After these two swaps, no index contains its forbidden value.

**Example 3**

- Input: `nums = [7,7], forbidden = [8,7]`
- Output: `-1`
- Explanation:
  - The two available values are both `7`, so no rearrangement can prevent index `1` from containing its forbidden value `7`.

**Example 4**

- Input: `nums = [1,2], forbidden = [2,1]`
- Output: `0`
- Explanation:
  - Both indices already avoid their forbidden values, so no swap is required.
