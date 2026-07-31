## Examples

**Example 1**

- Input: `nums = [0,2,1]`
- Output: `2`
- Explanation: Rotate left once to obtain `[2,1,0]`, then reverse the entire array to obtain `[0,1,2]`. Sorting in fewer than two operations is impossible, so the minimum is two.

**Example 2**

- Input: `nums = [1,0,2]`
- Output: `2`
- Explanation: Reverse first, producing `[2,0,1]`, and then rotate left once to reach `[0,1,2]`. This two-operation sequence is minimal.

**Example 3**

- Input: `nums = [2,0,1,3]`
- Output: `-1`
- Explanation: Neither rotations of this permutation nor rotations of its reversal equal `[0,1,2,3]`. Increasing order is therefore unreachable with the permitted operations.
