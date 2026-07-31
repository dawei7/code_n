## Examples

**Example 1**

- Input: `points = [[1,1],[1,2],[2,2]]`
- Output: `4`

- **Explanation:** Add `(1, 3)` and activate it. Its x-coordinate activates `(1, 1)` and `(1, 2)`. The newly activated `(1, 2)` shares `y = 2` with `(2, 2)`, so propagation activates that point as well. The activated set is `(1, 3)`, `(1, 1)`, `(1, 2)`, and `(2, 2)`, totaling `4`, which is maximal.

**Example 2**

- Input: `points = [[2,2],[1,1],[3,3]]`
- Output: `3`

- **Explanation:** Add `(1, 2)`. Sharing `x = 1` activates `(1, 1)`, while sharing `y = 2` activates `(2, 2)`. Together with the new point, these are `3` activated points, and no placement can activate more.

**Example 3**

- Input: `points = [[2,3],[2,2],[1,1],[4,5]]`
- Output: `4`

- **Explanation:** Add `(2, 1)`. Its x-coordinate activates both `(2, 3)` and `(2, 2)`, and its y-coordinate activates `(1, 1)`. Including `(2, 1)`, the activation reaches `4` points.
