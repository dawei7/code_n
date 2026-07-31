## Examples

**Example 1**

- Input: `nums = [2,0,1], pre = [2,3]`
- Output: `2`
- **Explanation:** Reverse the allowed prefix of length `3` to obtain `[1, 0, 2]`. Then reverse the prefix of length `2` to obtain `[0, 1, 2]`. No one-operation sequence reaches the target, so the minimum is `2`.

**Example 2**

- Input: `nums = [1,0,2], pre = [1,3]`
- Output: `-1`
- **Explanation:** A reversal of length `1` changes nothing, while a reversal of length `3` only alternates between `[1, 0, 2]` and `[2, 0, 1]`. The sorted permutation is therefore unreachable.

**Example 3**

- Input: `nums = [0,1], pre = [2]`
- Output: `0`
- **Explanation:** The input is already in ascending order, so no prefix reversal is needed.
