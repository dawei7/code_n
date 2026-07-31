## Examples

**Example 1**

- Input: `nums = [1,2,3], swaps = [[0,2],[1,2]]`
- Output: `4`
- Explanation: The maximum is obtained by either `[2,1,3]` or `[3,1,2]`. For example, `[2,1,3]` can be reached through these allowed operations:

  1. Swap indices `0` and `2`, producing `[3,2,1]`.
  2. Swap indices `1` and `2`, producing `[3,1,2]`.
  3. Swap indices `0` and `2` again, producing `[2,1,3]`.

  Its alternating sum is `2 - 1 + 3 = 4`.

**Example 2**

- Input: `nums = [1,2,3], swaps = [[1,2]]`
- Output: `2`
- Explanation: Performing no swaps is optimal, leaving the alternating sum `1 - 2 + 3 = 2`.

**Example 3**

- Input: `nums = [1,1000000000,1,1000000000,1,1000000000], swaps = []`
- Output: `-2999999997`
- Explanation: No exchange is available, so the original arrangement is the only reachable one and therefore supplies the maximum alternating sum.
