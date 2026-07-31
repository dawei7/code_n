## Examples

**Example 1**

- Input: `points = [[0, 0], [0, 2], [2, 0], [2, 2]]`
- Output: `4`
- Explanation: Split the points into `{[0, 0], [2, 2]}` and `{[0, 2], [2, 0]}`.

  - The only pair in the first group has distance `|0 - 2| + |0 - 2| = 4`.
  - The only pair in the second group has distance `|0 - 2| + |2 - 0| = 4`.

  This split has partition factor `min(4, 4) = 4`, and no split can produce a larger value.

**Example 2**

- Input: `points = [[0, 0], [0, 1], [10, 0]]`
- Output: `11`
- Explanation: Use the groups `{[0, 1], [10, 0]}` and `{[0, 0]}`.

  - The two-point group's only pair has distance `|0 - 10| + |1 - 0| = 11`.
  - The other group is a singleton, so it contributes no pair.

  The split's partition factor is therefore `11`, which is maximal.
