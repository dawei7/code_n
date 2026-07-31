## Examples

**Example 1**

- Input: `nums = [3,1,2], queries = [[0,1],[1,2],[0,2]]`
- Output: `[2,3,4]`
- Explanation:

  - For `queries[0] = [0,1]`, the selected segment is `[nums[0],nums[1]] = [3,1]`. Its stable subarrays are `[3]` and `[1]`, so this query contributes `2`.
  - For `queries[1] = [1,2]`, the selected segment is `[nums[1],nums[2]] = [1,2]`. Its stable subarrays are `[1]`, `[2]`, and `[1,2]`, giving `3`.
  - For `queries[2] = [0,2]`, the selected segment is `[nums[0],nums[1],nums[2]] = [3,1,2]`. Its stable subarrays are `[3]`, `[1]`, `[2]`, and `[1,2]`, giving `4`.

  Thus, `ans = [2,3,4]`.

**Example 2**

- Input: `nums = [2,2], queries = [[0,1],[0,0]]`
- Output: `[3,1]`
- Explanation:

  - For `queries[0] = [0,1]`, the selected segment is `[nums[0],nums[1]] = [2,2]`. Its stable subarrays are the first `[2]`, the second `[2]`, and `[2,2]`, giving `3`.
  - For `queries[1] = [0,0]`, the selected segment is `[nums[0]] = [2]`. Its sole stable subarray is `[2]`, giving `1`.

  Thus, `ans = [3,1]`.
