## Examples

**Example 1**

- Input: `edges = [[0,1],[0,2],[0,3],[1,4],[1,5]], nums = [1,0,-10,3,4,5], k = 2`
- Output: `23`
- Explanation:
  - Invert the subtree rooted at node `2`.
  - That leaf value changes from `-10` to `10`, while every other value is unchanged.
  - The resulting sum is `1 + 0 + 10 + 3 + 4 + 5 = 23`.

**Example 2**

- Input: `edges = [[0,1],[1,2]], nums = [5,-10,-10], k = 1`
- Output: `25`
- Explanation:
  - Invert the subtree rooted at node `1`, which contains nodes `1` and `2`.
  - Their values both become `10`, while the root remains `5`.
  - The maximum sum is therefore `5 + 10 + 10 = 25`.

**Example 3**

- Input: `edges = [[0,1],[0,2]], nums = [1,-5,-6], k = 2`
- Output: `12`
- Explanation:
  - Invert the subtrees rooted at nodes `1` and `2`, producing `nums = [1,5,6]`.
  - The path from node `1` to node `2` uses the two edges `1 -> 0` and `0 -> 2`, so their distance meets `k = 2`.
  - The resulting maximum sum is `1 + 5 + 6 = 12`.

**Example 4**

- Input: `edges = [[0,1],[0,2]], nums = [1,-5,-6], k = 3`
- Output: `10`
- Explanation:
  - Invert the subtree rooted at node `0`, changing the values to `[-1,5,6]`.
  - Nodes `1` and `2` cannot both be selected because their distance is only $2<3$.
  - The root inversion yields the maximum sum `(-1) + 5 + 6 = 10`.
