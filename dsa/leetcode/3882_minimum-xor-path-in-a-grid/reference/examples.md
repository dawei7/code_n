## Examples

**Example 1**

- Input: `grid = [[1,2],[3,4]]`
- Output: `6`
- Explanation: The two valid paths are:

  - `(0, 0) -> (0, 1) -> (1, 1)`, with `1 XOR 2 XOR 4 = 7`.
  - `(0, 0) -> (1, 0) -> (1, 1)`, with `1 XOR 3 XOR 4 = 6`.

  Their minimum cost is `6`.

**Example 2**

- Input: `grid = [[6,7],[5,8]]`
- Output: `9`
- Explanation: Again there are two paths:

  - `(0, 0) -> (0, 1) -> (1, 1)`, with `6 XOR 7 XOR 8 = 9`.
  - `(0, 0) -> (1, 0) -> (1, 1)`, with `6 XOR 5 XOR 8 = 11`.

  The smaller XOR is `9`.

**Example 3**

- Input: `grid = [[2,7,5]]`
- Output: `0`
- Explanation: Only `(0, 0) -> (0, 1) -> (0, 2)` is possible. Its cost is `2 XOR 7 XOR 5 = 0`, which is therefore the minimum.
