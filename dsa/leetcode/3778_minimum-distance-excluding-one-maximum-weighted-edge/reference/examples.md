## Examples

**Example 1**

- Input: `n = 5, edges = [[0,1,2],[1,2,7],[2,3,7],[3,4,4]]`
- Output: `13`
- Explanation:
  - The graph has only one path from node `0` to node `4`: `0 -> 1 -> 2 -> 3 -> 4`.
  - Its edge weights, in traversal order, are `2`, `7`, `7`, and `4`.
  - The maximum weight `7` first occurs on edge `1 -> 2`, so that edge alone is omitted. The later weight-`7` edge is still counted, giving `2 + 7 + 4 = 13`.

**Example 2**

- Input: `n = 3, edges = [[0,1,1],[1,2,1],[0,2,50000]]`
- Output: `0`
- Explanation:
  - There are two paths from node `0` to node `2`.
  - On `0 -> 1 -> 2`, the weights are `1` and `1`. Omitting the first maximum-weight edge, `0 -> 1`, leaves a cost of `1`.
  - On the direct path `0 -> 2`, the sole edge has weight `50000`. Omitting that edge leaves a cost of `0`.
  - The minimum is `min(1, 0) = 0`.
